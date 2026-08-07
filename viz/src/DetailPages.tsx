import { documentaryAssetForSource } from './evidence-assets'
import { RelationshipRecord } from './PortfolioPages'
import {
  ClaimCard,
  ClaimSources,
  ClaimState,
  EvidenceChip,
  MethodCard,
  SectionHeading,
  SourceAccessBadge,
  SupportPath,
} from './EvidenceUI'
import {
  caveatById,
  claimById,
  claimsForSource,
  conflictById,
  hrefForClaim,
  hrefForCaveat,
  hrefForConflict,
  hrefForMethod,
  hrefForPage,
  hrefForSource,
  humanize,
  methodById,
  methodForClaim,
  pageForClaim,
  portfolio,
  sourceById,
  supportsForClaim,
} from './portfolio-model'
import type { EvidenceLens, MethodInput, PortfolioMethod } from './portfolio-types'

function Breadcrumbs({ items }: { items: Array<{ label: string; href?: string }> }) {
  return (
    <nav className="obs-breadcrumbs" aria-label="Breadcrumb">
      <a href={hrefForPage(portfolio.pages[0])}>Brief</a>
      {items.map((item, index) => (
        <span key={`${item.label}-${index}`}>
          <i aria-hidden="true">/</i>
          {item.href ? <a href={item.href}>{item.label}</a> : <span aria-current="page">{item.label}</span>}
        </span>
      ))}
    </nav>
  )
}

export function ClaimDetailPage({ claimId, lens }: { claimId: string; lens: EvidenceLens }) {
  const claim = claimById.get(claimId)
  if (!claim) return <MissingRecord kind="claim" id={claimId} />
  const page = pageForClaim(claim)
  const supports = supportsForClaim(claim)
  const method = methodForClaim(claim)
  const caveats = claim.caveat_ids.flatMap(id => {
    const caveat = caveatById.get(id)
    return caveat ? [caveat] : []
  })
  const conflicts = claim.conflict_ids.flatMap(id => {
    const conflict = conflictById.get(id)
    return conflict ? [conflict] : []
  })
  const relationships = portfolio.relationships.filter(relationship =>
    relationship.claim_id === claim.id
    || relationship.from_claim_id === claim.id
    || relationship.to_claim_id === claim.id
  )

  return (
    <article className="obs-detail-page">
      <Breadcrumbs items={[
        ...(page ? [{ label: page.label, href: hrefForPage(page) }] : []),
        { label: claim.title },
      ]} />
      <header className="obs-detail-hero">
        <div>
          <span className="obs-detail-kicker">Claim record · {claim.id}</span>
          <ClaimState claim={claim} />
          <h1 id="detail-heading" tabIndex={-1}>{claim.title}</h1>
          <p>{claim.statement}</p>
        </div>
        {claim.metric && (
          <div className="obs-detail-metric">
            <strong>{claim.metric.display}</strong>
            {claim.metric.unit && <span>{claim.metric.unit}</span>}
            <small>{claim.period ?? 'Period declared in evidence'}</small>
          </div>
        )}
      </header>

      <section className="obs-claim-facts" aria-label="Claim boundaries">
        <div><span>Confidence</span><strong>{humanize(claim.confidence.level)}</strong><p>{claim.confidence.rationale}</p></div>
        <div><span>Attribution</span><strong>{humanize(claim.attribution)}</strong><p>{humanize(claim.scope)} scope</p></div>
        <div><span>Status</span><strong>{humanize(claim.status)}</strong><p>{claim.period ?? 'No period displayed'}</p></div>
        <div><span>Support</span><strong>{supports.length} records</strong><p>{sourcesUnique(supports.map(item => item.source_id))} unique sources</p></div>
      </section>

      <section className="obs-page-section">
        <SectionHeading
          eyebrow="Proof trail"
          title="Every supporting, qualifying, and contradictory record."
          copy="Solid lines denote direct support. Dashed lines denote aggregate, indirect, or interpretive support as declared by the dataset."
        />
        <div className="obs-support-paths">
          {supports.map(support => <SupportPath key={support.id} support={support} />)}
        </div>
        <ClaimSources claim={claim} />
      </section>

      {relationships.length > 0 && (
        <section className="obs-page-section">
          <SectionHeading
            eyebrow="Relationship context"
            title="Where this claim participates in an explicit cross-source proposition."
            copy="Each relationship exposes its endpoints, reasoning, support, method, confidence, and limitation."
          />
          <div className="obs-longitudinal-relations">
            {relationships.map((relationship, index) => (
              <RelationshipRecord key={relationship.id} relationship={relationship} index={index} />
            ))}
          </div>
        </section>
      )}

      {method && (
        <section className="obs-page-section">
          <SectionHeading eyebrow="Method record" title="How this result was produced." />
          <div className="obs-method-grid"><MethodCard method={method} /></div>
        </section>
      )}

      {(caveats.length > 0 || conflicts.length > 0) && (
        <section className="obs-page-section">
          <SectionHeading eyebrow="Interpretation boundaries" title="What this claim does not establish." />
          <div className="obs-boundary-grid">
            {caveats.map(caveat => (
              <article key={caveat.id}>
                <span>Caveat</span><h3>{caveat.label}</h3><p>{caveat.description}</p>
                <a href={hrefForCaveat(caveat.id)}>Open boundary record →</a>
              </article>
            ))}
            {conflicts.map(conflict => (
              <article className="is-conflict" key={conflict.id}>
                <span>{humanize(conflict.status)}</span><h3>{conflict.title}</h3><p>{conflict.description}</p><small>{conflict.resolution}</small>
                <div className="obs-boundary-links">
                  {conflict.source_ids.flatMap(id => {
                    const source = sourceById.get(id)
                    return source ? [<a key={id} href={hrefForSource(id)}>Source: {source.title}</a>] : []
                  })}
                  <a href={hrefForConflict(conflict.id)}>Open conflict record →</a>
                </div>
              </article>
            ))}
          </div>
        </section>
      )}

      {lens !== 'narrative' && (
        <section className="obs-page-section obs-detail-context">
          <SectionHeading eyebrow="Current lens" title={`${humanize(lens)} reading`} />
          <ClaimCard claim={claim} lens={lens} accent="violet" />
        </section>
      )}
    </article>
  )
}

