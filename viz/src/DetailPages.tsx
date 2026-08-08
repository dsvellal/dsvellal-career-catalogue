import { documentaryAssetForSource, profilePhoto } from './evidence-assets'
import {
  MethodCard,
  SectionHeading,
} from './EvidenceUI'
import {
  auditOnlyClaimIds,
  caveatById,
  claimById,
  claimsForSource,
  conflictById,
  hrefForClaim,
  hrefForMethod,
  hrefForPage,
  hrefForSource,
  humanize,
  methodById,
  methodForClaim,
  pageForClaim,
  portfolio,
  sourceById,
  storyClaimIds,
  storyBlockForPrimaryClaim,
  storyMethodIds,
  storySourceIds,
  supportsForClaim,
} from './portfolio-model'
import type {
  MethodInput,
  PortfolioClaim,
  PortfolioMethod,
  PortfolioSource,
  PortfolioSupport,
} from './portfolio-types'

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

function DetailPortrait() {
  return (
    <figure className="obs-detail-portrait">
      <img src={profilePhoto} alt="" />
      <figcaption>
        <strong>Datta Vellal</strong>
        <span>Evidence-backed leadership</span>
      </figcaption>
    </figure>
  )
}

export function ClaimDetailPage({ claimId }: { claimId: string }) {
  const claim = claimById.get(claimId)
  if (!claim || auditOnlyClaimIds.has(claimId)) return <MissingRecord kind="claim" id={claimId} />
  const page = pageForClaim(claim)
  const storyBlock = storyBlockForPrimaryClaim(claim.id)
  const foldedClaims = (storyBlock?.folded_claim_ids ?? []).flatMap(id => {
    const foldedClaim = claimById.get(id)
    return foldedClaim ? [foldedClaim] : []
  })
  const inspectionClaims = [claim, ...foldedClaims]
  const supports = [
    ...new Map(
      inspectionClaims.flatMap(item => supportsForClaim(item)).map(support => [support.id, support]),
    ).values(),
  ]
  const methods = [
    ...new Map(
      inspectionClaims.flatMap(item => {
        const method = methodForClaim(item)
        return method ? [[method.id, method] as const] : []
      }),
    ).values(),
  ]
  const executiveTitle = displayTitleForClaim(claim)
  const executiveMeaning = storyBlock?.proof ?? displaySummaryForClaim(claim)
  const whyThisMatters = storyBlock?.meaning
  const caveatIds = [...new Set(inspectionClaims.flatMap(item => item.caveat_ids))]
  const caveats = caveatIds.flatMap(id => {
    const caveat = caveatById.get(id)
    return caveat ? [caveat] : []
  })
  const conflictIds = [...new Set(inspectionClaims.flatMap(item => item.conflict_ids))]
  const conflicts = conflictIds.flatMap(id => {
    const conflict = conflictById.get(id)
    return conflict ? [conflict] : []
  })
  const sourceEvidence = groupSupportsBySource(supports)

  return (
    <article className="obs-detail-page">
      <Breadcrumbs items={[
        ...(page ? [{ label: page.label, href: hrefForPage(page) }] : []),
        { label: executiveTitle },
      ]} />
      <header className="obs-detail-hero">
        <div>
          <DetailPortrait />
          <span className="obs-detail-kicker">Evidence-backed impact{page ? ` · ${page.label}` : ''}</span>
          <h1 id="detail-heading" tabIndex={-1}>{executiveTitle}</h1>
          <p>{executiveMeaning}</p>
        </div>
      </header>

      <section className="obs-page-section obs-claim-inspection" aria-label="Claim explanation and evidence">
        {whyThisMatters && (
          <details className="obs-inspection-panel" open>
            <summary>
              <span>Why this matters</span>
              <small>Leadership meaning</small>
            </summary>
            <div className="obs-inspection-body">
              <p className="obs-claim-statement">{whyThisMatters}</p>
            </div>
          </details>
        )}

        <details className="obs-inspection-panel">
          <summary>
            <span>Evidence behind it</span>
            <small>
              {sourceEvidence.length} source{sourceEvidence.length === 1 ? '' : 's'}
              {foldedClaims.length > 0 ? ` · ${foldedClaims.length} supporting conclusions` : ''}
            </small>
          </summary>
          <div className="obs-inspection-body">
            {foldedClaims.length > 0 && (
              <details className="obs-supporting-conclusions">
                <summary>
                  <span>Supporting conclusions</span>
                  <small>{foldedClaims.length}</small>
                </summary>
                <div className="obs-detail-link-grid">
                  {foldedClaims.map(foldedClaim => (
                    <a key={foldedClaim.id} href={hrefForClaim(foldedClaim.id)}>
                      <span>Supporting conclusion</span>
                      <strong>{displayTitleForClaim(foldedClaim)}</strong>
                    </a>
                  ))}
                </div>
              </details>
            )}
            <div className="obs-source-claim-list">
              {sourceEvidence.map(({ source, supports: sourceSupports }) => (
                <article key={source.id}>
                  <div className="obs-source-card-top">
                    <SourceAccessLabel source={source} />
                    <span>{source.source_date ?? 'Date in source record'}</span>
                  </div>
                  <h3><a href={hrefForSource(source.id)}>{source.title}</a></h3>
                  {sourceSupports.map(support => {
                    const supportedClaim = claimById.get(support.claim_id)
                    return (
                      <div key={support.id}>
                        <p>{support.rationale}</p>
                        <small>
                          {supportedClaim ? `${displayTitleForClaim(supportedClaim)} · ` : ''}
                          {support.locator}
                        </small>
                      </div>
                    )
                  })}
                  <a href={hrefForSource(source.id)}>Open source record →</a>
                </article>
              ))}
            </div>
          </div>
        </details>

        {methods.length > 0 && (
          <details className="obs-inspection-panel">
            <summary>
              <span>How it was derived</span>
              <small>{methods.length} method{methods.length === 1 ? '' : 's'}</small>
            </summary>
            <div className="obs-inspection-body">
              <div className="obs-method-grid">
                {methods.map(method => <MethodCard key={method.id} method={method} />)}
              </div>
            </div>
          </details>
        )}

        <details className="obs-inspection-panel">
          <summary>
            <span>Scope &amp; definitions</span>
            <small>Reading context</small>
          </summary>
          <div className="obs-inspection-body">
            <dl className="obs-claim-scope">
              <div><dt>Period</dt><dd>{claim.period ?? 'Date in source record'}</dd></div>
              <div><dt>Scope</dt><dd>{humanize(claim.scope)}</dd></div>
              <div><dt>Attribution</dt><dd>{humanize(claim.attribution)}</dd></div>
              <div><dt>Record ID</dt><dd><code>{claim.id}</code></dd></div>
            </dl>

            {(caveats.length > 0 || conflicts.length > 0) && (
              <div className="obs-boundary-grid">
                {caveats.map(caveat => (
                  <article key={caveat.id}>
                    <span>Context note</span><h3>{scopeNoteFor(caveat.id, caveat.label, caveat.description).title}</h3><p>{scopeNoteFor(caveat.id, caveat.label, caveat.description).copy}</p>
                    <details className="obs-technical-record">
                      <summary>Technical record</summary>
                      <p>{caveat.description}</p>
                      <code>{caveat.id}</code>
                    </details>
                  </article>
                ))}
                {conflicts.map(conflict => (
                  <article key={conflict.id}>
                    <span>Source reconciliation</span><h3>{reconciliationFor(conflict.id, conflict.title, conflict.resolution).title}</h3><p>{reconciliationFor(conflict.id, conflict.title, conflict.resolution).copy}</p>
                    <div className="obs-boundary-links">
                      {conflict.source_ids.flatMap(id => {
                        const source = sourceById.get(id)
                        return source && storySourceIds.has(id) ? [<a key={id} href={hrefForSource(id)}>Source: {source.title}</a>] : []
                      })}
                    </div>
                    <details className="obs-technical-record">
                      <summary>Technical record</summary>
                      <p>{conflict.description}</p>
                      <small>{conflict.resolution}</small>
                      <code>{conflict.id}</code>
                    </details>
                  </article>
                ))}
              </div>
            )}
          </div>
        </details>
      </section>
    </article>
  )
}

