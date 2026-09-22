import React from 'react';
import type { EvidenceCardData } from '../types';
import { ShieldCheck, TrendingUp, AlertCircle, Compass, Zap, FileText, ArrowUpRight } from 'lucide-react';

interface EvidenceCardProps {
  card: EvidenceCardData;
}

export const EvidenceCard: React.FC<EvidenceCardProps> = ({ card }) => {
  return (
    <article className="evidence-card" id={card.id}>
      <div className="card-top-row">
        <div style={{ display: 'flex', gap: '0.6rem', alignItems: 'center', flexWrap: 'wrap' }}>
          <span className="card-company-badge">
            {card.company}, {card.timeframe}
          </span>
          <span className="card-archetype-badge">
            {card.archetype}
          </span>
        </div>
        <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)', fontWeight: 500 }}>
          {card.role}
        </span>
      </div>

      <h3 className="card-title">{card.title}</h3>
      <div className="card-scope">
        <strong>Scope:</strong> {card.scope}
      </div>

      {/* Structured Problem, Decision, Action, and Result Box */}
      <div className="intervention-flow">
        <div className="flow-step">
          <div className="step-marker marker-trajectory">
            <AlertCircle size={14} />
          </div>
          <div className="flow-content">
            <h4>Problem and Baseline Risk</h4>
            <p>{card.defaultTrajectory}</p>
          </div>
        </div>

        <div className="flow-step">
          <div className="step-marker marker-decision">
            <Compass size={14} />
          </div>
          <div className="flow-content">
            <h4>Decision and Trade-Off</h4>
            <p>{card.strategicDecision}</p>
          </div>
        </div>

        <div className="flow-step">
          <div className="step-marker marker-intervention">
            <Zap size={14} />
          </div>
          <div className="flow-content">
            <h4>Action Taken</h4>
            <p>{card.intervention}</p>
          </div>
        </div>

        <div className="flow-step">
          <div className="step-marker marker-consequence">
            <TrendingUp size={14} />
          </div>
          <div className="flow-content">
            <h4>Business and Technical Result</h4>
            <p>{card.observableConsequence}</p>
          </div>
        </div>
      </div>

      {/* Quantified Metric Pills */}
      <div className="card-metrics">
        {card.metrics.map((metric, idx) => (
          <span key={idx} className="metric-pill">
            <TrendingUp size={13} /> {metric}
          </span>
        ))}
      </div>

      {/* External Reference Links (Patents / Public Documents) */}
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

      {/* Verification Footer & Tags */}
      <div className="card-footer">
        <div className="verification-anchor">
          <ShieldCheck size={15} color="var(--gold-400)" />
          {card.verificationAnchor}
        </div>
        <div className="tag-list">
          {card.competencyTags.map((tag, idx) => (
            <span key={idx} className="competency-tag">
              #{tag}
            </span>
          ))}
        </div>
      </div>
    </article>
  );
};
