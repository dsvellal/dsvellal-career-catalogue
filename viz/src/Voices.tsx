import { useState, useEffect, useRef, useCallback } from 'react'
import voicesData from './data/voices.json'

interface Voice {
  quote: string
  company: string
  type: string
  date?: string
  issuer: string
}

const TYPE_COLORS: Record<string, string> = {
  recognition:     '#3987e5',
  recommendation:  '#199e70',
  certification:   '#c98500',
}

const TYPE_BG: Record<string, string> = {
  recognition:    'rgba(57,135,229,0.10)',
  recommendation: 'rgba(25,158,112,0.10)',
  certification:  'rgba(201,133,0,0.10)',
}

const ERA_COLORS: Record<string, string> = {
  Philips:  '#d95926',
  Amazon:   '#199e70',
  IBM:      '#3987e5',
}

const FILTERS = ['All', 'recognition', 'recommendation', 'certification'] as const

function eraColor(company: string) {
  for (const [k, v] of Object.entries(ERA_COLORS)) {
    if (company.toLowerCase().includes(k.toLowerCase())) return v
  }
  return '#898781'
}

function formatDate(d?: string) {
  if (!d) return ''
  // Try YYYY-MM-DD or YYYY-MM or YYYY
  const parts = d.split('-')
  if (parts.length === 3) {
    const date = new Date(d)
    if (!isNaN(date.getTime())) return date.toLocaleDateString('en-US', { month: 'short', year: 'numeric' })
  }
  if (parts.length === 2) return `${new Date(d + '-01').toLocaleDateString('en-US', { month: 'short', year: 'numeric' })}`
  return parts[0]
}

const voices: Voice[] = voicesData as Voice[]

export function VoicesView() {
  const [filter, setFilter] = useState<string>('All')
  const [featured, setFeatured] = useState<Voice>(voices[0])
  const [fadeKey, setFadeKey] = useState(0)
  const [idle, setIdle] = useState(true)
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null)
  const idleTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null)

  const filtered = filter === 'All' ? voices : voices.filter(v => v.type === filter)

  const setFeaturedAnimated = useCallback((v: Voice) => {
    setFeatured(v)
    setFadeKey(k => k + 1)
  }, [])

  const resetIdleTimer = useCallback(() => {
    setIdle(false)
    if (idleTimerRef.current) clearTimeout(idleTimerRef.current)
    idleTimerRef.current = setTimeout(() => setIdle(true), 3000)
  }, [])

  // Auto-rotate
  useEffect(() => {
    if (!idle) {
      if (timerRef.current) clearInterval(timerRef.current)
      return
    }
    const pool = filter === 'All' ? voices : voices.filter(v => v.type === filter)
    if (pool.length === 0) return
    timerRef.current = setInterval(() => {
      setFeaturedAnimated(pool[Math.floor(Math.random() * pool.length)])
    }, 5000)
    return () => { if (timerRef.current) clearInterval(timerRef.current) }
  }, [idle, filter, setFeaturedAnimated])

  // When filter changes, pick first from new pool
  useEffect(() => {
    const pool = filter === 'All' ? voices : voices.filter(v => v.type === filter)
    if (pool.length > 0) setFeaturedAnimated(pool[0])
  }, [filter, setFeaturedAnimated])

  const handleCardClick = (v: Voice) => {
    setFeaturedAnimated(v)
    resetIdleTimer()
  }

  const typeColor = (t: string) => TYPE_COLORS[t] ?? '#898781'
  const typeBg = (t: string) => TYPE_BG[t] ?? 'rgba(137,135,129,0.1)'

  const availableFilters = FILTERS.filter(f => {
    if (f === 'All') return true
    return voices.some(v => v.type === f)
  })

  return (
    <div className="voices-view">
      {/* Section header */}
      <div className="section-header">
        <div className="section-label">Voices</div>
        <h2 className="section-title">What others say</h2>
        <p className="section-subtitle">
          Recognition, recommendations and certifications across a 20-year career — {voices.length} voices.
        </p>
      </div>

      {/* Featured quote */}
      <div className="voices-featured-wrap">
        <div
          className="voices-featured-card"
          key={fadeKey}
          onMouseEnter={() => { setIdle(false) }}
          onMouseLeave={() => setIdle(true)}
        >
          <div className="voices-featured-quote">
            &ldquo;{featured.quote}&rdquo;
          </div>
          <div className="voices-featured-meta">
            <span
              className="voices-era-pill"
              style={{ background: `${eraColor(featured.company)}22`, color: eraColor(featured.company), borderColor: `${eraColor(featured.company)}44` }}
            >
              {featured.issuer || featured.company}
            </span>
            <span
              className="voices-type-badge"
              style={{ background: typeBg(featured.type), color: typeColor(featured.type), borderColor: `${typeColor(featured.type)}44` }}
            >
              {featured.type}
            </span>
            {featured.date && (
              <span className="voices-date">{formatDate(featured.date)}</span>
            )}
          </div>
        </div>
      </div>

      {/* Filter pills + grid */}
      <div className="voices-grid-section">
        <div className="voices-filter-row">
          {availableFilters.map(f => (
            <button
              key={f}
              className={`voices-filter-pill ${filter === f ? 'active' : ''}`}
              style={filter === f && f !== 'All' ? { borderColor: typeColor(f), color: typeColor(f) } : undefined}
              onClick={() => { setFilter(f); resetIdleTimer() }}
            >
              {f === 'All' ? 'All' : f.charAt(0).toUpperCase() + f.slice(1)}
              <span className="voices-filter-count">
                {f === 'All' ? voices.length : voices.filter(v => v.type === f).length}
              </span>
            </button>
          ))}
        </div>

        <div className="voices-grid">
          {filtered.map((v, i) => {
            const isActive = v === featured
            return (
              <div
                key={i}
                className={`voices-card ${isActive ? 'active' : ''}`}
                style={{ '--type-color': typeColor(v.type), '--type-bg': typeBg(v.type) } as React.CSSProperties}
                onClick={() => handleCardClick(v)}
              >
                <div className="voices-card-quote">{v.quote}</div>
                <div className="voices-card-footer">
                  <span
                    className="voices-card-company"
                    style={{ color: eraColor(v.company) }}
                  >
                    {v.company.length > 22 ? v.company.slice(0, 22) + '…' : v.company}
                  </span>
                  <span
                    className="voices-card-type"
                    style={{ background: typeBg(v.type), color: typeColor(v.type) }}
                  >
                    {v.type}
                  </span>
                </div>
              </div>
            )
          })}
        </div>
      </div>
    </div>
  )
}
