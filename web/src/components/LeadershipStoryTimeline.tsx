import React from 'react';
import { Milestone, TrendingUp, ShieldAlert, Award, Compass } from 'lucide-react';

interface TimelineEvent {
  period: string;
  role: string;
  company: string;
  title: string;
  narrative: string;
  catalyst: string;
  permanentShift: string;
  metrics: string[];
  icon: 'scale' | 'turnaround' | 'executive' | 'global';
}

const leadershipEvents: TimelineEvent[] = [
  {
    period: '2021 to Present',
    role: 'Software Excellence Competency Lead',
    company: 'Philips North America (Rochester Hills, MI)',
    title: 'Global Scale and Medical Device Software Governance',
    narrative: 'Inherited fragmented tooling and high release latency across global diagnostic product lines. Stepped in to standardize delivery and automate compliance across 7,000+ developers.',
    catalyst: 'Rejected localized division-by-division tooling in favor of a shared enterprise Service-Ops platform and automated IEC 62304 / ISO 13485 shift-left gates.',
    permanentShift: 'Cut product release cycles by 60%, saved $300K+ in recurring infrastructure overhead, held 99.999% uptime, and earned continuous audit readiness with zero regulatory stops.',
    metrics: ['7,000+ Engineers Supported', '99.999% Uptime', '60% Faster Release Cycle', '$300K Annual Savings'],
    icon: 'global'
  },
  {
    period: '2018 to 2021',
    role: 'Software Competency Lead & Principal (Youngest in History)',
    company: 'Philips India (Bangalore)',
    title: 'Enterprise Turnaround and Culture Transformation',
    narrative: 'Faced with multi-decade legacy technical debt threatening commercial competitiveness in hospital systems, while hiring rubrics suffered from subjective calibration.',
    catalyst: 'Resisted high-risk two-year total rewrites; executed a value-driven strangler modernization tied directly to customer milestones, while overhauling engineering hiring standards.',
    permanentShift: 'Delivered $2.3M in direct verified cost reductions, closed $3.8M in platform sales, boosted candidate NPS by +18%, and was promoted as the youngest Principal in Philips India history.',
    metrics: ['$2.3M Direct Savings', '$3.8M New Contracts', '+18% Candidate NPS', 'Youngest Principal Promotion'],
    icon: 'turnaround'
  },
  {
    period: '2016 to 2018',
    role: 'Software Development Engineer',
    company: 'Amazon (Bangalore)',
    title: 'High-Throughput Distributed Architecture',
    narrative: 'High transaction volumes threatened backend service latencies and availability during peak retail events.',
    catalyst: 'Architected and benchmarked six isolated microservices with asynchronous event processing and automated failover topologies.',
    permanentShift: 'Supported 8,000,000+ daily transactions with sub-second response times, cut release cycles by 18%, and unlocked $34K in cloud efficiency.',
    metrics: ['8M+ Daily Transactions', '18% Shorter Release Time', '6 Production Microservices'],
    icon: 'scale'
  },
  {
    period: '2012 to Present',
    role: 'Keynote Speaker, Inventor & Mentor',
    company: 'Global Industry and Academia',
    title: 'Intellectual Property and Ecosystem Influence',
    narrative: 'Observed widening knowledge gaps between traditional academic engineering curricula and modern distributed cloud-native architecture.',
    catalyst: 'Personally invested hundreds of hours into curriculum design, global craftsmanship keynotes, and active mentorship.',
    permanentShift: 'Trained over 2,000 engineers across 22 institutions globally, authored two software systems inventions (1 granted US Patent US 8,560,487 B2, 1 published application US 2015/0095117 A1), and earned the Outstanding Achievement Award.',
    metrics: ['1 Granted US Patent', '1 Published Application', '2,000+ Engineers Trained', '22 Academic Institutions'],
    icon: 'executive'
  }
];

export const LeadershipStoryTimeline: React.FC = () => {
  return (
    <section id="leadership-story" className="container" style={{ marginBottom: '5rem' }}>
      <div style={{ marginBottom: '2.5rem' }}>
        <div className="hero-tag" style={{ background: 'var(--indigo-bg)', borderColor: 'rgba(99, 102, 241, 0.3)', color: 'var(--indigo-400)' }}>
          <Milestone size={14} />
          The Leadership Story
        </div>
        <h2 className="section-title">The Evolution of an Executive Systems Leader</h2>
        <p className="section-subtitle" style={{ maxWidth: '800px' }}>
          From engineering high-throughput microservices at Amazon to leading digital turnaround as Philips India's youngest Principal, and scaling global platforms for 7,000+ developers in North America.
        </p>
      </div>

      <div className="story-timeline-wrapper">
        {leadershipEvents.map((evt, idx) => (
          <div key={idx} className="story-timeline-card">
            {/* Left Accent Pillar */}
            <div className="timeline-marker-col">
              <div className="timeline-node">
                <span className="node-number">0{idx + 1}</span>
              </div>
              {idx !== leadershipEvents.length - 1 && <div className="timeline-connector" />}
            </div>

            {/* Right Card Content */}
            <div className="timeline-card-body card-spotlight">
              <div className="timeline-header-row">
                <div>
                  <span className="timeline-period-badge">{evt.period}</span>
                  <h3 className="timeline-role-title">{evt.title}</h3>
                  <div className="timeline-company-sub">
                    <strong>{evt.role}</strong> • {evt.company}
                  </div>
                </div>
              </div>

              <div className="timeline-story-grid">
                <div className="story-col">
                  <div className="story-label">
                    <ShieldAlert size={14} color="#f87171" />
                    <span>The Situation & Friction:</span>
                  </div>
                  <p>{evt.narrative}</p>
                </div>

                <div className="story-col">
                  <div className="story-label">
                    <Compass size={14} color="#818cf8" />
                    <span>The Executive Intervention:</span>
                  </div>
                  <p>{evt.catalyst}</p>
                </div>

                <div className="story-col highlight-col">
                  <div className="story-label">
                    <TrendingUp size={14} color="#34d399" />
                    <span>Permanent Consequence:</span>
                  </div>
                  <p>{evt.permanentShift}</p>
                </div>
              </div>

              {/* Metric Chips */}
              <div className="timeline-metrics-strip">
                {evt.metrics.map((m, mIdx) => (
                  <span key={mIdx} className="timeline-metric-chip">
                    <Award size={12} color="var(--gold-400)" />
                    {m}
                  </span>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};