export function SourceDetailPage({ sourceId }: { sourceId: string }) {
  const source = sourceById.get(sourceId)
  if (!source || !storySourceIds.has(sourceId)) return <MissingRecord kind="source" id={sourceId} />
  const claims = claimsForSource(source).filter(claim => storyClaimIds.has(claim.id))
  const supports = portfolio.supports.filter(support => support.source_id === source.id && storyClaimIds.has(support.claim_id))
  const inputMethods = portfolio.methods.filter(method =>
    storyMethodIds.has(method.id) && method.inputs.some(input => input.source_id === source.id),
  )
  const reconciliationClaims = portfolio.claims.filter(claim =>
    storyClaimIds.has(claim.id)
    && claim.conflict_ids.some(id => conflictById.get(id)?.source_ids.includes(source.id)),
  )
  const asset = documentaryAssetForSource(source)

  return (
    <article className="obs-detail-page">
      <Breadcrumbs items={[{ label: 'Data Room', href: '#/data-room' }, { label: source.title }]} />
      <header className="obs-source-hero">
        <div>
          <DetailPortrait />
          <span className="obs-detail-kicker">Source record · {source.id}</span>
          <SourceAccessLabel source={source} />
          <h1 id="detail-heading" tabIndex={-1}>{source.title}</h1>
          <p>{humanize(source.source_type)}{source.publisher ? ` · ${source.publisher}` : ''}</p>
        </div>
        <dl>
          <div><dt>Source date</dt><dd>{source.source_date ?? 'Date in source record'}</dd></div>
          <div><dt>Evidence access</dt><dd>{sourceAccessText(source)}</dd></div>
          <div><dt>Public representation</dt><dd>{humanize(source.excerpt_kind)}</dd></div>
          <div><dt>Direct claim support</dt><dd>{claims.length}</dd></div>
          <div><dt>Method inputs</dt><dd>{inputMethods.length}</dd></div>
          <div><dt>Reconciliations</dt><dd>{reconciliationClaims.length}</dd></div>
          <div><dt>Checksum scope</dt><dd>{humanize(source.checksum_scope)}</dd></div>
          <div><dt>Held evidence SHA-256</dt><dd><code>{source.sha256}</code><span>{source.checksum_note}</span></dd></div>
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
          : <p>This source is represented through its approved metadata.</p>}
        {source.external_url && (
          <a href={source.external_url} target="_blank" rel="noreferrer noopener">Open original public source ↗</a>
        )}
      </section>

      {supports.length > 0 && (
        <section className="obs-page-section">
          <SectionHeading eyebrow="Claim coverage" title="What this source is used to establish directly." />
          <div className="obs-source-claim-list">
            {supports.map(support => {
              const claim = claimById.get(support.claim_id)
              if (!claim) return null
              return (
                <article key={support.id}>
                  <span className="obs-detail-kicker">Evidence link</span>
                  <h3><a href={hrefForClaim(claim.id)}>{displayTitleForClaim(claim)}</a></h3>
                  <p>{support.rationale}</p>
                  <small>{support.locator}</small>
                </article>
              )
            })}
          </div>
        </section>
      )}

      {(inputMethods.length > 0 || reconciliationClaims.length > 0) && (
        <section className="obs-page-section">
          <SectionHeading eyebrow="Traceability usage" title="Where this source enters the published reasoning." />
          <div className="obs-detail-link-grid">
            {inputMethods.map(method => (
              <a key={method.id} href={hrefForMethod(method.id)}>
                <span>Method input</span>
                <strong>{method.title}</strong>
              </a>
            ))}
            {reconciliationClaims.map(claim => (
              <a key={claim.id} href={hrefForClaim(claim.id)}>
                <span>Source reconciliation</span>
                <strong>{displayTitleForClaim(claim)}</strong>
              </a>
            ))}
          </div>
        </section>
      )}

      <aside className="obs-publication-boundary">
        <strong>Evidence access</strong>
        <p>
          {source.access_state === 'private_held'
            ? 'This record presents approved metadata and an excerpt from the held evidence while preserving confidential context.'
            : source.access_state === 'aggregate_only'
              ? 'This record presents a privacy-safe aggregate designed to preserve participant confidentiality.'
              : 'This source has an approved public representation and can be traced through the record above.'}
        </p>
      </aside>
    </article>
  )
}

