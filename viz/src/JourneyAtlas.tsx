import { useMemo } from 'react'
import journeyJson from './data/journey.json'
import photoUrl from '../public/photo.jpg'

export type JourneyViewId =
  | 'portrait'
  | 'journey'
  | 'capabilities'
  | 'outcomes'
  | 'respect'
  | 'influence'
  | 'service'
  | 'momentum'

export interface JourneyViewDefinition {
  id: JourneyViewId
  label: string
  shortLabel?: string
}

export const JOURNEY_VIEWS: JourneyViewDefinition[] = [
  { id: 'portrait', label: 'Executive Portrait', shortLabel: 'Portrait' },
  { id: 'journey', label: 'Twenty-Year Journey', shortLabel: 'Journey' },
  { id: 'capabilities', label: 'Capability Compounder', shortLabel: 'Capabilities' },
  { id: 'outcomes', label: 'Outcome Ledger', shortLabel: 'Outcomes' },
  { id: 'respect', label: 'Trust & Respect', shortLabel: 'Respect' },
  { id: 'influence', label: 'Influence Web', shortLabel: 'Influence' },
  { id: 'service', label: 'Teaching & Service Ripple', shortLabel: 'Service Ripple' },
  { id: 'momentum', label: 'Momentum & Next Horizon', shortLabel: 'Next Horizon' },
]

export const DEFAULT_JOURNEY_VIEW: JourneyViewId = 'portrait'

interface EvidenceRef {
  source_id: string
  year?: number
  tier: string
  supports: string
}

interface EvidenceBacked {
  evidence?: EvidenceRef[]
  caveat_labels?: string[]
}

interface Metric extends EvidenceBacked {
  id: string
  label: string
  value: string | number
  unit?: string
  display: string
  period?: string
}

interface Era extends EvidenceBacked {
  id: string
  label: string
  organization: string
  role: string
  start: number
  end: number
  summary: string
  capabilities: string[]
  impact_claims: string[]
}

interface ServiceMilestone extends EvidenceBacked {
  id?: string
  year?: number
  date?: string
  title?: string
  label?: string
  summary?: string
  description?: string
  [key: string]: unknown
}

interface ServiceLane extends EvidenceBacked {
  label: string
  start: number
  summary: string
  milestones: ServiceMilestone[]
  metrics: Metric[]
}

interface CapabilityStage extends EvidenceBacked {
  era_id: string
  level: number
  label: string
}

interface CapabilityStream {
  id: string
  label: string
  color: string
  stages: CapabilityStage[]
}

interface ImpactItem extends EvidenceBacked {
  id: string
  category: string
  scope?: string
  title: string
  statement: string
  metrics: Metric[]
}

type FlexibleRecord = EvidenceBacked & Record<string, unknown>

interface InfluenceData extends EvidenceBacked {
  annual_connects: FlexibleRecord[]
  reach_dimensions: FlexibleRecord[]
  stories: FlexibleRecord[]
}

interface RespectData extends EvidenceBacked {
  recommendation_count: number
  recommendation_manifest: FlexibleRecord[]
  quotes: FlexibleRecord[]
  recognitions: FlexibleRecord[]
}

interface TeachingServiceData extends EvidenceBacked {
  session_metrics: Metric[]
  college_program: FlexibleRecord
  service_programs: FlexibleRecord[]
}

interface MomentumData extends EvidenceBacked {
  ai_session_metrics: Metric[]
  frontier_projects: FlexibleRecord[]
  quality_guardrails: FlexibleRecord[]
  next_horizon: FlexibleRecord[]
}

interface JourneyMeta {
  title?: string
  generated_at?: string
  views?: Array<{
    id?: string
    key?: string
    label?: string
    description?: string
    intent?: string
    data_keys?: string[]
  }>
  [key: string]: unknown
}

interface JourneyData {
  meta: JourneyMeta
  thesis: FlexibleRecord
  headline_metrics: Metric[]
  eras: Era[]
  service_lane: ServiceLane
  capability_streams: CapabilityStream[]
  impact_ledger: ImpactItem[]
  influence: InfluenceData
  respect: RespectData
  teaching_service: TeachingServiceData
  momentum: MomentumData
  caveats: unknown
}

const data = journeyJson as unknown as JourneyData

const ERA_COLORS = ['#2563a8', '#0d7a52', '#b84c1a', '#8b5e00', '#6b46b0', '#b83d6b']

function asRecord(value: unknown): Record<string, unknown> {
  return value && typeof value === 'object' && !Array.isArray(value)
    ? value as Record<string, unknown>
    : {}
}

function textField(value: unknown, keys: string[], fallback = ''): string {
  if (typeof value === 'string' && value.trim()) return value.trim()
  if (typeof value === 'number') return String(value)
  const record = asRecord(value)
  for (const key of keys) {
    const candidate = record[key]
    if (typeof candidate === 'string' && candidate.trim()) return candidate.trim()
    if (typeof candidate === 'number') return String(candidate)
  }
  return fallback
}

function numberField(value: unknown, keys: string[], fallback = 0): number {
  const record = asRecord(value)
  for (const key of keys) {
    const candidate = record[key]
    if (typeof candidate === 'number' && Number.isFinite(candidate)) return candidate
    if (typeof candidate === 'string') {
      const parsed = Number(candidate.replace(/[^0-9.-]/g, ''))
      if (Number.isFinite(parsed)) return parsed
    }
  }
  return fallback
}

function arrayField(value: unknown, keys: string[]): unknown[] {
  const record = asRecord(value)
  for (const key of keys) {
    if (Array.isArray(record[key])) return record[key] as unknown[]
  }
  return []
}

function sentence(value: string, max = 180): string {
  if (value.length <= max) return value
  return `${value.slice(0, max).replace(/\s+\S*$/, '')}…`
}

function compactLabel(value: string, max = 24): string {
  return value.length <= max ? value : `${value.slice(0, max - 1)}…`
}

function evidenceFor(value: unknown): EvidenceRef[] {
  const record = asRecord(value)
  if (!Array.isArray(record.evidence)) return []
  return record.evidence.filter((entry): entry is EvidenceRef => {
    const evidence = asRecord(entry)
    return typeof evidence.source_id === 'string'
      && typeof evidence.tier === 'string'
      && typeof evidence.supports === 'string'
      && (evidence.year === undefined || (typeof evidence.year === 'number' && Number.isFinite(evidence.year)))
  }) as EvidenceRef[]
}

function caveatsFor(value: unknown): string[] {
  const record = asRecord(value)
  return Array.isArray(record.caveat_labels)
    ? record.caveat_labels.filter((item): item is string => typeof item === 'string')
    : []
}

