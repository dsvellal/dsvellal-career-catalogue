import { useMemo, useState } from 'react'
import { documentaryAssetForSource, profilePhoto } from './evidence-assets'
import { MethodCard, QuoteCard, SourceAccessBadge } from './EvidenceUI'
import {
  claimById,
  hrefForClaim,
  hrefForSource,
  humanize,
  pageAccent,
  portfolio,
  sourceById,
  storyClaimIds,
  storyBlocksForPage,
  storyMethodIds,
  storySourceIds,
  supportsForClaim,
} from './portfolio-model'
import type {
  PortfolioClaim,
  PortfolioPage,
  PortfolioRelationship,
  PortfolioSource,
  PortfolioStoryBlock,
  PortfolioSupport,
  SourceAccessState,
  SourceGrade,
} from './portfolio-types'

function routeIdentity(page: PortfolioPage): string {
  return `${page.id} ${page.route} ${page.label}`.toLowerCase()
}

function PageHero({ page, brief = false }: { page: PortfolioPage; brief?: boolean }) {
  return (
    <header className={`obs-page-hero accent-${pageAccent(page)}${brief ? ' is-brief' : ''}`}>
      <div className="obs-page-hero-copy">
        <span className="obs-page-label">{page.label}</span>
        <h1 id={`page-heading-${page.id}`} tabIndex={-1}>{page.question}</h1>
        <p>{page.summary}</p>
        {brief && (
          <div className="obs-hero-actions">
            <a className="obs-primary-action" href="#/leadership">Explore the leadership record</a>
            <a href="#/data-room">Search the evidence</a>
          </div>
        )}
      </div>
      <figure className="obs-page-portrait">
        <img src={profilePhoto} alt={brief ? 'Datta Vellal' : ''} />
        <figcaption>
          <strong>Datta Vellal</strong>
          <span>Leadership · innovation · service</span>
        </figcaption>
      </figure>
    </header>
  )
}

function sourceForStoryBlock(block: PortfolioStoryBlock): PortfolioSource | undefined {
  return block.image_source_id ? sourceById.get(block.image_source_id) : undefined
}

function StoryBlock({ block, index }: { block: PortfolioStoryBlock; index: number }) {
  const claim = claimById.get(block.primary_claim_id)
  if (!claim) return null
  const source = sourceForStoryBlock(block)
  const asset = source ? documentaryAssetForSource(source) : undefined

  return (
    <article className={`obs-story-block accent-${index % 3 === 0 ? 'cobalt' : index % 3 === 1 ? 'teal' : 'copper'}`}>
      {asset && source && (
        <a className="obs-story-image" href={hrefForSource(source.id)} aria-label={`Open evidence record: ${source.title}`}>
          <img src={asset.url} alt={asset.alt} loading="lazy" />
        </a>
      )}
      <div className="obs-story-content">
        <span className="obs-story-index" aria-hidden="true">{String(index + 1).padStart(2, '0')}</span>
        <h2>{block.title}</h2>
        <p className="obs-story-meaning">{block.meaning}</p>
        <div className="obs-story-proof">
          <span>Evidence signal</span>
          <p>{block.proof}</p>
        </div>
        <a className="obs-story-link" href={hrefForClaim(claim.id)}>Explore evidence <span aria-hidden="true">↗</span></a>
      </div>
    </article>
  )
}

function StoryGrid({ page }: { page: PortfolioPage }) {
  const blocks = storyBlocksForPage(page)
  return (
    <section className={`obs-story-grid is-${page.id}`} aria-label={`${page.label} leadership signals`}>
      {blocks.map((block, index) => <StoryBlock key={block.id} block={block} index={index} />)}
    </section>
  )
}

function quotePairs(claims: PortfolioClaim[]): Array<{
  claim: PortfolioClaim
  support: PortfolioSupport
  source: PortfolioSource
}> {
  const seen = new Set<string>()
  return claims.flatMap(claim => supportsForClaim(claim).flatMap(support => {
    const source = sourceById.get(support.source_id)
    if (!source?.approved_excerpt || seen.has(source.id)) return []
    seen.add(source.id)
    return [{ claim, support, source }]
  }))
}

function claimsOwnedByPage(page: PortfolioPage): PortfolioClaim[] {
  const ids = storyBlocksForPage(page).flatMap(block => [block.primary_claim_id, ...block.folded_claim_ids])
  return ids.flatMap(id => {
    const claim = claimById.get(id)
    return claim ? [claim] : []
  })
}

function StoryPage({ page, brief = false }: { page: PortfolioPage; brief?: boolean }) {
  return (
    <>
      <PageHero page={page} brief={brief} />
      <StoryGrid page={page} />
    </>
  )
}

