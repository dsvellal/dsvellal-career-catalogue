import { useEffect, useMemo, useState } from 'react'
import { documentaryAssetsForSources, profilePhoto } from './evidence-assets'
import {
  ClaimCard,
  EvidenceChip,
  MethodCard,
  QuoteCard,
  SectionHeading,
  SourceAccessBadge,
  SupportPath,
} from './EvidenceUI'
import {
  caveatById,
  claimById,
  claimsForPage,
  hrefForCaveat,
  hrefForClaim,
  hrefForMethod,
  hrefForSource,
  humanize,
  methodById,
  pageAccent,
  portfolio,
  qualityEntries,
  sourceById,
  supportById,
  supportsForClaim,
} from './portfolio-model'
import type {
  EvidenceLens,
  PortfolioClaim,
  PortfolioPage,
  PortfolioSource,
  PortfolioSupport,
  PortfolioRelationship,
  SourceAccessState,
  SourceGrade,
} from './portfolio-types'

function routeIdentity(page: PortfolioPage): string {
  return `${page.id} ${page.route} ${page.label}`.toLowerCase()
}

function PageHeader({ page, claimCount, sourceCount }: {
  page: PortfolioPage
  claimCount: number
  sourceCount: number
}) {
  return (
    <header className={`obs-page-header accent-${pageAccent(page)}`}>
      <div className="obs-page-kicker">
        <span>Executive question</span>
        <span>{String(claimCount).padStart(2, '0')} claims · {String(sourceCount).padStart(2, '0')} sources</span>
      </div>
      <h1 id={`page-heading-${page.id}`} tabIndex={-1}>{page.question}</h1>
      <div className="obs-page-intro">
        <p>{page.summary}</p>
        <div className="obs-page-index">
          <span>{page.label}</span>
          <strong>{String(portfolio.pages.findIndex(item => item.id === page.id) + 1).padStart(2, '0')}</strong>
        </div>
      </div>
    </header>
  )
}

function ClaimGallery({ claims, lens, accent, compact = false }: {
  claims: PortfolioClaim[]
  lens: EvidenceLens
  accent: string
  compact?: boolean
}) {
  return (
    <div className={`obs-claim-grid${compact ? ' is-compact' : ''}`}>
      {claims.map((claim, index) => (
        <ClaimCard key={claim.id} claim={claim} lens={lens} accent={accent} compact={compact} index={index} />
      ))}
    </div>
  )
}

function DocumentaryGallery({ page }: { page: PortfolioPage }) {
  const assets = documentaryAssetsForSources(portfolio.sources, routeIdentity(page))
  if (assets.length === 0) return null
  return (
    <section className="obs-documentary-section" role="region" aria-labelledby={`${page.id}-documentary-title`}>
      <SectionHeading
        id={`${page.id}-documentary-title`}
        eyebrow="Documentary layer"
        title="The record is visible—not merely cited."
        copy="Only explicitly approved, non-sensitive media is included in the public presentation."
      />
      <div className="obs-documentary-grid">
        {assets.map((asset, index) => (
          <figure className={index === 0 && assets.length > 1 ? 'is-featured' : ''} key={asset.id}>
            <a href={hrefForSource(asset.source.id)} aria-label={`Open source record: ${asset.source.title}`}>
              <img src={asset.url} alt={asset.alt} loading="eager" />
            </a>
            <figcaption>
              <SourceAccessBadge source={asset.source} />
              <a href={hrefForSource(asset.source.id)}>{asset.source.title}</a>
            </figcaption>
          </figure>
        ))}
      </div>
    </section>
  )
}