function mergeEvidence(...values: unknown[]): EvidenceRef[] {
  const seen = new Set<string>()
  return values.flatMap(evidenceFor).filter(evidence => {
    const key = `${evidence.source_id}|${evidence.year ?? ''}|${evidence.tier}|${evidence.supports}`
    if (seen.has(key)) return false
    seen.add(key)
    return true
  })
}

function normalizedTier(tier: string): string {
  const normalized = tier.toLowerCase().replace(/[\s_]+/g, '-')
  if (normalized.includes('corroborat') || normalized === 'a' || normalized.includes('tier-a')) return 'corroborated'
  if (normalized.includes('document') || normalized.includes('primary') || normalized.includes('first-party') || normalized === 'b' || normalized.includes('tier-b')) return 'documented'
  if (normalized.includes('self') || normalized.includes('resume') || normalized === 'c' || normalized.includes('tier-c')) return 'self-reported'
  if (normalized.includes('deriv') || normalized.includes('synth')) return 'derived'
  return normalized
}

const EVIDENCE_TIER_STRENGTH: Record<string, number> = {
  corroborated: 4,
  documented: 3,
  'self-reported': 2,
  derived: 1,
}

function strongestEvidence(evidence: EvidenceRef[]): EvidenceRef | undefined {
  return evidence.reduce<EvidenceRef | undefined>((strongest, candidate) => {
    if (!strongest) return candidate
    const currentRank = EVIDENCE_TIER_STRENGTH[normalizedTier(strongest.tier)] ?? 0
    const candidateRank = EVIDENCE_TIER_STRENGTH[normalizedTier(candidate.tier)] ?? 0
    return candidateRank > currentRank ? candidate : strongest
  }, undefined)
}

function tierLabel(tier: string): string {
  const normalized = normalizedTier(tier)
  if (normalized === 'corroborated') return 'Tier A · Corroborated'
  if (normalized === 'documented') return 'Tier B · Documented'
  if (normalized === 'self-reported') return 'Tier C · Self-reported'
  if (normalized === 'derived') return 'Derived synthesis'
  return tier.replace(/[_-]+/g, ' ')
}

function tierDescription(tier: string): string {
  const normalized = normalizedTier(tier)
  if (normalized === 'corroborated') return 'Supported by an independently attributable artifact or direct third-party record.'
  if (normalized === 'documented') return 'Supported by a dated first-party artifact, ledger, workbook, or program record.'
  if (normalized === 'self-reported') return 'Reported in first-party career material and not independently corroborated in this dataset.'
  if (normalized === 'derived') return 'A transparent synthesis or calculation across evidence; not a standalone source claim.'
  return 'Evidence is classified using the source tier supplied in the journey dataset.'
}

function evidenceYear(evidence: EvidenceRef): number | null {
  return typeof evidence.year === 'number' && evidence.year >= 1900 && evidence.year <= 2100
    ? evidence.year
    : null
}

function itemYear(value: unknown): number | null {
  const direct = numberField(value, ['year', 'start_year', 'start'], Number.NaN)
  if (Number.isFinite(direct) && direct >= 1900 && direct <= 2100) return direct
  const date = textField(value, ['date', 'period', 'start_date'])
  const match = date.match(/(?:19|20)\d{2}/)
  if (match) return Number(match[0])
  const yearFromEvidence = evidenceFor(value).map(evidenceYear).find((year): year is number => year !== null)
  return yearFromEvidence ?? null
}

function caveatDescription(label: string): string {
  if (Array.isArray(data.caveats)) {
    const match = data.caveats.find(item => {
      const record = asRecord(item)
      return [record.id, record.label, record.key].includes(label)
    })
    return match ? textField(match, ['description', 'text', 'detail'], label) : label
  }
  const caveatMap = asRecord(data.caveats)
  const entry = caveatMap[label]
  if (typeof entry === 'string') return entry
  return textField(entry, ['description', 'text', 'detail'], label)
}

function viewMeta(id: JourneyViewId) {
  const views = data.meta.views ?? []
  const exact = views.find(view => (view.id ?? view.key) === id)
  if (exact) return exact
  const index = JOURNEY_VIEWS.findIndex(view => view.id === id)
  return index >= 0 ? views[index] : undefined
}

function EvidenceDisclosure({
  tier,
  summary,
  supports,
  sourceId,
  year,
}: {
  tier?: string
  summary?: string
  supports?: string
  sourceId?: string
  year?: number
}) {
  const normalized = tier ? normalizedTier(tier) : 'pending'
  const label = summary ?? (tier ? tierLabel(tier) : 'Evidence pending')
  return (
    <details className="ja-evidence-disclosure">
      <summary className="ja-provenance" data-tier={normalized}>{label}</summary>
      <div className="ja-disclosure-copy">
        <strong>{tier ? tierLabel(tier) : 'Evidence status'}</strong>
        <p>{tier ? tierDescription(tier) : 'No supporting source is attached to this synthesized display element.'}</p>
        {supports && <p><span>Supports</span>{supports}</p>}
        {(sourceId || year) && (
          <p className="ja-source-identity">
            {sourceId && <code>{sourceId}</code>}
            {year && <span>{year}</span>}
          </p>
        )}
      </div>
    </details>
  )
}

function EvidenceBadge({ evidence }: { evidence?: EvidenceRef }) {
  if (!evidence) return <EvidenceDisclosure />
  return (
    <EvidenceDisclosure
      tier={evidence.tier}
      supports={evidence.supports}
      sourceId={evidence.source_id}
      year={evidence.year}
    />
  )
}

function SourceLine({ evidence, prefix = 'Basis' }: { evidence: EvidenceRef[]; prefix?: string }) {
  if (evidence.length === 0) return <EvidenceBadge />
  const tier = strongestEvidence(evidence)
  return (
    <div className="ja-source-line">
      <EvidenceBadge evidence={tier} />
      <span>{prefix}: {evidence.length} source{evidence.length === 1 ? '' : 's'}</span>
      {evidence.length > 1 && <span>· strongest tier shown</span>}
    </div>
  )
}

function CaveatLabels({ labels }: { labels: string[] }) {
  const unique = [...new Set(labels)]
  if (unique.length === 0) return null
  return (
    <div className="ja-caveat-tags" role="group" aria-label="Claim caveats">
      {unique.map(label => (
        <details className="ja-caveat-disclosure" key={label}>
          <summary className="ja-caveat-tag">△ {label.replace(/[_-]+/g, ' ')}</summary>
          <div className="ja-disclosure-copy ja-caveat-explanation">
            <strong>Interpretation boundary</strong>
            <p>{caveatDescription(label)}</p>
          </div>
        </details>
      ))}
    </div>
  )
}