function TrustPage({ page }: { page: PortfolioPage }) {
  const quotes = quotePairs(claimsOwnedByPage(page))
    .filter(item => item.source.id !== 'source-connect-program-2021')
    .slice(0, 2)
  return (
    <>
      <PageHero page={page} />
      <StoryGrid page={page} />
      {quotes.length > 0 && (
        <section className="obs-voices-section" aria-labelledby="trust-voices-heading">
          <header className="obs-simple-heading">
            <span>In their words</span>
            <h2 id="trust-voices-heading">Trust described by the people who experienced it.</h2>
          </header>
          <div className="obs-quote-grid">
            {quotes.map(item => <QuoteCard key={`${item.claim.id}:${item.source.id}`} {...item} eyebrow="Colleague observation" />)}
          </div>
        </section>
      )}
    </>
  )
}

function LearningPage({ page }: { page: PortfolioPage }) {
  const participantClaims = claimsOwnedByPage(page).filter(claim => claim.category === 'participant_takeaway')
  const takeaways = quotePairs(participantClaims).slice(0, 2)
  return (
    <>
      <PageHero page={page} />
      <StoryGrid page={page} />
      {takeaways.length > 0 && (
        <section className="obs-voices-section" aria-labelledby="learning-voices-heading">
          <header className="obs-simple-heading">
            <span>What stayed with participants</span>
            <h2 id="learning-voices-heading">Practical lessons, expressed in participant language.</h2>
          </header>
          <div className="obs-quote-grid">
            {takeaways.map(item => <QuoteCard key={`${item.claim.id}:${item.source.id}`} {...item} eyebrow="Participant takeaway" />)}
          </div>
        </section>
      )}
    </>
  )
}

export function RelationshipRecord({ relationship, index }: {
  relationship: PortfolioRelationship
  index: number
}) {
  const fromClaim = claimById.get(relationship.from_claim_id)
  const toClaim = claimById.get(relationship.to_claim_id)
  const relationshipClaim = claimById.get(relationship.claim_id)
  if (!fromClaim || !toClaim || !relationshipClaim) return null

  return (
    <article className="obs-relationship-record" data-line={relationship.state === 'observed' ? 'solid' : 'dashed'}>
      <span className="obs-relation-number" aria-hidden="true">{String(index + 1).padStart(2, '0')}</span>
      <header>
        <span>{relationship.state === 'observed' ? 'Observed record' : 'Evidence synthesis'}</span>
        <h3>{relationship.title}</h3>
      </header>
      <div className="obs-relation-endpoints">
        <a href={hrefForClaim(fromClaim.id)}><span>{fromClaim.period ?? 'Earlier signal'}</span><strong>{fromClaim.title}</strong></a>
        <i aria-hidden="true">→</i>
        <a href={hrefForClaim(toClaim.id)}><span>{toClaim.period ?? 'Later signal'}</span><strong>{toClaim.title}</strong></a>
      </div>
      <p>{relationship.reasoning}</p>
      <a className="obs-story-link" href={hrefForClaim(relationshipClaim.id)}>Explore this connection <span aria-hidden="true">↗</span></a>
    </article>
  )
}

