import React, { useState } from 'react';
import type { PortfolioData } from '../types';
import { X, Printer, Copy, Check, Sparkles, Mail, Globe, MapPin, ShieldCheck, Quote, CheckCircle2 } from 'lucide-react';

interface DossierModalProps {
  isOpen: boolean;
  onClose: () => void;
  data: PortfolioData;
}

type EvaluationLensKey = 'ORG_SCALE' | 'TECH_STRATEGY' | 'PLATFORM_SCALE' | 'REGULATED' | 'AI_GOVERNANCE';

interface RoleDossierConfig {
  key: EvaluationLensKey;
  tabLabel: string;
  category: string;
  letterheadRole: string;
  badge: string;
  subtitle: string;
  summaryMapping: string;
  profileSummary: string;
  metrics: { value: string; label: string; detail: string }[];
  highlights: string[];
  featuredTurnaround: {
    title: string;
    scope: string;
    defaultTrajectory: string;
    intervention: string;
    outcome: string;
  };
  endorsement: {
    author: string;
    role: string;
    text: string;
  };
  competencies: string[];
}

export const DossierModal: React.FC<DossierModalProps> = ({ isOpen, onClose, data }) => {
  const [evaluationLens, setEvaluationLens] = useState<EvaluationLensKey>(() => {
    if (typeof window !== 'undefined') {
      const params = new URLSearchParams(window.location.search);
      const lens = params.get('lens');
      if (lens && ['ORG_SCALE', 'TECH_STRATEGY', 'PLATFORM_SCALE', 'REGULATED', 'AI_GOVERNANCE'].includes(lens)) {
        return lens as EvaluationLensKey;
      }
    }
    return 'ORG_SCALE';
  });
  const [copied, setCopied] = useState(false);

  const lensConfigs: Record<EvaluationLensKey, RoleDossierConfig> = {
    ORG_SCALE: {
      key: 'ORG_SCALE',
      tabLabel: 'VP / Engineering Leadership',
      category: 'Global Engineering Organization Leadership and Delivery Execution',
      letterheadRole: 'VP / Head of Engineering • Global Organization Leadership and Talent Multiplier',
      badge: 'EXECUTIVE LEADERSHIP DOSSIER',
      subtitle: 'Scale, Hiring Bar, Team Velocity, Culture Transformation, and Execution Cadence',
      summaryMapping: 'Evaluates executive capability in managing large multi-site engineering organizations, raising technical talent density, establishing delivery cadence, and mentoring technical leaders.',
      profileSummary: 'Engineering executive with 18+ years leading global technical organizations across Philips and Amazon. Track record of scaling developer ecosystems to 7,000+ engineers, standardizing delivery across multi-site global teams, elevating hiring bars through Amazon Bar Raiser protocols with +18% candidate NPS, and mentoring 30+ senior engineers into Staff and Principal leadership roles with zero attrition among key leads.',
      metrics: [
        { value: '7,000+', label: 'Developer Ecosystem', detail: 'Worldwide engineering teams on standardized shared platforms' },
        { value: '100%', label: 'On-Time Delivery', detail: 'Sustained milestone execution across high-visibility enterprise programs' },
        { value: '30+', label: 'Staff & Principal Leads', detail: 'Engineers directly mentored and promoted into senior technical leadership' },
        { value: '900+', label: 'Masterclass Evaluations', detail: '4.64/5 Amazon Senpai rating, 9.57/10 seminar score across 50+ sessions' },
        { value: '+18%', label: 'Hiring NPS Lift', detail: 'Overhauled assessment standards and raised talent density across business units' },
        { value: '32', label: 'Academic Recruits Cultivated', detail: 'University incubation cohorts trained, evaluated, and retained full-time' }
      ],
      highlights: [
        'Rebuilt multi-site engineering delivery rhythms across distributed divisions, converting delayed multi-quarter releases into reliable quarterly deployment milestones with 100% on-time execution.',
        'Established the Software Excellence Competency across Philips, creating uniform craftsmanship standards, architecture review boards, and career ladders spanning North America, Europe, and Asia.',
        'Calibrated interview and hiring standards across global teams using Amazon Bar Raiser methodology, resulting in a +18% candidate NPS and +15% hiring manager satisfaction lift.',
        'Delivered 50+ masterclasses and keynotes across Amazon, Philips, and top universities with 900+ verified post-session evaluations (4.64/5 Amazon Senpai rating, 9.57/10 seminar score).',
        'Constructed the university talent incubation pipeline, assessing 100+ candidates and guiding 32 university recruits through structured engineering bootcamps with zero early attrition.'
      ],
      featuredTurnaround: {
        title: 'Global Engineering Organization and Craftsmanship Standardization',
        scope: '7,000+ Developers Across North America, Europe, and Asia',
        defaultTrajectory: 'Disparate engineering practices and inconsistent quality gates across business units resulted in recurring release slips and prolonged onboarding times.',
        intervention: 'Institutionalized uniform engineering standards, established competency review boards, and introduced structured masterclasses with documented participant feedback loops.',
        outcome: 'Attained 100% on-time delivery on core releases, elevated talent density across 3 global divisions, and mentored 30+ senior engineers into Staff and Principal roles.'
      },
      endorsement: {
        author: 'Client Delivery and Account Leadership',
        role: 'Enterprise Delivery Leadership',
        text: 'Datta resolved critical end-to-end integration issues under high-pressure release deadlines, creating repeatable process discipline and rebuilding partner confidence.'
      },
      competencies: [
        'Global Engineering Org Scaling (7,000+ developers)',
        'Amazon Bar Raiser Hiring Bar Calibration',
        'Multi-Site Delivery Rhythm and Cadence Execution',
        'Talent Incubation and University Pipeline (32 cohorts)',
        'Cross-Functional Stakeholder Alignment and P&L Accountability',
        'Engineering Competency Leadership and Career Laddering'
      ]
    },

    TECH_STRATEGY: {
      key: 'TECH_STRATEGY',
      tabLabel: 'CTO / Technology Strategy',
      category: 'Enterprise Technology Strategy and Architecture Modernization',
      letterheadRole: 'Chief Technology Officer / Chief Architect • Systems Modernization and IP',
      badge: 'TECHNOLOGY STRATEGY & ARCHITECTURE DOSSIER',
      subtitle: 'Architecture Turnaround, Technical Debt Elimination, Patent Innovation, and P&L Alignment',
      summaryMapping: 'Evaluates architectural judgment under commercial constraints, systemic legacy modernizations, intellectual property creation, and alignment with corporate balance sheets.',
      profileSummary: 'Enterprise technology strategist and systems architect with 18+ years modernizing mission-critical architectures and eliminating systemic technical debt. Holder of 2 software systems inventions (1 Granted US Patent, 1 Published Application). Proven track record turning around high-risk legacy codebases via incremental strangler migrations, delivering $2.3M in direct verified savings and $3.8M in contracted platform pipeline without business disruption or downtime.',
      metrics: [
        { value: '$2.3M', label: 'Direct Technical Savings', detail: 'Recurring cost reduction achieved through legacy technical debt elimination' },
        { value: '$3.8M', label: 'Platform Revenue Pipeline', detail: 'Contracted enterprise customer pipeline unblocked through architecture turnaround' },
        { value: '2 Patents', label: 'US Systems Inventions', detail: 'US 8,560,487 (Granted Patent) and US 2015/0095117 (Published Application)' },
        { value: '138 Projects', label: 'State of Craftsmanship Audit', detail: 'Audited and benchmarked engineering maturity across 80% of global software org' },
        { value: '100%', label: 'Zero-Downtime Migration', detail: 'Strangler modernizations executed without active commercial contract disruption' },
        { value: '0 Breaches', label: 'Compliance & IP Integrity', detail: 'Zero regulatory non-conformances across international audit cycles' }
      ],
      highlights: [
        'Architected a multi-year digital modernization that dismantled legacy technical debt, realizing $2.3M in direct verified savings and unblocking $3.8M in contracted client pipeline.',
        'Resisted high-risk full codebase rewrites, designing modular strangler pattern migrations that maintained 99.99% availability throughout the 3-year transformation.',
        'Authored 2 US software systems inventions: US Patent 8,560,487 B2 (Decision tracking systems) and US Application 2015/0095117 A1 (Advanced search systems).',
        'Conducted the global State of Craftsmanship audit across 138 projects covering 80% of Philips worldwide software organization, establishing baseline architecture maturity benchmarks.',
        'Co-authored the Enterprise DevOps Reference Architecture whitepaper in the Chief Architect Office (CAO) alongside Philips Fellow Architects.'
      ],
      featuredTurnaround: {
        title: 'Three-Year Enterprise Digital Modernization and Debt Elimination',
        scope: 'Healthcare Enterprise Platform Modernization',
        defaultTrajectory: 'Accumulated technical debt and fragile monolithic dependencies threatened active commercial contracts and caused recurring integration failures.',
        intervention: 'Devised an incremental strangler migration strategy, isolating critical business logic into containerized modular microservices with automated regression boundaries.',
        outcome: 'Generated $2.3M in direct operational savings, enabled $3.8M in new customer platform contracts, and eliminated single points of systemic failure.'
      },
      endorsement: {
        author: 'Global VP of Design and Innovation',
        role: 'Executive Leadership, Design and Innovation',
        text: 'Datta and team built a practical, intuitive platform that solves real engineering friction. His structured approach kept stakeholders aligned and demonstrated meaningful systems leadership.'
      },
      competencies: [
        'Enterprise Technology Strategy and P&L Alignment',
        'Systemic Technical Debt Elimination ($2.3M Saved)',
        'Strangler Pattern Legacy Modernization',
        'US Patent Portfolio Development (US 8,560,487)',
        'Global Craftsmanship Auditing (138 Projects)',
        'Chief Architect Office Governance and Whitepapers'
      ]
    },

    PLATFORM_SCALE: {
      key: 'PLATFORM_SCALE',
      tabLabel: 'Head of Platform / Cloud',
      category: 'Platform Engineering, Cloud Infrastructure, and Distributed Systems',
      letterheadRole: 'Head of Platform Engineering • Cloud Infrastructure, FinOps and Scalability',
      badge: 'PLATFORM & CLOUD INFRASTRUCTURE DOSSIER',
      subtitle: 'Distributed Systems, FinOps Optimization, Containerization, and Multi-Region Availability',
      summaryMapping: 'Evaluates platform engineering leadership, distributed backend scalability, cloud financial optimization (FinOps), containerization, and platform reliability.',
      profileSummary: 'Platform engineering leader specializing in high-throughput distributed infrastructure, containerization, and cloud financial optimization (FinOps). Led backend engineering teams at Amazon scaling microservices to 8M+ daily transactions with sub-second latency, engineered automated enterprise Service-Ops platforms unlocking $300K+ in recurring infrastructure savings, and spearheaded OS-agnostic containerization across diagnostic medical platforms.',
      metrics: [
        { value: '8M+', label: 'Daily Distributed Tx', detail: 'High-throughput microservices processed with sub-second latency at Amazon' },
        { value: '99.999%', label: 'Platform Reliability SLA', detail: 'Shared engineering platforms delivering uninterrupted service to 7,000+ developers' },
        { value: '$300K+', label: 'Recurring FinOps Savings', detail: 'Cloud infrastructure optimization and automated resource reclamation at Philips' },
        { value: '100%', label: 'OS-Agnostic Portability', detail: 'Diagnostic software decoupled from host operating systems via containerization' },
        { value: '0 Downtime', label: 'Multi-Region Migration', detail: 'Multi-region data cutover completed with zero production interruption' },
        { value: 'CAO Author', label: 'DevOps Reference Arch', detail: 'Enterprise CI/CD whitepaper authored for Chief Architect Office' }
      ],
      highlights: [
        'Engineered backend microservices at Amazon handling 8M+ daily transactions, maintaining sub-second latency and resilient failure domains during peak load spikes.',
        'Spearheaded Project Themis, containerizing complex diagnostic software into OS-agnostic modular environments and eliminating cross-site environment configuration drift.',
        'Constructed the enterprise Service-Ops automation platform, eliminating redundant cloud instances and returning $300K+ in annual recurring cloud spend to engineering balance sheets.',
        'Architected zero-downtime multi-region cloud migrations, isolating failover blast radiuses and guaranteeing continuous platform availability.',
        'Co-authored the Chief Architect Office (CAO) Enterprise DevOps Reference Architecture, standardizing container deployment pipelines for global healthcare product lines.'
      ],
      featuredTurnaround: {
        title: 'OS-Agnostic Diagnostic Platform Containerization (Project Themis)',
        scope: 'Diagnostic Systems Global Engineering',
        defaultTrajectory: 'Diagnostic software tightly coupled to specific host operating systems caused multi-week environment setup delays and configuration drift across distributed sites.',
        intervention: 'Mandated containerized architecture across diagnostic services, decoupling business logic from underlying host OS dependencies and standardizing deployment images.',
        outcome: 'Attained 100% OS-agnostic portability, eliminated cross-site setup downtime, and unblocked milestone reviews with predictable deployment cadence.'
      },
      endorsement: {
        author: 'Diagnostic Systems Engineering Lead',
        role: 'Precision Diagnosis Systems Engineering',
        text: 'Datta guided the team to containerize the application, making it OS-agnostic and fast to port to new environments. His structured approach kept stakeholders aligned and prevented work from stalling due to unresolved dependencies.'
      },
      competencies: [
        'High-Throughput Distributed Systems (8M+ Daily Tx)',
        'Cloud FinOps Optimization ($300K+ Annual Savings)',
        'Containerized Platform Architecture (Docker / K8s)',
        'Zero-Downtime Multi-Region Cloud Migrations',
        'Enterprise DevOps Reference Architecture (CAO)',
        'Service-Ops Automation and 99.999% SLA Platform Resilience'
      ]
    },

    REGULATED: {
      key: 'REGULATED',
      tabLabel: 'VP / MedTech Quality & Compliance',
      category: 'Regulated Medical Device Software and Mission-Critical Quality',
      letterheadRole: 'VP of Software Quality and Regulatory Engineering • MedTech Systems',
      badge: 'REGULATED SYSTEMS & CLINICAL QUALITY DOSSIER',
      subtitle: 'IEC 62304, ISO 13485, Risk Management, and Automated Compliance Engineering',
      summaryMapping: 'Evaluates leadership in mission-critical healthcare systems, clinical device audits, risk management (ISO 14971), and automated regulatory quality gates.',
      profileSummary: 'Mission-critical healthcare systems leader with deep expertise in regulated medical device software (IEC 62304, ISO 13485, ISO 14971). Authorized clinical ultrasound architectures across international markets, embedded automated regulatory quality gates into CI/CD pipelines to cut audit readiness from 90 days to continuous real-time verification, and maintained zero regulatory release halts across all external audit cycles.',
      metrics: [
        { value: '75%', label: 'Traceability Time Cut', detail: 'Regulatory validation cycle accelerated from 40 hours down to 10 hours per release' },
        { value: '0 Halts', label: 'Regulatory Audit Halts', detail: 'Zero release suspensions across international FDA and notified body audits' },
        { value: 'Real-Time', label: 'Continuous Audit Prep', detail: 'Audit evidence generation compressed from 90 days down to real-time CI/CD verification' },
        { value: 'Class II/III', label: 'Medical Device Scope', detail: 'Authorized software architectures for clinical ultrasound and diagnostic imaging' },
        { value: '100%', label: 'Compliance Seal', detail: 'Verified adherence to IEC 62304, ISO 13485, and ISO 14971 standards' },
        { value: '3 Global BUs', label: 'Enterprise Regulatory Reach', detail: 'Regulatory traceability framework standardized across 3 international business divisions' }
      ],
      highlights: [
        'Architected SUTRA, an automated AI-indexed knowledge graph for regulatory traceability that reduced release validation overhead by 75% (from 40 hours down to 10 hours).',
        'Authorized mission-critical software architectures for clinical ultrasound devices, ensuring full traceability between clinical requirements, hazards, and verification proofs.',
        'Integrated automated compliance verification checks into daily CI/CD build pipelines, cutting formal audit preparation cycles from 90 days down to real-time readiness.',
        'Enforced strict data isolation and redaction boundary protocols, ensuring zero proprietary or customer patient data exposure across published technical assets.',
        'Maintained an unbroken track record of zero regulatory launch delays or non-compliance release halts across all external notified body and regulatory audits.'
      ],
      featuredTurnaround: {
        title: 'Automated Regulatory Traceability and Verification Platform (SUTRA)',
        scope: 'Philips Healthcare Multi-Business Enterprise Deployment',
        defaultTrajectory: 'Engineers spent 40 hours per release manually linking requirements, risk hazard matrices, and test proofs across fragmented databases, creating audit risk.',
        intervention: 'Architected an automated semantic graph data platform linking requirements to test outcomes and regulatory artifacts with automated gap detection.',
        outcome: 'Compressed validation cycle time from 40 hours down to 10 hours (75% gain), secured adoption across 3 global divisions, and earned executive commendation.'
      },
      endorsement: {
        author: 'Global VP of Design and Innovation',
        role: 'Executive Leadership, Design and Innovation',
        text: 'SUTRA demonstrates a meaningful step forward in how our engineering teams navigate complex systems. Datta and team built a practical, intuitive platform that solves real engineering friction.'
      },
      competencies: [
        'Medical Device Software Engineering (IEC 62304)',
        'Quality Management Systems (ISO 13485)',
        'Clinical Risk Hazard Management (ISO 14971)',
        'Automated CI/CD Regulatory Quality Gates',
        'Knowledge-Graph Regulatory Traceability (SUTRA)',
        'Zero-Raw-File Compliance Boundary Verification'
      ]
    },

    AI_GOVERNANCE: {
      key: 'AI_GOVERNANCE',
      tabLabel: 'Head of Enterprise AI',
      category: 'Enterprise AI Strategy, Applied Machine Learning, and Regulatory Governance',
      letterheadRole: 'Head of Enterprise AI and Applied Intelligence • AI Systems and Governance',
      badge: 'ENTERPRISE AI & REGULATORY GOVERNANCE DOSSIER',
      subtitle: 'Zero-Hallucination Boundaries, Knowledge Graphs, FDA Safe Harbor, and Enterprise Traceability',
      summaryMapping: 'Evaluates leadership in generative AI adoption, semantic knowledge graph architectures, zero-hallucination deterministic validation, and regulated AI governance.',
      profileSummary: 'Enterprise AI engineering leader pioneering responsible, audit-defensible AI adoption in regulated healthcare. Architect of SUTRA, an enterprise AI-indexed knowledge-graph platform that reduced release validation overhead by 75% across 3 global business units. Established multi-tier GenAI safe harbor frameworks enforcing zero-hallucination boundaries, mathematical traceability, and strict HIPAA data isolation.',
      metrics: [
        { value: 'SUTRA', label: 'AI Traceability Platform', detail: 'AI-indexed semantic knowledge graph connecting engineering artifacts' },
        { value: '75%', label: 'Validation Acceleration', detail: 'Release validation cycle compressed from 40 hours to 10 hours' },
        { value: 'Zero', label: 'Unverified Inferences', detail: 'Zero unverified AI outputs permitted in regulated production environments' },
        { value: '3 Divisions', label: 'Production Enterprise Scale', detail: 'Deployed across 3 global healthcare business units' },
        { value: '100% Sealed', label: 'HIPAA & IP Boundary', detail: 'Multi-tier risk classification with air-gapped private model isolation' },
        { value: 'FDA Align', label: 'Pre-Market Regulatory Guard', detail: 'Deterministic validation boundary satisfying FDA healthcare AI guidelines' }
      ],
      highlights: [
        'Envisioned and architected SUTRA, transforming disconnected enterprise data into an AI-indexed knowledge graph that reduced engineering validation overhead by 75%.',
        'Architected the multi-tier Enterprise AI Governance Framework, classifying AI workloads into Tier 1 (Deterministic/Regulated), Tier 2 (Internal Product), and Tier 3 (Exploratory).',
        'Instituted zero-hallucination engineering guardrails, replacing unconstrained generative LLM outputs with semantic retrieval and deterministic schema-bound validation.',
        'Secured adoption of AI-assisted engineering discovery across 3 global business units, receiving formal executive commendation from the Global VP of Design and Innovation.',
        'Delivered Sutra Release 3 in 2026, shipping automated test-scenario gap detection and generation across AV&I, SRC, and IGT-MoS, and expanding into AIOrchestration.',
        'Secured 2 XITE Cohort 5 selections for Ultrasound Defect-Triaging and AV&I automated test generation; earned public commendation from Executive VP and Chief Patient Safety and Quality Officer on Viva Engage for Kairos ReqSpec IEC 62304 compliance acceleration.',
        'Enforced private, zero-retention model tenancy ensuring proprietary healthcare intellectual property and patient records are never leaked to external public models.'
      ],
      featuredTurnaround: {
        title: 'Enterprise AI Knowledge Graph and Automated Traceability Platform',
        scope: 'Multi-Business Unit Enterprise AI Adoption',
        defaultTrajectory: 'Engineers spent days manually searching disconnected databases to correlate requirements and verification evidence, limiting release velocity.',
        intervention: 'Architected an AI-indexed semantic knowledge graph with automated relationship extraction, semantic query indexing, and automated coverage gap detection.',
        outcome: 'Reduced verification latency by 75%, established the enterprise standard for audit-defensible AI, and demonstrated responsible AI adoption in regulated MedTech.'
      },
      endorsement: {
        author: 'Global VP of Design and Innovation',
        role: 'Executive Leadership, Design and Innovation',
        text: 'SUTRA demonstrates a meaningful step forward in how our engineering teams navigate complex systems. Datta and team built a practical, intuitive platform that solves real engineering friction.'
      },
      competencies: [
        'Enterprise Knowledge-Graph Architecture (SUTRA)',
        'Zero-Hallucination Deterministic Validation',
        'Multi-Tier AI Risk Classification and Governance',
        'FDA Pre-Market Healthcare AI Alignment',
        'HIPAA Zero-Data-Leak Private Model Tenancy',
        'Semantic Search and Automated Relationship Indexing'
      ]
    }
  };

  const currentLens = lensConfigs[evaluationLens];

  // Keep document title in sync with active evaluation lens for native Cmd+P / Print dialogs
  React.useEffect(() => {
    if (!isOpen) return;
    const originalTitle = document.title;
    document.title = `${data.profile.name} - ${currentLens.category}`;
    return () => {
      document.title = originalTitle;
    };
  }, [isOpen, evaluationLens, currentLens.category, data.profile.name]);

  const handlePrint = () => {
    const originalTitle = document.title;
    document.title = `${data.profile.name} - ${currentLens.category}`;
    window.print();
    setTimeout(() => {
      document.title = originalTitle;
    }, 1000);
  };

  const handleCopy = () => {
    const text = `
EXECUTIVE CANDIDATE DOSSIER: ${data.profile.name.toUpperCase()}
Executive Alignment: ${currentLens.letterheadRole}
Dossier Type: ${currentLens.badge}
Evaluation Focus: ${currentLens.category} (${currentLens.subtitle})

EXECUTIVE SUMMARY:
${currentLens.profileSummary}

SCORECARD FOCUS:
${currentLens.summaryMapping}

KEY QUANTITATIVE BENCHMARKS:
${currentLens.metrics.map(m => `- ${m.label}: ${m.value} (${m.detail})`).join('\n')}

DEMONSTRATED INTERVENTIONS & MEASURABLE IMPACT:
${currentLens.highlights.map(h => `- ${h}`).join('\n')}

FEATURED SYSTEMIC TURNAROUND:
Title: ${currentLens.featuredTurnaround.title} (${currentLens.featuredTurnaround.scope})
- Default Trajectory: ${currentLens.featuredTurnaround.defaultTrajectory}
- Strategic Intervention: ${currentLens.featuredTurnaround.intervention}
- Measurable Consequence: ${currentLens.featuredTurnaround.outcome}

VERIFIED EXECUTIVE ENDORSEMENT:
"${currentLens.endorsement.text}"
- ${currentLens.endorsement.author}, ${currentLens.endorsement.role}

CORE COMPETENCIES:
${currentLens.competencies.map(c => `- ${c}`).join('\n')}

CONTACT:
Email: ${data.profile.email} | LinkedIn: linkedin.com/in/${data.profile.linkedin}
Website: ${data.profile.website} | Location: ${data.profile.location}
    `.trim();

    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        {/* Interactive Screen-Only Header */}
        <div className="modal-header screen-only">
          <div>
            <div className="hero-tag" style={{ marginBottom: '0.5rem' }}>
              <Sparkles size={14} /> Search Committee Evaluation Memorandum
            </div>
            <h2 style={{ fontSize: '1.6rem' }}>Executive Candidate Evaluation Dossier</h2>
            <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
              Fully customized dossier tailored to specific executive search mandates, committee scorecards, and verifiable business impact.
            </p>
          </div>
          <button className="modal-close-btn" onClick={onClose} aria-label="Close modal">
            <X size={20} />
          </button>
        </div>

        {/* Interactive Screen-Only Lens Switcher (Pill Bar + Dropdown Fallback) */}
        <div className="role-selector screen-only">
          <label htmlFor="role-select">Select Executive Mandate & Search Committee Scorecard:</label>
          <div className="dossier-lens-pills">
            {(Object.keys(lensConfigs) as EvaluationLensKey[]).map((k) => {
              const cfg = lensConfigs[k];
              const isSelected = evaluationLens === k;
              return (
                <button
                  key={k}
                  type="button"
                  className={`dossier-lens-pill ${isSelected ? 'active' : ''}`}
                  onClick={() => setEvaluationLens(k)}
                >
                  <span>{cfg.tabLabel}</span>
                </button>
              );
            })}
          </div>
          <select
            id="role-select"
            className="role-select dossier-select-fallback"
            value={evaluationLens}
            onChange={(e) => setEvaluationLens(e.target.value as EvaluationLensKey)}
          >
            {(Object.keys(lensConfigs) as EvaluationLensKey[]).map((k) => (
              <option key={k} value={k}>
                {lensConfigs[k].category} ({lensConfigs[k].tabLabel})
              </option>
            ))}
          </select>
        </div>

        {/* Printable Executive Dossier Memorandum */}
        <div className="printable-dossier dossier-preview">
          {/* Executive Letterhead */}
          <div className="dossier-letterhead">
            <div className="letterhead-top">
              <div>
                <h1 className="letterhead-name">{data.profile.name}</h1>
                <div className="letterhead-title">{currentLens.letterheadRole}</div>
              </div>
              <div className="letterhead-badge">
                {currentLens.badge}
              </div>
            </div>

            <div className="letterhead-contact-strip">
              <span><Mail size={13} /> {data.profile.email}</span>
              <span><Globe size={13} /> {data.profile.website}</span>
              <span>
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ verticalAlign: 'middle', marginRight: '3px' }}>
                  <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                  <rect x="2" y="9" width="4" height="12"></rect>
                  <circle cx="4" cy="4" r="2"></circle>
                </svg>
                linkedin.com/in/{data.profile.linkedin}
              </span>
              <span><MapPin size={13} /> {data.profile.location}</span>
            </div>
          </div>

          {/* Evaluation Lens Banner */}
          <div className="dossier-scorecard-banner">
            <div className="banner-title">
              <strong>Committee Scorecard Mandate:</strong> {currentLens.category}
            </div>
            <div className="banner-desc">
              {currentLens.summaryMapping}
            </div>
          </div>

          {/* Executive Profile Summary */}
          <div className="dossier-section">
            <h3 className="dossier-section-title">Mandate-Specific Executive Summary</h3>
            <p className="dossier-body-text">
              {currentLens.profileSummary}
            </p>
          </div>

          {/* Role-Specific Headline Impact Metrics Grid */}
          <div className="dossier-section">
            <h3 className="dossier-section-title">Verified Quantitative Benchmarks for this Role</h3>
            <div className="dossier-metrics-grid">
              {currentLens.metrics.map((m, idx) => (
                <div key={idx} className="dossier-metric-box">
                  <div className="metric-box-val">{m.value}</div>
                  <div className="metric-box-label">{m.label}</div>
                  <div className="metric-box-detail">{m.detail}</div>
                </div>
              ))}
            </div>
          </div>

          {/* Verified Interventions */}
          <div className="dossier-section">
            <h3 className="dossier-section-title">Demonstrated Systemic Interventions & Documented Impacts</h3>
            <ul className="dossier-highlight-list">
              {currentLens.highlights.map((item, idx) => (
                <li key={idx}>{item}</li>
              ))}
            </ul>
          </div>

          {/* Featured Systemic Turnaround Case Study */}
          <div className="dossier-section">
            <h3 className="dossier-section-title">Featured Signature Turnaround Case Study</h3>
            <div className="dossier-case-card">
              <div className="case-card-header">
                <span className="case-card-title">{currentLens.featuredTurnaround.title}</span>
                <span className="case-card-scope">{currentLens.featuredTurnaround.scope}</span>
              </div>
              <div className="case-card-grid">
                <div className="case-card-item">
                  <div className="case-item-lbl">Default Trajectory:</div>
                  <div className="case-item-val">{currentLens.featuredTurnaround.defaultTrajectory}</div>
                </div>
                <div className="case-card-item">
                  <div className="case-item-lbl">Strategic Intervention:</div>
                  <div className="case-item-val">{currentLens.featuredTurnaround.intervention}</div>
                </div>
                <div className="case-card-item highlight-outcome">
                  <div className="case-item-lbl">Observable Consequence:</div>
                  <div className="case-item-val">{currentLens.featuredTurnaround.outcome}</div>
                </div>
              </div>
            </div>
          </div>

          {/* Verified Executive Endorsement Quote */}
          <div className="dossier-section">
            <h3 className="dossier-section-title">Verified Executive Endorsement</h3>
            <div className="dossier-quote-card">
              <Quote size={20} className="dossier-quote-icon" />
              <p className="dossier-quote-text">"{currentLens.endorsement.text}"</p>
              <div className="dossier-quote-author">
                <strong>{currentLens.endorsement.author}</strong> • <span>{currentLens.endorsement.role}</span>
              </div>
            </div>
          </div>

          {/* Role-Specific Core Competencies */}
          <div className="dossier-section">
            <h3 className="dossier-section-title">Prioritized Scorecard Competencies</h3>
            <div className="dossier-competencies-grid">
              {currentLens.competencies.map((comp, idx) => (
                <div key={idx} className="dossier-comp-pill">
                  <CheckCircle2 size={13} color="var(--gold-400)" />
                  <span>{comp}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Footer Validation Strip */}
          <div className="dossier-print-footer">
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.4rem' }}>
              <ShieldCheck size={14} color="#10b981" />
              <span>Verified Track Record across Philips (18+ yrs, Youngest Principal) & Amazon (Distributed Scale). Zero-Raw-File Boundary Sealed.</span>
            </div>
            <div className="confidential-seal">
              Confidential • Prepared for Search Committee Review
            </div>
          </div>
        </div>

        {/* Interactive Screen-Only Actions */}
        <div className="screen-only" style={{ display: 'flex', justifyContent: 'flex-end', gap: '1rem', flexWrap: 'wrap', marginTop: '1.75rem' }}>
          <button className="btn btn-outline" onClick={handleCopy}>
            {copied ? <Check size={16} color="#34d399" /> : <Copy size={16} />}
            {copied ? 'Copied to Clipboard' : 'Copy Markdown'}
          </button>
          <button className="btn btn-gold" onClick={handlePrint}>
            <Printer size={16} />
            Print or Save as PDF
          </button>
        </div>
      </div>
    </div>
  );
};
