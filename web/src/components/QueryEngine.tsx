import React from 'react';
import { Search, X, Filter, Calendar, LayoutGrid, GitCommitVertical } from 'lucide-react';

interface TimelineEraOption {
  key: string;
  label: string;
  count: number;
}

interface QueryEngineProps {
  searchQuery: string;
  onSearchChange: (query: string) => void;
  selectedTimeline: string;
  onSelectTimeline: (timeline: string) => void;
  timelineEras: TimelineEraOption[];
  selectedArchetype: string;
  onSelectArchetype: (archetype: string) => void;
  archetypes: string[];
  viewMode: 'grid' | 'timeline';
  onViewModeChange: (mode: 'grid' | 'timeline') => void;
  totalResults: number;
  filteredResults: number;
}

export const QueryEngine: React.FC<QueryEngineProps> = ({
  searchQuery,
  onSearchChange,
  selectedTimeline,
  onSelectTimeline,
  timelineEras,
  selectedArchetype,
  onSelectArchetype,
  archetypes,
  viewMode,
  onViewModeChange,
  totalResults,
  filteredResults
}) => {
  return (
    <section id="query-engine" className="container">
      <div className="search-container">
        {/* Search Bar & View Mode Toggle */}
        <div style={{ display: 'flex', gap: '1rem', alignItems: 'center', flexWrap: 'wrap', marginBottom: '1.5rem' }}>
          <div className="search-bar-wrapper" style={{ flex: 1, minWidth: '280px', marginBottom: 0 }}>
            <Search className="search-icon" size={20} />
            <input
              type="text"
              className="search-input"
              placeholder="Search by keyword, company, or metric (e.g., 'DORA', 'audit', 'savings', 'Amazon', 'Philips')..."
              value={searchQuery}
              onChange={(e) => onSearchChange(e.target.value)}
            />
            {searchQuery && (
              <button
                onClick={() => onSearchChange('')}
                style={{
                  position: 'absolute',
                  right: '1.25rem',
                  top: '50%',
                  transform: 'translateY(-50%)',
                  background: 'none',
                  border: 'none',
                  color: 'var(--text-muted)',
                  cursor: 'pointer'
                }}
                aria-label="Clear search"
              >
                <X size={18} />
              </button>
            )}
          </div>

          {/* View Mode Switcher & Results Pill */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', flexWrap: 'wrap' }}>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', fontFamily: 'var(--font-mono)' }}>
              {filteredResults} / {totalResults} Records
            </span>

            <div style={{
              display: 'inline-flex',
              background: 'rgba(255, 255, 255, 0.04)',
              border: '1px solid var(--border-subtle)',
              borderRadius: 'var(--radius-md)',
              padding: '0.25rem',
              gap: '0.25rem'
            }}>
              <button
                onClick={() => onViewModeChange('grid')}
                style={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '0.4rem',
                  background: viewMode === 'grid' ? 'var(--gold-400)' : 'transparent',
                  color: viewMode === 'grid' ? '#000' : 'var(--text-secondary)',
                  border: 'none',
                  borderRadius: 'var(--radius-sm)',
                  padding: '0.45rem 0.85rem',
                  fontSize: '0.8rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                  transition: 'all 0.2s ease'
                }}
                aria-label="Executive Grid View"
              >
                <LayoutGrid size={14} />
                Grid View
              </button>
              <button
                onClick={() => onViewModeChange('timeline')}
                style={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '0.4rem',
                  background: viewMode === 'timeline' ? 'var(--gold-400)' : 'transparent',
                  color: viewMode === 'timeline' ? '#000' : 'var(--text-secondary)',
                  border: 'none',
                  borderRadius: 'var(--radius-sm)',
                  padding: '0.45rem 0.85rem',
                  fontSize: '0.8rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                  transition: 'all 0.2s ease'
                }}
                aria-label="Chronological Timeline View"
              >
                <GitCommitVertical size={14} />
                Timeline Stream
              </button>
            </div>
          </div>
        </div>

        {/* Timeline Eras Filter Strip */}
        <div style={{ marginBottom: '1.25rem' }}>
          <div className="filter-pills-label" style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', marginBottom: '0.5rem' }}>
            <Calendar size={13} color="var(--gold-400)" />
            Filter by Career Timeline:
          </div>
          <div className="filter-pills" style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem' }}>
            {timelineEras.map((era) => {
              const isActive = selectedTimeline === era.key;
              return (
                <button
                  key={era.key}
                  className={`pill-btn ${isActive ? 'active' : ''}`}
                  onClick={() => onSelectTimeline(era.key)}
                  style={{
                    fontSize: '0.8rem',
                    padding: '0.35rem 0.75rem',
                    border: isActive ? '1px solid var(--gold-400)' : '1px solid var(--border-subtle)',
                    background: isActive ? 'var(--gold-400)' : 'rgba(255, 255, 255, 0.03)',
                    color: isActive ? '#000' : 'var(--text-secondary)'
                  }}
                >
                  {era.label}
                  <span style={{
                    marginLeft: '0.35rem',
                    fontSize: '0.7rem',
                    opacity: 0.85,
                    fontWeight: 700
                  }}>
                    ({era.count})
                  </span>
                </button>
              );
            })}
          </div>
        </div>

        {/* Archetype / Focus Area Pills */}
        <div>
          <div className="filter-pills-label" style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', marginBottom: '0.5rem' }}>
            <Filter size={13} />
            Filter by Executive Archetype:
          </div>
          <div className="filter-pills">
            <button
              className={`pill-btn ${selectedArchetype === 'ALL' ? 'active' : ''}`}
              onClick={() => onSelectArchetype('ALL')}
            >
              All Outcomes ({totalResults})
            </button>
            {archetypes.map((arch) => (
              <button
                key={arch}
                className={`pill-btn ${selectedArchetype === arch ? 'active' : ''}`}
                onClick={() => onSelectArchetype(arch)}
              >
                {arch}
              </button>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};