function TierLegend() {
  return (
    <div className="ja-tier-legend" role="group" aria-label="Evidence tier legend">
      <span>Evidence vocabulary</span>
      <EvidenceDisclosure tier="corroborated" />
      <EvidenceDisclosure tier="documented" />
      <EvidenceDisclosure tier="self-reported" />
      <EvidenceDisclosure tier="derived" />
    </div>
  )
}

function ViewHeader({
  id,
  eyebrow,
  title,
  accent,
  lede,
  caveat,
}: {
  id: JourneyViewId
  eyebrow: string
  title: React.ReactNode
  accent: string
  lede: string
  caveat: string
}) {
  const meta = viewMeta(id)
  const dataKeys = meta?.data_keys ?? []
  return (
    <header className="ja-section-head">
      <div>
        <span className="ja-eyebrow">{eyebrow}</span>
        <h1 className="ja-title" id={`journey-heading-${id}`} tabIndex={-1}>{title}</h1>
        <p className="ja-lede">{lede}</p>
      </div>
      <aside className="ja-head-note">
        <strong>{meta?.label ?? 'Reading note'}</strong>
        <p>{meta?.description ?? meta?.intent ?? 'A focused evidence-backed reading of this part of the journey.'}</p>
        <div className="ja-head-boundary">
          <strong>Boundary</strong>
          <span>{caveat}</span>
        </div>
        {dataKeys.length > 0 && (
          <span className="ja-data-basis">Data basis · {dataKeys.join(' + ')}</span>
        )}
      </aside>
    </header>
  )
}

function MetricGrid({ metrics, limit = 4 }: { metrics: Metric[]; limit?: number }) {
  const visible = metrics.slice(0, limit)
  if (visible.length === 0) return null
  return (
    <div className="ja-metric-grid">
      {visible.map((metric, index) => (
        <article
          className="ja-metric"
          key={metric.id || `${metric.label}-${index}`}
          style={{ '--metric-color': ERA_COLORS[index % ERA_COLORS.length] } as React.CSSProperties}
        >
          <span className="ja-metric-value">{metric.display || `${metric.value}${metric.unit ?? ''}`}</span>
          <span className="ja-metric-label">{metric.label}</span>
          {metric.period && <span className="ja-metric-period">{metric.period}</span>}
          <EvidenceBadge evidence={strongestEvidence(evidenceFor(metric))} />
          <CaveatLabels labels={caveatsFor(metric)} />
        </article>
      ))}
    </div>
  )
}

function GlobalCaveat({ children }: { children: React.ReactNode }) {
  return (
    <div className="ja-caveat">
      <strong>Interpretation boundary · </strong>{children}
    </div>
  )
}

function ExecutivePortrait() {
  const thesisHeadline = textField(data.thesis, ['headline', 'identity', 'title'], 'Engineering excellence that compounds through people')
  const thesisStatement = textField(
    data.thesis,
    ['statement', 'thesis', 'summary', 'value_proposition'],
    'A technical leader who turns regulated complexity into systems, standards, and communities that help other engineers do their best work.'
  )
  const role = textField(data.thesis, ['role', 'positioning', 'subtitle'], 'Digital transformation leader · Medical device software')

  const principles = [
    ['Engineer', 'Technical depth remains the foundation: architecture, reliability, craft, and regulated delivery.'],
    ['Translator', 'Connects executive intent, engineering reality, standards, and measurable outcomes.'],
    ['Multiplier', 'Scales impact through coaching, reusable practices, communities, and influence without authority.'],
    ['Steward', 'Pairs professional ambition with teaching, yoga, service, and long-horizon responsibility.'],
  ]

  return (
    <section className="ja-view ja-view--portrait" aria-labelledby="journey-heading-portrait">
      <div className="ja-frame">
        <div className="ja-portrait-hero">
          <div>
            <span className="ja-eyebrow">Executive portrait · 2007—2026</span>
            <h1 className="ja-portrait-name" id="journey-heading-portrait" tabIndex={-1}>
              <span>Dattatreya Subramanya</span>
              Datta Vellal
            </h1>
            <p className="ja-portrait-thesis">“{thesisHeadline}.”</p>
            <p className="ja-lede">{thesisStatement}</p>
            <div className="ja-portrait-role">{role}</div>
            <SourceLine evidence={evidenceFor(data.thesis)} prefix="Thesis synthesis" />
          </div>
          <div className="ja-portrait-photo-wrap">
            <img className="ja-portrait-photo" src={photoUrl} alt="Datta Vellal" />
          </div>
        </div>

        <div className="ja-portrait-metrics">
          <MetricGrid metrics={data.headline_metrics} />
        </div>

        <div className="ja-operating-system" role="list" aria-label="Datta's operating system">
          {principles.map(([title, description], index) => (
            <article className="ja-operating-principle" role="listitem" key={title}>
              <span className="ja-operating-index">MODE / {String(index + 1).padStart(2, '0')}</span>
              <h3>{title}</h3>
              <p>{description}</p>
              <EvidenceDisclosure tier="derived" supports="Interpretation across the evidence-backed journey record." />
            </article>
          ))}
        </div>

        <TierLegend />
        <GlobalCaveat>
          Headline metrics preserve their source tier. Resume-originated figures are presented as self-reported unless another artifact independently corroborates them.
        </GlobalCaveat>
      </div>
    </section>
  )
}

function smoothPath(points: Array<[number, number]>): string {
  if (points.length === 0) return ''
  if (points.length === 1) return `M ${points[0][0]} ${points[0][1]}`
  return points.slice(1).reduce((path, point, index) => {
    const previous = points[index]
    const midpoint = (previous[0] + point[0]) / 2
    return `${path} C ${midpoint} ${previous[1]}, ${midpoint} ${point[1]}, ${point[0]} ${point[1]}`
  }, `M ${points[0][0]} ${points[0][1]}`)
}

