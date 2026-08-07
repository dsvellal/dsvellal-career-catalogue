import type { CSSProperties, ReactNode } from 'react'
import {
  caveatById,
  claimById,
  conflictById,
  hrefForClaim,
  hrefForCaveat,
  hrefForConflict,
  hrefForMethod,
  hrefForSource,
  humanize,
  methodForClaim,
  sourceById,
  sourcesForClaim,
  supportsForClaim,
} from './portfolio-model'
import type {
  EvidenceLens,
  PortfolioClaim,
  PortfolioMethod,
  PortfolioSource,
  PortfolioSupport,
  SourceGrade,
} from './portfolio-types'

const LENS_COPY: Record<EvidenceLens, { label: string; description: string }> = {
  narrative: { label: 'Narrative', description: 'Read the executive story' },
  proof: { label: 'Proof', description: 'Expose source support' },
  method: { label: 'Method', description: 'Inspect calculations and synthesis' },
  gaps: { label: 'Gaps', description: 'Surface caveats and conflicts' },
}

export function LensControl({ lens, onChange }: {
  lens: EvidenceLens
  onChange: (lens: EvidenceLens) => void
}) {
  return (
    <div className="obs-lens" role="group" aria-label="Evidence lens">
      <span className="obs-lens-label">Evidence lens</span>
      <div className="obs-lens-options">
        {(Object.keys(LENS_COPY) as EvidenceLens[]).map(option => (
          <button
            key={option}
            type="button"
            className={`obs-lens-button${lens === option ? ' is-active' : ''}`}
            aria-pressed={lens === option}
            title={LENS_COPY[option].description}
            onClick={() => onChange(option)}
          >
            <span>{LENS_COPY[option].label}</span>
          </button>
        ))}
      </div>
    </div>
  )
}

function supportTone(grade: SourceGrade): string {
  if (grade === 'corroborated') return 'teal'
  if (grade === 'documented') return 'cobalt'
  return 'copper'
}

export function EvidenceChip({ support, compact = false }: {
  support: PortfolioSupport
  compact?: boolean
}) {
  const relation = support.relationship === 'supports' ? support.grade : support.relationship
  return (
    <span
      className={`obs-evidence-chip tone-${supportTone(support.grade)}${compact ? ' is-compact' : ''}`}
      data-directness={support.directness}
      title={`${humanize(support.grade)} · ${humanize(support.directness)} · ${humanize(support.relationship)}`}
    >
      <span className="obs-chip-line" aria-hidden="true" />
      {humanize(relation)}
    </span>
  )
}

export function ClaimState({ claim }: { claim: PortfolioClaim }) {
  return (
    <span className={`obs-claim-state is-${claim.kind}`}>
      {humanize(claim.kind)} claim
    </span>
  )
}

function ClaimLensBody({ claim, lens }: { claim: PortfolioClaim; lens: EvidenceLens }) {
  const supports = supportsForClaim(claim)
  const method = methodForClaim(claim)

  if (lens === 'proof') {
    return (
      <div className="obs-card-proof">
        {supports.length === 0 ? (
          <p className="obs-empty-copy">No public support record is attached.</p>
        ) : supports.slice(0, 4).map(support => {
          const source = sourceById.get(support.source_id)
          return (
            <div className="obs-card-proof-row" key={support.id}>
              <EvidenceChip support={support} compact />
              {source
                ? <a href={hrefForSource(source.id)}>{source.title}</a>
                : <span>{support.source_id}</span>}
            </div>
          )
        })}
        {supports.length > 4 && <span className="obs-more-count">+{supports.length - 4} support records</span>}
      </div>
    )
  }

  if (lens === 'method') {
    return method ? (
      <div className="obs-method-peek">
        <span>{humanize(method.kind)} · v{method.version}</span>
        <p>{method.description}</p>
        <a href={hrefForMethod(method.id)}>Open method →</a>
      </div>
    ) : (
      <p className="obs-empty-copy">No separate method record is attached to this claim.</p>
    )
  }

  if (lens === 'gaps') {
    const caveats = claim.caveat_ids.flatMap(id => {
      const caveat = caveatById.get(id)
      return caveat ? [caveat] : []
    })
    const conflicts = claim.conflict_ids.flatMap(id => {
      const conflict = conflictById.get(id)
      return conflict ? [conflict] : []
    })
    return (
      <div className="obs-gap-peek">
        <strong>{humanize(claim.confidence.level)} confidence</strong>
        <p>{claim.confidence.rationale}</p>
        {caveats.slice(0, 2).map(caveat => <a href={hrefForCaveat(caveat.id)} key={caveat.id}>△ {caveat.label}</a>)}
        {conflicts.slice(0, 2).map(conflict => <a href={hrefForConflict(conflict.id)} className="is-conflict" key={conflict.id}>! {conflict.title}</a>)}
      </div>
    )
  }

  return <p className="obs-claim-statement">{claim.statement}</p>
}

