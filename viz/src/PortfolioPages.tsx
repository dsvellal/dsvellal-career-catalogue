import { useEffect, useMemo, useRef, useState, type KeyboardEvent as ReactKeyboardEvent } from 'react'
import { documentaryAssetForSource, profilePhoto } from './evidence-assets'
import { MethodCard, QuoteCard, SourceAccessBadge } from './EvidenceUI'
import {
  claimById,
  hrefForClaim,
  hrefForSource,
  humanize,
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

const QUESTION_PARTS: Record<string, { lead: string; focus: string }> = {
  brief: { lead: 'What makes Datta ready', focus: 'to lead at executive scale?' },
  leadership: { lead: 'How does Datta lead', focus: 'across levels, functions, and formal boundaries?' },
  journey: { lead: 'How has Datta turned technical depth', focus: 'into organizational leverage?' },
  trust: { lead: 'Why do colleagues seek Datta out', focus: 'and trust his leadership?' },
  innovation: { lead: 'How does Datta turn emerging technology', focus: 'into governed execution?' },
  learning: { lead: 'What do people value and carry forward', focus: 'after learning with Datta?' },
  community: { lead: 'How does Datta create value', focus: 'beyond formal responsibility?' },
}

function questionParts(page: PortfolioPage): { lead: string; focus: string } {
  return QUESTION_PARTS[page.id] ?? { lead: page.question, focus: '' }
}

function PageHero({ page, brief = false }: { page: PortfolioPage; brief?: boolean }) {
  const parts = questionParts(page)
  const pageIndex = portfolio.pages.indexOf(page) + 1
  return (
    <header className={`obs-page-hero${brief ? ' is-brief' : ''}`}>
      <div className="obs-page-hero-copy">
        <span className="obs-page-label"><i aria-hidden="true">{String(pageIndex).padStart(2, '0')} /</i>{page.label}</span>
        <h1 id={`page-heading-${page.id}`} tabIndex={-1}>
          <span>{parts.lead}</span>
          {parts.focus && <em>{parts.focus}</em>}
        </h1>
        <p>{page.summary}</p>
        {brief && (
          <div className="obs-hero-actions">
            <a className="obs-primary-action" href="#/leadership">Explore the leadership record</a>
            <a href="#/data-room">Search the evidence</a>
          </div>
        )}
      </div>
      <figure className="obs-page-portrait">
        <img src={profilePhoto} alt="Datta Vellal" />
        <figcaption>
          <strong>Datta Vellal</strong>
          <span>Leadership through evidence</span>
        </figcaption>
      </figure>
    </header>
  )
}

function sourceForStoryBlock(block: PortfolioStoryBlock): PortfolioSource | undefined {
  return block.image_source_id ? sourceById.get(block.image_source_id) : undefined
}

function StoryFocus({ page }: { page: PortfolioPage }) {
  const blocks = useMemo(() => storyBlocksForPage(page), [page.id])
  const focusId = new URLSearchParams(window.location.hash.split('?')[1] ?? '').get('focus')
  const [selectedIndex, setSelectedIndex] = useState(() => {
    const focusedIndex = blocks.findIndex(block => block.id === focusId)
    return focusedIndex >= 0 ? focusedIndex : 0
  })
  const tabRefs = useRef<Array<HTMLButtonElement | null>>([])
  const selectedBlock = blocks[selectedIndex] ?? blocks[0]
  const selectedClaim = selectedBlock ? claimById.get(selectedBlock.primary_claim_id) : undefined
  const selectedSource = selectedBlock ? sourceForStoryBlock(selectedBlock) : undefined
  const selectedAsset = selectedSource ? documentaryAssetForSource(selectedSource) : undefined

  const selectStory = (index: number) => {
    setSelectedIndex(index)
    const currentPath = window.location.hash.split('?')[0]
    const hashParameters = new URLSearchParams(window.location.hash.split('?')[1] ?? '')
    hashParameters.set('focus', blocks[index].id)
    window.history.replaceState(null, '', `${currentPath}?${hashParameters.toString()}`)
  }

  useEffect(() => {
    const requestedIndex = focusId ? blocks.findIndex(block => block.id === focusId) : 0
    const nextIndex = requestedIndex >= 0 ? requestedIndex : 0
    setSelectedIndex(currentIndex => currentIndex === nextIndex ? currentIndex : nextIndex)

    if (focusId && requestedIndex < 0 && blocks[0]) {
      const currentPath = window.location.hash.split('?')[0]
      const hashParameters = new URLSearchParams(window.location.hash.split('?')[1] ?? '')
      hashParameters.set('focus', blocks[0].id)
      window.history.replaceState(null, '', `${currentPath}?${hashParameters.toString()}`)
    }

    if (!focusId) return
    const focusFrame = window.requestAnimationFrame(() => {
      const selectedTab = tabRefs.current[nextIndex]
      selectedTab?.scrollIntoView({ block: 'start', inline: 'nearest' })
      selectedTab?.focus({ preventScroll: true })
    })
    return () => window.cancelAnimationFrame(focusFrame)
  }, [blocks, focusId, page.id])

  const handleTabKeyDown = (event: ReactKeyboardEvent<HTMLButtonElement>, index: number) => {
    let nextIndex: number | undefined
    if (event.key === 'ArrowRight') nextIndex = (index + 1) % blocks.length
    if (event.key === 'ArrowLeft') nextIndex = (index - 1 + blocks.length) % blocks.length
    if (event.key === 'Home') nextIndex = 0
    if (event.key === 'End') nextIndex = blocks.length - 1
    if (nextIndex === undefined) return
    event.preventDefault()
    selectStory(nextIndex)
  }

  if (!selectedBlock || !selectedClaim) return null

  return (
    <section className={`obs-focus-deck is-${page.id}`} aria-label={`${page.label} leadership signals`}>
      <div className="obs-focus-rail" role="tablist" aria-label="Choose one leadership signal">
        {blocks.map((block, index) => (
          <button
            type="button"
            role="tab"
            key={block.id}
            id={`story-tab-${page.id}-${block.id}`}
            ref={node => { tabRefs.current[index] = node }}
            className={selectedIndex === index ? 'is-selected' : ''}
            aria-selected={selectedIndex === index}
            aria-controls={`story-panel-${page.id}`}
            tabIndex={selectedIndex === index ? 0 : -1}
            onClick={() => selectStory(index)}
            onKeyDown={event => handleTabKeyDown(event, index)}
          >
            <span>{String(index + 1).padStart(2, '0')}</span>
            <strong>{block.title}</strong>
          </button>
        ))}
      </div>

      <article
        className="obs-focus-stage"
        id={`story-panel-${page.id}`}
        role="tabpanel"
        aria-labelledby={`story-tab-${page.id}-${selectedBlock.id}`}
        tabIndex={0}
        key={selectedBlock.id}
      >
        <div className="obs-focus-title">
          <span>Signal {String(selectedIndex + 1).padStart(2, '0')} / {String(blocks.length).padStart(2, '0')}</span>
          <h2>{selectedBlock.title}</h2>
        </div>
        <div className="obs-focus-detail">
          <p>{selectedBlock.meaning}</p>
          <div className="obs-focus-proof">
            <span>Evidence</span>
            <strong>{selectedBlock.proof}</strong>
          </div>
          <a href={hrefForClaim(selectedClaim.id)}>Inspect claim <span aria-hidden="true">↗</span></a>
        </div>
        {selectedAsset && selectedSource && (
          <a className="obs-focus-media" href={hrefForSource(selectedSource.id)} aria-label={`Open evidence record: ${selectedSource.title}`}>
            <img src={selectedAsset.url} alt={selectedAsset.alt} loading="lazy" />
            <span>View source · {selectedSource.title} ↗</span>
          </a>
        )}
      </article>

      <div className="obs-focus-print" aria-hidden="true">
        {blocks.map((block, index) => {
          const source = sourceForStoryBlock(block)
          return (
            <article key={block.id}>
              <span>Signal {String(index + 1).padStart(2, '0')}</span>
              <h2>{block.title}</h2>
              <p>{block.meaning}</p>
              <strong>{block.proof}</strong>
              <a href={hrefForClaim(block.primary_claim_id)}>Claim record</a>
              {source && <a href={hrefForSource(source.id)}>Source: {source.title}</a>}
            </article>
          )
        })}
      </div>
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
      <StoryFocus key={page.id} page={page} />
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
      <StoryFocus key={page.id} page={page} />
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
      <StoryFocus key={page.id} page={page} />
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
