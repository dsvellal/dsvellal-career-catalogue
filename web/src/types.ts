export interface LinkItem {
  label: string;
  url: string;
  type?: string;
}

export interface MetricItem {
  label: string;
  value: string;
  detail: string;
  links?: LinkItem[];
}

export interface Endorsement {
  id: string;
  year?: string;
  company?: string;
  author: string;
  role: string;
  initiative: string;
  context: string;
  quote: string;
}

export interface EvidenceCardData {
  id: string;
  title: string;
  company: string;
  role: string;
  timeframe: string;
  timelineEra?: string;
  scope: string;
  archetype: string;
  defaultTrajectory: string;
  strategicDecision: string;
  intervention: string;
  observableConsequence: string;
  verificationAnchor: string;
  competencyTags: string[];
  metrics: string[];
  links?: LinkItem[];
}

export interface DecisionCaseStudy {
  id: string;
  year: string;
  company: string;
  timelineEra: string;
  domain: string;
  title: string;
  context: string;
  tradeOff: string;
  theBet: string;
  outcome: string;
  impactMetric?: string;
}

export interface ExecutiveProfile {
  name: string;
  headline: string;
  location: string;
  website: string;
  email: string;
  linkedin: string;
  summary: string;
  headlineMetrics: MetricItem[];
  coreCompetencies: string[];
}

export interface PortfolioData {
  profile: ExecutiveProfile;
  evidence: EvidenceCardData[];
  decisions: DecisionCaseStudy[];
  endorsements: Endorsement[];
  metadata: {
    version: string;
    complianceAudited: boolean;
    confidentialityTier: string;
    generatedBy: string;
  };
}