function MethodInputRow({ input }: { input: MethodInput }) {
  const claim = input.claim_id && storyClaimIds.has(input.claim_id) ? claimById.get(input.claim_id) : undefined
  const source = input.source_id && storySourceIds.has(input.source_id) ? sourceById.get(input.source_id) : undefined
  return (
    <li>
      <div>
        <span>{input.label}</span>
        {(input.value !== undefined || input.unit) && <strong>{String(input.value ?? '')}{input.unit ? ` ${input.unit}` : ''}</strong>}
      </div>
      {input.locator && <p>{input.locator}</p>}
      <div className="obs-input-links">
        {claim && <a href={hrefForClaim(claim.id)}>Input claim: {displayTitleForClaim(claim)}</a>}
        {source && <a href={hrefForSource(source.id)}>Input source: {source.title}</a>}
      </div>
    </li>
  )
}

function RuleList({ title, rules }: { title: string; rules: string[] }) {
  return (
    <section>
      <h3>{title}</h3>
      {rules.length > 0 ? <ul>{rules.map((rule, index) => <li key={`${title}-${index}`}>{rule}</li>)}</ul> : <p>Core method definition applies.</p>}
    </section>
  )
}

export function MethodDetailPage({ methodId }: { methodId: string }) {
  const method = methodById.get(methodId)
  if (!method || !storyMethodIds.has(methodId)) return <MissingRecord kind="method" id={methodId} />
  const outputClaims = portfolio.claims.filter(claim => storyClaimIds.has(claim.id) && claim.method_id === method.id)
  const caveats = method.caveat_ids.flatMap(id => {
    const caveat = caveatById.get(id)
    return caveat ? [caveat] : []
  })

  return (
    <article className="obs-detail-page">
      <Breadcrumbs items={[{ label: 'Data Room', href: '#/data-room' }, { label: method.title }]} />
      <header className="obs-method-hero">
        <DetailPortrait />
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
        <RuleList title="Scope exclusions" rules={method.exclusion_rules} />
        <section><h3>Deduplication</h3><p>{method.deduplication}</p></section>
        <section><h3>Rounding</h3><p>{method.rounding}</p></section>
      </section>

      <section className="obs-method-result">
        <span>Declared result</span>
        <strong>{method.result}</strong>
      </section>

      {outputClaims.length > 0 && (
        <section className="obs-page-section">
          <SectionHeading eyebrow="Outputs" title="Conclusions supported by this method." />
          <div className="obs-detail-link-grid">
            {outputClaims.map(claim => <a key={claim.id} href={hrefForClaim(claim.id)}><span>Supported conclusion</span><strong>{displayTitleForClaim(claim)}</strong></a>)}
          </div>
        </section>
      )}

      {caveats.length > 0 && (
        <section className="obs-page-section">
          <SectionHeading eyebrow="Scope & definitions" title="Interpretation notes." />
          <div className="obs-boundary-grid">{caveats.map(caveat => (
            <article key={caveat.id}>
              <span>Context note</span><h3>{scopeNoteFor(caveat.id, caveat.label, caveat.description).title}</h3><p>{scopeNoteFor(caveat.id, caveat.label, caveat.description).copy}</p>
              <details className="obs-technical-record">
                <summary>Technical record</summary>
                <p>{caveat.description}</p>
                <code>{caveat.id}</code>
              </details>
            </article>
          ))}</div>
        </section>
      )}
    </article>
  )
}

