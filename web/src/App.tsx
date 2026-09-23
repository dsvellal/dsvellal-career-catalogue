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
import { PerspectiveBanner } from './components/PerspectiveBanner';
import { Shield, Sparkles, Mail, ArrowUpRight, Compass, Briefcase, Cpu, Users, Award, Layers, ChevronRight } from 'lucide-react';

const portfolioData = portfolioRawData as PortfolioData;

export function App() {
  const [activePerspective, setActivePerspective] = useState<LeadershipPerspective>(() => {
    if (typeof window !== 'undefined') {
      const hash = window.location.hash.replace('#', '').toLowerCase();
      if (hash === 'boardroom' || hash === 'leadership' || hash === 'architecture' || hash === 'governance' || hash === 'career' || hash === 'catalog') {
        return hash;
      }
      if (hash === 'boardroom-brief') return 'boardroom';
      if (hash === 'leadership-os') return 'leadership';
      if (hash === 'decisions-section') return 'architecture';
      if (hash === 'enterprise-ai-governance') return 'governance';
      if (hash === 'query-engine') return 'catalog';
      if (hash === 'timeline-section' || hash === 'endorsements-section') return 'career';
    }
    return 'boardroom';
  });

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
    window.location.hash = perspective;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, []);

  useEffect(() => {
    const handleUrl = () => {
      if (window.location.hash.includes('dossier') || window.location.search.includes('dossier') || window.location.search.includes('lens')) {
        setIsDossierOpen(true);
      }
      const rawHash = window.location.hash.replace('#', '').toLowerCase();
      if (rawHash === 'boardroom' || rawHash === 'leadership' || rawHash === 'architecture' || rawHash === 'governance' || rawHash === 'career' || rawHash === 'catalog') {
        setActivePerspective(rawHash);
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
      {/* Site Header with Distinct Executive Perspective Navigation */}
      <header className="site-nav">
        <div className="container nav-wrapper">
          <div
            className="nav-brand"
            onClick={() => handleSelectPerspective('boardroom')}
            role="button"
            tabIndex={0}
            onKeyDown={(e) => e.key === 'Enter' && handleSelectPerspective('boardroom')}
          >
            <span className="brand-badge">DSV</span>
            <div>
              <div className="brand-title">Dattatreya S Vellal</div>
              <div className="brand-subtitle">Engineering Executive & Systems Turnaround Leader</div>
            </div>
          </div>

          <nav className="nav-actions" aria-label="Executive perspectives">
            <div className="nav-perspectives-tabs">
              <button
                type="button"
                className={`nav-tab-btn ${activePerspective === 'boardroom' ? 'active' : ''}`}
                onClick={() => handleSelectPerspective('boardroom')}
              >
                <Briefcase size={14} />
                <span>60s Brief</span>
              </button>
              <button
                type="button"
                className={`nav-tab-btn ${activePerspective === 'leadership' ? 'active' : ''}`}
                onClick={() => handleSelectPerspective('leadership')}
              >
                <Users size={14} />
                <span>Leadership OS</span>
              </button>
              <button
                type="button"
                className={`nav-tab-btn ${activePerspective === 'architecture' ? 'active' : ''}`}
                onClick={() => handleSelectPerspective('architecture')}
              >
                <Compass size={14} />
                <span>Architecture</span>
              </button>
              <button
                type="button"
                className={`nav-tab-btn ${activePerspective === 'governance' ? 'active' : ''}`}
                onClick={() => handleSelectPerspective('governance')}
              >
                <Cpu size={14} />
                <span>Enterprise AI</span>
              </button>
              <button
                type="button"
                className={`nav-tab-btn ${activePerspective === 'career' ? 'active' : ''}`}
                onClick={() => handleSelectPerspective('career')}
              >
                <Award size={14} />
                <span>Career Lineage</span>
              </button>
              <button
                type="button"
                className={`nav-tab-btn ${activePerspective === 'catalog' ? 'active' : ''}`}
                onClick={() => handleSelectPerspective('catalog')}
              >
                <Layers size={14} />
                <span>Catalog</span>
              </button>
            </div>

            <button
              type="button"
              className="btn btn-dossier-nav"
              onClick={() => setIsDossierOpen(true)}
            >
              <Sparkles size={13} />
              <span>Dossier</span>
            </button>
          </nav>
        </div>
      </header>

      {/* Main Perspective Page Layouts */}
      <main>
        {/* VIEW 01: 60-SECOND BOARDROOM BRIEF */}
        {activePerspective === 'boardroom' && (
          <div className="perspective-page-view animate-fade-in">
            <ExecutiveHero
              profile={portfolioData.profile}
              activePerspective={activePerspective}
              onSelectPerspective={handleSelectPerspective}
              onOpenDossier={() => setIsDossierOpen(true)}
            />
            <BoardBriefView onExplorePerspective={handleSelectPerspective} />

            {/* Logical Page Bridge Card */}
            <div className="container" style={{ marginBottom: '5rem' }}>
              <div className="perspective-transition-card">
                <div className="transition-info">
                  <span className="transition-tag">Next Logical Lens</span>
                  <h3 className="transition-title">Leadership Operating System & Talent Pipeline</h3>
                  <p className="transition-desc">
                    Inspect the three institutional pillars: 900+ verified masterclass evaluations, standardized architectural governance, and university talent pipeline.
                  </p>
                </div>
                <button
                  type="button"
                  className="btn btn-gold"
                  onClick={() => handleSelectPerspective('leadership')}
                >
                  Explore Leadership OS <ChevronRight size={16} />
                </button>
              </div>
            </div>
          </div>
        )}

        {/* VIEW 02: LEADERSHIP OPERATING SYSTEM */}
        {activePerspective === 'leadership' && (
          <div className="perspective-page-view animate-fade-in">
            <PerspectiveBanner
              index="02"
              title="Leadership Operating System & Engineering Culture Lineage"
              subtitle="Three institutional pillars driving sustained high performance across 100+ engineers: continuous capability uplift, standardized architectural governance, and university talent incubation."
              stats={[
                { label: 'On-Time High-Integrity Delivery', value: '100%' },
                { label: 'Verified Masterclass Evaluations', value: '900+' },
                { label: 'Net Quality & Relevance Score', value: '91%' },
                { label: 'Academic Recruits Cultivated', value: '32' }
              ]}
              onNavigate={handleSelectPerspective}
            />
            <LeadershipOperatingSystem />

            {/* Logical Page Bridge Card */}
            <div className="container" style={{ marginBottom: '5rem' }}>
              <div className="perspective-transition-card">
                <div className="transition-info">
                  <span className="transition-tag">Next Logical Lens</span>
                  <h3 className="transition-title">Systems Architecture & Strategic Decision Arena</h3>
                  <p className="transition-desc">
                    Evaluate high-stakes architectural crossroads through explicit context, trade-offs, systemic bets, and audited empirical outcomes.
                  </p>
                </div>
                <button
                  type="button"
                  className="btn btn-gold"
                  onClick={() => handleSelectPerspective('architecture')}
                >
                  Explore Systems Architecture <ChevronRight size={16} />
                </button>
              </div>
            </div>
          </div>
        )}

        {/* VIEW 03: SYSTEMS ARCHITECTURE & DECISION CLASH */}
        {activePerspective === 'architecture' && (
          <div className="perspective-page-view animate-fade-in">
            <PerspectiveBanner
              index="03"
              title="Systems Architecture & Strategic Decision Arena"
              subtitle="High-stakes technical forks evaluated through context, explicit trade-offs, systemic bets, and audited empirical outcomes across healthcare, cloud platform, and distributed scale."
              stats={[
                { label: 'Multi-Region Migration', value: 'Zero Downtime' },
                { label: 'Peak Distributed Throughput', value: '12M Ops/Sec' },
                { label: 'Platform Availability SLA', value: '99.99%' },
                { label: 'Active US Patents Granted', value: '2 Patents' }
              ]}
              onNavigate={handleSelectPerspective}
            />
            <DecisionExplorer decisions={portfolioData.decisions} />

            {/* Logical Page Bridge Card */}
            <div className="container" style={{ marginBottom: '5rem' }}>
              <div className="perspective-transition-card">
                <div className="transition-info">
                  <span className="transition-tag">Next Logical Lens</span>
                  <h3 className="transition-title">Enterprise AI & Healthcare Regulatory Governance</h3>
                  <p className="transition-desc">
                    Examine the SUTRA knowledge-graph platform, FDA pre-market alignment, and multi-tier GenAI safe harbor validation.
                  </p>
                </div>
                <button
                  type="button"
                  className="btn btn-gold"
                  onClick={() => handleSelectPerspective('governance')}
                >
                  Explore Enterprise AI <ChevronRight size={16} />
                </button>
              </div>
            </div>
          </div>
        )}

        {/* VIEW 04: ENTERPRISE AI GOVERNANCE */}
        {activePerspective === 'governance' && (
          <div className="perspective-page-view animate-fade-in">
            <PerspectiveBanner
              index="04"
              title="Enterprise AI & Healthcare Regulatory Governance"
              subtitle="Institutional AI adoption frameworks enforcing zero-hallucination boundaries, multi-tier risk classification, FDA pre-market alignment, and HIPAA data isolation."
              stats={[
                { label: 'AI Traceability Platform', value: 'SUTRA' },
                { label: 'Validation Cycle Acceleration', value: '75%' },
                { label: 'Unverified Inferences in Prod', value: 'Zero' },
                { label: 'FDA / HIPAA Compliance Boundaries', value: '100% Sealed' }
              ]}
              onNavigate={handleSelectPerspective}
            />
            <EnterpriseAIGovernance />

            {/* Logical Page Bridge Card */}
            <div className="container" style={{ marginBottom: '5rem' }}>
              <div className="perspective-transition-card">
                <div className="transition-info">
                  <span className="transition-tag">Next Logical Lens</span>
                  <h3 className="transition-title">Career Lineage & Executive Endorsements</h3>
                  <p className="transition-desc">
                    Follow a 20-year progression from Amazon distributed scale to Philips corporate turnaround, validated by VP and Director endorsements.
                  </p>
                </div>
                <button
                  type="button"
                  className="btn btn-gold"
                  onClick={() => handleSelectPerspective('career')}
                >
                  Explore Career Lineage <ChevronRight size={16} />
                </button>
              </div>
            </div>
          </div>
        )}

        {/* VIEW 05: CAREER LINEAGE & ENDORSEMENTS */}
        {activePerspective === 'career' && (
          <div className="perspective-page-view animate-fade-in">
            <PerspectiveBanner
              index="05"
              title="Career Lineage & Executive Endorsements"
              subtitle="A 20-year trajectory from distributed systems engineering at Amazon to corporate turnaround leadership, validated by Directors, Architects, and cross-functional peers."
              stats={[
                { label: 'Systems Engineering Lineage', value: '20+ Years' },
                { label: 'Global VP & Director Endorsements', value: '100% Verified' },
                { label: 'Enterprise Transformation Scope', value: 'Amazon to Philips' },
                { label: 'Audited Peer Recommendations', value: 'Unanimous' }
              ]}
              onNavigate={handleSelectPerspective}
            />
            <LeadershipStoryTimeline />
            {portfolioData.endorsements && portfolioData.endorsements.length > 0 && (
              <EndorsementsWall endorsements={portfolioData.endorsements} />
            )}

            {/* Logical Page Bridge Card */}
            <div className="container" style={{ marginBottom: '5rem' }}>
              <div className="perspective-transition-card">
                <div className="transition-info">
                  <span className="transition-tag">Next Logical Lens</span>
                  <h3 className="transition-title">Full Evidence Catalog & Systemic Impact Matrix</h3>
                  <p className="transition-desc">
                    Search and inspect all 2,200+ audited artifacts, patent filings, and engineering interventions.
                  </p>
                </div>
                <button
                  type="button"
                  className="btn btn-gold"
                  onClick={() => handleSelectPerspective('catalog')}
                >
                  Explore Evidence Catalog <ChevronRight size={16} />
                </button>
              </div>
            </div>
          </div>
        )}

        {/* VIEW 06: FULL EVIDENCE CATALOG */}
        {activePerspective === 'catalog' && (
          <div className="perspective-page-view animate-fade-in">
            <PerspectiveBanner
              index="06"
              title="Verified Evidence Catalog & Impact Matrix"
              subtitle="Comprehensive repository of 2,200+ engineering artifacts, patents, and interventions filterable by archetype, timeline era, and systemic impact."
              stats={[
                { label: 'Total Audited Artifacts', value: '2,200+' },
                { label: 'Core Technical Archetypes', value: '6 Patterns' },
                { label: 'Compliance Boundary Verification', value: '100% Redacted' },
                { label: 'Timeline Eras Covered', value: '2005 to Present' }
              ]}
              onNavigate={handleSelectPerspective}
            />

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
                    type="button"
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

            {/* Logical Page Bridge Card */}
            <div className="container" style={{ marginBottom: '5rem' }}>
              <div className="perspective-transition-card">
                <div className="transition-info">
                  <span className="transition-tag">Review Complete</span>
                  <h3 className="transition-title">Return to Boardroom Executive Brief or Export Dossier</h3>
                  <p className="transition-desc">
                    Re-examine headline metrics and signature turnarounds or generate a formatted evaluation dossier for executive search partners.
                  </p>
                </div>
                <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap' }}>
                  <button
                    type="button"
                    className="btn btn-outline"
                    onClick={() => handleSelectPerspective('boardroom')}
                  >
                    Return to 60s Brief
                  </button>
                  <button
                    type="button"
                    className="btn btn-gold"
                    onClick={() => setIsDossierOpen(true)}
                  >
                    <Sparkles size={15} /> Open Executive Dossier
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
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
