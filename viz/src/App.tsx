import { useEffect, useMemo, useState } from 'react'
import { ClaimDetailPage, MethodDetailPage, SourceDetailPage } from './DetailPages'
import { LensControl } from './EvidenceUI'
import { PortfolioPageView } from './PortfolioPages'
import {
  hrefForPage,
  pageById,
  parseRoute,
  portfolio,
} from './portfolio-model'
import type { EvidenceLens, PortfolioRoute } from './portfolio-types'

// Archived view components remain type-checked even though the observatory router
// no longer mounts them.
export type Tab = 'hero' | 'constellation' | 'arc' | 'impact' | 'timeline' | 'voices' | 'talks' | 'graph'

function initialLens(): EvidenceLens {
  try {
    const stored = window.localStorage.getItem('datta-evidence-lens')
    if (stored === 'narrative' || stored === 'proof' || stored === 'method' || stored === 'gaps') return stored
  } catch {
    // Storage is an enhancement; the narrative lens remains the safe default.
  }
  return 'narrative'
}

function routeTitle(route: PortfolioRoute): string {
  if (route.type === 'page') return pageById.get(route.pageId)?.label ?? 'Executive Brief'
  if (route.type === 'claim') return portfolio.claims.find(item => item.id === route.id)?.title ?? 'Claim Record'
  if (route.type === 'source') return portfolio.sources.find(item => item.id === route.id)?.title ?? 'Source Record'
  return portfolio.methods.find(item => item.id === route.id)?.title ?? 'Method Record'
}

function routeKey(route: PortfolioRoute): string {
  return route.type === 'page' ? `page:${route.pageId}` : `${route.type}:${route.id}`
}

function detailLabel(route: PortfolioRoute): string | undefined {
  if (route.type === 'page') return undefined
  if (route.type === 'claim') return 'Claim record'
  if (route.type === 'source') return 'Source record'
  return 'Method record'
}

export default function App() {
  const [route, setRoute] = useState<PortfolioRoute>(() => parseRoute(window.location.hash))
  const [lens, setLens] = useState<EvidenceLens>(initialLens)
  const activePage = route.type === 'page' ? pageById.get(route.pageId) : undefined
  const title = useMemo(() => routeTitle(route), [route])

  useEffect(() => {
    if (!window.location.hash || window.location.hash === '#') {
      window.history.replaceState(null, '', hrefForPage(portfolio.pages[0]))
    }
    const onHashChange = () => setRoute(parseRoute(window.location.hash))
    window.addEventListener('hashchange', onHashChange)
    return () => window.removeEventListener('hashchange', onHashChange)
  }, [])

  useEffect(() => {
    try {
      window.localStorage.setItem('datta-evidence-lens', lens)
    } catch {
      // Ignore storage errors in private/restricted browser contexts.
    }
    document.documentElement.dataset.evidenceLens = lens
  }, [lens])

  useEffect(() => {
    document.title = `${title} — Datta Vellal`
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    window.scrollTo({ top: 0, behavior: reducedMotion ? 'auto' : 'smooth' })
    window.requestAnimationFrame(() => {
      const hashParameters = new URLSearchParams(window.location.hash.split('?')[1] ?? '')
      if (route.type === 'page' && hashParameters.has('focus')) return
      const heading = route.type === 'page'
        ? document.getElementById(`page-heading-${route.pageId}`)
        : document.getElementById('detail-heading')
      heading?.classList.add('obs-programmatic-focus')
      heading?.focus({ preventScroll: true })
    })
  }, [route, title])

  const selectRoute = (value: string) => {
    const page = pageById.get(value)
    if (page) window.location.hash = hrefForPage(page).slice(1)
  }

  return (
    <div className="obs-app">
      <a
        className="obs-skip-link"
        href="#main-content"
        onClick={event => {
          event.preventDefault()
          document.getElementById('main-content')?.focus()
        }}
      >Skip to dossier</a>
      <div className="obs-atmosphere" aria-hidden="true"><i /><i /><i /></div>

      <header className="obs-shell-header">
        <div className="obs-header-primary">
          <a className="obs-brand" href={hrefForPage(portfolio.pages[0])} aria-label="Datta Vellal executive brief">
            <span className="obs-brand-mark">DV</span>
            <span className="obs-brand-copy">
              <strong>Datta Vellal</strong>
              <small>Executive data observatory</small>
            </span>
          </a>

          <div className="obs-header-status" role="group" aria-label="Public portfolio record counts">
            <span><strong>{portfolio.claims.length}</strong> claims</span>
            <span><strong>{portfolio.sources.length}</strong> sources</span>
            <span><strong>{portfolio.methods.length}</strong> methods</span>
          </div>

          <label className="obs-mobile-route">
            <span>Portfolio view</span>
            <select value={activePage?.id ?? ''} onChange={event => selectRoute(event.target.value)}>
              {!activePage && <option value="">{detailLabel(route)}</option>}
              {portfolio.pages.map((page, index) => (
                <option key={page.id} value={page.id}>{String(index + 1).padStart(2, '0')} · {page.label}</option>
              ))}
            </select>
          </label>

          <LensControl lens={lens} onChange={setLens} />
        </div>

        <nav className="obs-primary-nav" aria-label="Executive dossier">
          {portfolio.pages.map((page, index) => (
            <a
              key={page.id}
              href={hrefForPage(page)}
              className={activePage?.id === page.id ? 'is-active' : ''}
              aria-current={activePage?.id === page.id ? 'page' : undefined}
              title={page.question}
            >
              <span>{String(index + 1).padStart(2, '0')}</span>
              <strong>{page.label}</strong>
            </a>
          ))}
        </nav>
      </header>

      <main id="main-content" className="obs-main" tabIndex={-1}>
        <div className="obs-route-transition" key={routeKey(route)}>
          {route.type === 'page' && activePage && <PortfolioPageView page={activePage} lens={lens} />}
          {route.type === 'claim' && <ClaimDetailPage claimId={route.id} lens={lens} />}
          {route.type === 'source' && <SourceDetailPage sourceId={route.id} />}
          {route.type === 'method' && <MethodDetailPage methodId={route.id} />}
        </div>
      </main>

      <footer className="obs-footer">
        <div>
          <strong>Datta Vellal</strong>
          <span>Leadership claims presented with their evidence, methods, conflicts, and publication boundaries.</span>
        </div>
        <nav aria-label="Footer">
          <a href="#/data-room">Data Room</a>
          <a href={hrefForPage(portfolio.pages[0])}>Executive Brief</a>
        </nav>
        <small>Public projection · {String(portfolio.meta.as_of ?? portfolio.meta.generated_at ?? 'date recorded in dataset')}</small>
      </footer>
    </div>
  )
}