function MissingRecord({ kind }: { kind: string; id: string }) {
  return (
    <section className="obs-missing-record">
      <DetailPortrait />
      <span>Explore the evidence portfolio</span>
      <h1 id="detail-heading" tabIndex={-1}>Browse the available {kind} records.</h1>
      <a href="#/data-room">Search the Data Room</a>
    </section>
  )
}

interface ScopePresentation {
  title: string
  copy: string
}

const SCOPE_PRESENTATION: Record<string, ScopePresentation> = {
  'caveat-calendar-span-not-tenure': {
    title: 'Inclusive calendar-year coverage',
    copy: 'Measure: calendar years touched from 2007 through 2026, counted inclusively.',
  },
  'caveat-response-unit': {
    title: 'Response-record unit',
    copy: 'Unit: one submitted row in a source dataset. A person may contribute across recorded interactions, while attendance is measured separately.',
  },
  'caveat-rating-observation-unit': {
    title: 'Question-level rating unit',
    copy: 'Unit: one answer to one rating question. A respondent may contribute several rating observations.',
  },
  'caveat-qualitative-entry-unit': {
    title: 'Qualitative field-value unit',
    copy: 'Unit: one populated qualitative field. A response may contribute several entries.',
  },
  'caveat-surveys-separated': {
    title: 'Pre-session surveys reported separately',
    copy: 'Population: two pre-session surveys sit beside the post-session feedback analysis as a distinct group.',
  },
  'caveat-category-labels': {
    title: 'Filename-derived topic categories',
    copy: 'Classification: the current rule set assigns one filename-pattern-derived category to each file; overlapping lexical themes sit outside this single-label taxonomy.',
  },
  'caveat-private-held-source': {
    title: 'Held-evidence representation',
    copy: 'Access: the public record provides the approved excerpt, hash, metadata, and locator for the held evidence.',
  },
  'caveat-self-authored-source': {
    title: 'First-party evidence',
    copy: 'Attribution: this source records Datta’s own account and is presented as first-party evidence.',
  },
  'caveat-team-attribution': {
    title: 'Team and program attribution',
    copy: 'Attribution: the outcome belongs to the team or program; the claim focuses on Datta’s evidenced contribution.',
  },
  'caveat-potential-not-realized': {
    title: 'Estimated potential value',
    copy: 'Measure: announced potential annual portfolio value expressed in hours and euros.',
  },
  'caveat-initiative-scope': {
    title: 'Initiative-specific measure',
    copy: 'Scope: Sutra describes one initiative; XITE describes the aggregate portfolio estimate.',
  },
  'caveat-non-causal-synthesis': {
    title: 'Longitudinal concordance',
    copy: 'Interpretation: the time-ordered evidence supports recurrence, concordance, or plausible lineage; causation sits outside this evidence design.',
  },
  'caveat-assessment-not-performance': {
    title: 'Assessment interpretation',
    copy: 'Scope: the assessment records preferences, while later similar language is treated as concordance. Capability validation sits outside this measure.',
  },
  'caveat-selected-evidence': {
    title: 'Representative evidence path',
    copy: 'Coverage: the relationship path uses reviewed representative sources selected for the stated proposition.',
  },
  'caveat-patent-scope': {
    title: 'Patent lineage and co-inventorship',
    copy: 'Scope: the record links a 2010 first-application recognition to a public grant for the same invention and names Datta among three inventors. Commercial outcomes, adoption, revenue, current legal status, and sole inventorship sit outside this record.',
  },
  'caveat-touchpoints-not-people': {
    title: 'Recorded touchpoints',
    copy: 'Unit: conversation and participant totals represent recorded touchpoints and can include repeat participation.',
  },
  'caveat-active-years-with-gaps': {
    title: 'Ten recorded program years',
    copy: 'Coverage: ten active years are recorded across 2014–2026; 2020–2021 and 2024 remain outside the reviewed program records and unquantified.',
  },
  'caveat-currency-not-normalized': {
    title: 'Nominal rupee values',
    copy: 'Currency basis: annual rupee amounts are presented in nominal terms; inflation and exchange-rate normalization sit outside this measure.',
  },
  'caveat-identity-withheld': {
    title: 'Privacy-protected continuity',
    copy: 'Privacy: the public record protects identity and individual contribution amounts while preserving the cross-record continuity signal.',
  },
  'caveat-inference-not-motive': {
    title: 'Cross-context participation signal',
    copy: 'Interpretation: recorded cross-context participation supplies the trust signal; participant motive remains outside the available evidence.',
  },
  'caveat-export-gap': {
    title: 'Retrieved graph coverage',
    copy: 'Coverage: the graph reflects retrieved provenance, while each portfolio claim maintains its own source-linked traceability.',
  },
  'caveat-source-label-conflict': {
    title: 'Versioned source definitions',
    copy: 'Reconciliation: the current method aligns legacy summaries that used different units or labels.',
  },
  'caveat-feedback-not-longitudinal': {
    title: 'Cross-sectional feedback design',
    copy: 'Design: observations at different dates generally represent different participants and sessions.',
  },
  'caveat-session-tracker-boundary': {
    title: 'Reviewed-tracker coverage',
    copy: 'Coverage: counts reflect available reviewed tracker records and provide a documented lower bound for activity.',
  },
  'caveat-student-tracker-separate': {
    title: 'Separate community-teaching tracker',
    copy: 'Population: the 13-form community-teaching tracker is reported separately from professional feedback and the talks ledger.',
  },
  'caveat-student-response-rows': {
    title: 'Student response-row unit',
    copy: 'Unit: the 494 figure represents submitted response rows; unique-participant and attendance measures come from separate evidence.',
  },
  'caveat-student-context-boundary': {
    title: 'Six institutions and one corporate context',
    copy: 'Context: the seven settings comprise six educational institutions and one Exeter corporate yoga session.',
  },
  'caveat-student-rating-scales': {
    title: 'Original rating scales preserved',
    copy: 'Method: 5-point and 10-point presenter ratings retain their original scales and separate response populations; weighted means retain source rounding.',
  },
  'caveat-recommendation-not-nps': {
    title: 'Recommendation-likelihood mean',
    copy: 'Measure: 8.87/10 is the arithmetic mean of recommendation-likelihood ratings; NPS classification sits outside the available fields.',
  },
  'caveat-360-benchmark-scope': {
    title: '2020 company comparison',
    copy: 'Benchmark: deltas compare other-rater averages with the company-average column in the 2020 assessment as a source-specific historical comparison.',
  },
}