export function SourceDetailPage({ sourceId }: { sourceId: string }) {
  const source = sourceById.get(sourceId)
  if (!source) return <MissingRecord kind="source" id={sourceId} />
  const claims = claimsForSource(source)
  const supports = portfolio.supports.filter(support => support.source_id === source.id)
  const asset = documentaryAssetForSource(source)

  return (
    <article className="obs-detail-page">
      <Breadcrumbs items={[{ label: 'Data Room', href: '#/data-room' }, { label: source.title }]} />
      <header className="obs-source-hero">
        <div>
          <span className="obs-detail-kicker">Source record · {source.id}</span>
          <SourceAccessBadge source={source} />
          <h1 id="detail-heading" tabIndex={-1}>{source.title}</h1>
          <p>{humanize(source.source_type)}{source.publisher ? ` · ${source.publisher}` : ''}</p>
        </div>
        <dl>
          <div><dt>Source date</dt><dd>{source.source_date ?? 'Not stated'}</dd></div>
          <div><dt>Access</dt><dd>{humanize(source.access_state)}</dd></div>
          <div><dt>Excerpt representation</dt><dd>{humanize(source.excerpt_kind)}</dd></div>
          <div><dt>Claims supported</dt><dd>{claims.length}</dd></div>
          <div><dt>Checksum scope</dt><dd>{humanize(source.checksum_scope)}</dd></div>
          <div><dt>Held artifact SHA-256</dt><dd><code>{source.sha256}</code><span>{source.checksum_note}</span></dd></div>
        </dl>
      </header>

      {asset && (
        <figure className="obs-source-document">
          <img src={asset.url} alt={asset.alt} />
          <figcaption>{source.title}</figcaption>
        </figure>
      )}

      <section className="obs-source-excerpt">
        <span>Approved public {source.excerpt_kind === 'verbatim' ? 'verbatim excerpt' : 'editorial summary'}</span>
        {source.approved_excerpt
          ? source.excerpt_kind === 'verbatim'
            ? <blockquote>“{source.approved_excerpt}”</blockquote>
            : <p>{source.approved_excerpt}</p>
          : <p>No body text is approved for public display.</p>}
        {source.external_url && (
          <a href={source.external_url} target="_blank" rel="noreferrer noopener">Open original public source ↗</a>
        )}
      </section>

      <section className="obs-page-section">
        <SectionHeading eyebrow="Claim coverage" title="What this source is used to establish." />
        <div className="obs-source-claim-list">
          {supports.map(support => {
            const claim = claimById.get(support.claim_id)
            if (!claim) return null
            return (
              <article key={support.id}>
                <EvidenceChip support={support} />
                <h3><a href={hrefForClaim(claim.id)}>{claim.title}</a></h3>
                <p>{support.rationale}</p>
                <small>{support.locator}</small>
              </article>
            )
          })}
        </div>
      </section>

      <aside className="obs-publication-boundary">
        <strong>Publication boundary</strong>
        <p>
          {source.access_state === 'private_held'
            ? 'The original artifact is held privately. This record exposes approved metadata and excerpt only.'
            : source.access_state === 'aggregate_only'
              ? 'Only aggregate information is approved for public use; individual-level material is withheld.'
              : 'This source has an approved public representation.'}
        </p>
      </aside>
    </article>
  )
}

