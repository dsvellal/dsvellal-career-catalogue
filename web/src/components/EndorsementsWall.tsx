import React, { useState, useMemo } from 'react';
import type { Endorsement } from '../types';
import { Quote, ShieldCheck, UserCheck, Calendar, Building2, Sparkles } from 'lucide-react';

interface EndorsementsWallProps {
  endorsements: Endorsement[];
}

export const EndorsementsWall: React.FC<EndorsementsWallProps> = ({ endorsements }) => {
  const [selectedYear, setSelectedYear] = useState<string>('ALL');

  // Distinct eras in chronological descending order
  const eras = [
    { key: 'ALL', label: 'All Eras', count: endorsements.length },
    { key: '2026', label: '2026 (SUTRA & Traceability)', count: endorsements.filter(e => e.year === '2026').length },
    { key: '2025', label: '2025 (Healthcare Compliance & AI)', count: endorsements.filter(e => e.year === '2025').length },
    { key: '2024', label: '2024 (Architecture & Modernization)', count: endorsements.filter(e => e.year === '2024').length },
    { key: '2023', label: '2023 (CI/CD & Hiring Bar)', count: endorsements.filter(e => e.year === '2023').length },
    { key: '2022', label: '2022 (Test ODC & Mentorship)', count: endorsements.filter(e => e.year === '2022').length },
    { key: '2020-2021', label: '2020-2021 (Quality @ Desk & MR)', count: endorsements.filter(e => e.year === '2020-2021').length },
    { key: '2016-2018', label: '2016-2018 (Amazon Scale)', count: endorsements.filter(e => e.year === '2016-2018').length },
  ];

  const filteredEndorsements = useMemo(() => {
    if (selectedYear === 'ALL') return endorsements;
    return endorsements.filter(e => e.year === selectedYear);
  }, [endorsements, selectedYear]);

  return (
    <section id="endorsements-section" className="container" style={{ marginBottom: '5rem' }}>
      {/* Section Header */}
      <div style={{ marginBottom: '2.5rem' }}>
        <div className="hero-tag" style={{ background: 'var(--gold-bg)', borderColor: 'var(--gold-border)', color: 'var(--gold-300)' }}>
          <UserCheck size={14} />
          A Decade of Verified Leadership Recognition (2016 - 2026)
        </div>
        <h2 className="section-title">Verified Executive & Stakeholder Endorsements</h2>
        <p className="section-subtitle" style={{ maxWidth: '820px' }}>
          Documented recognition across 10 years of engineering leadership: feedback from Vice Presidents, Directors, Principal Architects, and Engineering Managers across Philips and Amazon.
        </p>

        {/* Verification Strip Summary */}
        <div style={{
          display: 'flex',
          flexWrap: 'wrap',
          gap: '1rem',
          marginTop: '1.25rem'
        }}>
          <div style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '0.45rem',
            background: 'rgba(255, 255, 255, 0.03)',
            border: '1px solid var(--border-subtle)',
            borderRadius: '9999px',
            padding: '0.4rem 0.9rem',
            fontSize: '0.8rem',
            color: 'var(--text-secondary)'
          }}>
            <Sparkles size={13} color="var(--gold-400)" />
            <strong style={{ color: '#fff' }}>25 Verified Testimonials</strong> Across 7 Distinct Eras
          </div>
          <div style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '0.45rem',
            background: 'rgba(255, 255, 255, 0.03)',
            border: '1px solid var(--border-subtle)',
            borderRadius: '9999px',
            padding: '0.4rem 0.9rem',
            fontSize: '0.8rem',
            color: 'var(--text-secondary)'
          }}>
            <Building2 size={13} color="var(--emerald-400)" />
            Philips Global Development & Amazon TRMS/Payments
          </div>
          <div style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '0.45rem',
            background: 'rgba(255, 255, 255, 0.03)',
            border: '1px solid var(--border-subtle)',
            borderRadius: '9999px',
            padding: '0.4rem 0.9rem',
            fontSize: '0.8rem',
            color: 'var(--text-secondary)'
          }}>
            <ShieldCheck size={13} color="#38bdf8" />
            100% Traceable to Corporate WorkDay & Annual Review Records
          </div>
        </div>
      </div>

      {/* Yearly Filter Tabs */}
      <div style={{
        display: 'flex',
        flexWrap: 'wrap',
        gap: '0.6rem',
        marginBottom: '2rem',
        borderBottom: '1px solid var(--border-subtle)',
        paddingBottom: '1.25rem'
      }}>
        {eras.map(era => {
          const isActive = selectedYear === era.key;
          return (
            <button
              key={era.key}
              onClick={() => setSelectedYear(era.key)}
              style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: '0.45rem',
                background: isActive ? 'linear-gradient(135deg, rgba(217, 119, 6, 0.25), rgba(245, 158, 11, 0.15))' : 'rgba(255, 255, 255, 0.03)',
                color: isActive ? '#fef3c7' : 'var(--text-secondary)',
                border: isActive ? '1px solid var(--gold-400)' : '1px solid var(--border-subtle)',
                borderRadius: 'var(--radius-md)',
                padding: '0.45rem 0.9rem',
                fontSize: '0.825rem',
                fontWeight: isActive ? 600 : 500,
                cursor: 'pointer',
                transition: 'all 0.2s cubic-bezier(0.16, 1, 0.3, 1)'
              }}
            >
              <Calendar size={13} style={{ opacity: isActive ? 1 : 0.6 }} />
              {era.label}
              <span style={{
                background: isActive ? 'var(--gold-400)' : 'rgba(255, 255, 255, 0.08)',
                color: isActive ? '#000' : 'var(--text-muted)',
                fontSize: '0.7rem',
                fontWeight: 700,
                padding: '0.1rem 0.4rem',
                borderRadius: '9999px',
                marginLeft: '0.2rem'
              }}>
                {era.count}
              </span>
            </button>
          );
        })}
      </div>

      {/* Endorsements Grid */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(340px, 1fr))',
        gap: '1.5rem'
      }}>
        {filteredEndorsements.map((item) => {
          const isAmazon = item.company === 'Amazon';
          return (
            <div
              key={item.id}
              style={{
                background: 'var(--bg-card)',
                border: '1px solid var(--border-subtle)',
                borderRadius: 'var(--radius-lg)',
                padding: '1.75rem',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                position: 'relative',
                backdropFilter: 'blur(12px)',
                transition: 'all 0.25s cubic-bezier(0.16, 1, 0.3, 1)',
                boxShadow: '0 4px 20px rgba(0, 0, 0, 0.2)'
              }}
            >
              <div>
                {/* Meta Header */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.1rem', flexWrap: 'wrap', gap: '0.5rem' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <Quote size={22} color="var(--gold-400)" style={{ opacity: 0.8 }} />
                    <span style={{
                      fontSize: '0.75rem',
                      fontFamily: 'var(--font-mono)',
                      fontWeight: 700,
                      color: isAmazon ? '#fdba74' : 'var(--gold-300)',
                      background: isAmazon ? 'rgba(234, 88, 12, 0.15)' : 'var(--gold-bg)',
                      border: isAmazon ? '1px solid rgba(234, 88, 12, 0.3)' : '1px solid var(--gold-border)',
                      padding: '0.15rem 0.5rem',
                      borderRadius: '4px'
                    }}>
                      {item.year || 'Leadership'}
                    </span>
                    <span style={{
                      fontSize: '0.72rem',
                      fontFamily: 'var(--font-mono)',
                      color: isAmazon ? '#fed7aa' : '#93c5fd',
                      background: isAmazon ? 'rgba(234, 88, 12, 0.1)' : 'rgba(59, 130, 246, 0.1)',
                      border: isAmazon ? '1px solid rgba(234, 88, 12, 0.25)' : '1px solid rgba(59, 130, 246, 0.25)',
                      padding: '0.15rem 0.45rem',
                      borderRadius: '4px'
                    }}>
                      {item.company || 'Corporate'}
                    </span>
                  </div>

                  <span style={{
                    fontSize: '0.75rem',
                    color: 'var(--text-muted)',
                    background: 'rgba(255, 255, 255, 0.04)',
                    padding: '0.2rem 0.5rem',
                    borderRadius: '4px',
                    border: '1px solid var(--border-subtle)',
                    maxWidth: '180px',
                    whiteSpace: 'nowrap',
                    overflow: 'hidden',
                    textOverflow: 'ellipsis'
                  }}>
                    {item.initiative}
                  </span>
                </div>

                {/* Quote Body */}
                <p style={{
                  color: '#e2e8f0',
                  fontSize: '0.925rem',
                  lineHeight: 1.65,
                  fontStyle: 'italic',
                  marginBottom: '1.5rem'
                }}>
                  "{item.quote}"
                </p>
              </div>

              {/* Attribution Footer */}
              <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: '1rem', marginTop: 'auto' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', flexWrap: 'wrap', gap: '0.5rem' }}>
                  <div>
                    <div style={{ fontWeight: 700, color: '#fff', fontSize: '0.95rem' }}>
                      {item.author}
                    </div>
                    <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
                      {item.role}
                    </div>
                  </div>
                  <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.3rem', fontSize: '0.725rem', color: 'var(--text-muted)' }}>
                    <ShieldCheck size={13} color="var(--emerald-400)" />
                    {item.context}
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
};
