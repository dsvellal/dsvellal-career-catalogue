import { useEffect, useRef, useState } from 'react'
import {
  DEFAULT_JOURNEY_VIEW,
  JOURNEY_VIEWS,
  JourneyAtlas,
  type JourneyViewId,
} from './JourneyAtlas'
import logoUrl from '../public/logo.jpg'
import './journey-atlas.css'

// Retained for the archived view components, which remain in the source tree.
export type Tab = 'hero' | 'constellation' | 'arc' | 'impact' | 'timeline' | 'voices' | 'talks' | 'graph'

function viewFromHash(): JourneyViewId {
  const hash = window.location.hash.replace(/^#\/?/, '')
  return JOURNEY_VIEWS.some(view => view.id === hash)
    ? hash as JourneyViewId
    : DEFAULT_JOURNEY_VIEW
}

export default function App() {
  const [activeView, setActiveView] = useState<JourneyViewId>(viewFromHash)
  const navRef = useRef<HTMLElement>(null)

  useEffect(() => {
    const hashIsValid = JOURNEY_VIEWS.some(view => `#${view.id}` === window.location.hash)
    if (!hashIsValid) {
      window.history.replaceState(null, '', `#${DEFAULT_JOURNEY_VIEW}`)
    }

    const onHashChange = () => setActiveView(viewFromHash())
    window.addEventListener('hashchange', onHashChange)
    return () => window.removeEventListener('hashchange', onHashChange)
  }, [])

  useEffect(() => {
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    window.scrollTo({ top: 0, behavior: reducedMotion ? 'auto' : 'smooth' })
    document.title = `${JOURNEY_VIEWS.find(view => view.id === activeView)?.label ?? 'Journey'} — Datta Vellal`
    window.requestAnimationFrame(() => {
      document.getElementById(`journey-heading-${activeView}`)?.focus({ preventScroll: true })
    })
  }, [activeView])

  const navigate = (view: JourneyViewId) => {
    setActiveView(view)
    if (window.location.hash !== `#${view}`) window.location.hash = view
  }

  const handleNavKeyDown = (event: React.KeyboardEvent<HTMLElement>) => {
    if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return

    const links = Array.from(navRef.current?.querySelectorAll<HTMLAnchorElement>('[data-journey-nav]') ?? [])
    if (links.length === 0) return

    const currentIndex = Math.max(0, links.indexOf(document.activeElement as HTMLAnchorElement))
    let nextIndex = currentIndex
    if (event.key === 'ArrowLeft') nextIndex = (currentIndex - 1 + links.length) % links.length
    if (event.key === 'ArrowRight') nextIndex = (currentIndex + 1) % links.length
    if (event.key === 'Home') nextIndex = 0
    if (event.key === 'End') nextIndex = links.length - 1

    event.preventDefault()
    links[nextIndex].focus()
  }

  return (
    <div className="atlas-app-shell">
      <a
        className="atlas-skip-link"
        href="#main-content"
        onClick={event => {
          event.preventDefault()
          document.getElementById('main-content')?.focus()
        }}
      >
        Skip to portfolio
      </a>
      <header className="atlas-shell-header">
        <a className="atlas-shell-brand" href={`#${DEFAULT_JOURNEY_VIEW}`} onClick={() => setActiveView(DEFAULT_JOURNEY_VIEW)}>
          <img src={logoUrl} alt="Datta Vellal" className="atlas-shell-logo" />
          <span className="atlas-shell-brand-copy">
            <strong>Datta Vellal</strong>
            <span>Evidence-backed journey atlas</span>
          </span>
        </a>

        <div className="atlas-shell-positioning">
          Digital transformation · Regulated software · Human-scale influence
        </div>

        <label className="atlas-mobile-picker">
          <span>Portfolio view</span>
          <select value={activeView} onChange={event => navigate(event.target.value as JourneyViewId)}>
            {JOURNEY_VIEWS.map((view, index) => (
              <option key={view.id} value={view.id}>{String(index + 1).padStart(2, '0')} · {view.label}</option>
            ))}
          </select>
        </label>

        <nav
          ref={navRef}
          className="atlas-shell-nav"
          aria-label="Journey views"
          onKeyDown={handleNavKeyDown}
        >
          {JOURNEY_VIEWS.map((view, index) => (
            <a
              key={view.id}
              id={`journey-tab-${view.id}`}
              href={`#${view.id}`}
              data-journey-nav
              className={`atlas-shell-nav-link${activeView === view.id ? ' is-active' : ''}`}
              aria-current={activeView === view.id ? 'page' : undefined}
              onClick={() => setActiveView(view.id)}
            >
              <span className="atlas-shell-nav-index">{String(index + 1).padStart(2, '0')}</span>
              <span>{view.shortLabel ?? view.label}</span>
            </a>
          ))}
        </nav>
      </header>

      <main className="atlas-shell-main" id="main-content" tabIndex={-1}>
        <JourneyAtlas activeView={activeView} />
      </main>
    </div>
  )
}