function MethodInputRow({ input }: { input: MethodInput }) {
  const claim = input.claim_id ? claimById.get(input.claim_id) : undefined
  const source = input.source_id ? sourceById.get(input.source_id) : undefined
  return (
    <li>
      <div>
        <span>{input.label}</span>
        {(input.value !== undefined || input.unit) && <strong>{String(input.value ?? '')}{input.unit ? ` ${input.unit}` : ''}</strong>}
      </div>
      {input.locator && <p>{input.locator}</p>}
      <div className="obs-input-links">
        {claim && <a href={hrefForClaim(claim.id)}>Input claim: {claim.title}</a>}
        {source && <a href={hrefForSource(source.id)}>Input source: {source.title}</a>}
      </div>
    </li>
  )
}

function RuleList({ title, rules }: { title: string; rules: string[] }) {
  return (
    <section>
      <h3>{title}</h3>
      {rules.length > 0 ? <ul>{rules.map((rule, index) => <li key={`${title}-${index}`}>{rule}</li>)}</ul> : <p>No additional rules declared.</p>}
    </section>
  )
}

export function MethodDetailPage({ methodId }: { methodId: string }) {
  const method = methodById.get(methodId)
  if (!method) return <MissingRecord kind="method" id={methodId} />
  const outputClaims = portfolio.claims.filter(claim => claim.method_id === method.id)
  const caveats = method.caveat_ids.flatMap(id => {
    const caveat = caveatById.get(id)
    return caveat ? [caveat] : []
  })

  return (
    <article className="obs-detail-page">
      <Breadcrumbs items={[{ label: 'Data Room', href: '#/data-room' }, { label: method.title }]} />
      <header className="obs-method-hero">
        <span className="obs-detail-kicker">Method record · {method.id}</span>
        <span>{humanize(method.kind)} · version {method.version}</span>
        <h1 id="detail-heading" tabIndex={-1}>{method.title}</h1>
        <p>{method.description}</p>
        {method.formula && <pre><code>{method.formula}</code></pre>}
      </header>

      <section className="obs-page-section">
        <SectionHeading eyebrow="Declared inputs" title={`${method.inputs.length} inputs feed this method.`} />
        <ol className="obs-method-inputs">{method.inputs.map(input => <MethodInputRow key={input.id} input={input} />)}</ol>
      </section>

      <section className="obs-method-rules">
        <RuleList title="Included" rules={method.inclusion_rules} />
        <RuleList title="Excluded" rules={method.exclusion_rules} />
        <section><h3>Deduplication</h3><p>{method.deduplication}</p></section>
        <section><h3>Rounding</h3><p>{method.rounding}</p></section>
      </section>

      <section className="obs-method-result">
        <span>Declared result</span>
        <strong>{method.result}</strong>
      </section>

      {outputClaims.length > 0 && (
        <section className="obs-page-section">
          <SectionHeading eyebrow="Outputs" title="Claims produced or interpreted with this method." />
          <div className="obs-detail-link-grid">
            {outputClaims.map(claim => <a key={claim.id} href={hrefForClaim(claim.id)}><span>{humanize(claim.kind)}</span><strong>{claim.title}</strong></a>)}
          </div>
        </section>
      )}

      {caveats.length > 0 && (
        <section className="obs-page-section">
          <SectionHeading eyebrow="Method boundaries" title="Declared caveats." />
          <div className="obs-boundary-grid">{caveats.map(caveat => (
            <article key={caveat.id}>
              <span>Caveat</span><h3>{caveat.label}</h3><p>{caveat.description}</p>
              <a href={hrefForCaveat(caveat.id)}>Open boundary record →</a>
            </article>
          ))}</div>
        </section>
      )}
    </article>
  )
}

function MissingRecord({ kind, id }: { kind: string; id: string }) {
  return (
    <section className="obs-missing-record">
      <span>Record not found</span>
      <h1 id="detail-heading" tabIndex={-1}>This {kind} is not in the public portfolio.</h1>
      <p><code>{id}</code></p>
      <a href="#/data-room">Search the Data Room</a>
    </section>
  )
}

function sourcesUnique(sourceIds: string[]): number {
  return new Set(sourceIds).size
}

// Keep this type import anchored for strict TypeScript builds when the generated
// dataset contains no methods yet.
export type PublicMethodRecord = PortfolioMethod
