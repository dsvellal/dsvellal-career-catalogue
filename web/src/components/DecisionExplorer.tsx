import React, { useState, useMemo } from 'react';
import type { DecisionCaseStudy } from '../types';
import {
  Compass,
  Calendar,
  Building2,
  Tag,
  TrendingUp,
  Search,
  CheckCircle2,
  AlertCircle,
  GitCommit,
  LayoutGrid,
  Layers,
  ShieldAlert,
  Zap,
  Scale,
  Sparkles
} from 'lucide-react';

interface DecisionExplorerProps {
  decisions: DecisionCaseStudy[];
}

type EraKey = 'ALL' | 'PHILIPS_US' | 'PHILIPS_INDIA' | 'AMAZON' | 'EXETER' | 'IBM';

interface EraOption {
  key: EraKey;
  label: string;
  count: number;
}

export const DecisionExplorer: React.FC<DecisionExplorerProps> = ({ decisions }) => {
  const [selectedEra, setSelectedEra] = useState<EraKey>('ALL');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [viewMode, setViewMode] = useState<'timeline' | 'grid'>('timeline');

  // Quick Filter Suggestion Chips
  const quickFilters = [
    { label: 'SUTRA (Graph)', query: 'SUTRA' },
    { label: 'Docker (Themis)', query: 'Docker' },
    { label: 'IEC 62304 Compliance', query: '62304' },
    { label: 'Strangler ($6.1M)', query: 'Strangler' },
    { label: 'AmazonPay Scale', query: 'AmazonPay' },
    { label: 'JVM FinOps', query: 'JVM' },
    { label: 'US Patent Telemetry', query: 'Patent' },
  ];

  // Compute Era Counts dynamically
  const eraOptions: EraOption[] = useMemo(() => {
    return [
      { key: 'ALL', label: 'All Eras', count: decisions.length },
      { key: 'PHILIPS_US', label: 'Philips NA (2021-Present)', count: decisions.filter(d => d.timelineEra === 'PHILIPS_US').length },
      { key: 'PHILIPS_INDIA', label: 'Philips India (2018-2021)', count: decisions.filter(d => d.timelineEra === 'PHILIPS_INDIA').length },
      { key: 'AMAZON', label: 'Amazon (2016-2018)', count: decisions.filter(d => d.timelineEra === 'AMAZON').length },
      { key: 'EXETER', label: 'Exeter / ACA (2013-2015)', count: decisions.filter(d => d.timelineEra === 'EXETER').length },
      { key: 'IBM', label: 'IBM Labs (2007-2013)', count: decisions.filter(d => d.timelineEra === 'IBM').length }
    ];
  }, [decisions]);

  // Filter decisions based on Era and Search Query
  const filteredDecisions = useMemo(() => {
    return decisions.filter((d) => {
      const matchesEra = selectedEra === 'ALL' || d.timelineEra === selectedEra;
      if (!matchesEra) return false;

      if (!searchQuery.trim()) return true;

      const q = searchQuery.toLowerCase();
      return (
        d.title.toLowerCase().includes(q) ||
        d.domain.toLowerCase().includes(q) ||
        d.context.toLowerCase().includes(q) ||
        d.tradeOff.toLowerCase().includes(q) ||
        d.theBet.toLowerCase().includes(q) ||
        d.outcome.toLowerCase().includes(q) ||
        d.company.toLowerCase().includes(q) ||
        (d.impactMetric && d.impactMetric.toLowerCase().includes(q))
      );
    });
  }, [decisions, selectedEra, searchQuery]);

  // Helper for company pill style
  const getCompanyClass = (company: string) => {
    if (company.includes('Amazon')) return 'company-amazon';
    if (company.includes('Exeter')) return 'company-exeter';
    if (company.includes('IBM')) return 'company-ibm';
    return 'company-philips';
  };

  return (
    <section id="decisions-section" className="decisions-section">
      <div className="container">
        {/* Section Header */}
        <div style={{ marginBottom: '2.5rem' }}>
          <div className="hero-tag" style={{ background: 'var(--indigo-bg)', borderColor: 'rgba(99, 102, 241, 0.3)', color: 'var(--indigo-400)' }}>
            <Compass size={15} />
            Execution Under Uncertainty
          </div>
          <h2 className="section-title">Strategic Decisions and System Trade-Offs</h2>
          <p className="section-subtitle" style={{ maxWidth: '820px', color: 'var(--text-secondary)' }}>
            High-stakes engineering leadership requires navigating architectural crossroads where every path carries inherent risk. Each case study deconstructs the conventional trap, the calculated strategic intervention, and the permanent business consequence.
          </p>
        </div>

        {/* Interactive Controls Bar */}
        <div className="decisions-controls-bar">
          {/* Search Box */}
          <div className="decisions-search-wrapper">
            <Search size={16} className="search-icon" />
            <input
              type="text"
              className="decisions-search-input"
              placeholder="Search trade-offs, technologies, or keywords (e.g., SUTRA, Docker, JVM, Strangler)..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
            {searchQuery && (
              <button
                type="button"
                className="search-clear-btn"
                onClick={() => setSearchQuery('')}
                aria-label="Clear search"
              >
                ✕
              </button>
            )}
          </div>

          {/* View Mode Switcher */}
          <div className="view-mode-switcher">
            <button
              type="button"
              className={`view-mode-btn ${viewMode === 'timeline' ? 'active' : ''}`}
              onClick={() => setViewMode('timeline')}
            >
              <GitCommit size={15} />
              Chronological Stream
            </button>
            <button
              type="button"
              className={`view-mode-btn ${viewMode === 'grid' ? 'active' : ''}`}
              onClick={() => setViewMode('grid')}
            >
              <LayoutGrid size={15} />
              Strategic Matrix
            </button>
          </div>
        </div>

        {/* Era Filter Pills */}
        <div className="decisions-era-filters">
          {eraOptions.map((opt) => (
            <button
              key={opt.key}
              type="button"
              className={`decisions-era-pill ${selectedEra === opt.key ? 'active' : ''}`}
              onClick={() => setSelectedEra(opt.key)}
            >
              <span>{opt.label}</span>
              <span className="era-count">{opt.count}</span>
            </button>
          ))}
        </div>

        {/* Quick Suggestion Chips */}
        <div className="quick-tags-strip">
          <span className="quick-tags-label">
            <Sparkles size={12} color="var(--gold-400)" />
            Quick Inspect:
          </span>
          {quickFilters.map((qf, idx) => (
            <button
              key={idx}
              type="button"
              className={`quick-tag-chip ${searchQuery === qf.query ? 'active' : ''}`}
              onClick={() => {
                if (searchQuery === qf.query) {
                  setSearchQuery('');
                } else {
                  setSearchQuery(qf.query);
                  setSelectedEra('ALL');
                }
              }}
            >
              {qf.label}
            </button>
          ))}
        </div>

        {/* Results Counter Strip */}
        <div className="decisions-meta-strip">
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--text-muted)', fontSize: '0.875rem' }}>
            <Layers size={14} color="var(--gold-400)" />
            <span>Showing <strong>{filteredDecisions.length}</strong> of {decisions.length} verified system trade-offs</span>
            {selectedEra !== 'ALL' && <span style={{ color: 'var(--indigo-400)' }}>• Filtered by era</span>}
            {searchQuery && <span style={{ color: 'var(--gold-400)' }}>• Matching "{searchQuery}"</span>}
          </div>
        </div>

        {/* Empty State */}
        {filteredDecisions.length === 0 && (
          <div className="decisions-empty-state">
            <ShieldAlert size={40} color="var(--gold-400)" style={{ margin: '0 auto 1rem' }} />
            <h4>No strategic decisions matched your query</h4>
            <p>Try searching for broader terms like "cloud", "Amazon", "compliance", "scale", or "traceability".</p>
            <button
              type="button"
              className="btn btn-outline"
              style={{ marginTop: '1rem' }}
              onClick={() => {
                setSelectedEra('ALL');
                setSearchQuery('');
              }}
            >
              Reset Filters
            </button>
          </div>
        )}

        {/* TIMELINE STREAM VIEW */}
        {viewMode === 'timeline' && filteredDecisions.length > 0 && (
          <div className="decisions-timeline-container">
            <div className="decisions-timeline-rail" />

            {filteredDecisions.map((item) => (
              <div key={item.id} className="decisions-timeline-node" id={`decision-${item.id}`}>
                {/* Glowing Timeline Marker */}
                <div className="decisions-node-marker">
                  <div className="decisions-marker-dot" />
                  <div className="decisions-marker-ring" />
                </div>

                {/* Timeline Card */}
                <div className="decision-theatrical-card">
                  {/* Top Bar Header */}
                  <div className="decision-theatrical-header">
                    <div className="decision-header-badges">
                      <span className="decision-year-pill">
                        <Calendar size={13} />
                        {item.year}
                      </span>
                      <span className={`decision-company-pill ${getCompanyClass(item.company)}`}>
                        <Building2 size={13} />
                        {item.company}
                      </span>
                      <span className="decision-domain-pill">
                        <Tag size={12} />
                        {item.domain}
                      </span>
                    </div>

                    {item.impactMetric && (
                      <div className="decision-glow-metric">
                        <TrendingUp size={14} />
                        <span>{item.impactMetric}</span>
                      </div>
                    )}
                  </div>

                  {/* High-Impact Title */}
                  <h3 className="decision-theatrical-title">{item.title}</h3>

                  {/* Stage 1: The Context & Inherent Friction Banner */}
                  <div className="theatrical-context-banner">
                    <div className="context-indicator">
                      <AlertCircle size={15} />
                      <span>THE SYSTEMIC FRICTION & BASELINE STAKES</span>
                    </div>
                    <p>{item.context}</p>
                  </div>

                  {/* Stage 2: The Architectural Clash Arena (VS Trade-Off) */}
                  <div className="tradeoff-arena">
                    {/* Left Wing: The Conventional Option / Status Quo */}
                    <div className="tradeoff-branch branch-conventional">
                      <div className="branch-header">
                        <div className="branch-icon-wrap icon-amber">
                          <Scale size={15} />
                        </div>
                        <div>
                          <div className="branch-eyebrow">OPTION A: THE CONVENTIONAL PATH</div>
                          <div className="branch-title">The Dilemma & High-Risk Trap</div>
                        </div>
                      </div>
                      <div className="branch-body">
                        <p>{item.tradeOff}</p>
                      </div>
                    </div>

                    {/* Central Nexus Divider: The VS Clash */}
                    <div className="tradeoff-nexus">
                      <div className="nexus-line" />
                      <div className="nexus-badge">
                        <span>VS</span>
                      </div>
                      <div className="nexus-line" />
                    </div>

                    {/* Right Wing: The Strategic Bet / Datta's Leverage Point */}
                    <div className="tradeoff-branch branch-strategic">
                      <div className="branch-header">
                        <div className="branch-icon-wrap icon-indigo">
                          <Zap size={15} />
                        </div>
                        <div>
                          <div className="branch-eyebrow">OPTION B: STRATEGIC INTERVENTION</div>
                          <div className="branch-title">The Calculated Bet & Architecture Choice</div>
                        </div>
                      </div>
                      <div className="branch-body">
                        <p>{item.theBet}</p>
                      </div>
                    </div>
                  </div>

                  {/* Stage 3: The Observable Consequence Ribbon */}
                  <div className="theatrical-outcome-ribbon">
                    <div className="outcome-icon-circle">
                      <CheckCircle2 size={18} color="#34d399" />
                    </div>
                    <div className="outcome-content">
                      <div className="outcome-eyebrow">VERIFIED SYSTEMIC OUTCOME & PERMANENT ROI</div>
                      <p>{item.outcome}</p>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* MATRIX GRID VIEW */}
        {viewMode === 'grid' && filteredDecisions.length > 0 && (
          <div className="decisions-matrix-grid">
            {filteredDecisions.map((item) => (
              <div key={item.id} className="decision-theatrical-card grid-card">
                {/* Header */}
                <div className="decision-theatrical-header" style={{ marginBottom: '1rem' }}>
                  <div className="decision-header-badges">
                    <span className="decision-year-pill">
                      <Calendar size={13} />
                      {item.year}
                    </span>
                    <span className={`decision-company-pill ${getCompanyClass(item.company)}`}>
                      <Building2 size={13} />
                      {item.company}
                    </span>
                  </div>

                  {item.impactMetric && (
                    <div className="decision-glow-metric">
                      <TrendingUp size={13} />
                      <span>{item.impactMetric}</span>
                    </div>
                  )}
                </div>

                <div style={{ marginBottom: '0.65rem' }}>
                  <span className="decision-domain-pill">
                    <Tag size={12} />
                    {item.domain}
                  </span>
                </div>

                <h3 className="decision-theatrical-title" style={{ fontSize: '1.2rem', marginBottom: '1.25rem' }}>
                  {item.title}
                </h3>

                {/* Context */}
                <div className="theatrical-context-banner" style={{ padding: '0.9rem 1.1rem', marginBottom: '1rem' }}>
                  <div className="context-indicator" style={{ fontSize: '0.72rem' }}>
                    <AlertCircle size={13} />
                    <span>SYSTEMIC FRICTION</span>
                  </div>
                  <p style={{ fontSize: '0.85rem' }}>{item.context}</p>
                </div>

                {/* Vertical Trade-Off Clash */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', marginBottom: '1rem' }}>
                  <div className="tradeoff-branch branch-conventional" style={{ padding: '1rem' }}>
                    <div className="branch-header" style={{ marginBottom: '0.4rem' }}>
                      <Scale size={14} color="#fbbf24" />
                      <div className="branch-eyebrow" style={{ color: '#fbbf24' }}>THE DILEMMA</div>
                    </div>
                    <p style={{ fontSize: '0.85rem', margin: 0 }}>{item.tradeOff}</p>
                  </div>

                  <div className="tradeoff-branch branch-strategic" style={{ padding: '1rem' }}>
                    <div className="branch-header" style={{ marginBottom: '0.4rem' }}>
                      <Zap size={14} color="#818cf8" />
                      <div className="branch-eyebrow" style={{ color: '#818cf8' }}>THE STRATEGIC BET</div>
                    </div>
                    <p style={{ fontSize: '0.85rem', margin: 0 }}>{item.theBet}</p>
                  </div>
                </div>

                {/* Outcome */}
                <div className="theatrical-outcome-ribbon" style={{ padding: '0.85rem 1rem' }}>
                  <CheckCircle2 size={16} color="#34d399" style={{ flexShrink: 0, marginTop: '2px' }} />
                  <div className="outcome-content">
                    <div className="outcome-eyebrow" style={{ fontSize: '0.7rem' }}>OUTCOME</div>
                    <p style={{ fontSize: '0.85rem', margin: 0 }}>{item.outcome}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </section>
  );
};
