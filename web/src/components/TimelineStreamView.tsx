import React from 'react';
import type { EvidenceCardData } from '../types';
import { ShieldCheck, TrendingUp, AlertCircle, Compass, Zap, Calendar, Building2, FileText, ArrowUpRight } from 'lucide-react';

interface TimelineStreamViewProps {
  evidence: EvidenceCardData[];
}

export const TimelineStreamView: React.FC<TimelineStreamViewProps> = ({ evidence }) => {
  return (
    <div className="timeline-stream-container">
      <div className="timeline-rail" />

      {evidence.map((card) => {
        const isAmazon = card.company.includes('Amazon');
        const isExeter = card.company.includes('Exeter');

        return (
          <div key={card.id} className="timeline-stream-node" id={`timeline-${card.id}`}>
            {/* Timeline Dot with Pulse */}
            <div className="timeline-node-marker">
              <div className="marker-dot" />
              <div className="marker-ring" />
            </div>

            {/* Timeline Content Block */}
            <div className="timeline-node-card">
              {/* Header Strip */}
              <div className="timeline-node-header">
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', flexWrap: 'wrap' }}>
                  <span className="timeline-era-pill">
                    <Calendar size={13} />
                    {card.timeframe}
                  </span>
                  <span className={`timeline-company-pill ${isAmazon ? 'company-amazon' : isExeter ? 'company-exeter' : 'company-philips'}`}>
                    <Building2 size={13} />
                    {card.company}
                  </span>
                  <span className="card-archetype-badge">
                    {card.archetype}
                  </span>
                </div>

                <div className="timeline-role-text">
                  {card.role}
                </div>
              </div>

              {/* Title & Scope */}
              <h3 className="timeline-node-title">{card.title}</h3>
              <div className="card-scope" style={{ marginBottom: '1.25rem' }}>
                <strong>Strategic Scope:</strong> {card.scope}
              </div>

              {/* 4-Step Systemic Intervention Flow */}
              <div className="intervention-flow">
                <div className="flow-step">
                  <div className="step-marker marker-trajectory">
                    <AlertCircle size={14} />
                  </div>
                  <div className="flow-content">
                    <h4>Problem & Baseline Risk</h4>
                    <p>{card.defaultTrajectory}</p>
                  </div>
                </div>

                <div className="flow-step">
                  <div className="step-marker marker-decision">
                    <Compass size={14} />
                  </div>
                  <div className="flow-content">
                    <h4>Strategic Decision & Trade-Off</h4>
                    <p>{card.strategicDecision}</p>
                  </div>
                </div>

                <div className="flow-step">
                  <div className="step-marker marker-intervention">
                    <Zap size={14} />
                  </div>
                  <div className="flow-content">
                    <h4>Executive Intervention</h4>
                    <p>{card.intervention}</p>
                  </div>
                </div>

                <div className="flow-step">
                  <div className="step-marker marker-consequence">
                    <TrendingUp size={14} />
                  </div>
                  <div className="flow-content">
                    <h4>Observable Consequence & Measurable Result</h4>
                    <p>{card.observableConsequence}</p>
                  </div>
                </div>
              </div>

              {/* Headline Metrics Grid */}
              <div className="card-metrics" style={{ marginTop: '1.25rem' }}>
                {card.metrics.map((metric, mIdx) => (
                  <span key={mIdx} className="metric-pill">
                    <TrendingUp size={13} /> {metric}
                  </span>
                ))}
              </div>

              {/* External Reference Links (Patents / Publications) */}
              {card.links && card.links.length > 0 && (
                <div style={{ display: 'flex', gap: '0.6rem', flexWrap: 'wrap', marginTop: '1rem', paddingTop: '0.85rem', borderTop: '1px dashed var(--border-subtle)' }}>
                  {card.links.map((link, lIdx) => (
                    <a
                      key={lIdx}
                      href={link.url}
                      target="_blank"
                      rel="noreferrer"
                      style={{
                        display: 'inline-flex',
                        alignItems: 'center',
                        gap: '0.35rem',
                        fontSize: '0.775rem',
                        fontWeight: 600,
                        color: 'var(--gold-300)',
                        background: 'rgba(245, 158, 11, 0.1)',
                        border: '1px solid var(--gold-border)',
                        padding: '0.35rem 0.65rem',
                        borderRadius: '6px',
                        textDecoration: 'none',
                        transition: 'all 0.2s ease'
                      }}
                    >
                      <FileText size={13} color="var(--gold-400)" />
                      {link.label}
                      <ArrowUpRight size={12} />
                    </a>
                  ))}
                </div>
              )}

              {/* Verification & Tags */}
              <div className="card-footer" style={{ marginTop: '1.25rem', paddingTop: '1rem' }}>
                <div className="verification-anchor">
                  <ShieldCheck size={15} color="var(--gold-400)" />
                  {card.verificationAnchor}
                </div>
                <div className="tag-list">
                  {card.competencyTags.map((tag, tIdx) => (
                    <span key={tIdx} className="competency-tag">
                      #{tag}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
};
