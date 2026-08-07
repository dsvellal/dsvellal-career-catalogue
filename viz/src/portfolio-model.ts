import portfolioJson from './data/portfolio.json'
import type {
  PortfolioClaim,
  PortfolioData,
  PortfolioMethod,
  PortfolioPage,
  PortfolioRoute,
  PortfolioSource,
  PortfolioSupport,
} from './portfolio-types'

export const portfolio = portfolioJson as PortfolioData

export const pageById = new Map(portfolio.pages.map(page => [page.id, page]))
export const claimById = new Map(portfolio.claims.map(claim => [claim.id, claim]))
export const supportById = new Map(portfolio.supports.map(support => [support.id, support]))
export const sourceById = new Map(portfolio.sources.map(source => [source.id, source]))
export const methodById = new Map(portfolio.methods.map(method => [method.id, method]))
export const relationshipById = new Map(portfolio.relationships.map(relationship => [relationship.id, relationship]))
export const caveatById = new Map(portfolio.caveats.map(caveat => [caveat.id, caveat]))
export const conflictById = new Map(portfolio.conflicts.map(conflict => [conflict.id, conflict]))

function normalizedPath(value: string): string {
  const withoutQuery = value.split('?')[0].replace(/^#?\/?/, '').replace(/\/$/, '')
  return withoutQuery || normalizedPageRoute(portfolio.pages[0])
}

export function normalizedPageRoute(page?: PortfolioPage): string {
  if (!page) return 'brief'
  return page.route.replace(/^#?\/?/, '').replace(/\/$/, '') || page.id
}

export function parseRoute(hash: string): PortfolioRoute {
  const path = normalizedPath(hash)
  const [kind, ...rest] = path.split('/')
  const id = decodeURIComponent(rest.join('/'))

  if (kind === 'claim' && id) return { type: 'claim', id }
  if (kind === 'source' && id) return { type: 'source', id }
  if (kind === 'method' && id) return { type: 'method', id }

  const page = portfolio.pages.find(item => normalizedPageRoute(item) === path || item.id === path)
  return { type: 'page', pageId: page?.id ?? portfolio.pages[0]?.id ?? 'brief' }
}

export function hrefForPage(page: PortfolioPage): string {
  return `#/${normalizedPageRoute(page)}`
}

export function hrefForClaim(claimId: string): string {
  return `#/claim/${encodeURIComponent(claimId)}`
}

export function hrefForSource(sourceId: string): string {
  return `#/source/${encodeURIComponent(sourceId)}`
}

export function hrefForMethod(methodId: string): string {
  return `#/method/${encodeURIComponent(methodId)}`
}

export function hrefForCaveat(caveatId: string): string {
  return `#/data-room?mode=methodology&focus=${encodeURIComponent(caveatId)}`
}

export function hrefForConflict(conflictId: string): string {
  return `#/data-room?mode=methodology&focus=${encodeURIComponent(conflictId)}`
}

export function claimsForPage(page: PortfolioPage): PortfolioClaim[] {
  return page.claim_ids.flatMap(id => {
    const claim = claimById.get(id)
    return claim ? [claim] : []
  })
}

export function supportsForClaim(claim: PortfolioClaim | string): PortfolioSupport[] {
  const claimId = typeof claim === 'string' ? claim : claim.id
  const preferredIds = typeof claim === 'string' ? undefined : claim.support_ids
  if (preferredIds && preferredIds.length > 0) {
    return preferredIds.flatMap(id => {
      const support = supportById.get(id)
      return support ? [support] : []
    })
  }
  return portfolio.supports.filter(support => support.claim_id === claimId)
}

export function sourcesForClaim(claim: PortfolioClaim): PortfolioSource[] {
  const seen = new Set<string>()
  return supportsForClaim(claim).flatMap(support => {
    if (seen.has(support.source_id)) return []
    const source = sourceById.get(support.source_id)
    if (!source) return []
    seen.add(source.id)
    return [source]
  })
}

export function claimsForSource(source: PortfolioSource | string): PortfolioClaim[] {
  const sourceId = typeof source === 'string' ? source : source.id
  const seen = new Set<string>()
  return portfolio.supports.flatMap(support => {
    if (support.source_id !== sourceId || seen.has(support.claim_id)) return []
    const claim = claimById.get(support.claim_id)
    if (!claim) return []
    seen.add(claim.id)
    return [claim]
  })
}

export function methodForClaim(claim: PortfolioClaim): PortfolioMethod | undefined {
  return claim.method_id ? methodById.get(claim.method_id) : undefined
}

export function pageForClaim(claim: PortfolioClaim): PortfolioPage | undefined {
  return portfolio.pages.find(page => page.claim_ids.includes(claim.id))
}

export function pageAccent(page: PortfolioPage): string {
  const route = `${page.id} ${page.route} ${page.label}`.toLowerCase()
  if (route.includes('trust')) return 'violet'
  if (route.includes('impact')) return 'copper'
  if (route.includes('innovation')) return 'cobalt'
  if (route.includes('learn')) return 'teal'
  if (route.includes('community') || route.includes('service')) return 'copper'
  if (route.includes('data')) return 'violet'
  if (route.includes('journey')) return 'cobalt'
  if (route.includes('leadership')) return 'teal'
  return 'cobalt'
}

export function compactDate(value?: string): string {
  if (!value) return 'Date held in source record'
  const match = value.match(/(?:19|20)\d{2}/)
  return match?.[0] ?? value
}

export function humanize(value: string): string {
  return value.replace(/[_-]+/g, ' ').replace(/\b\w/g, char => char.toUpperCase())
}

export function qualityEntries(): Array<[string, unknown]> {
  return Object.entries(portfolio.data_quality ?? {})
}