const RECONCILIATION_PRESENTATION: Record<string, ScopePresentation> = {
  'conflict-session-population-accounting': {
    title: 'Analysis population',
    copy: 'Version 1 uses 88 post-event or interaction files after duplicate handling and reports two pre-session surveys separately.',
  },
  'conflict-session-rating-units': {
    title: 'Rating observation unit',
    copy: 'The published formula sums question-level rating counts across the 88-file analysis population.',
  },
  'conflict-session-year-count': {
    title: 'Recorded calendar range',
    copy: 'The portfolio reports the evidence-backed date range of 2018–2026.',
  },
  'conflict-session-category-counts': {
    title: 'Category population',
    copy: 'Category counts use the 88-file analysis population and represent filename-pattern-derived file counts.',
  },
  'conflict-career-duration-labels': {
    title: 'Inclusive career coverage',
    copy: 'The portfolio reports the reproducible measure as 20 inclusive calendar years touched.',
  },
  'conflict-jscpd-causality': {
    title: 'JSCPD evidence design',
    copy: 'The current presentation limits JSCPD to the evidence-supported observation; causal effect sits outside the available design.',
  },
  'conflict-sutra-onboarding-arithmetic': {
    title: 'Sutra baseline definition',
    copy: 'Published Sutra evidence focuses on traceability and attributed AI delivery while onboarding arithmetic awaits a shared baseline definition.',
  },
  'conflict-sutra-zero-quality-boundary': {
    title: 'Observed quality controls',
    copy: 'The evidence records commit gates and external quality tooling; the conclusion is confined to those observed controls.',
  },
}