function BriefPage({ page, claims, lens }: PageProps) {
  const metrics = claims.filter(claim => claim.metric)
  const narrative = claims.filter(claim => !claim.metric)
  return (
    <>
      <section className="obs-brief-hero">
        <div className="obs-brief-copy">
          <PageHeader page={page} claimCount={claims.length} sourceCount={sourceCountForClaims(claims)} />
          <div className="obs-brief-actions">
            <a href={portfolio.pages[1] ? `#/${portfolio.pages[1].route.replace(/^\//, '')}` : '#/'}>Follow the leadership system</a>
            <a href="#/data-room">Audit the data room</a>
          </div>
        </div>
        <div className="obs-portrait-stage">
          <div className="obs-portrait-orbit" aria-hidden="true" />
          <img src={profilePhoto} alt="Datta Vellal" />
          <div className="obs-portrait-caption">
            <span>Datta Vellal</span>
            <span>Evidence-backed executive dossier</span>
          </div>
        </div>
      </section>

      {metrics.length > 0 && (
        <section className="obs-metric-runway" aria-label="Headline evidence">
          {metrics.slice(0, 6).map((claim, index) => (
            <ClaimCard key={claim.id} claim={claim} lens={lens} accent={index % 2 ? 'teal' : 'cobalt'} compact index={index} />
          ))}
        </section>
      )}

      {narrative.length > 0 && (
        <section className="obs-page-section">
          <SectionHeading eyebrow="Leadership brief" title="A concise reading, with every conclusion inspectable." />
          <ClaimGallery claims={narrative} lens={lens} accent="cobalt" />
        </section>
      )}
      <DocumentaryGallery page={page} />
    </>
  )
}

function LeadershipPage({ page, claims, lens }: PageProps) {
  const paths = claims.flatMap(supportsForClaim).slice(0, 8)
  const claimIds = new Set(claims.map(claim => claim.id))
  const declaredRelationships = portfolio.relationships.filter(relationship =>
    claimIds.has(relationship.claim_id)
    || (claimIds.has(relationship.from_claim_id) && claimIds.has(relationship.to_claim_id))
  )
  return (
    <>
      <PageHeader page={page} claimCount={claims.length} sourceCount={sourceCountForClaims(claims)} />
      <section className="obs-page-section obs-system-section">
        <SectionHeading
          eyebrow="Operating system"
          title="Leadership is shown as repeatable practice."
          copy="Claims remain separate; source paths show only relationships declared in the portfolio dataset."
        />
        <ClaimGallery claims={claims} lens={lens} accent="teal" />
      </section>
      {paths.length > 0 && (
        <section className="obs-page-section obs-path-section">
          <SectionHeading eyebrow="Influence mechanisms" title="From claim to record, without invented causality." />
          <div className="obs-support-paths">
            {paths.map(support => <SupportPath key={support.id} support={support} />)}
          </div>
        </section>
      )}
      {declaredRelationships.length > 0 && (
        <section className="obs-page-section">
          <SectionHeading
            eyebrow="Declared relationships"
            title="Leadership mechanisms with their reasoning and limits."
            copy="These are explicit relationship records from the publication dataset; dashed lines mark calculated or interpreted propositions."
          />
          <div className="obs-longitudinal-relations">
            {declaredRelationships.slice(0, 4).map((relationship, index) => (
              <RelationshipRecord key={relationship.id} relationship={relationship} index={index} />
            ))}
          </div>
        </section>
      )}
      <DocumentaryGallery page={page} />
    </>
  )
}

function JourneyPage({ page, claims, lens }: PageProps) {
  const yearFor = (claim: PortfolioClaim) => Number(claim.period?.match(/(?:19|20)\d{2}/)?.[0] ?? 0)
  const sorted = [...claims].sort((a, b) => yearFor(b) - yearFor(a))
  return (
    <>
      <PageHeader page={page} claimCount={claims.length} sourceCount={sourceCountForClaims(claims)} />
      <section className="obs-page-section">
        <SectionHeading
          eyebrow="Longitudinal record"
          title="Career, learning, and contribution move on the same clock."
          copy="Periods are taken directly from claim records; undated records remain explicitly undated."
        />
        <div className="obs-timeline">
          {sorted.map((claim, index) => (
            <article className="obs-timeline-entry" key={claim.id}>
              <div className="obs-timeline-date"><span>{claim.period ?? 'Period held in source'}</span><i aria-hidden="true" /></div>
              <ClaimCard claim={claim} lens={lens} accent={index % 3 === 0 ? 'copper' : index % 2 ? 'teal' : 'cobalt'} />
            </article>
          ))}
        </div>
      </section>
    </>
  )
}

