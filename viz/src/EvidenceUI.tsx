import type { ReactNode } from 'react'
import {
  hrefForMethod,
  hrefForSource,
  humanize,
} from './portfolio-model'
import type {
  PortfolioClaim,
  PortfolioMethod,
  PortfolioSource,
  PortfolioSupport,
} from './portfolio-types'

export function SourceAccessBadge({ source }: { source: PortfolioSource }) {
  const label: Record<PortfolioSource['access_state'], string> = {
    public_external: 'Public record',
    public_excerpt: 'Approved excerpt',
    private_held: 'Held evidence',
    aggregate_only: 'Privacy-safe aggregate',
  }
  return <span className={`obs-access-badge is-${source.access_state}`}>{label[source.access_state]}</span>
}

export function QuoteCard({ claim, source, eyebrow }: {
  claim: PortfolioClaim
  support: PortfolioSupport
  source: PortfolioSource
  eyebrow?: string
}) {
  if (!source.approved_excerpt) return null
  const isVerbatim = source.excerpt_kind === 'verbatim'
  return (
    <figure className="obs-quote-card" data-excerpt-kind={source.excerpt_kind}>
      <figcaption>{eyebrow ?? humanize(claim.category)}</figcaption>
      {isVerbatim
        ? <blockquote>“{source.approved_excerpt}”</blockquote>
        : <p className="obs-source-excerpt-copy">{source.approved_excerpt}</p>}
      <a className="obs-story-link" href={hrefForSource(source.id)}>View evidence <span aria-hidden="true">↗</span></a>
    </figure>
  )
}

export function MethodCard({ method }: { method: PortfolioMethod }) {
  return (
    <article className="obs-method-card">
      <span>{humanize(method.kind)}</span>
      <h3><a href={hrefForMethod(method.id)}>{method.title}</a></h3>
      <p>{method.description}</p>
      {method.formula && <code>{method.formula}</code>}
      <footer>
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