function scopeNoteFor(id: string, fallbackTitle: string, fallbackCopy: string): ScopePresentation {
  return SCOPE_PRESENTATION[id] ?? { title: fallbackTitle, copy: fallbackCopy }
}

function reconciliationFor(
  id: string,
  fallbackTitle: string,
  fallbackCopy: string,
): ScopePresentation {
  return RECONCILIATION_PRESENTATION[id] ?? { title: fallbackTitle, copy: fallbackCopy }
}

function displayTitleForClaim(claim: PortfolioClaim): string {
  const presentationTitles: Record<string, string> = {
    'claim-session-post-datasets': 'Nine years of structured feedback evidence',
    'claim-session-rating-observations': 'Question-level ratings strengthen the feedback picture',
    'claim-session-qualitative-entries': 'Written feedback adds depth to participant evidence',
    'claim-student-feedback-coverage': 'Community-teaching feedback spans seven settings',
    'claim-student-recommendation-likelihood': 'Learners showed strong recommendation intent',
    'claim-book-program-growth': 'Giving grew across recorded endpoints',
    'claim-xite-potential-hours': 'Portfolio opportunity includes 18,000 productivity hours',
    'claim-sutra-traceability': 'AI delivery improved traceability by more than 90%',
    'claim-sutra-delivery-recognition': 'AI delivery earned organizational recognition',
    'claim-session-dora-feedback': 'DORA learning drew measured participant feedback',
    'claim-2019-practical-feedback-request': 'Learners asked for more relevant examples and practice',
    'claim-2026-hands-on-depth-request': 'Learners asked for deeper hands-on AI practice',
  }
  return storyBlockForPrimaryClaim(claim.id)?.title ?? presentationTitles[claim.id] ?? claim.title
}