function ImpactPage({ page, claims, lens }: PageProps) {
  const [scope, setScope] = useState('all')
  const scopes = ['all', ...new Set(claims.map(claim => claim.scope).filter(Boolean))]
  const visible = scope === 'all' ? claims : claims.filter(claim => claim.scope === scope)
  return (
    <>
      <PageHeader page={page} claimCount={claims.length} sourceCount={sourceCountForClaims(claims)} />
      <section className="obs-page-section">
        <SectionHeading
          eyebrow="Attribution scope"
          title="Outcomes are separated by the level at which value appeared."
          action={(
            <div className="obs-filter-pills" role="group" aria-label="Filter by attribution scope">
              {scopes.map(option => (
                <button key={option} type="button" className={scope === option ? 'is-active' : ''} onClick={() => setScope(option)}>
                  {humanize(option)}
                </button>
              ))}
            </div>
          )}
        />
        <div className="obs-impact-ledger">
          {visible.map((claim, index) => (
            <ClaimCard key={claim.id} claim={claim} lens={lens} accent={index % 2 ? 'violet' : 'copper'} index={index} />
          ))}
        </div>
      </section>
      <DocumentaryGallery page={page} />
    </>
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
    if (!source?.approved_excerpt || seen.has(`${claim.id}:${source.id}`)) return []
    seen.add(`${claim.id}:${source.id}`)
    return [{ claim, support, source }]
  }))
}

function RelationshipLab() {
  const [filter, setFilter] = useState<'all' | 'observed' | 'derived'>('all')
  const relationships = portfolio.relationships
  const visible = filter === 'all'
    ? relationships
    : relationships.filter(relationship => relationship.state === 'observed' ? filter === 'observed' : filter === 'derived')
  return (
    <section className="obs-relationship-lab">
      <div className="obs-relationship-toolbar">
        <div className="obs-relationship-legend">
          <span><i className="is-solid" /> Observed relationship</span>
          <span><i className="is-dashed" /> Calculated or interpreted relationship</span>
        </div>
        <div className="obs-filter-pills" role="group" aria-label="Filter relationship state">
          {(['all', 'observed', 'derived'] as const).map(option => (
            <button type="button" key={option} className={filter === option ? 'is-active' : ''} onClick={() => setFilter(option)}>
              {humanize(option)}
            </button>
          ))}
        </div>
      </div>
      <div className="obs-longitudinal-relations">
        {visible.map((relationship, index) => <RelationshipRecord key={relationship.id} relationship={relationship} index={index} />)}
      </div>
      {visible.length === 0 && <p className="obs-empty-copy">No declared relationship records match this view.</p>}
    </section>
  )
}

export function RelationshipRecord({ relationship, index }: { relationship: PortfolioRelationship; index: number }) {
  const fromClaim = claimById.get(relationship.from_claim_id)
  const toClaim = claimById.get(relationship.to_claim_id)
  const relationshipClaim = claimById.get(relationship.claim_id)
  const method = relationship.method_id ? methodById.get(relationship.method_id) : undefined
  const supports = relationship.support_ids.flatMap(id => {
    const support = supportById.get(id)
    return support ? [support] : []
  })
  const caveats = relationship.caveat_ids.flatMap(id => {
    const caveat = caveatById.get(id)
    return caveat ? [caveat] : []
  })
  if (!fromClaim || !toClaim || !relationshipClaim) return null
  const isObserved = relationship.state === 'observed'
  return (
    <article className="obs-relationship-record" data-line={isObserved ? 'solid' : 'dashed'}>
      <div className="obs-relation-sequence"><span>{String(index + 1).padStart(2, '0')}</span><i aria-hidden="true" /></div>
      <header>
        <div><span>{humanize(relationship.relation_type)}</span><span>{humanize(relationship.state)}</span></div>
        <h3><a href={hrefForClaim(relationshipClaim.id)}>{relationship.title}</a></h3>
        <p>{relationship.statement}</p>
      </header>
      <div className="obs-relation-endpoints">
        <a href={hrefForClaim(fromClaim.id)}>
          <span>{fromClaim.period ?? 'Earlier signal'}</span>
          <strong>{fromClaim.title}</strong>
        </a>
        <div className="obs-relation-arrow" role="img" aria-label={`${humanize(relationship.state)} relationship`}><i /><b>→</b></div>
        <a href={hrefForClaim(toClaim.id)}>
          <span>{toClaim.period ?? 'Later signal'}</span>
          <strong>{toClaim.title}</strong>
        </a>
      </div>
      <div className="obs-relation-reasoning">
        <strong>Why linked</strong>
        <p>{relationship.reasoning}</p>
        <small>{relationship.limitation}</small>
      </div>
      <footer>
        <span className={`obs-confidence is-${relationship.confidence.level}`}>{humanize(relationship.confidence.level)} confidence</span>
        <div>{supports.slice(0, 3).map(support => {
          const source = sourceById.get(support.source_id)
          return source ? (
            <a key={support.id} href={hrefForSource(source.id)} aria-label={`Open source: ${source.title}`}>
              <EvidenceChip support={support} compact />
            </a>
          ) : <EvidenceChip key={support.id} support={support} compact />
        })}</div>
        {method && <a href={hrefForMethod(method.id)}>Method: {method.title}</a>}
        {caveats.map(caveat => <a className="obs-caveat-link" key={caveat.id} href={hrefForCaveat(caveat.id)}>△ {caveat.label}</a>)}
        <a href={hrefForClaim(relationshipClaim.id)}>Inspect relationship claim →</a>
      </footer>
    </article>
  )
}