export function ClaimCard({
  claim,
  lens,
  accent = 'cobalt',
  compact = false,
  index,
}: {
  claim: PortfolioClaim
  lens: EvidenceLens
  accent?: string
  compact?: boolean
  index?: number
}) {
  const supports = supportsForClaim(claim)
  const firstCaveat = claim.caveat_ids.flatMap(id => {
    const caveat = caveatById.get(id)
    return caveat ? [caveat] : []
  })[0]
  return (
    <article
      className={`obs-claim-card accent-${accent}${compact ? ' is-compact' : ''}`}
      style={{ '--card-order': index ?? 0 } as CSSProperties}
    >
      <div className="obs-claim-meta">
        <ClaimState claim={claim} />
        <span className={`obs-card-confidence is-${claim.confidence.level}`}>{humanize(claim.confidence.level)} confidence</span>
        <span>{humanize(claim.scope)}</span>
        {claim.period && <span>{claim.period}</span>}
        {firstCaveat && <a className="obs-card-caveat" href={hrefForCaveat(firstCaveat.id)}>△ {firstCaveat.label}</a>}
      </div>
      {claim.metric && (
        <a className="obs-claim-metric" href={hrefForClaim(claim.id)} aria-label={`${claim.title}: ${claim.metric.display}`}>
          {claim.metric.display}
          {claim.metric.unit && <small>{claim.metric.unit}</small>}
        </a>
      )}
      <h3><a href={hrefForClaim(claim.id)}>{claim.title}</a></h3>
      <ClaimLensBody claim={claim} lens={lens} />
      <footer className="obs-claim-footer">
        <span>{supports.length} support{supports.length === 1 ? '' : 's'} · {humanize(claim.attribution)}</span>
        <a href={hrefForClaim(claim.id)}>Inspect claim <span aria-hidden="true">↗</span></a>
      </footer>
    </article>
  )
}

export function SourceAccessBadge({ source }: { source: PortfolioSource }) {
  const label: Record<PortfolioSource['access_state'], string> = {
    public_external: 'Public source',
    public_excerpt: 'Approved excerpt',
    private_held: 'Privately held',
    aggregate_only: 'Aggregate only',
  }
  return <span className={`obs-access-badge is-${source.access_state}`}>{label[source.access_state]}</span>
}

export function SourceCard({ source, support }: {
  source: PortfolioSource
  support?: PortfolioSupport
}) {
  return (
    <article className="obs-source-card">
      <div className="obs-source-card-top">
        <SourceAccessBadge source={source} />
        <span>{source.source_date ?? 'Undated'}</span>
      </div>
      <h3><a href={hrefForSource(source.id)}>{source.title}</a></h3>
      {support && <EvidenceChip support={support} />}
      {source.approved_excerpt && <p>{source.approved_excerpt}</p>}
      <footer>
        <span>{humanize(source.source_type)} · {humanize(source.excerpt_kind)}</span>
        <a href={hrefForSource(source.id)}>Source record →</a>
      </footer>
    </article>
  )
}

export function QuoteCard({ claim, support, source, eyebrow }: {
  claim: PortfolioClaim
  support: PortfolioSupport
  source: PortfolioSource
  eyebrow?: string
}) {
  if (!source.approved_excerpt) return null
  const isVerbatim = source.excerpt_kind === 'verbatim'
  return (
    <figure className="obs-quote-card" data-excerpt-kind={source.excerpt_kind}>
      <figcaption>
        <span>{eyebrow ?? humanize(claim.category)} · {isVerbatim ? 'verbatim excerpt' : 'editorial summary'}</span>
        <EvidenceChip support={support} compact />
      </figcaption>
      {isVerbatim
        ? <blockquote>“{source.approved_excerpt}”</blockquote>
        : <p className="obs-source-excerpt-copy">{source.approved_excerpt}</p>}
      <div className="obs-quote-links">
        <a href={hrefForClaim(claim.id)}>Why this matters</a>
        <a href={hrefForSource(source.id)}>Source record</a>
      </div>
    </figure>
  )
}

export function MethodCard({ method }: { method: PortfolioMethod }) {
  return (
    <article className="obs-method-card">
      <span>{humanize(method.kind)} · v{method.version}</span>
      <h3><a href={hrefForMethod(method.id)}>{method.title}</a></h3>
      <p>{method.description}</p>
      {method.formula && <code>{method.formula}</code>}
      <footer>
        <span>{method.inputs.length} declared input{method.inputs.length === 1 ? '' : 's'}</span>
        <a href={hrefForMethod(method.id)}>Inspect method →</a>
      </footer>
    </article>
  )
}

export function SectionHeading({ eyebrow, title, copy, action, id }: {
  eyebrow: string
  title: string
  copy?: string
  action?: ReactNode
  id?: string
}) {
  return (
    <header className="obs-section-heading">
      <div>
        <span>{eyebrow}</span>
        <h2 id={id}>{title}</h2>
        {copy && <p>{copy}</p>}
      </div>
      {action && <div>{action}</div>}
    </header>
  )
}

export function SupportPath({ support }: { support: PortfolioSupport }) {
  const claim = claimById.get(support.claim_id)
  const source = sourceById.get(support.source_id)
  if (!claim || !source) return null
  const isSolid = support.directness === 'direct'
  return (
    <article className="obs-support-path" data-line={isSolid ? 'solid' : 'dashed'}>
      <a className="obs-path-node is-claim" href={hrefForClaim(claim.id)}>
        <span>Claim</span>
        <strong>{claim.title}</strong>
      </a>
      <div className="obs-path-edge">
        <span aria-hidden="true" />
        <EvidenceChip support={support} compact />
        <small>{support.rationale}</small>
      </div>
      <a className="obs-path-node is-source" href={hrefForSource(source.id)}>
        <span>Source</span>
        <strong>{source.title}</strong>
      </a>
    </article>
  )
}

export function ClaimSources({ claim }: { claim: PortfolioClaim }) {
  const sources = sourcesForClaim(claim)
  return (
    <div className="obs-source-grid">
      {sources.map(source => {
        const support = supportsForClaim(claim).find(item => item.source_id === source.id)
        return <SourceCard key={source.id} source={source} support={support} />
      })}
    </div>
  )
}
