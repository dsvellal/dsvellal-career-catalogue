import React from 'react';
import type { ExecutiveProfile } from '../types';
import { Award, ShieldCheck, FileText, Sparkles, MapPin, Mail, Globe, ArrowUpRight } from 'lucide-react';

interface ExecutiveHeroProps {
  profile: ExecutiveProfile;
  onOpenDossier: () => void;
}

export const ExecutiveHero: React.FC<ExecutiveHeroProps> = ({ profile, onOpenDossier }) => {
  return (
    <section className="hero-section">
      <div className="container">
        <div className="hero-tag">
          <ShieldCheck size={16} />
          Verified Executive Track Record
        </div>

        <h1 className="hero-title">
          Engineering Leadership with <span className="highlight">Measurable Business Impact</span>.
        </h1>

        <p className="hero-subtitle">
          {profile.summary}
        </p>

        {/* Quick Contact & Social Ribbon */}
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '1.25rem', marginBottom: '2.5rem', color: 'var(--text-muted)', fontSize: '0.9rem' }}>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '0.4rem' }}>
            <MapPin size={15} color="var(--gold-400)" /> {profile.location}
          </span>
          <a href={`mailto:${profile.email}`} style={{ display: 'inline-flex', alignItems: 'center', gap: '0.4rem', color: 'var(--text-secondary)' }}>
            <Mail size={15} color="var(--gold-400)" /> {profile.email}
          </a>
          <a href={`https://${profile.website}`} target="_blank" rel="noreferrer" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.4rem', color: 'var(--text-secondary)' }}>
            <Globe size={15} color="var(--gold-400)" /> {profile.website}
          </a>
          <a href={`https://linkedin.com/in/${profile.linkedin}`} target="_blank" rel="noreferrer" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.4rem', color: 'var(--text-secondary)' }}>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
              <rect x="2" y="9" width="4" height="12"></rect>
              <circle cx="4" cy="4" r="2"></circle>
            </svg>
            linkedin.com/in/{profile.linkedin}
          </a>
        </div>

        {/* Metrics Grid */}
        <div className="metrics-grid">
          {profile.headlineMetrics.map((metric, idx) => (
            <div key={idx} className="metric-card">
              <div className="metric-value">{metric.value}</div>
              <div className="metric-label">{metric.label}</div>
              <div className="metric-detail">{metric.detail}</div>
              {metric.links && metric.links.length > 0 && (
                <div style={{ display: 'flex', gap: '0.4rem', marginTop: '0.65rem', flexWrap: 'wrap' }}>
                  {metric.links.map((link, lIdx) => (
                    <a
                      key={lIdx}
                      href={link.url}
                      target="_blank"
                      rel="noreferrer"
                      style={{
                        display: 'inline-flex',
                        alignItems: 'center',
                        gap: '0.25rem',
                        fontSize: '0.72rem',
                        fontWeight: 600,
                        color: 'var(--gold-300)',
                        background: 'rgba(245, 158, 11, 0.12)',
                        border: '1px solid var(--gold-border)',
                        padding: '0.2rem 0.5rem',
                        borderRadius: '4px',
                        textDecoration: 'none',
                        transition: 'all 0.2s ease'
                      }}
                      title={`${link.label} (${link.type})`}
                    >
                      {link.label} <ArrowUpRight size={11} />
                    </a>
                  ))}
                </div>
              )}
            </div>
          ))}
        </div>

        {/* Primary CTAs */}
        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap', alignItems: 'center' }}>
          <button className="btn btn-gold" onClick={onOpenDossier}>
            <Sparkles size={16} />
            Generate Executive Dossier
          </button>
          <a href="#endorsements-section" className="btn btn-outline">
            <ShieldCheck size={16} />
            Executive Endorsements
          </a>
          <a href="#query-engine" className="btn btn-outline">
            <FileText size={16} />
            Search Evidence Database
          </a>
          <a href="#decisions-section" className="btn btn-outline">
            <Award size={16} />
            Key Strategic Decisions
          </a>
        </div>
      </div>
    </section>
  );
};