function TrustPage({ page, claims, lens }: PageProps) {
  const [tab, setTab] = useState<'voices' | 'relationships'>('voices')
  const quotes = quotePairs(claims)
  return (
    <>
      <PageHeader page={page} claimCount={claims.length} sourceCount={sourceCountForClaims(claims)} />
      <section className="obs-page-section">
        <div className="obs-subtabs" role="tablist" aria-label="Trust views">
          <button id="trust-tab-voices" type="button" role="tab" aria-controls="trust-panel-voices" aria-selected={tab === 'voices'} onClick={() => setTab('voices')}>Attributed observations</button>
          <button id="trust-tab-relationships" type="button" role="tab" aria-controls="trust-panel-relationships" aria-selected={tab === 'relationships'} onClick={() => setTab('relationships')}>Relationship lab</button>
        </div>
        {tab === 'voices' ? (
          <div id="trust-panel-voices" role="tabpanel" aria-labelledby="trust-tab-voices" className="obs-voice-layout">
            <SectionHeading eyebrow="Trust record" title="Attributed observations remain attached to their source context." />
            <div className="obs-quote-grid">
              {quotes.slice(0, 12).map(item => (
                <QuoteCard key={`${item.claim.id}:${item.source.id}`} {...item} />
              ))}
            </div>
            <ClaimGallery claims={claims} lens={lens} accent="violet" compact />
          </div>
        ) : (
          <div id="trust-panel-relationships" role="tabpanel" aria-labelledby="trust-tab-relationships"><RelationshipLab /></div>
        )}
      </section>
      <DocumentaryGallery page={page} />
    </>
  )
}

function InnovationPage({ page, claims, lens }: PageProps) {
  const statuses = [...new Set(claims.map(claim => claim.status).filter(Boolean))]
  return (
    <>
      <PageHeader page={page} claimCount={claims.length} sourceCount={sourceCountForClaims(claims)} />
      <section className="obs-page-section">
        <SectionHeading
          eyebrow="Innovation portfolio"
          title="Novelty, adoption, and guardrails stay distinct."
          copy="Status labels are carried from the claim record so active direction is not presented as delivered impact."
        />
        <div className="obs-status-board">
          {statuses.map((status, column) => (
            <div className="obs-status-column" key={status}>
              <h3>{humanize(status)} <span>{claims.filter(claim => claim.status === status).length}</span></h3>
              {claims.filter(claim => claim.status === status).map((claim, index) => (
                <ClaimCard key={claim.id} claim={claim} lens={lens} accent={column % 2 ? 'violet' : 'cobalt'} compact index={index} />
              ))}
            </div>
          ))}
          {statuses.length === 0 && <ClaimGallery claims={claims} lens={lens} accent="cobalt" />}
        </div>
      </section>
      <DocumentaryGallery page={page} />
    </>
  )
}

