import React from 'react';
import { Users, Target, Shield, BookOpen, CheckCircle, GraduationCap, Sparkles } from 'lucide-react';

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
