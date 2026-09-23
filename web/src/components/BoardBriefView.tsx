import React from 'react';
import { Award, TrendingUp, ShieldCheck, Zap, ArrowRight, Building, CheckCircle2 } from 'lucide-react';
import type { LeadershipPerspective } from '../types';

interface BoardBriefViewProps {
  onExplorePerspective: (perspective: LeadershipPerspective) => void;
}

export const BoardBriefView: React.FC<BoardBriefViewProps> = ({ onExplorePerspective }) => {
  const turnarounds = [
    {
      id: 'turnaround-sutra',
      label: 'Turnaround 01',
      title: 'Philips Enterprise Knowledge Graph and AI Traceability Platform (SUTRA)',
      timeframe: '2024 to Present',
      company: 'Philips Healthcare',
      defaultTrajectory:
        'Engineers spent 40 hours per release manually linking requirements, verification proofs, and risk items across disconnected legacy databases, delaying releases and increasing audit vulnerability.',
      strategicIntervention:
        'Architected an AI-indexed knowledge-graph schema that replaced relational database bottlenecks with automated semantic linkage. Directed cross-functional data ingestion and automated gap analysis.',
      businessImpact:
        'Reduced release validation time by 75% (from 40 hours down to 10 hours per cycle). Secured enterprise adoption across 3 global business units and received formal executive commendation from the Global VP of Design and Innovation.',
      executiveQuote: {
        author: 'Global VP of Design and Innovation',
        role: 'Executive Leadership, Design and Innovation',
        text: 'SUTRA demonstrates a meaningful step forward in how our engineering teams navigate complex systems. Datta and team built a practical, intuitive platform that solves real engineering friction.'
      },
      metrics: ['75% Validation Time Reduction', '3 Global Divisions Live', '40h to 10h per Cycle']
    },
    {
      id: 'turnaround-themis',
      label: 'Turnaround 02',
      title: 'OS-Agnostic Containerized Diagnostic Platform (Project Themis)',
      timeframe: '2024 to Present',
      company: 'Philips Diagnostic Systems',
      defaultTrajectory:
        'Coupling diagnostic software directly to host operating systems created multi-week environment configuration delays and integration drift across distributed engineering sites.',
      strategicIntervention:
        'Mandated containerized architecture across all core diagnostic services, decoupling business logic from host dependencies. Implemented uniform Docker standards and strict sprint backlog triage.',
      businessImpact:
        'Eliminated cross-site environment setup delays, enabled instant multi-environment portability, delivered milestone reviews without downtime, and maintained predictable release velocity.',
      executiveQuote: {
        author: 'Diagnostic Systems Engineering Lead',
        role: 'Precision Diagnosis Systems Engineering',
        text: 'Datta guided the team to containerize the application, making it OS-agnostic and fast to port to new environments. His structured approach kept stakeholders aligned and prevented work from stalling due to unresolved dependencies.'
      },
      metrics: ['100% OS-Agnostic Portability', 'Zero Setup Downtime', 'On-Time Milestone Execution']
    },
    {
      id: 'turnaround-exeter',
      label: 'Turnaround 03',
      title: 'High-Throughput Healthcare EDI Integration and Core Re-Architecture',
      timeframe: '2013 to 2015',
      company: 'Exeter Group / Edifecs Healthcare',
      defaultTrajectory:
        'Unbounded batch processing jobs and opaque error logging produced cascading transaction failures during high-volume healthcare plan enrollment windows.',
      strategicIntervention:
        'Re-engineered batch execution pipelines, instituted automated data validation gates, introduced centralized transaction logging, and realigned delivery schedules with client leadership.',
      businessImpact:
        'Eliminated batch transaction failures during critical open enrollment periods, unblocked high-priority customer deliverables, and secured multiple client commendations for production stability.',
      executiveQuote: {
        author: 'Client Delivery and Account Leadership',
        role: 'Enterprise Delivery Leadership',
        text: 'Datta resolved critical end-to-end integration issues under high-pressure release deadlines, creating repeatable process discipline and rebuilding partner confidence.'
      },
      metrics: ['Zero Data Loss in Open Enrollment', '100% On-Time Batch Processing', 'Multi-Client Commendations']
    }
  ];

  return (
    <section className="board-brief-section" id="boardroom-brief">
      <div className="board-brief-header">
        <div className="brief-badge">
          <Award size={16} />
          <span>Boardroom Executive Brief: 60-Second Scan</span>
        </div>
        <h2 className="board-brief-title">
          Three Signature Turnarounds. Quantifiable Capital and Velocity Impact.
        </h2>
        <p className="board-brief-subtitle">
          Curated for Chief Executive Officers, Board Members, and Executive Search Partners.
          Grounded strictly in verified data, enterprise balance sheet leverage, and active leadership interventions.
        </p>
      </div>

      {/* High-Velocity Metrics Banner */}
      <div className="boardroom-metrics-grid">
        <div className="board-metric-card">
          <div className="board-metric-number">75%</div>
          <div className="board-metric-label">Cycle Time Reduction</div>
          <div className="board-metric-desc">SUTRA cut regulatory validation from 40h to 10h per release</div>
        </div>
        <div className="board-metric-card">
          <div className="board-metric-number">138 Projects</div>
          <div className="board-metric-label">State of Craftsmanship Audit</div>
          <div className="board-metric-desc">Benchmarked engineering maturity across 80% of Philips global software organization</div>
        </div>
        <div className="board-metric-card">
          <div className="board-metric-number">CAO Author</div>
          <div className="board-metric-label">Enterprise DevOps Reference Arch</div>
          <div className="board-metric-desc">Co-authored Chief Architect Office CI/CD whitepaper with Philips Fellow Architects</div>
        </div>
        <div className="board-metric-card">
          <div className="board-metric-number">2 Patents</div>
          <div className="board-metric-label">Active US Intellectual Property</div>
          <div className="board-metric-desc">Patented systems in decision tracking (US 8,560,487) and search (US 2015/0095117)</div>
        </div>
        <div className="board-metric-card">
          <div className="board-metric-number">100+</div>
          <div className="board-metric-label">Engineers Bar-Raised</div>
          <div className="board-metric-desc">Amazon Bar Raiser hiring discipline and university talent incubation</div>
        </div>
        <div className="board-metric-card">
          <div className="board-metric-number">1,007+</div>
          <div className="board-metric-label">2026 AI Upskilled Engineers</div>
          <div className="board-metric-desc">28 masterclasses delivered across PU, Elevate, and IEN (8.77 / 10 rating)</div>
        </div>
      </div>

      {/* Signature Turnaround Deep Dives */}
      <div className="turnaround-cards-container">
        {turnarounds.map((t) => (
          <div key={t.id} className="turnaround-card">
            <div className="turnaround-header-row">
              <span className="turnaround-pill">{t.label}</span>
              <span className="turnaround-meta">
                <Building size={14} />
                {t.company} ({t.timeframe})
              </span>
            </div>

            <h3 className="turnaround-title">{t.title}</h3>

            <div className="turnaround-body-grid">
              <div className="turnaround-block default-trajectory-block">
                <div className="block-title">
                  <ShieldCheck size={14} /> Default Trajectory (Risk if Unchecked)
                </div>
                <p>{t.defaultTrajectory}</p>
              </div>

              <div className="turnaround-block strategic-intervention-block">
                <div className="block-title">
                  <Zap size={14} /> Strategic Leadership Intervention
                </div>
                <p>{t.strategicIntervention}</p>
              </div>

              <div className="turnaround-block observable-outcome-block">
                <div className="block-title">
                  <TrendingUp size={14} /> Verified Business and P&amp;L Outcome
                </div>
                <p>{t.businessImpact}</p>
              </div>
            </div>

            <div className="turnaround-footer">
              <div className="turnaround-metrics-chips">
                {t.metrics.map((m, idx) => (
                  <span key={idx} className="metric-chip">
                    <CheckCircle2 size={13} /> {m}
                  </span>
                ))}
              </div>

              <blockquote className="turnaround-quote">
                <p>&ldquo;{t.executiveQuote.text}&rdquo;</p>
                <footer>
                  <strong>{t.executiveQuote.author}</strong> - {t.executiveQuote.role}
                </footer>
              </blockquote>
            </div>
          </div>
        ))}
      </div>

      {/* Navigation Bridge to Other Lenses */}
      <div className="brief-bridge-banner">
        <div className="bridge-text">
          <h4>Looking for deeper architectural or cultural evaluation?</h4>
          <p>Examine the technical decision matrices, Amazon Bar Raiser hiring protocols, or the full evidence catalog.</p>
        </div>
        <div className="bridge-buttons">
          <button
            type="button"
            className="bridge-btn"
            onClick={() => onExplorePerspective('architecture')}
          >
            Systems Architecture Lens <ArrowRight size={14} />
          </button>
          <button
            type="button"
            className="bridge-btn"
            onClick={() => onExplorePerspective('leadership')}
          >
            Leadership OS Lens <ArrowRight size={14} />
          </button>
          <button
            type="button"
            className="bridge-btn"
            onClick={() => onExplorePerspective('governance')}
          >
            Enterprise AI Lens <ArrowRight size={14} />
          </button>
        </div>
      </div>
    </section>
  );
};