function LearningPage({ page, claims, lens }: PageProps) {
  const excerpts = quotePairs(claims)
  const takeaways = excerpts.filter(item => item.claim.category === 'participant_takeaway')
  const improvements = excerpts.filter(item => item.claim.category === 'requested_improvement')
  return (
    <>
      <PageHeader page={page} claimCount={claims.length} sourceCount={sourceCountForClaims(claims)} />
      <section className="obs-page-section">
        <SectionHeading
          eyebrow="Participant signal"
          title="Takeaways and requested improvements are shown together."
          copy="Grouping uses the explicit participant_takeaway and requested_improvement claim categories in the evidence dataset. The browser performs no sentiment or keyword classification."
        />
        <div className="obs-learning-columns">
          <div>
            <h3>What participants took away <span>{takeaways.length}</span></h3>
            {takeaways.slice(0, 8).map(item => <QuoteCard key={`${item.claim.id}:${item.source.id}`} {...item} eyebrow="Participant takeaway" />)}
            {takeaways.length === 0 && <p className="obs-empty-copy">No approved excerpts are classified as participant takeaways.</p>}
          </div>
          <div className="is-improvement">
            <h3>What participants asked to improve <span>{improvements.length}</span></h3>
            {improvements.slice(0, 8).map(item => <QuoteCard key={`${item.claim.id}:${item.source.id}`} {...item} eyebrow="Requested improvement" />)}
            {improvements.length === 0 && <p className="obs-empty-copy">No approved excerpts are classified as requested improvements.</p>}
          </div>
        </div>
      </section>
      <section className="obs-page-section">
        <SectionHeading eyebrow="Multiplication record" title="The claims behind the learning system." />
        <ClaimGallery claims={claims} lens={lens} accent="teal" />
      </section>
    </>
  )
}

function CommunityPage({ page, claims, lens }: PageProps) {
  return (
    <>
      <PageHeader page={page} claimCount={claims.length} sourceCount={sourceCountForClaims(claims)} />
      <section className="obs-community-layout">
        <div>
          <SectionHeading eyebrow="Service record" title="Contribution outside formal authority remains part of the same dossier." />
          <ClaimGallery claims={claims} lens={lens} accent="copper" />
        </div>
        <aside className="obs-community-aside">
          <span>Publication boundary</span>
          <p>Only approved aggregate records and material-only documentary images are presented here.</p>
        </aside>
      </section>
      <DocumentaryGallery page={page} />
    </>
  )
}

function flattenQuality(value: unknown): string {
  if (typeof value === 'string' || typeof value === 'number' || typeof value === 'boolean') return String(value)
  if (Array.isArray(value)) return value.map(flattenQuality).join(' · ')
  if (value && typeof value === 'object') {
    return Object.entries(value as Record<string, unknown>)
      .map(([key, child]) => `${humanize(key)}: ${flattenQuality(child)}`)
      .join(' · ')
  }
  return 'Not reported'
}