function DataRoomPage({ page }: { page: PortfolioPage }) {
  const [query, setQuery] = useState('')
  const [browseAll, setBrowseAll] = useState(false)
  const [access, setAccess] = useState<'all' | SourceAccessState>('all')
  const [grade, setGrade] = useState<'all' | SourceGrade>('all')
  const hasSearch = browseAll || query.trim().length > 0 || access !== 'all' || grade !== 'all'
  const queryTokens = query.trim().toLowerCase().split(/[^a-z0-9€₹×.]+/).filter(Boolean)

  const matchesQuery = (value: string) => {
    if (queryTokens.length === 0) return true
    const words = value.toLowerCase().split(/[^a-z0-9€₹×.]+/).filter(Boolean)
    return queryTokens.every(token => words.some(word => word === token || (token.length > 2 && word.startsWith(token))))
  }

  const visibleStories = useMemo(() => {
    if (!hasSearch) return []
    return portfolio.story_blocks.filter(block => {
      const blockClaims = [block.primary_claim_id, ...block.folded_claim_ids].flatMap(id => {
        const claim = claimById.get(id)
        return claim ? [claim] : []
      })
      const supports = blockClaims.flatMap(claim => supportsForClaim(claim))
      const sourceText = supports.map(support => {
        const source = sourceById.get(support.source_id)
        return source ? `${source.title} ${source.publisher ?? ''} ${source.approved_excerpt}` : ''
      }).join(' ')
      const claimText = blockClaims.map(claim => `${claim.title} ${claim.statement} ${claim.category}`).join(' ')
      if (!matchesQuery(`${block.title} ${block.meaning} ${block.proof} ${claimText} ${sourceText}`)) return false
      if (access === 'all' && grade === 'all') return true
      return supports.some(support => {
        const source = sourceById.get(support.source_id)
        return source
          && (access === 'all' || source.access_state === access)
          && (grade === 'all' || support.grade === grade)
      })
    })
  }, [access, grade, hasSearch, query])

  const visibleSources = useMemo(() => {
    if (!hasSearch) return []
    return portfolio.sources.filter(source => storySourceIds.has(source.id)).filter(source => {
      if (!matchesQuery(`${source.title} ${source.source_type} ${source.publisher ?? ''} ${source.approved_excerpt}`)) return false
      if (access !== 'all' && source.access_state !== access) return false
      if (grade !== 'all') {
        const supportMatches = portfolio.supports.some(support => support.source_id === source.id && support.grade === grade)
        if (!supportMatches) return false
      }
      return true
    })
  }, [access, grade, hasSearch, query])

  const clearSearch = () => {
    setQuery('')
    setBrowseAll(false)
    setAccess('all')
    setGrade('all')
  }

  return (
    <>
      <PageHero page={page} />
      <section className="obs-data-room" aria-labelledby="evidence-search-heading">
        <header className="obs-simple-heading">
          <span>Trace the story</span>
          <h2 id="evidence-search-heading">Find the claim, then follow it to the record.</h2>
        </header>
        <div className="obs-room-search">
          <label>
            <span>Search evidence</span>
            <input
              type="search"
              value={query}
              onChange={event => setQuery(event.target.value)}
              placeholder="Try leadership, mentoring, AI, service…"
            />
          </label>
          <button type="button" onClick={() => hasSearch ? clearSearch() : setBrowseAll(true)}>
            {hasSearch ? 'Clear results' : 'Browse all records'}
          </button>
        </div>

        {hasSearch && (
          <>
            <details className="obs-search-filters">
              <summary>Refine results</summary>
              <div>
                <label>
                  <span>Evidence access</span>
                  <select value={access} onChange={event => setAccess(event.target.value as 'all' | SourceAccessState)}>
                    <option value="all">All evidence access</option>
                    <option value="public_external">Public record</option>
                    <option value="public_excerpt">Approved excerpt</option>
                    <option value="private_held">Held evidence</option>
                    <option value="aggregate_only">Privacy-safe aggregate</option>
                  </select>
                </label>
                <label>
                  <span>Evidence basis</span>
                  <select value={grade} onChange={event => setGrade(event.target.value as 'all' | SourceGrade)}>
                    <option value="all">All evidence bases</option>
                    <option value="corroborated">Corroborated</option>
                    <option value="documented">Documented</option>
                    <option value="self_reported">Recorded account</option>
                  </select>
                </label>
              </div>
            </details>
            <p className="obs-result-count" aria-live="polite">{visibleStories.length} conclusions · {visibleSources.length} source records</p>
            <div className="obs-room-results">
              <section aria-labelledby="claim-results-heading">
                <h3 id="claim-results-heading">Conclusions</h3>
                <div className="obs-data-claim-grid">
                  {visibleStories.map(block => (
                    <article key={block.id}>
                      <span>{portfolio.pages.find(candidate => candidate.id === block.page_id)?.label ?? 'Leadership conclusion'}</span>
                      <h4><a href={hrefForClaim(block.primary_claim_id)}>{block.title}</a></h4>
                      <p>{block.meaning}</p>
                      <a href={hrefForClaim(block.primary_claim_id)}>Inspect claim →</a>
                    </article>
                  ))}
                  {visibleStories.length === 0 && <p className="obs-empty-copy">No conclusions match this search.</p>}
                </div>
              </section>
              <section aria-labelledby="source-results-heading">
                <h3 id="source-results-heading">Source records</h3>
                <div className="obs-source-table" role="list">
                  {visibleSources.map(source => (
                    <article role="listitem" key={source.id}>
                      <SourceAccessBadge source={source} />
                      <h4><a href={hrefForSource(source.id)}>{source.title}</a></h4>
                      <p>{humanize(source.source_type)}{source.source_date ? ` · ${source.source_date}` : ''}</p>
                      <a href={hrefForSource(source.id)}>Open record →</a>
                    </article>
                  ))}
                  {visibleSources.length === 0 && <p className="obs-empty-copy">No source records match this search.</p>}
                </div>
              </section>
            </div>
          </>
        )}
        {!hasSearch && <p className="obs-room-empty">Begin with a topic, or browse the complete public evidence index.</p>}
      </section>

      <section className="obs-data-disclosures" aria-label="Evidence methodology and relationships">
        <details>
          <summary>
            <span>Calculation methods</span>
            <strong>See how derived values were produced</strong>
          </summary>
          <div className="obs-method-grid">
            {portfolio.methods.filter(method => storyMethodIds.has(method.id)).map(method => <MethodCard key={method.id} method={method} />)}
          </div>
        </details>
        <details>
          <summary>
            <span>Evidence relationships</span>
            <strong>Explore patterns across time and context</strong>
          </summary>
          <div className="obs-longitudinal-relations">
            {portfolio.relationships.filter(relationship => storyClaimIds.has(relationship.claim_id)).map((relationship, index) => (
              <RelationshipRecord key={relationship.id} relationship={relationship} index={index} />
            ))}
          </div>
        </details>
      </section>
    </>
  )
}

export function PortfolioPageView({ page }: { page: PortfolioPage }) {
  const identity = routeIdentity(page)
  if (identity.includes('data')) return <DataRoomPage page={page} />
  if (identity.includes('trust')) return <TrustPage page={page} />
  if (identity.includes('learn')) return <LearningPage page={page} />
  return <StoryPage page={page} brief={identity.includes('brief')} />
}
