import { useState, useMemo, useEffect, useCallback } from 'react';
import type { PortfolioData, EvidenceCardData, LeadershipPerspective } from './types';
import portfolioRawData from './data/executive_evidence.json';
import { ExecutiveHero } from './components/ExecutiveHero';
import { BoardBriefView } from './components/BoardBriefView';
import { LeadershipOperatingSystem } from './components/LeadershipOperatingSystem';
import { EnterpriseAIGovernance } from './components/EnterpriseAIGovernance';
import { LeadershipStoryTimeline } from './components/LeadershipStoryTimeline';
import { EndorsementsWall } from './components/EndorsementsWall';
import { QueryEngine } from './components/QueryEngine';
import { EvidenceCard } from './components/EvidenceCard';
import { TimelineStreamView } from './components/TimelineStreamView';
import { DecisionExplorer } from './components/DecisionExplorer';
import { DossierModal } from './components/DossierModal';
import { Shield, Sparkles, FileText, Mail, ArrowUpRight, Compass, Briefcase, Cpu, Users } from 'lucide-react';

const portfolioData = portfolioRawData as PortfolioData;

export function App() {
  const [activePerspective, setActivePerspective] = useState<LeadershipPerspective>('boardroom');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedArchetype, setSelectedArchetype] = useState('ALL');
  const [selectedTimeline, setSelectedTimeline] = useState('ALL');
  const [viewMode, setViewMode] = useState<'grid' | 'timeline'>('grid');
  const [isDossierOpen, setIsDossierOpen] = useState(() => {
    if (typeof window !== 'undefined') {
      return window.location.hash.includes('dossier') || window.location.search.includes('dossier') || window.location.search.includes('lens');
    }
    return false;
  });

  const handleSelectPerspective = useCallback((perspective: LeadershipPerspective) => {
    setActivePerspective(perspective);
    const anchorMap: Record<LeadershipPerspective, string> = {
      boardroom: 'boardroom-brief',
      architecture: 'decisions-section',
      leadership: 'leadership-os',
      governance: 'enterprise-ai-governance',
      catalog: 'query-engine'
    };
    const targetId = anchorMap[perspective];
    if (targetId) {
      const el = document.getElementById(targetId);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  }, []);

  useEffect(() => {
    const handleUrl = () => {
      if (window.location.hash.includes('dossier') || window.location.search.includes('dossier') || window.location.search.includes('lens')) {
        setIsDossierOpen(true);
      }
    };
    handleUrl();
    window.addEventListener('hashchange', handleUrl);
    return () => window.removeEventListener('hashchange', handleUrl);
  }, []);

  // Extract distinct archetypes
  const archetypes = useMemo(() => {
    const set = new Set<string>();
    portfolioData.evidence.forEach(item => set.add(item.archetype));
    return Array.from(set);
  }, []);

  // Distinct timeline eras
  const timelineEras = useMemo(() => [
    { key: 'ALL', label: 'All Timelines', count: portfolioData.evidence.length },
    { key: '2024_PRESENT', label: '2024 to Present (AI & Containerization)', count: portfolioData.evidence.filter(e => e.timelineEra === '2024_PRESENT').length },
    { key: '2021_2024', label: '2021 to 2024 (Platform & Compliance)', count: portfolioData.evidence.filter(e => e.timelineEra === '2021_2024').length },
    { key: '2018_2021', label: '2018 to 2021 (Modernization & Org Scale)', count: portfolioData.evidence.filter(e => e.timelineEra === '2018_2021').length },
    { key: '2016_2018', label: '2016 to 2018 (Amazon Distributed Scale)', count: portfolioData.evidence.filter(e => e.timelineEra === '2016_2018').length },
    { key: '2013_2016', label: '2013 to 2016 (Exeter Healthcare Systems)', count: portfolioData.evidence.filter(e => e.timelineEra === '2013_2016').length },
    { key: 'PATENTS', label: 'Patents & Industry Standards', count: portfolioData.evidence.filter(e => e.timelineEra === 'PATENTS').length }
  ], []);

  // Filter evidence cards based on query, archetype, and timeline era
  const filteredEvidence = useMemo(() => {
    return portfolioData.evidence.filter((item: EvidenceCardData) => {
      // Timeline era match
      if (selectedTimeline !== 'ALL' && item.timelineEra !== selectedTimeline) {
        return false;
      }

      // Archetype match
      if (selectedArchetype !== 'ALL' && item.archetype !== selectedArchetype) {
        return false;
      }

      // Query match across title, intervention, consequence, tags, company, metrics
      if (!searchQuery.trim()) return true;

      const q = searchQuery.toLowerCase();
      const matchText = [
        item.title,
        item.company,
        item.scope,
        item.archetype,
        item.timeframe,
        item.defaultTrajectory,
        item.strategicDecision,
        item.intervention,
        item.observableConsequence,
        item.verificationAnchor,
        ...item.competencyTags,
        ...item.metrics
      ].join(' ').toLowerCase();

      return matchText.includes(q);
    });
  }, [searchQuery, selectedArchetype, selectedTimeline]);

  return (
    <div className="app-root">
      {/* ReactBits-Inspired Ambient Aurora Background Glow */}
      <div className="ambient-aurora">
        <div className="aurora-blob aurora-1" />
        <div className="aurora-blob aurora-2" />
        <div className="aurora-blob aurora-3" />
      </div>

      {/* Site Header */}
      <header className="site-nav">
        <div className="container nav-wrapper">
          <div className="nav-brand">
            <span className="brand-badge">DSV</span>
            <div>
              <div className="brand-title">Dattatreya S Vellal</div>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Engineering Executive & Systems Turnaround Leader</div>
            </div>
          </div>

          <div className="nav-actions">
            <button
              type="button"
              className={`btn ${activePerspective === 'boardroom' ? 'btn-gold' : 'btn-outline'}`}
              style={{ fontSize: '0.8rem', padding: '0.4rem 0.75rem' }}
              onClick={() => handleSelectPerspective('boardroom')}
            >
              <Briefcase size={13} /> 60s Brief
            </button>
            <button
              type="button"
              className={`btn ${activePerspective === 'leadership' ? 'btn-gold' : 'btn-outline'}`}
              style={{ fontSize: '0.8rem', padding: '0.4rem 0.75rem' }}
              onClick={() => handleSelectPerspective('leadership')}
            >
              <Users size={13} /> Leadership OS
            </button>
            <button
              type="button"
              className={`btn ${activePerspective === 'governance' ? 'btn-gold' : 'btn-outline'}`}
              style={{ fontSize: '0.8rem', padding: '0.4rem 0.75rem' }}
              onClick={() => handleSelectPerspective('governance')}
            >
              <Cpu size={13} /> Enterprise AI
            </button>
            <button
              type="button"
              className={`btn ${activePerspective === 'architecture' ? 'btn-gold' : 'btn-outline'}`}
              style={{ fontSize: '0.8rem', padding: '0.4rem 0.75rem' }}
              onClick={() => handleSelectPerspective('architecture')}
            >
              <Compass size={13} /> Architecture
            </button>
            <button
              type="button"
              className={`btn ${activePerspective === 'catalog' ? 'btn-gold' : 'btn-outline'}`}
              style={{ fontSize: '0.8rem', padding: '0.4rem 0.75rem' }}
              onClick={() => handleSelectPerspective('catalog')}
            >
              <FileText size={13} /> Catalog
            </button>
            <button
              type="button"
              className="btn btn-gold"
              style={{ fontSize: '0.8rem', padding: '0.4rem 0.9rem' }}
              onClick={() => setIsDossierOpen(true)}
            >
              <Sparkles size={13} /> Dossier
            </button>
          </div>
        </div>
      </header>

      {/* Main Narrative Flow */}
      <main>
        {/* Prologue: The Executive Thesis & Headline Metrics */}
        <ExecutiveHero
          profile={portfolioData.profile}
          activePerspective={activePerspective}
          onSelectPerspective={handleSelectPerspective}
          onOpenDossier={() => setIsDossierOpen(true)}
        />

        {/* Perspective 01: The 60-Second Boardroom Brief */}
        <BoardBriefView onExplorePerspective={handleSelectPerspective} />

        {/* Perspective 02: Leadership Operating System & Culture Lineage */}
        <LeadershipOperatingSystem />

        {/* Perspective 03: Enterprise AI & MedTech Regulatory Governance */}
        <EnterpriseAIGovernance />

        {/* Perspective 04: Systems Architecture & The Strategy Clash Arena */}
        <DecisionExplorer decisions={portfolioData.decisions} />

        {/* Perspective 05: 20-Year Story Arc & Endorsements Wall */}
        <LeadershipStoryTimeline />

        {portfolioData.endorsements && portfolioData.endorsements.length > 0 && (
          <EndorsementsWall endorsements={portfolioData.endorsements} />
        )}

        {/* Interactive Query Engine & Evidence Matrix */}
        <QueryEngine
          searchQuery={searchQuery}
          onSearchChange={setSearchQuery}
          selectedTimeline={selectedTimeline}
          onSelectTimeline={setSelectedTimeline}
          timelineEras={timelineEras}
          selectedArchetype={selectedArchetype}
          onSelectArchetype={setSelectedArchetype}
          archetypes={archetypes}
          viewMode={viewMode}
          onViewModeChange={setViewMode}
          totalResults={portfolioData.evidence.length}
          filteredResults={filteredEvidence.length}
        />

        {/* Evidence List */}
        <section className="container" style={{ marginBottom: '5rem' }}>
          <div className="evidence-section-header">
            <div>
              <h2 className="section-title">Verified Evidence and Systemic Impact</h2>
              <p className="section-subtitle">
                Documented outcomes and Systemic Interventions across healthcare, enterprise platform, and e-commerce scale environments.
              </p>
            </div>
            <div className="results-count">
              Showing {filteredEvidence.length} of {portfolioData.evidence.length} records
            </div>
          </div>

          {filteredEvidence.length === 0 ? (
            <div style={{ textAlign: 'center', padding: '4rem 1rem', background: 'var(--bg-card)', borderRadius: 'var(--radius-lg)' }}>
              <p style={{ color: 'var(--text-muted)', marginBottom: '1rem' }}>No evidence records match your search filters.</p>
              <button
                className="btn btn-outline"
                onClick={() => {
                  setSearchQuery('');
                  setSelectedArchetype('ALL');
                  setSelectedTimeline('ALL');
                }}
              >
                Reset Search Filters
              </button>
            </div>
          ) : viewMode === 'timeline' ? (
            <TimelineStreamView evidence={filteredEvidence} />
          ) : (
            <div className="evidence-grid">
              {filteredEvidence.map((card) => (
                <EvidenceCard key={card.id} card={card} />
              ))}
            </div>
          )}
        </section>
      </main>

      {/* Candidate Evaluation Dossier Modal */}
      <DossierModal
        isOpen={isDossierOpen}
        onClose={() => setIsDossierOpen(false)}
        data={portfolioData}
      />

      {/* Executive Footer */}
      <footer className="site-footer">
        <div className="container footer-content">
          <div>
            <div style={{ fontWeight: 700, fontSize: '1.15rem', marginBottom: '0.35rem', color: '#fff' }}>
              Dattatreya Subramanya Vellal
            </div>
            <p style={{ fontSize: '0.85rem', maxWidth: '520px', color: 'var(--text-muted)' }}>
              Software Excellence Competency Lead and Systems Architect. All published records adhere to company non-disclosure agreements and strict compliance standards.
            </p>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: '0.75rem' }}>
            <div className="compliance-seal">
              <Shield size={14} /> Zero-Raw-File Compliance Boundary Verified
            </div>
            <div style={{ display: 'flex', gap: '1rem', fontSize: '0.85rem' }}>
              <a href={`mailto:${portfolioData.profile.email}`} style={{ color: 'var(--text-secondary)', display: 'inline-flex', alignItems: 'center', gap: '0.3rem' }}>
                <Mail size={14} /> Contact Directly
              </a>
              <a href={`https://linkedin.com/in/${portfolioData.profile.linkedin}`} target="_blank" rel="noreferrer" style={{ color: 'var(--gold-400)', display: 'inline-flex', alignItems: 'center', gap: '0.3rem' }}>
                LinkedIn Profile <ArrowUpRight size={13} />
              </a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