function DataRoomPage({ page, claims }: PageProps) {
  const hashQuery = window.location.hash.split('?')[1] ?? ''
  const hashParameters = new URLSearchParams(hashQuery)
  const requestedMode = hashParameters.get('mode') === 'methodology' ? 'methodology' : 'evidence'
  const focusedRecord = hashParameters.get('focus')
  const [mode, setMode] = useState<'evidence' | 'methodology'>(requestedMode)
  const [query, setQuery] = useState('')
  const [access, setAccess] = useState<'all' | SourceAccessState>('all')
  const [grade, setGrade] = useState<'all' | SourceGrade>('all')

  const selectMode = (nextMode: 'evidence' | 'methodology') => {
    setMode(nextMode)
    const base = `#/${page.route.replace(/^#?\/?/, '').replace(/\/$/, '')}`
    window.history.replaceState(null, '', nextMode === 'methodology' ? `${base}?mode=methodology` : base)
  }

  useEffect(() => setMode(requestedMode), [requestedMode])

  useEffect(() => {
    if (mode !== 'methodology' || !focusedRecord) return
    window.requestAnimationFrame(() => {
      const record = document.getElementById(`boundary-${focusedRecord}`)
      const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
      record?.scrollIntoView({ behavior: reducedMotion ? 'auto' : 'smooth', block: 'center' })
      record?.focus({ preventScroll: true })
    })
  }, [focusedRecord, mode])

  const visibleClaims = useMemo(() => portfolio.claims.filter(claim => {
    const supports = supportsForClaim(claim)
    const linkedSourceText = supports.map(support => {
      const source = sourceById.get(support.source_id)
      return source ? `${source.title} ${source.publisher ?? ''} ${source.approved_excerpt}` : ''
    }).join(' ')
    const haystack = [
      claim.title,
      claim.statement,
      claim.category,
      claim.scope,
      claim.attribution,
      claim.status,
      claim.period ?? '',
      linkedSourceText,
    ].join(' ').toLowerCase()
    if (query && !haystack.includes(query.toLowerCase())) return false
    if (access !== 'all' || grade !== 'all') {
      return supports.some(support => {
        const source = sourceById.get(support.source_id)
        if (!source) return false
        if (access !== 'all' && source.access_state !== access) return false
        if (grade !== 'all' && support.grade !== grade) return false
        return true
      })
    }
    return true
  }), [query, access, grade])

  const visibleSources = useMemo(() => portfolio.sources.filter(source => {
    const haystack = `${source.title} ${source.source_type} ${source.publisher ?? ''} ${source.approved_excerpt}`.toLowerCase()
    if (query && !haystack.includes(query.toLowerCase())) return false
    if (access !== 'all' && source.access_state !== access) return false
    if (grade !== 'all') {
      const sourceSupports = portfolio.supports.filter(support => support.source_id === source.id)
      if (!sourceSupports.some(support => support.grade === grade)) return false
    }
    return true
  }), [query, access, grade])

  return (
    <>
      <PageHeader page={page} claimCount={claims.length} sourceCount={portfolio.sources.length} />
      <section className="obs-data-room">
        <div className="obs-subtabs" role="tablist" aria-label="Data room modes">
          <button id="data-tab-evidence" type="button" role="tab" aria-controls="data-panel-evidence" aria-selected={mode === 'evidence'} onClick={() => selectMode('evidence')}>Evidence</button>
          <button id="data-tab-methodology" type="button" role="tab" aria-controls="data-panel-methodology" aria-selected={mode === 'methodology'} onClick={() => selectMode('methodology')}>Methodology</button>
        </div>

        {mode === 'evidence' ? (
          <div id="data-panel-evidence" role="tabpanel" aria-labelledby="data-tab-evidence">
            <div className="obs-data-controls">
              <label>
                <span>Search records</span>
                <input value={query} onChange={event => setQuery(event.target.value)} placeholder="Claim, statement, source, publisher…" type="search" />
              </label>
              <label>
                <span>Access state</span>
                <select value={access} onChange={event => setAccess(event.target.value as 'all' | SourceAccessState)}>
                  <option value="all">All access states</option>
                  <option value="public_external">Public source</option>
                  <option value="public_excerpt">Approved excerpt</option>
                  <option value="private_held">Privately held</option>
                  <option value="aggregate_only">Aggregate only</option>
                </select>
              </label>
              <label>
                <span>Evidence grade</span>
                <select value={grade} onChange={event => setGrade(event.target.value as 'all' | SourceGrade)}>
                  <option value="all">All grades</option>
                  <option value="corroborated">Corroborated</option>
                  <option value="documented">Documented</option>
                  <option value="self_reported">Self-reported</option>
                </select>
              </label>
            </div>
            <div className="obs-result-count" aria-live="polite">
              {visibleClaims.length} claim records · {visibleSources.length} source records
            </div>
            <section className="obs-data-claims">
              <SectionHeading
                eyebrow="Claim register"
                title="Every published statement remains directly inspectable."
                copy="Search and evidence filters apply to both the claim register and source catalog."
              />
              <div className="obs-data-claim-grid">
                {visibleClaims.map(claim => {
                  const matchingSupports = supportsForClaim(claim).filter(support => {
                    const source = sourceById.get(support.source_id)
                    if (!source) return false
                    if (access !== 'all' && source.access_state !== access) return false
                    if (grade !== 'all' && support.grade !== grade) return false
                    return true
                  })
                  return (
                    <article key={claim.id}>
                      <div><span>{humanize(claim.kind)}</span><span>{humanize(claim.confidence.level)} confidence</span></div>
                      <h3><a href={hrefForClaim(claim.id)}>{claim.title}</a></h3>
                      <p>{claim.statement}</p>
                      <footer>
                        <span>{matchingSupports.length} matching support record{matchingSupports.length === 1 ? '' : 's'}</span>
                        <a href={hrefForClaim(claim.id)}>Inspect claim →</a>
                      </footer>
                    </article>
                  )
                })}
                {visibleClaims.length === 0 && <p className="obs-empty-copy">No claim records match these filters.</p>}
              </div>
            </section>
            <SectionHeading eyebrow="Source catalog" title="The records behind the claims." />
            <div className="obs-source-table" role="list">
              {visibleSources.slice(0, 120).map(source => {
                const sourceSupports = portfolio.supports.filter(support => support.source_id === source.id)
                return (
                  <article role="listitem" key={source.id}>
                    <div><SourceAccessBadge source={source} /><span>{source.source_date ?? 'Undated'}</span></div>
                    <h3><a href={hrefForSource(source.id)}>{source.title}</a></h3>
                    <p>{humanize(source.source_type)} · {humanize(source.excerpt_kind)}{source.publisher ? ` · ${source.publisher}` : ''}</p>
                    <div className="obs-table-supports">
                      {sourceSupports.slice(0, 3).map(support => <EvidenceChip key={support.id} support={support} compact />)}
                    </div>
                    <a href={hrefForSource(source.id)}>Open record →</a>
                  </article>
                )
              })}
              {visibleSources.length === 0 && <p className="obs-empty-copy">No source records match these filters.</p>}
            </div>
          </div>
        ) : (
          <div id="data-panel-methodology" role="tabpanel" aria-labelledby="data-tab-methodology" className="obs-methodology-room">
            <section>
              <SectionHeading eyebrow="Reproducible methods" title="Calculations and synthesis disclose their rules." />
              <div className="obs-method-grid">{portfolio.methods.map(method => <MethodCard key={method.id} method={method} />)}</div>
            </section>
            <section>
              <SectionHeading eyebrow="Known boundaries" title="Caveats, conflicts, and export gaps stay visible." />
              <div className="obs-boundary-grid">
                {portfolio.caveats.map(caveat => (
                  <article
                    className={focusedRecord === caveat.id ? 'is-focused' : undefined}
                    id={`boundary-${caveat.id}`}
                    key={caveat.id}
                    tabIndex={-1}
                  ><span>Caveat · {caveat.id}</span><h3>{caveat.label}</h3><p>{caveat.description}</p></article>
                ))}
                {portfolio.conflicts.map(conflict => (
                  <article
                    className={`is-conflict${focusedRecord === conflict.id ? ' is-focused' : ''}`}
                    id={`boundary-${conflict.id}`}
                    key={conflict.id}
                    tabIndex={-1}
                  >
                    <span>{humanize(conflict.status)} · {conflict.id}</span>
                    <h3>{conflict.title}</h3><p>{conflict.description}</p><small>{conflict.resolution}</small>
                    <div className="obs-boundary-links">
                      {conflict.source_ids.flatMap(id => {
                        const source = sourceById.get(id)
                        return source ? [<a key={`source-${id}`} href={hrefForSource(id)}>Source: {source.title}</a>] : []
                      })}
                      {conflict.affected_claim_ids.flatMap(id => {
                        const claim = claimById.get(id)
                        return claim ? [<a key={`claim-${id}`} href={hrefForClaim(id)}>Claim: {claim.title}</a>] : []
                      })}
                    </div>
                  </article>
                ))}
              </div>
            </section>
            <section>
              <SectionHeading eyebrow="Data quality" title="Coverage is reported, not implied." />
              <div className="obs-quality-grid">
                {qualityEntries().map(([key, value]) => <article key={key}><span>{humanize(key)}</span><p>{flattenQuality(value)}</p></article>)}
              </div>
            </section>
          </div>
        )}
      </section>
      <DocumentaryGallery page={page} />
    </>
  )
}