function displaySummaryForClaim(claim: PortfolioClaim): string {
  const presentationSummaries: Record<string, string> = {
    'claim-session-post-datasets': 'The feedback corpus provides a multi-year evidence base with a clearly defined analysis population.',
    'claim-session-rating-observations': 'Question-level ratings add a reproducible quantitative dimension to participant feedback.',
    'claim-session-qualitative-entries': 'Written participant input adds qualitative depth to the learning record.',
    'claim-student-feedback-coverage': 'A privacy-safe community-teaching tracker spans six educational institutions and one corporate context.',
    'claim-student-recommendation-likelihood': 'Learners recorded an 8.87/10 mean likelihood to recommend on the original source scale.',
    'claim-book-program-growth': 'Recorded education-material support increased across the 2014 and 2026 endpoints.',
    'claim-xite-potential-hours': 'The announced portfolio estimate identifies approximately 18,000 potential productivity hours across eight initiatives.',
    'claim-sutra-traceability': 'The initiative record reports a 90%+ improvement in traceability.',
    'claim-sutra-delivery-recognition': 'Organizational recognition connects AI delivery with learning and collaboration.',
    'claim-session-dora-feedback': 'DORA learning generated structured participant-feedback records in 2025.',
    'claim-2019-practical-feedback-request': 'Participant feedback requested more relevant examples and hands-on depth, providing direction for later iterations.',
    'claim-2026-hands-on-depth-request': 'Recent participant feedback signals strong demand for additional hands-on agent practice.',
  }
  return presentationSummaries[claim.id] ?? claim.statement
}

function sourceAccessText(source: PortfolioSource): string {
  const labels: Record<PortfolioSource['access_state'], string> = {
    public_external: 'Public evidence',
    public_excerpt: 'Approved evidence excerpt',
    private_held: 'Held evidence',
    aggregate_only: 'Privacy-safe aggregate',
  }
  return labels[source.access_state]
}

function SourceAccessLabel({ source }: { source: PortfolioSource }) {
  return <span className={`obs-access-badge is-${source.access_state}`}>{sourceAccessText(source)}</span>
}

function groupSupportsBySource(supports: PortfolioSupport[]): Array<{
  source: PortfolioSource
  supports: PortfolioSupport[]
}> {
  const grouped = new Map<string, { source: PortfolioSource; supports: PortfolioSupport[] }>()
  supports.forEach(support => {
    const source = sourceById.get(support.source_id)
    if (!source) return
    const group = grouped.get(source.id)
    if (group) {
      group.supports.push(support)
    } else {
      grouped.set(source.id, { source, supports: [support] })
    }
  })
  return [...grouped.values()]
}

// Keep this type import anchored for strict TypeScript builds when the generated
// dataset contains no methods yet.
export type PublicMethodRecord = PortfolioMethod