function TwentyYearJourney() {
  const startYear = Math.min(...data.eras.map(era => era.start), data.service_lane.start || 2007)
  const endYear = Math.max(...data.eras.map(era => era.end), new Date().getFullYear())
  const xForYear = (year: number) => 74 + ((year - startYear) / Math.max(1, endYear - startYear)) * 852

  const careerPoints: Array<[number, number]> = data.eras.map((era, index) => [
    xForYear((era.start + era.end) / 2),
    112 + Math.sin(index * 1.65) * 23,
  ])
  const serviceMilestones = data.service_lane.milestones
    .map(milestone => ({ milestone, year: itemYear(milestone) }))
    .filter((item): item is { milestone: ServiceMilestone; year: number } => item.year !== null)
  const servicePoints: Array<[number, number]> = serviceMilestones.map((item, index) => [
    xForYear(item.year),
    276 + Math.sin(index * 1.25 + 1) * 18,
  ])
  const learningMoments = data.eras.map((era, index) => {
    const stages = data.capability_streams
      .flatMap(stream => stream.stages)
      .filter(stage => stage.era_id === era.id)
    const averageLevel = stages.length > 0
      ? stages.reduce((sum, stage) => sum + stage.level, 0) / stages.length
      : 1
    return {
      era,
      evidenceCount: mergeEvidence(...stages).length,
      point: [
        xForYear(era.start),
        425 - averageLevel * 7 + Math.sin(index * 0.8) * 4,
      ] as [number, number],
    }
  })
  const learningPoints = learningMoments.map(moment => moment.point)

  const yearTicks = Array.from({ length: Math.floor((endYear - startYear) / 3) + 1 }, (_, index) => startYear + index * 3)

  return (
    <section className="ja-view ja-view--journey" aria-labelledby="journey-heading-journey">
      <div className="ja-frame">
        <ViewHeader
          id="journey"
          eyebrow="The braided record"
          title={<>Twenty years, <em>three strands</em>, one operating philosophy.</>}
          accent="blue"
          lede="The professional story, the service story, and the capability story did not happen in sequence. They reinforced one another across every era."
          caveat="Employment dates use the authoritative resume chronology; service and learning moments retain their own evidence tier."
        />

        <div className="ja-panel ja-braid">
          <div className="ja-braid-legend">
            <span style={{ '--strand-color': '#2563a8' } as React.CSSProperties}><i />Professional responsibility</span>
            <span style={{ '--strand-color': '#6b46b0' } as React.CSSProperties}><i />Teaching & service</span>
            <span style={{ '--strand-color': '#0d7a52' } as React.CSSProperties}><i />Capability growth</span>
          </div>
          <div className="ja-braid-scroll" role="region" tabIndex={0} aria-label="Braided career timeline; scroll horizontally on small screens">
            <svg className="ja-braid-svg" viewBox="0 0 1000 500" role="img" aria-labelledby="braid-title braid-desc">
              <title id="braid-title">Datta Vellal's braided twenty-year journey</title>
              <desc id="braid-desc">Three timelines show professional roles, service milestones, and capability growth from {startYear} to {endYear}.</desc>
              {yearTicks.map(year => (
                <g key={year}>
                  <line className="ja-braid-guide" x1={xForYear(year)} x2={xForYear(year)} y1="44" y2="455" />
                  <text className="ja-braid-year" x={xForYear(year)} y="478" textAnchor="middle">{year}</text>
                </g>
              ))}
              <path className="ja-braid-track ja-braid-track--career" d={smoothPath(careerPoints)} />
              <path className="ja-braid-track ja-braid-track--service" d={smoothPath(servicePoints)} />
              <path className="ja-braid-track ja-braid-track--learning" d={smoothPath(learningPoints)} />

              {data.eras.map((era, index) => {
                const [x, y] = careerPoints[index]
                return (
                  <g key={era.id}>
                    <title>{era.organization}, {era.role}, {era.start}–{era.end}</title>
                    <circle className="ja-braid-dot ja-braid-dot--career" cx={x} cy={y} r="8" />
                    <text className="ja-braid-label" x={x} y={y - 18} textAnchor="middle">{compactLabel(era.label || era.organization, 18)}</text>
                    <text className="ja-braid-caption" x={x} y={y + 24} textAnchor="middle">{era.start}—{era.end}</text>
                  </g>
                )
              })}

              {serviceMilestones.slice(0, 9).map(({ milestone, year }, index) => {
                const [x, y] = servicePoints[index]
                const label = textField(milestone, ['title', 'label'], `Service · ${year}`)
                return (
                  <g key={milestone.id ?? `${year}-${index}`}>
                    <title>{label}</title>
                    <circle className="ja-braid-dot ja-braid-dot--service" cx={x} cy={y} r="6" />
                    <text className="ja-braid-caption" x={x} y={y + (index % 2 ? 25 : -15)} textAnchor="middle">{compactLabel(label, 22)}</text>
                  </g>
                )
              })}

              {learningMoments.map(({ era, evidenceCount, point: [x, y] }) => (
                <g key={era.id}>
                  <title>{era.start}: {evidenceCount} capability evidence links across this era</title>
                  <circle className="ja-braid-dot ja-braid-dot--learning" cx={x} cy={y} r="5" />
                </g>
              ))}
              <text className="ja-braid-label" x="28" y="116">WORK</text>
              <text className="ja-braid-label" x="28" y="280">SERVICE</text>
              <text className="ja-braid-label" x="28" y="406">GROWTH</text>
            </svg>
          </div>

          <div className="ja-era-cards">
            {data.eras.map((era, index) => (
              <article className="ja-era-card" key={era.id} style={{ '--era-color': ERA_COLORS[index % ERA_COLORS.length] } as React.CSSProperties}>
                <time>{era.start}—{era.end}</time>
                <h3>{era.label}</h3>
                <p>{era.organization} · {era.role}</p>
                <p>{sentence(era.summary, 120)}</p>
                <SourceLine evidence={evidenceFor(era)} />
                <CaveatLabels labels={caveatsFor(era)} />
              </article>
            ))}
          </div>
        </div>

        <GlobalCaveat>
          Line proximity communicates parallel development, not statistical causality. Milestones are deliberately curated; the complete evidence archive remains the source of record.
        </GlobalCaveat>
      </div>
    </section>
  )
}

