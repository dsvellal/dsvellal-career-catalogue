import React from 'react';
import {
  Users,
  Target,
  Shield,
  BookOpen,
  CheckCircle,
  GraduationCap,
  Sparkles,
  BarChart3,
  Layers,
  FileText
} from 'lucide-react';

export const LeadershipOperatingSystem: React.FC = () => {
  const pillars = [
    {
      id: 'pillar-bar-raiser',
      icon: Target,
      tag: 'Hiring Governance',
      title: 'The Amazon Bar Raiser Talent Framework',
      subtitle: 'Institutionalizing hiring standards that raise team competency over time.',
      principles: [
        'Enforced independent veto authority on hiring decisions to protect long-term talent density against urgent headcount pressures.',
        'Calibrated interview panels against standardized behavioral and system architecture competencies to eliminate interviewer bias.',
        'Conducted bar raiser evaluations across distributed teams, ensuring every new hire outperformed the median team capability.'
      ],
      impact: 'Scaled engineering organizations across Amazon and Philips while maintaining zero degradation in technical delivery bars.'
    },
    {
      id: 'pillar-craftsmanship',
      icon: Shield,
      tag: 'Execution Discipline',
      title: 'Architectural Craftsmanship and Debt Control',
      subtitle: 'Eliminating architectural drift through deterministic verification and automated quality gates.',
      principles: [
        'Mandated static code health tracking, CodeScene technical debt analysis, and automated CI/CD validation gates prior to production merges.',
        'Enforced strict decoupling between core medical domain logic and operational infrastructure to prevent vendor lock-in.',
        'Instituted peer-led architecture review boards with written decision records to anchor accountability.'
      ],
      impact: 'Prevented multi-week integration blockers and sustained high release predictability across multi-site teams.'
    },
    {
      id: 'pillar-multiplier',
      icon: GraduationCap,
      tag: 'Talent Incubation',
      title: 'The Talent Multiplier and University Pipeline',
      subtitle: 'Developing engineering leaders from within and cultivating external academic talent pools.',
      principles: [
        'Mentored over 100 software engineers directly, guiding engineers from junior ICs to Lead Architects and Engineering Managers.',
        'Conducted guest lecture series on technical presentation, system design, and interview readiness at institutions including RVCE, BMSIT, NIE, and SIT.',
        'Organized annual academic book distributions and sponsorship drives to support underprivileged engineering scholars.'
      ],
      impact: 'Built a sustainable talent pipeline with proven retention, high peer engagement, and industry leadership recognition.'
    }
  ];

  const universityWorkshops = [
    { institution: 'RV College of Engineering (RVCE)', topic: 'SOLID Principles of Programming and Technical Interview Preparation' },
    { institution: 'BMS Institute of Technology (BMSIT)', topic: 'Cultivating Growth Attitude and Tackling System Uncertainty' },
    { institution: 'National Institute of Engineering (NIE)', topic: 'High-Stakes Technical Interview Mastery and Problem Deconstruction' },
    { institution: 'Siddaganga Institute of Technology (SIT)', topic: 'Microservices Architecture, Presentation Craft, and Rapid Decision-Making' }
  ];

  return (
    <section className="leadership-os-section" id="leadership-os">
      <div className="leadership-os-header">
        <div className="os-badge">
          <Users size={16} />
          <span>Leadership Operating System: Culture &amp; Talent Density</span>
        </div>
        <h2 className="leadership-os-title">
          How I Build Organizations: The Bar Raiser and Craftsmanship Model
        </h2>
        <p className="leadership-os-subtitle">
          Sustainable engineering excellence requires more than strong code. It requires an immutable hiring bar,
          relentless architectural discipline, and continuous investment in the next generation of engineers.
        </p>
      </div>

      {/* 3 Core Operating Pillars */}
      <div className="os-pillars-grid">
        {pillars.map((pillar) => {
          const Icon = pillar.icon;
          return (
            <div key={pillar.id} className="os-pillar-card">
              <div className="pillar-header">
                <div className="pillar-icon-box">
                  <Icon size={22} />
                </div>
                <span className="pillar-tag">{pillar.tag}</span>
              </div>

              <h3 className="pillar-title">{pillar.title}</h3>
              <p className="pillar-subtitle">{pillar.subtitle}</p>

              <div className="pillar-principles-list">
                {pillar.principles.map((principle, idx) => (
                  <div key={idx} className="principle-item">
                    <CheckCircle size={15} className="principle-bullet" />
                    <span>{principle}</span>
                  </div>
                ))}
              </div>

              <div className="pillar-impact-box">
                <strong>Verifiable Impact:</strong> {pillar.impact}
              </div>
            </div>
          );
        })}
      </div>

      {/* Enterprise Architectural Research and Governance Standards */}
      <div className="os-governance-section">
        <div className="os-governance-header">
          <div className="os-badge" style={{ color: '#a78bfa', background: 'rgba(167, 139, 250, 0.12)', borderColor: 'rgba(167, 139, 250, 0.25)' }}>
            <FileText size={16} />
            <span>Enterprise Research &amp; Governance Standards</span>
          </div>
          <h3 className="os-governance-title">
            Empirical Quality Audits and Architectural Reference Baselines
          </h3>
          <p className="os-governance-desc">
            Rigorous engineering governance requires verifiable empirical baselines. These institutional artifacts established corporate standards for software craftsmanship and CI/CD automation across global engineering divisions.
          </p>
        </div>

        <div className="os-governance-grid">
          {/* Card 1: 138-Project State of Craftsmanship Audit */}
          <div className="os-governance-card">
            <div className="governance-card-top">
              <div className="governance-icon-badge" style={{ color: '#38bdf8', background: 'rgba(56, 189, 248, 0.12)', borderColor: 'rgba(56, 189, 248, 0.25)' }}>
                <BarChart3 size={22} />
              </div>
              <span className="governance-tag">Global Empirical Audit (2023)</span>
            </div>

            <h4 className="governance-card-title">State of Software Craftsmanship: 138-Project Empirical Audit</h4>
            <div className="governance-card-scope">
              <strong>Scope:</strong> Innovation Excellence (IEX) / Software Excellence audit analyzing 138 active software engineering projects covering over 80% of Philips global engineering staff.
            </div>

            <div className="governance-key-metrics">
              <div className="gov-metric-item">
                <span className="gov-metric-num">138</span>
                <span className="gov-metric-lbl">Active Projects Audited</span>
              </div>
              <div className="gov-metric-item">
                <span className="gov-metric-num">&gt;80%</span>
                <span className="gov-metric-lbl">Global Developer Coverage</span>
              </div>
              <div className="gov-metric-item">
                <span className="gov-metric-num">94.1%</span>
                <span className="gov-metric-lbl">Manual Test Legacy Identified</span>
              </div>
              <div className="gov-metric-item">
                <span className="gov-metric-num">6 Mo</span>
                <span className="gov-metric-lbl">Avg Debt Payback Delay</span>
              </div>
            </div>

            <div className="governance-content-block">
              <div className="gov-block-label">Empirical Findings:</div>
              <ul className="gov-bullet-list">
                <li>Demonstrated direct correlation between unmonitored code rot, manual test dependencies, and critical regulatory CAPA failures in medical software.</li>
                <li>Identified systemic release blockers caused by 6-month debt repayment lag across enterprise business units.</li>
              </ul>
            </div>

            <div className="governance-content-block">
              <div className="gov-block-label">Systemic Intervention &amp; Mandate:</div>
              <ul className="gov-bullet-list">
                <li>Instituted automated architectural verification gates, CodeScene behavioral debt tracking, and deterministic build pipelines prior to production release.</li>
                <li>Shifted testing left to eliminate manual test bottlenecks and secure continuous audit readiness for medical regulatory bodies.</li>
              </ul>
            </div>

            <div className="governance-card-footer">
              <strong>Outcome:</strong> Delivered quantitative debt transparency to executive leadership and halted recurring regression escapes across core clinical product lines.
            </div>
          </div>

          {/* Card 2: CAO DevOps Reference Architecture */}
          <div className="os-governance-card">
            <div className="governance-card-top">
              <div className="governance-icon-badge" style={{ color: '#a78bfa', background: 'rgba(167, 139, 250, 0.12)', borderColor: 'rgba(167, 139, 250, 0.25)' }}>
                <Layers size={22} />
              </div>
              <span className="governance-tag" style={{ color: '#c084fc' }}>Enterprise CAO Architecture (Nov 2020)</span>
            </div>

            <h4 className="governance-card-title">Chief Architect Office: Enterprise DevOps Reference Architecture</h4>
            <div className="governance-card-scope">
              <strong>Authorship:</strong> Co-authored by Datta Vellal with Fellow Architect Herwig Wens, Principal Architect Rajesh Arasu; Reviewed by Fellow Architect Klaas Wijbrans (Philips Bangalore &amp; Eindhoven).
            </div>

            <div className="governance-key-metrics">
              <div className="gov-metric-item">
                <span className="gov-metric-num">100%</span>
                <span className="gov-metric-lbl">Standardized CI/CD Spec</span>
              </div>
              <div className="gov-metric-item">
                <span className="gov-metric-num">Multi-Cluster</span>
                <span className="gov-metric-lbl">Enterprise Deployment Scope</span>
              </div>
              <div className="gov-metric-item">
                <span className="gov-metric-num">IEC 62304</span>
                <span className="gov-metric-lbl">Traceable Build Provenance</span>
              </div>
              <div className="gov-metric-item">
                <span className="gov-metric-num">Zero</span>
                <span className="gov-metric-lbl">Environment Drift Variance</span>
              </div>
            </div>

            <div className="governance-content-block">
              <div className="gov-block-label">Default Trajectory:</div>
              <ul className="gov-bullet-list">
                <li>Disparate product engineering units maintained disconnected Jenkins and custom script toolchains, creating fragile releases and multi-week integration blockers.</li>
                <li>Lack of standardized container baselines led to environment drift and regulatory verification gaps.</li>
              </ul>
            </div>

            <div className="governance-content-block">
              <div className="gov-block-label">Architecture Decisions &amp; Intervention:</div>
              <ul className="gov-bullet-list">
                <li>Codified common pipeline architectures across enterprise clusters, establishing immutable Docker container build environments.</li>
                <li>Standardized automated static analysis, security vulnerability scanning, and binary artifact management for clinical compliance.</li>
              </ul>
            </div>

            <div className="governance-card-footer">
              <strong>Outcome:</strong> Unified disparate toolchains into a certified enterprise deployment pipeline, accelerating delivery velocity across multi-site medical systems.
            </div>
          </div>
        </div>
      </div>

      {/* University and Community Giveback Banner */}
      <div className="university-pipeline-card">
        <div className="pipeline-header">
          <div className="pipeline-title-group">
            <BookOpen size={20} className="pipeline-icon" />
            <div>
              <h3>Academic Outreach and Talent Pipeline Incubation</h3>
              <p>Continuous commitment to engineering education and community giveback across leading academic institutions.</p>
            </div>
          </div>
          <span className="pipeline-metric-badge">
            <Sparkles size={14} /> 10+ Years Active Outreach
          </span>
        </div>

        <div className="workshops-grid">
          {universityWorkshops.map((w, idx) => (
            <div key={idx} className="workshop-pill">
              <div className="workshop-institution">{w.institution}</div>
              <div className="workshop-topic">{w.topic}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
