import portfolioJson from './data/portfolio.json'
import type {
  PortfolioClaim,
  PortfolioData,
  PortfolioMethod,
  PortfolioPage,
  PortfolioRoute,
  PortfolioSource,
  PortfolioStoryBlock,
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
export const storyBlockById = new Map((portfolio.story_blocks ?? []).map(block => [block.id, block]))

export const auditOnlyClaimIds = new Set(portfolio.audit_only_claim_ids ?? [])
export const storyClaimIds = new Set(
  (portfolio.story_blocks ?? []).flatMap(block => [block.primary_claim_id, ...block.folded_claim_ids]),
)
export const storyMethodIds = new Set([
  ...portfolio.claims
    .filter(claim => storyClaimIds.has(claim.id) && claim.method_id)
    .map(claim => claim.method_id as string),
  ...portfolio.relationships
    .filter(relationship => storyClaimIds.has(relationship.claim_id) && relationship.method_id)
    .map(relationship => relationship.method_id as string),
])
const storyConflictIds = new Set(
  portfolio.claims.filter(claim => storyClaimIds.has(claim.id)).flatMap(claim => claim.conflict_ids),
)
export const storySourceIds = new Set([
  ...portfolio.supports
    .filter(support => storyClaimIds.has(support.claim_id))
    .map(support => support.source_id),
  ...(portfolio.story_blocks ?? []).flatMap(block => block.image_source_id ? [block.image_source_id] : []),
  ...portfolio.methods
    .filter(method => storyMethodIds.has(method.id))
    .flatMap(method => method.inputs.flatMap(input => input.source_id ? [input.source_id] : [])),
  ...portfolio.conflicts
    .filter(conflict => storyConflictIds.has(conflict.id))
    .flatMap(conflict => conflict.source_ids),
])

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

  const resolvedPath = path === 'impact' ? 'innovation' : path
  const page = portfolio.pages.find(item => normalizedPageRoute(item) === resolvedPath || item.id === resolvedPath)
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
  const story = storyBlockForPrimaryClaim(claim.id)
  if (story) return pageById.get(story.page_id)
  return portfolio.pages.find(page => page.claim_ids.includes(claim.id))
}

export function storyBlocksForPage(page: PortfolioPage | string): PortfolioStoryBlock[] {
  const pageId = typeof page === 'string' ? page : page.id
  return (portfolio.story_blocks ?? []).filter(block => block.page_id === pageId)
}

export function storyBlockForPrimaryClaim(claimId: string): PortfolioStoryBlock | undefined {
  return (portfolio.story_blocks ?? []).find(block => block.primary_claim_id === claimId)
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
  if (!value) return 'Date in source record'
  const match = value.match(/(?:19|20)\d{2}/)
  return match?.[0] ?? value
}

export function humanize(value: string): string {
  return value.replace(/[_-]+/g, ' ').replace(/\b\w/g, char => char.toUpperCase())
}