function CapabilityCompounder() {
  const startYear = Math.min(...data.eras.map(era => era.start))
  const endYear = Math.max(...data.eras.map(era => era.end))
  const years = [startYear, startYear + 5, startYear + 10, startYear + 15, endYear]

  const streamRows = data.capability_streams.map(stream => {
    const datedStages = stream.stages.map(stage => ({ stage, era: data.eras.find(era => era.id === stage.era_id) }))
    const firstYear = datedStages.find(item => item.era)?.era?.start ?? startYear
    const lastYear = [...datedStages].reverse().find(item => item.era)?.era?.end ?? endYear
    const latest = stream.stages[stream.stages.length - 1]
    return { stream, firstYear, lastYear, latest }
  })

  const strongest = [...streamRows].sort((a, b) => (b.latest?.level ?? 0) - (a.latest?.level ?? 0)).slice(0, 3)

  return (
    <section className="ja-view ja-view--capabilities" aria-labelledby="journey-heading-capabilities">
      <div className="ja-frame">
        <ViewHeader
          id="capabilities"
          eyebrow="Capability compounder"
          title={<>Skills were not collected. They were <em>reinvested.</em></>}
          accent="green"
          lede="Each era converted technical depth into a wider form of leverage: delivery, systems thinking, organizational change, teaching, and executive influence."
          caveat="Levels describe the journey dataset's evidence synthesis; they are not psychometric scores or a comparison with other people."
        />

        <div className="ja-capability-layout">
          <div className="ja-panel ja-capability-river">
            <div className="ja-panel-label"><span>Capability river · first evidence to current expression</span><span>{data.capability_streams.length} streams</span></div>
            <div className="ja-river-head">
              <span className="ja-river-label">Capability</span>
              <div className="ja-river-years">{years.map(year => <span key={year}>{Math.round(year)}</span>)}</div>
              <span>Level</span>
            </div>
            {streamRows.map(({ stream, firstYear, lastYear, latest }) => {
              const left = ((firstYear - startYear) / Math.max(1, endYear - startYear)) * 100
              const width = Math.max(2, ((lastYear - firstYear) / Math.max(1, endYear - startYear)) * 100)
              const evidence = mergeEvidence(...stream.stages)
              return (
                <div className="ja-river-row" key={stream.id}>
                  <div className="ja-river-label">
                    {stream.label}
                    <small>{evidence.length} evidence link{evidence.length === 1 ? '' : 's'}</small>
                  </div>
                  <div className="ja-river-track" title={`${stream.label}: evidenced from ${firstYear}`}>
                    <div
                      className="ja-river-flow"
                      style={{ left: `${left}%`, width: `${Math.min(100 - left, width)}%`, '--flow-color': stream.color || '#0d7a52' } as React.CSSProperties}
                    />
                  </div>
                  <div className="ja-river-score"><strong>{latest?.level ?? '—'}</strong><span>{latest?.label ?? 'current'}</span></div>
                </div>
              )
            })}
          </div>

          <aside className="ja-panel ja-capability-matrix">
            <div className="ja-panel-label"><span>Current signature</span></div>
            {strongest.map(({ stream, latest }) => (
              <article className="ja-matrix-cell" key={stream.id}>
                <span>Compounded capability</span>
                <strong>{stream.label}</strong>
                <p>{latest?.label ?? 'Visible across multiple eras'}</p>
                <EvidenceBadge evidence={strongestEvidence(evidenceFor(latest))} />
                <CaveatLabels labels={caveatsFor(latest)} />
              </article>
            ))}
          </aside>
        </div>

        <GlobalCaveat>
          Stream length means “present in dated evidence,” not uninterrupted use. The level values are ordinal narrative stages supplied by the dataset.
        </GlobalCaveat>
      </div>
    </section>
  )
}

const OUTCOME_COLORS: Record<string, string> = {
  individual: '#2563a8',
  team: '#0d7a52',
  organization: '#b84c1a',
  enterprise: '#8b5e00',
  ecosystem: '#6b46b0',
  community: '#b83d6b',
}

function outcomeScope(category: string, context = ''): string {
  const value = `${category} ${context}`.toLowerCase()
  if (value.includes('communit') || value.includes('social') || value.includes('service')) return 'community'
  if (value.includes('enterprise') || value.includes('global') || value.includes('ecosystem') || value.includes('7,000') || value.includes('7000')) return 'ecosystem'
  if (value.includes('org') || value.includes('business') || value.includes('financial') || value.includes('saving') || value.includes('roadmap') || value.includes('delivery time')) return 'organization'
  if (value.includes('team') || value.includes('people') || value.includes('hiring') || value.includes('engineer') || value.includes('mentor')) return 'team'
  return 'individual'
}

const OUTCOME_SCOPE_BY_ID: Record<string, string> = {
  'amazon-scale': 'individual',
  'hiring-onboarding': 'team',
  'philips-value': 'organization',
  'learning-system': 'organization',
  'global-platform': 'ecosystem',
  'connect-system': 'ecosystem',
  sutra: 'ecosystem',
  'book-program': 'community',
}

function scopeForOutcome(item: ImpactItem): string {
  return item.scope || OUTCOME_SCOPE_BY_ID[item.id] || outcomeScope(item.category, `${item.title} ${item.statement}`)
}

function OutcomeLedger() {
  const byScope = data.impact_ledger.reduce<Record<string, number>>((counts, item) => {
    const scope = scopeForOutcome(item)
    counts[scope] = (counts[scope] ?? 0) + 1
    return counts
  }, {})
  const ladder = [
    ['individual', 'Individual craft'],
    ['team', 'Team capability'],
    ['organization', 'Organizational systems'],
    ['ecosystem', 'Enterprise & community'],
  ]

  return (
    <section className="ja-view ja-view--outcomes" aria-labelledby="journey-heading-outcomes">
      <div className="ja-frame">
        <ViewHeader
          id="outcomes"
          eyebrow="Outcome ledger"
          title={<>Value is strongest when <em>leverage rises.</em></>}
          accent="orange"
          lede="The record moves from solving problems personally to changing the systems through which teams and organizations solve problems repeatedly."
          caveat="Every number retains its provenance. Currency, attribution, audience, and time-window caveats stay attached to the claim."
        />

        <div className="ja-outcome-layout">
          <aside className="ja-panel ja-leverage-ladder" aria-label="Outcome leverage ladder">
            {ladder.map(([scope, label], index) => (
              <div className="ja-ladder-rung" key={scope} style={{ '--rung-color': OUTCOME_COLORS[scope] } as React.CSSProperties}>
                <span>Leverage {index + 1}</span>
                <strong>{label}</strong>
                <span>{scope === 'ecosystem' ? (byScope.ecosystem ?? 0) + (byScope.community ?? 0) : (byScope[scope] ?? 0)} ledger entries</span>
              </div>
            ))}
          </aside>

          <div className="ja-outcome-ledger">
            {data.impact_ledger.map(item => {
              const metric = item.metrics[0]
              const scope = scopeForOutcome(item)
              const evidence = mergeEvidence(item, ...item.metrics)
              return (
                <article className="ja-outcome-card" key={item.id} style={{ '--outcome-color': OUTCOME_COLORS[scope] ?? '#b84c1a' } as React.CSSProperties}>
                  <span className="ja-outcome-scope">{scope} leverage · {item.category}</span>
                  <strong className="ja-outcome-value">{metric?.display ?? 'Documented'}</strong>
                  <h3>{item.title}</h3>
                  <p>{sentence(item.statement, 190)}</p>
                  <SourceLine evidence={evidence} />
                  <CaveatLabels labels={[...caveatsFor(item), ...item.metrics.flatMap(caveatsFor)]} />
                </article>
              )
            })}
          </div>
        </div>

        <GlobalCaveat>
          The ladder describes scale of leverage, not moral worth. Outcomes with shared or team attribution are presented as contributions, not sole credit.
        </GlobalCaveat>
      </div>
    </section>
  )
}

