import React, { useState } from 'react';
import type { PortfolioData } from '../types';
import { X, Printer, Copy, Check, Sparkles, Mail, Globe, MapPin, ShieldCheck, ArrowUpRight } from 'lucide-react';

interface DossierModalProps {
  isOpen: boolean;
  onClose: () => void;
  data: PortfolioData;
}

export const DossierModal: React.FC<DossierModalProps> = ({ isOpen, onClose, data }) => {
  const [evaluationLens, setEvaluationLens] = useState<'ORG_SCALE' | 'TECH_STRATEGY' | 'PLATFORM_SCALE' | 'REGULATED'>(() => {
    if (typeof window !== 'undefined') {
      const params = new URLSearchParams(window.location.search);
      const lens = params.get('lens');
      if (lens && ['ORG_SCALE', 'TECH_STRATEGY', 'PLATFORM_SCALE', 'REGULATED'].includes(lens)) {
        return lens as any;
      }
    }
    return 'ORG_SCALE';
  });
  const [copied, setCopied] = useState(false);

  const lensConfigs = {
    ORG_SCALE: {
      category: 'Engineering Organization Leadership',
      letterheadRole: 'Engineering Executive • Software Excellence Competency Lead',
      badge: 'EXECUTIVE LEADERSHIP DOSSIER',
      subtitle: 'Scale, Hiring Bar, Team Velocity, and Culture Transformation',
      summaryMapping: 'Evaluates executive capability in managing large multi-site engineering organizations, raising talent bars, and mentoring senior technical leaders.',
      profileSummary: 'Engineering executive with 18+ years leading global technical organizations across Philips and Amazon. Track record of scaling developer ecosystems to 7,000+ engineers, cutting delivery lead times by 60% with 99.999% platform reliability, elevating hiring bars with +18% candidate NPS, and mentoring 30+ senior engineers into Staff and Principal leadership roles.',
      highlights: [
        'Standardized software delivery across 7,000 developers worldwide, cutting product delivery cycles by 60% with 99.999% platform uptime.',
        'Directly mentored 30+ senior engineers into Staff and Principal leadership roles.',
        'Overhauled engineering hiring standards alongside executive leadership, driving +18% candidate NPS and +15% manager satisfaction gains.',
        'Delivered 50+ masterclasses and keynotes across Amazon, Philips, and top universities with 900+ verified post-session evaluations (4.64/5 Amazon Senpai rating, 9.57/10 seminar score).'
      ],
      metricOrder: ['Global Developer Reach', 'Leadership Influence', 'Direct P&L Impact', 'Validation Efficiency', 'Transaction Scale', 'Engineering Patents']
    },
    TECH_STRATEGY: {
      category: 'Enterprise Technology Strategy & Modernization',
      letterheadRole: 'Chief Architect & Enterprise Technology Strategist',
      badge: 'TECHNOLOGY STRATEGY & ARCHITECTURE DOSSIER',
      subtitle: 'Architecture Turnaround, Technical Debt Elimination, and P&L Alignment',
      summaryMapping: 'Evaluates architectural judgment under business constraints, legacy modernizations, and alignment with commercial milestones.',
      profileSummary: 'Enterprise technology strategist and systems architect with 18+ years modernizing mission-critical architectures and eliminating systemic technical debt. Holder of 2 software systems inventions (1 Granted US Patent, 1 Published Application). Proven track record turning around high-risk legacy codebases via incremental strangler migrations, delivering $2.3M in direct verified savings and $3.8M in contracted platform pipeline without business disruption.',
      highlights: [
        'Architected a 3-year digital modernization that produced $2.3M in direct verified savings and $3.8M in contracted platform pipeline.',
        'Replaced high-risk complete rewrites with disciplined incremental strangler migrations, protecting active client revenue.',
        'Authored 2 software systems inventions (1 Granted US Patent US 8,560,487, 1 Published Application US 2015/0095117) and the global 2024 State of Craftsmanship report.'
      ],
      metricOrder: ['Direct P&L Impact', 'Engineering Patents', 'Validation Efficiency', 'Global Developer Reach', 'Transaction Scale', 'Leadership Influence']
    },
    PLATFORM_SCALE: {
      category: 'Cloud Platform & High-Throughput Infrastructure',
      letterheadRole: 'Head of Platform Engineering • Cloud Infrastructure & FinOps Lead',
      badge: 'PLATFORM & CLOUD INFRASTRUCTURE DOSSIER',
      subtitle: 'Distributed Systems, FinOps Optimization, and Service-Ops Automation',
      summaryMapping: 'Evaluates platform engineering leadership, distributed backend scalability, and cloud infrastructure efficiency.',
      profileSummary: 'Platform engineering leader specializing in high-throughput distributed infrastructure and cloud financial optimization (FinOps). Led backend engineering teams at Amazon scaling microservices to 8M+ daily transactions with sub-second latency, and engineered automated enterprise Service-Ops platforms at Philips unlocking $300K+ in recurring infrastructure savings.',
      highlights: [
        'Built an enterprise Service-Ops platform unlocking $300K+ in recurring infrastructure savings at Philips.',
        'Led engineering teams at Amazon scaling 6 microservices that processed 8M+ daily transactions with sub-second latency.',
        'Consolidated fragmented multi-site CI/CD setups into an automated, zero-trust enterprise deployment standard.'
      ],
      metricOrder: ['Transaction Scale', 'Direct P&L Impact', 'Global Developer Reach', 'Validation Efficiency', 'Engineering Patents', 'Leadership Influence']
    },
    REGULATED: {
      category: 'Regulated Systems & Clinical Software Quality',
      letterheadRole: 'VP of Software Quality & Systems Architecture (Medical Devices)',
      badge: 'REGULATED SYSTEMS & CLINICAL QUALITY DOSSIER',
      subtitle: 'IEC 62304, ISO 13485, Risk Management, and Automated Compliance',
      summaryMapping: 'Evaluates leadership in mission-critical healthcare systems, clinical device audits, and shift-left quality gates.',
      profileSummary: 'Mission-critical healthcare systems leader with deep expertise in regulated medical device software (IEC 62304, ISO 13485). Authorized clinical ultrasound architectures across international markets, embedded automated regulatory quality gates into CI/CD pipelines to cut audit readiness from 90 days to real-time, and maintained zero regulatory release halts across all audit cycles.',
      highlights: [
        'Authorized mission-critical software architectures for clinical ultrasound and diagnostic devices across international markets.',
        'Integrated automated compliance checks into daily build pipelines, cutting audit preparation from 90 days to continuous real-time readiness.',
        'Maintained zero regulatory launch delays or non-compliance halts across all audit cycles.'
      ],
      metricOrder: ['Validation Efficiency', 'Engineering Patents', 'Global Developer Reach', 'Direct P&L Impact', 'Leadership Influence', 'Transaction Scale']
    }
  };

  const currentLens = lensConfigs[evaluationLens];

  // Dynamically prioritize metrics based on selected lens
  const prioritizedMetrics = [...data.profile.headlineMetrics].sort((a, b) => {
    const idxA = currentLens.metricOrder.indexOf(a.label);
    const idxB = currentLens.metricOrder.indexOf(b.label);
    return (idxA === -1 ? 99 : idxA) - (idxB === -1 ? 99 : idxB);
  });

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

DEMONSTRATED IMPACT IN THIS FOCUS AREA:
${currentLens.highlights.map(h => `- ${h}`).join('\n')}

VERIFIED METRICS:
${prioritizedMetrics.map(m => `- ${m.label}: ${m.value} (${m.detail})`).join('\n')}

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
              <Sparkles size={14} /> Committee Evaluation Tool
            </div>
            <h2 style={{ fontSize: '1.6rem' }}>Candidate Evaluation Dossier</h2>
            <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
              Tailored candidate summary aligned with specific executive search committee scorecards.
            </p>
          </div>
          <button className="modal-close-btn" onClick={onClose} aria-label="Close modal">
            <X size={20} />
          </button>
        </div>

        {/* Interactive Screen-Only Selector */}
        <div className="role-selector screen-only">
          <label htmlFor="role-select">Select Evaluation Lens (Hiring Committee Scorecard):</label>
          <select
            id="role-select"
            className="role-select"
            value={evaluationLens}
            onChange={(e) => setEvaluationLens(e.target.value as any)}
          >
            <option value="ORG_SCALE">Engineering Organization Leadership (Scale, People & P&L)</option>
            <option value="TECH_STRATEGY">Enterprise Technology Strategy & Modernization (Architecture & Debt)</option>
            <option value="PLATFORM_SCALE">Cloud Platform & High-Throughput Infrastructure (FinOps & Scale)</option>
            <option value="REGULATED">Regulated Healthcare & Mission-Critical Software (Quality & Compliance)</option>
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
              <strong>Evaluation Scorecard:</strong> {currentLens.category}
            </div>
            <div className="banner-desc">
              {currentLens.summaryMapping}
            </div>
          </div>

          {/* Executive Profile Summary */}
          <div className="dossier-section">
            <h3 className="dossier-section-title">Executive Profile</h3>
            <p className="dossier-body-text">
              {currentLens.profileSummary}
            </p>
          </div>

          {/* Verified Interventions */}
          <div className="dossier-section">
            <h3 className="dossier-section-title">Demonstrated Interventions & Measurable Impact</h3>
            <ul className="dossier-highlight-list">
              {currentLens.highlights.map((item, idx) => (
                <li key={idx}>{item}</li>
              ))}
            </ul>
          </div>

          {/* Headline Impact Metrics Grid */}
          <div className="dossier-section">
            <h3 className="dossier-section-title">Key Executive Benchmarks</h3>
            <div className="dossier-metrics-grid">
              {prioritizedMetrics.map((m, idx) => (
                <div key={idx} className="dossier-metric-box">
                  <div className="metric-box-val">{m.value}</div>
                  <div className="metric-box-label">{m.label}</div>
                  <div className="metric-box-detail">{m.detail}</div>
                  {m.links && m.links.length > 0 && (
                    <div className="screen-only" style={{ display: 'flex', gap: '0.35rem', marginTop: '0.4rem', flexWrap: 'wrap' }}>
                      {m.links.map((link, lIdx) => (
                        <a
                          key={lIdx}
                          href={link.url}
                          target="_blank"
                          rel="noreferrer"
                          style={{
                            fontSize: '0.675rem',
                            color: 'var(--gold-400)',
                            display: 'inline-flex',
                            alignItems: 'center',
                            gap: '0.2rem',
                            textDecoration: 'underline'
                          }}
                        >
                          {link.label} <ArrowUpRight size={10} />
                        </a>
                      ))}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>

          {/* Footer Validation Strip */}
          <div className="dossier-print-footer">
            <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.4rem' }}>
              <ShieldCheck size={14} color="#10b981" />
              <span>Verified Track Record across Philips (18+ yrs, Youngest Principal) & Amazon (Distributed Scale).</span>
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
