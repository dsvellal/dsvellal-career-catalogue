export type EvidenceLens = 'narrative' | 'proof' | 'method' | 'gaps'

export type ClaimKind = 'observed' | 'calculated' | 'interpreted'
export type ConfidenceLevel = 'high' | 'supported' | 'limited' | 'contested'
export type SupportRelationship = 'supports' | 'qualifies' | 'contradicts' | 'context'
export type SupportDirectness = 'direct' | 'aggregate' | 'indirect' | 'interpretive'
export type SourceGrade = 'corroborated' | 'documented' | 'self_reported'
export type SourceAccessState =
  | 'public_external'
  | 'public_excerpt'
  | 'private_held'
  | 'aggregate_only'

export interface PortfolioMeta {
  title?: string
  subtitle?: string
  generated_at?: string
  as_of?: string
  [key: string]: unknown
}

export interface PortfolioPage {
  id: string
  route: string
  label: string
  question: string
  summary: string
  claim_ids: string[]
}

export interface ClaimMetric {
  value: string | number
  display: string
  unit?: string
}

export interface ClaimConfidence {
  level: ConfidenceLevel
  rationale: string
}

export interface PortfolioClaim {
  id: string
  title: string
  statement: string
  kind: ClaimKind
  category: string
  scope: string
  attribution: string
  status: string
  period?: string
  metric?: ClaimMetric
  support_ids: string[]
  method_id?: string
  caveat_ids: string[]
  conflict_ids: string[]
  confidence: ClaimConfidence
}

export interface PortfolioSupport {
  id: string
  claim_id: string
  source_id: string
  relationship: SupportRelationship
  locator: string
  directness: SupportDirectness
  grade: SourceGrade
  rationale: string
}

export interface PortfolioSource {
  id: string
  title: string
  source_type: string
  source_date?: string
  publisher?: string
  access_state: SourceAccessState
  sha256: string
  checksum_scope: 'held_canonical_artifact'
  checksum_note: string
  approved_excerpt: string
  excerpt_kind: 'verbatim' | 'editorial_summary'
  external_url?: string
}

export interface MethodInput {
  id: string
  label: string
  source_id?: string
  claim_id?: string
  locator?: string
  value?: string | number
  unit?: string
}

export interface PortfolioMethod {
  id: string
  title: string
  kind: string
  version: string
  description: string
  formula?: string
  inputs: MethodInput[]
  inclusion_rules: string[]
  exclusion_rules: string[]
  deduplication: string
  rounding: string
  result: string
  caveat_ids: string[]
}

export interface PortfolioCaveat {
  id: string
  label: string
  description: string
}

export interface PortfolioConflict {
  id: string
  title: string
  status: string
  severity: string
  description: string
  source_ids: string[]
  affected_claim_ids: string[]
  resolution: string
}

export interface PortfolioRelationship {
  id: string
  title: string
  claim_id: string
  from_claim_id: string
  to_claim_id: string
  relation_type: string
  state: string
  statement: string
  reasoning: string
  method_id?: string
  support_ids: string[]
  confidence: ClaimConfidence
  caveat_ids: string[]
  limitation: string
}

export interface DataQuality {
  summary?: string
  coverage?: Record<string, unknown> | unknown[]
  export_gaps?: Record<string, unknown> | unknown[]
  [key: string]: unknown
}

export interface PortfolioData {
  meta: PortfolioMeta
  pages: PortfolioPage[]
  claims: PortfolioClaim[]
  supports: PortfolioSupport[]
  sources: PortfolioSource[]
  methods: PortfolioMethod[]
  relationships: PortfolioRelationship[]
  caveats: PortfolioCaveat[]
  conflicts: PortfolioConflict[]
  data_quality: DataQuality
}

export type PortfolioRoute =
  | { type: 'page'; pageId: string }
  | { type: 'claim'; id: string }
  | { type: 'source'; id: string }
  | { type: 'method'; id: string }