function TrustRespect() {
  const quotes = data.respect.quotes.filter(quote => textField(quote, ['quote', 'text', 'statement', 'excerpt']))
  const organizations = new Set(data.respect.recommendation_manifest
    .map(recommendation => textField(recommendation, ['organization', 'company', 'issuer']))
    .filter(Boolean))
  const summaryMetrics: Metric[] = [
    { id: 'recommendations', label: 'Attributed recommendations', value: data.respect.recommendation_count, display: String(data.respect.recommendation_count), evidence: data.respect.evidence ?? [], caveat_labels: data.respect.caveat_labels ?? [] },
    { id: 'quotes', label: 'Curated direct voices', value: quotes.length, display: String(quotes.length), evidence: mergeEvidence(...quotes), caveat_labels: [] },
    { id: 'organizations', label: 'Organizations represented', value: organizations.size, display: String(organizations.size), evidence: mergeEvidence(...data.respect.recommendation_manifest), caveat_labels: [] },
    { id: 'recognitions', label: 'Recognition records', value: data.respect.recognitions.length, display: String(data.respect.recognitions.length), evidence: mergeEvidence(...data.respect.recognitions), caveat_labels: [] },
  ]

  return (
    <section className="ja-view ja-view--respect" aria-labelledby="journey-heading-respect">
      <div className="ja-frame">
        <ViewHeader
          id="respect"
          eyebrow="Trust & respect"
          title={<>Influence becomes visible in <em>other people’s words.</em></>}
          accent="rose"
          lede="Direct, attributable recommendations reveal a consistent pattern: technical credibility earns attention; calm leadership and generosity turn that attention into trust."
          caveat="This view prioritizes person-attributed direct quotations. Generic achievement descriptions are excluded from the testimonial timeline."
        />

        <div className="ja-respect-summary"><MetricGrid metrics={summaryMetrics} /></div>

        <div className="ja-respect-timeline">
          {quotes.slice(0, 10).map((quote, index) => {
            const text = textField(quote, ['quote', 'text', 'statement', 'excerpt'])
            const person = textField(quote, ['person', 'author', 'name', 'issuer'], 'Attributed colleague')
            const role = textField(quote, ['role', 'relationship', 'title'])
            const organization = textField(quote, ['organization', 'company'])
            const year = itemYear(quote)
            return (
              <article className="ja-respect-entry" key={textField(quote, ['id'], `${person}-${index}`)}>
                <div className="ja-respect-card">
                  <blockquote>“{text}”</blockquote>
                  <div className="ja-respect-person">
                    <strong>{person}</strong>
                    {(role || organization) && <span>{[role, organization].filter(Boolean).join(' · ')}</span>}
                  </div>
                  <SourceLine evidence={evidenceFor(quote)} prefix="Direct source" />
                  <CaveatLabels labels={caveatsFor(quote)} />
                </div>
                <time className="ja-respect-node" dateTime={year ? String(year) : undefined}>{year ?? String(index + 1).padStart(2, '0')}</time>
              </article>
            )
          })}
        </div>

        <GlobalCaveat>
          Recommendations are selected evidence, not an unbiased survey. Names and roles are shown only when the source data identifies them.
        </GlobalCaveat>
      </div>
    </section>
  )
}

function InfluenceWeb() {
  const strengths = data.capability_streams.slice(0, 5).map(stream => ({
    id: stream.id,
    label: stream.label,
    count: mergeEvidence(...stream.stages).length,
  }))
  const mechanisms = data.influence.stories.slice(0, 5).map((story, index) => ({
    id: textField(story, ['id'], `story-${index}`),
    label: textField(story, ['mechanism', 'title', 'label', 'name'], `Influence pattern ${index + 1}`),
    count: evidenceFor(story).length,
  }))
  const outcomes = data.influence.reach_dimensions.slice(0, 5).map((dimension, index) => ({
    id: textField(dimension, ['id'], `reach-${index}`),
    label: textField(dimension, ['label', 'title', 'name', 'dimension'], `Reach dimension ${index + 1}`),
    count: numberField(dimension, ['value', 'count', 'reach'], evidenceFor(dimension).length),
  }))

  const connectMetrics: Metric[] = data.influence.annual_connects.slice(-4).map((item, index) => ({
    id: textField(item, ['id'], `connect-${index}`),
    label: `${itemYear(item) ?? 'Annual'} connections`,
    value: numberField(item, ['unique_people', 'unique_people_reached', 'people', 'people_reached', 'participants', 'sessions', 'count', 'connects', 'total', 'value']),
    display: textField(item, ['display'], String(numberField(item, ['unique_people', 'unique_people_reached', 'people', 'people_reached', 'participants', 'sessions', 'count', 'connects', 'total', 'value']))),
    period: itemYear(item)?.toString(),
    evidence: evidenceFor(item),
    caveat_labels: caveatsFor(item),
  }))

  const nodeY = (index: number, count: number) => 65 + (index + 0.5) * (440 / Math.max(1, count))

  return (
    <section className="ja-view ja-view--influence" aria-labelledby="journey-heading-influence">
      <div className="ja-frame">
        <ViewHeader
          id="influence"
          eyebrow="Influence web"
          title={<>Respect is earned. Influence is <em>made reusable.</em></>}
          accent="violet"
          lede="The recurring pattern is structured: credible capability enables a mechanism—coaching, facilitation, standards, or community—and that mechanism expands reach."
          caveat="This is a structured narrative flow, not a raw network graph and not a statistical claim of causality."
        />

        {connectMetrics.length > 0 && <div className="ja-influence-metrics"><MetricGrid metrics={connectMetrics} /></div>}

        <div className="ja-panel ja-influence-flow">
          <svg className="ja-influence-flow-svg" viewBox="0 0 1000 560" preserveAspectRatio="none" aria-hidden="true">
            {strengths.map((strength, index) => {
              const targetIndex = index % Math.max(1, mechanisms.length)
              return <path key={`s-${strength.id}`} className="ja-influence-link" style={{ '--link-color': '#6b46b0', '--link-width': Math.min(8, 1.5 + strength.count / 3) } as React.CSSProperties} d={`M 245 ${nodeY(index, strengths.length)} C 350 ${nodeY(index, strengths.length)}, 390 ${nodeY(targetIndex, mechanisms.length)}, 475 ${nodeY(targetIndex, mechanisms.length)}`} />
            })}
            {mechanisms.map((mechanism, index) => {
              const targetIndex = index % Math.max(1, outcomes.length)
              return <path key={`m-${mechanism.id}`} className="ja-influence-link" style={{ '--link-color': '#0d7a52', '--link-width': Math.min(8, 1.5 + mechanism.count / 2) } as React.CSSProperties} d={`M 525 ${nodeY(index, mechanisms.length)} C 620 ${nodeY(index, mechanisms.length)}, 660 ${nodeY(targetIndex, outcomes.length)}, 755 ${nodeY(targetIndex, outcomes.length)}`} />
            })}
          </svg>

          {[
            { title: 'Credibility', nodes: strengths, color: '#2563a8' },
            { title: 'Mechanism', nodes: mechanisms, color: '#6b46b0' },
            { title: 'Expanded reach', nodes: outcomes, color: '#0d7a52' },
          ].map(column => (
            <div className="ja-influence-column" key={column.title}>
              <h3>{column.title}</h3>
              {column.nodes.map(node => (
                <div className="ja-influence-node" key={node.id} style={{ '--node-color': column.color } as React.CSSProperties}>
                  <strong>{compactLabel(node.label, 31)}</strong>
                  <span>{node.count || '•'}</span>
                </div>
              ))}
            </div>
          ))}
        </div>

        <div className="ja-influence-thesis">
          <p>Influence without authority is the through-line: make the problem legible, build a credible practice, help others own it, and leave behind a system that continues to work without you.</p>
          <EvidenceDisclosure tier="derived" supports="Interpretation across the capability and influence records." />
        </div>
        <CaveatLabels labels={caveatsFor(data.influence)} />
      </div>
    </section>
  )
}

