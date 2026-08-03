import { useState } from 'react'
import { ConstellationView } from './Constellation'
import { CareerArcView } from './CareerArc'
import { HeroView } from './Hero'
import { ImpactWallView } from './ImpactWall'
import { TimelineView } from './Timeline'
import { VoicesView } from './Voices'
import { TalksGivebacksView } from './TalksGivebacks'
import { KnowledgeGraphView } from './KnowledgeGraph'

export type Tab = 'hero' | 'constellation' | 'arc' | 'impact' | 'timeline' | 'voices' | 'talks' | 'graph'

export default function App() {
  const [tab, setTab] = useState<Tab>('hero')

  return (
    <div className="app">
      <nav className="nav">
        <span className="nav-brand">
          <img src="/logo.jpg" alt="दत्ta011ya" className="nav-logo" />
        </span>
        <div className="nav-tabs">
          <button className={`nav-tab ${tab === 'hero' ? 'active' : ''}`} onClick={() => setTab('hero')}>
            Overview
          </button>
          <button className={`nav-tab ${tab === 'constellation' ? 'active' : ''}`} onClick={() => setTab('constellation')}>
            Professional Identity
          </button>
          <button className={`nav-tab ${tab === 'arc' ? 'active' : ''}`} onClick={() => setTab('arc')}>
            Career Arc
          </button>
          <button className={`nav-tab ${tab === 'impact' ? 'active' : ''}`} onClick={() => setTab('impact')}>
            Impact
          </button>
          <button className={`nav-tab ${tab === 'timeline' ? 'active' : ''}`} onClick={() => setTab('timeline')}>
            Timeline
          </button>
          <button className={`nav-tab ${tab === 'voices' ? 'active' : ''}`} onClick={() => setTab('voices')}>
            Voices
          </button>
          <button className={`nav-tab ${tab === 'talks' ? 'active' : ''}`} onClick={() => setTab('talks')}>
            Talks &amp; Givebacks
          </button>
          <button className={`nav-tab ${tab === 'graph' ? 'active' : ''}`} onClick={() => setTab('graph')}>
            Knowledge Graph
          </button>
        </div>
        <div className="nav-right">
          <span className="nav-right-tagline">Digital Transformation Leader · Medical Device Software</span>
        </div>
      </nav>

      <div className="view">
        {tab === 'hero' && <HeroView onNavigate={setTab} />}
        {tab === 'constellation' && <ConstellationView />}
        {tab === 'arc' && <CareerArcView />}
        {tab === 'impact' && <ImpactWallView />}
        {tab === 'timeline' && <TimelineView />}
        {tab === 'voices' && <VoicesView />}
        {tab === 'talks' && <TalksGivebacksView />}
        {tab === 'graph' && <KnowledgeGraphView />}
      </div>
    </div>
  )
}