interface PageProps {
  page: PortfolioPage
  claims: PortfolioClaim[]
  lens: EvidenceLens
}

function sourceCountForClaims(claims: PortfolioClaim[]): number {
  return new Set(claims.flatMap(claim => supportsForClaim(claim).map(support => support.source_id))).size
}

export function PortfolioPageView({ page, lens }: { page: PortfolioPage; lens: EvidenceLens }) {
  const claims = claimsForPage(page)
  const identity = routeIdentity(page)
  const props = { page, claims, lens }

  if (identity.includes('brief')) return <BriefPage {...props} />
  if (identity.includes('leadership')) return <LeadershipPage {...props} />
  if (identity.includes('journey')) return <JourneyPage {...props} />
  if (identity.includes('impact')) return <ImpactPage {...props} />
  if (identity.includes('trust')) return <TrustPage {...props} />
  if (identity.includes('innovation')) return <InnovationPage {...props} />
  if (identity.includes('learn') || identity.includes('multiplication')) return <LearningPage {...props} />
  if (identity.includes('community') || identity.includes('service')) return <CommunityPage {...props} />
  if (identity.includes('data')) return <DataRoomPage {...props} />

  return (
    <>
      <PageHeader page={page} claimCount={claims.length} sourceCount={sourceCountForClaims(claims)} />
      <section className="obs-page-section"><ClaimGallery claims={claims} lens={lens} accent={pageAccent(page)} /></section>
    </>
  )
}