function metricsFromFlexible(value: unknown): Metric[] {
  return arrayField(value, ['metrics', 'session_metrics']).filter((metric): metric is Metric => {
    const record = asRecord(metric)
    return typeof record.label === 'string' && (typeof record.display === 'string' || record.value !== undefined)
  }) as Metric[]
}

function TeachingServiceRipple() {
  const collegeMetrics = metricsFromFlexible(data.teaching_service.college_program)
  const programMetrics = data.teaching_service.service_programs.flatMap(metricsFromFlexible)
  const allMetrics = [...data.teaching_service.session_metrics, ...collegeMetrics, ...programMetrics]
  const ringMetrics = allMetrics.slice(0, 3)
  const careerStart = Math.min(...data.eras.map(era => era.start))
  const continuity = Math.max(...data.eras.map(era => era.end)) - careerStart + 1

  const programs = [data.teaching_service.college_program, ...data.teaching_service.service_programs]
    .filter(program => Object.keys(asRecord(program)).length > 0)
    .sort((a, b) => (itemYear(b) ?? 0) - (itemYear(a) ?? 0))

  return (
    <section className="ja-view ja-view--service" aria-labelledby="journey-heading-service">
      <div className="ja-frame">
        <ViewHeader
          id="service"
          eyebrow="Teaching & service ripple"
          title={<>Knowledge becomes valuable when it <em>keeps traveling.</em></>}
          accent="green"
          lede="Talks, mentoring, yoga, rural education, and community programs form a second career lane: sustained contribution that turns expertise into access for others."
          caveat="Reach figures vary in evidentiary strength. Direct session records and spreadsheets are separated from cumulative program estimates."
        />

        <div className="ja-service-layout">
          <div className="ja-panel ja-ripple-stage" role="img" aria-label="Concentric rings representing the growing reach of teaching and service">
            <div className="ja-ripple-ring ja-ripple-ring--4" style={{ '--ring-color': '#6b46b0' } as React.CSSProperties}><span>{ringMetrics[2]?.display ?? `${continuity} years`} · {ringMetrics[2]?.label ?? 'continuity'}</span></div>
            <div className="ja-ripple-ring ja-ripple-ring--3" style={{ '--ring-color': '#0d7a52' } as React.CSSProperties}><span>{ringMetrics[1]?.display ?? programs.length} · {ringMetrics[1]?.label ?? 'programs'}</span></div>
            <div className="ja-ripple-ring ja-ripple-ring--2" style={{ '--ring-color': '#2563a8' } as React.CSSProperties}><span>{ringMetrics[0]?.display ?? data.teaching_service.session_metrics.length} · {ringMetrics[0]?.label ?? 'session measures'}</span></div>
            <div className="ja-ripple-ring ja-ripple-ring--1" style={{ '--ring-color': '#b84c1a' } as React.CSSProperties}><span>Practice shared</span></div>
            <div className="ja-ripple-core">Datta<br />teaches</div>
          </div>

          <div className="ja-service-streams">
            {programs.slice(0, 9).map((program, index) => {
              const year = itemYear(program)
              const title = textField(program, ['title', 'label', 'name', 'program'], `Service program ${index + 1}`)
              const summary = textField(program, ['summary', 'description', 'statement', 'detail'])
              const kind = textField(program, ['category', 'type', 'kind'], index === 0 ? 'Teaching' : 'Service')
              const color = ERA_COLORS[(index + 1) % ERA_COLORS.length]
              return (
                <article className="ja-service-stream" key={textField(program, ['id'], `${title}-${index}`)} style={{ '--stream-color': color } as React.CSSProperties}>
                  <span className="ja-service-year">{year ?? '∞'}</span>
                  <div>
                    <h3>{title}</h3>
                    {summary && <p>{sentence(summary, 180)}</p>}
                    <SourceLine evidence={evidenceFor(program)} />
                    <CaveatLabels labels={caveatsFor(program)} />
                  </div>
                  <span className="ja-service-kind">{kind}</span>
                </article>
              )
            })}
          </div>
        </div>

        <GlobalCaveat>
          Concentric rings communicate widening kinds of reach, not proportional area. Cumulative audience claims should be read with their displayed tier and caveat.
        </GlobalCaveat>
      </div>
    </section>
  )
}

function collectEvidence(value: unknown, seenObjects = new Set<object>()): EvidenceRef[] {
  if (!value || typeof value !== 'object') return []
  if (seenObjects.has(value as object)) return []
  seenObjects.add(value as object)
  if (Array.isArray(value)) return value.flatMap(item => collectEvidence(item, seenObjects))
  const record = value as Record<string, unknown>
  return [...evidenceFor(record), ...Object.entries(record).filter(([key]) => key !== 'evidence').flatMap(([, item]) => collectEvidence(item, seenObjects))]
}

function dedupeEvidenceRefs(evidence: EvidenceRef[]): EvidenceRef[] {
  const seen = new Set<string>()
  return evidence.filter(item => {
    const key = `${item.source_id}|${item.year ?? ''}|${item.tier}|${item.supports}`
    if (seen.has(key)) return false
    seen.add(key)
    return true
  })
}

function MomentumHorizon() {
  const momentumEvidence = dedupeEvidenceRefs(collectEvidence(data.momentum))
  const currentYear = Math.max(new Date().getFullYear(), ...momentumEvidence.map(evidenceYear).filter((year): year is number => year !== null))
  const startYear = Math.max(2019, currentYear - 7)
  const yearlyCounts = Array.from({ length: currentYear - startYear + 1 }, (_, index) => {
    const year = startYear + index
    return { year, count: momentumEvidence.filter(evidence => evidenceYear(evidence) === year).length }
  })
  const maxCount = Math.max(1, ...yearlyCounts.map(point => point.count))
  const points: Array<[number, number]> = yearlyCounts.map((point, index) => [
    55 + index * (790 / Math.max(1, yearlyCounts.length - 1)),
    270 - (point.count / maxCount) * 190,
  ])
  const chartPath = smoothPath(points)
  const areaPath = points.length > 0 ? `${chartPath} L ${points[points.length - 1][0]} 290 L ${points[0][0]} 290 Z` : ''
  const horizons = data.momentum.next_horizon
  const currentSignals = [
    ...data.momentum.frontier_projects.map((item, index) => ({ item, kind: 'Frontier project', index })),
    ...data.momentum.quality_guardrails.map((item, index) => ({ item, kind: 'Quality guardrail', index })),
  ]
  const recentSignals = yearlyCounts.reduce((total, point) => total + point.count, 0)

  return (
    <section className="ja-view ja-view--momentum" aria-labelledby="journey-heading-momentum">
      <div className="ja-frame">
        <ViewHeader
          id="momentum"
          eyebrow="Momentum & next horizon"
          title={<>The next chapter is already <em>leaving evidence.</em></>}
          accent="gold"
          lede="Recent work joins AI-native engineering, regulated-software rigor, measurable quality guardrails, and teaching. The future direction is visible without pretending it is guaranteed."
          caveat="The curve counts dated evidence references in the momentum dataset. It is a documentation signal—not a productivity score or forecast."
        />

        {data.momentum.ai_session_metrics.length > 0 && (
          <div className="ja-momentum-metrics"><MetricGrid metrics={data.momentum.ai_session_metrics} /></div>
        )}

        <div className="ja-momentum-layout">
          <div className="ja-momentum-primary">
            <div className="ja-panel ja-momentum-chart">
              <div className="ja-panel-label"><span>Dated momentum signals</span><span>{startYear}—{currentYear}</span></div>
              <div className="ja-chart-scroll" role="region" tabIndex={0} aria-label="Momentum evidence chart; scroll horizontally on small screens">
                <svg className="ja-momentum-svg" viewBox="0 0 900 330" role="img" aria-labelledby="momentum-chart-title momentum-chart-desc">
                  <title id="momentum-chart-title">Recent momentum evidence by year</title>
                  <desc id="momentum-chart-desc">Counts of evidence references attached to AI, frontier projects, quality guardrails, and next-horizon work.</desc>
                  <defs>
                    <linearGradient id="momentum-gradient" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="0%" stopColor="#8b5e00" stopOpacity="0.32" />
                      <stop offset="100%" stopColor="#8b5e00" stopOpacity="0.015" />
                    </linearGradient>
                  </defs>
                  {[90, 150, 210, 270].map(y => <line key={y} className="ja-momentum-grid" x1="45" x2="855" y1={y} y2={y} />)}
                  <path className="ja-momentum-area" d={areaPath} />
                  <path className="ja-momentum-line" d={chartPath} />
                  {yearlyCounts.map((point, index) => {
                    const [x, y] = points[index]
                    return (
                      <g key={point.year}>
                        <circle className="ja-momentum-dot" cx={x} cy={y} r="6"><title>{point.year}: {point.count} dated evidence signals</title></circle>
                        <text className="ja-momentum-year" x={x} y="313" textAnchor="middle">{point.year}</text>
                        {point.count > 0 && <text className="ja-momentum-label" x={x} y={y - 13} textAnchor="middle">{point.count}</text>}
                      </g>
                    )
                  })}
                </svg>
              </div>
            </div>

            <div className="ja-momentum-callout">
              <strong>{recentSignals}</strong>
              <p>
                dated evidence signals support the current trajectory across AI sessions, frontier projects, quality guardrails, and next-horizon work. Direction is grounded; outcomes remain to be earned.
              </p>
            </div>
          </div>

          <aside className="ja-panel ja-horizon-list">
            <div className="ja-panel-label"><span>Next horizon</span><span>Aspirational, not forecast</span></div>
            {horizons.slice(0, 6).map((item, index) => {
              const title = textField(item, ['title', 'label', 'name', 'horizon'], `Horizon ${index + 1}`)
              const description = textField(item, ['summary', 'description', 'statement', 'detail'])
              return (
                <article className="ja-horizon-item" key={textField(item, ['id'], `${title}-${index}`)}>
                  <span className="ja-horizon-number">VECTOR / {String(index + 1).padStart(2, '0')}</span>
                  <h3>{title}</h3>
                  {description && <p>{sentence(description, 165)}</p>}
                  <EvidenceBadge evidence={strongestEvidence(evidenceFor(item))} />
                  <CaveatLabels labels={caveatsFor(item)} />
                </article>
              )
            })}
          </aside>

        </div>

        {currentSignals.length > 0 && (
          <div className="ja-momentum-signals" role="list" aria-label="Current frontier projects and quality guardrails">
            {currentSignals.slice(0, 8).map(({ item, kind, index }) => {
              const title = textField(item, ['title', 'label', 'name', 'project', 'guardrail'], `${kind} ${index + 1}`)
              const description = textField(item, ['summary', 'description', 'statement', 'detail'])
              return (
                <article className="ja-momentum-signal" role="listitem" key={`${kind}-${textField(item, ['id'], `${title}-${index}`)}`}>
                  <span>{kind}</span>
                  <h3>{title}</h3>
                  {description && <p>{sentence(description, 170)}</p>}
                  <SourceLine evidence={evidenceFor(item)} />
                  <CaveatLabels labels={caveatsFor(item)} />
                </article>
              )
            })}
          </div>
        )}

        <GlobalCaveat>
          Next-horizon entries describe direction and active exploration. They must not be read as delivered outcomes unless a separate outcome-ledger record documents completion.
        </GlobalCaveat>
      </div>
    </section>
  )
}

const VIEW_COMPONENTS: Record<JourneyViewId, () => React.JSX.Element> = {
  portrait: ExecutivePortrait,
  journey: TwentyYearJourney,
  capabilities: CapabilityCompounder,
  outcomes: OutcomeLedger,
  respect: TrustRespect,
  influence: InfluenceWeb,
  service: TeachingServiceRipple,
  momentum: MomentumHorizon,
}

export function JourneyAtlas({ activeView }: { activeView: JourneyViewId }) {
  const ActiveView = useMemo(() => VIEW_COMPONENTS[activeView] ?? ExecutivePortrait, [activeView])
  return (
    <div
      role="region"
      aria-labelledby={`journey-heading-${activeView}`}
      data-active-view={activeView}
    >
      <ActiveView />
    </div>
  )
}
