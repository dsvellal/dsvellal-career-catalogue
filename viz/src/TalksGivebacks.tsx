import { useState, useRef, useEffect, useMemo } from 'react'
import talksData from './data/talks.json'

interface Talk {
  title: string
  detail: string
  year: number
  era: string
  category: string
  skills?: string[]
}

const ERA_COLORS: Record<string, string> = {
  IBM:         '#3987e5',
  Exeter:      '#d95926',
  Amazon:      '#199e70',
  Philips:     '#c98500',
  Independent: '#898781',
}

const CAT_COLORS: Record<string, string> = {
  talk:     '#3987e5',
  social:   '#199e70',
  yoga:     '#d55181',
  giveback: '#c98500',
}

const talks: Talk[] = talksData as Talk[]

const MIN_YEAR = 2007
const MAX_YEAR = 2026

function TalkItem({ t }: { t: Talk }) {
  const [open, setOpen] = useState(false)
  const eraColor = ERA_COLORS[t.era] ?? '#898781'
  const catColor = CAT_COLORS[t.category] ?? '#898781'

  return (
    <div className={`talks-item ${open ? 'expanded' : ''}`} onClick={() => setOpen(o => !o)}>
      <div className="talks-item-header">
        <span className="talks-year-badge" style={{ background: `${catColor}20`, color: catColor }}>
          {t.year}
        </span>
        <span className="talks-item-title">{t.title.length > 90 ? t.title.slice(0, 90) + '…' : t.title}</span>
        <span className="talks-era-chip" style={{ background: `${eraColor}20`, color: eraColor }}>
          {t.era}
        </span>
        <span className="talks-expand-icon">{open ? '−' : '+'}</span>
      </div>
      {open && (
        <div className="talks-item-detail">
          {t.detail.length > 300 ? t.detail.slice(0, 300) + '…' : t.detail}
        </div>
      )}
    </div>
  )
}

function Column({ title, items, accent }: { title: string; items: Talk[]; accent: string }) {
  return (
    <div className="talks-column">
      <div className="talks-col-header">
        <span className="talks-col-title" style={{ color: accent }}>{title}</span>
        <span className="talks-col-count" style={{ background: `${accent}20`, color: accent }}>{items.length}</span>
      </div>
      <div className="talks-col-scroll">
        {items.length === 0 ? (
          <div className="talks-empty">No entries</div>
        ) : (
          items.map((t, i) => <TalkItem key={i} t={t} />)
        )}
      </div>
    </div>
  )
}

function TimelineBar() {
  const svgRef = useRef<SVGSVGElement>(null)
  const [dims, setDims] = useState({ w: 800, h: 56 })

  useEffect(() => {
    const el = svgRef.current?.parentElement
    if (!el) return
    const obs = new ResizeObserver(entries => {
      const { width } = entries[0].contentRect
      setDims({ w: width || 800, h: 56 })
    })
    obs.observe(el)
    setDims({ w: el.clientWidth || 800, h: 56 })
    return () => obs.disconnect()
  }, [])

  const years = useMemo(() => {
    const map: Record<number, { count: number; dominant: string; counts: Record<string, number> }> = {}
    for (let y = MIN_YEAR; y <= MAX_YEAR; y++) {
      map[y] = { count: 0, dominant: 'talk', counts: {} }
    }
    for (const t of talks) {
      if (t.year < MIN_YEAR || t.year > MAX_YEAR) continue
      map[t.year].count++
      map[t.year].counts[t.category] = (map[t.year].counts[t.category] ?? 0) + 1
    }
    for (const y in map) {
      const cnts = map[y].counts
      const dom = Object.entries(cnts).sort((a, b) => b[1] - a[1])[0]
      map[y].dominant = dom ? dom[0] : 'talk'
    }
    return map
  }, [])

  const totalYears = MAX_YEAR - MIN_YEAR + 1
  const maxCount = Math.max(...Object.values(years).map(y => y.count), 1)
  const barW = Math.max(2, (dims.w - totalYears * 2) / totalYears)
  const gap = 2
  const topPad = 4
  const labelH = 16
  const barMaxH = dims.h - labelH - topPad

  return (
    <div className="talks-timeline-outer">
      <svg
        ref={svgRef}
        className="talks-timeline-svg"
        width={dims.w}
        height={dims.h}
        aria-label="Activity by year"
      >
        {Array.from({ length: totalYears }, (_, i) => {
          const year = MIN_YEAR + i
          const d = years[year]
          const barH = d.count > 0 ? Math.max(3, (d.count / maxCount) * barMaxH) : 2
          const x = i * (barW + gap)
          const y = topPad + barMaxH - barH
          const color = CAT_COLORS[d.dominant] ?? '#898781'
          const showLabel = year % 4 === 1 || year === MIN_YEAR || year === MAX_YEAR

          return (
            <g key={year}>
              <rect
                x={x}
                y={y}
                width={barW}
                height={barH}
                rx={Math.min(2, barW / 2)}
                fill={d.count > 0 ? color : 'var(--surface-3)'}
                opacity={d.count > 0 ? 0.85 : 0.3}
              >
                <title>{year}: {d.count} {d.count === 1 ? 'entry' : 'entries'}</title>
              </rect>
              {showLabel && (
                <text
                  x={x + barW / 2}
                  y={dims.h - 2}
                  textAnchor="middle"
                  fontSize={9}
                  fill="var(--ink-muted)"
                  style={{ fontVariantNumeric: 'tabular-nums' }}
                >
                  {year}
                </text>
              )}
            </g>
          )
        })}
      </svg>
    </div>
  )
}

export function TalksGivebacksView() {
  const techTalks = useMemo(
    () => talks.filter(t => t.category === 'talk' || t.category === 'giveback').sort((a, b) => b.year - a.year),
    []
  )
  const socialItems = useMemo(
    () => talks.filter(t => t.category === 'social').sort((a, b) => b.year - a.year),
    []
  )
  const yogaItems = useMemo(
    () => talks.filter(t => t.category === 'yoga').sort((a, b) => b.year - a.year),
    []
  )

  return (
    <div className="talks-view">
      {/* Section header */}
      <div className="section-header">
        <div className="section-label">Talks &amp; Givebacks</div>
        <h2 className="section-title">Not just an engineer. A teacher, a yogi, a community builder.</h2>
        <p className="section-subtitle">
          {talks.length} engagements across {MAX_YEAR - MIN_YEAR + 1} years: talks, social givebacks, and yoga.
        </p>
      </div>

      {/* Three-column layout */}
      <div className="talks-layout">
        <Column title="Tech Talks &amp; Givebacks" items={techTalks} accent={CAT_COLORS.talk} />
        <div className="talks-right-stack">
          <Column title="Social Givebacks" items={socialItems} accent={CAT_COLORS.social} />
          <Column title="Yoga &amp; Wellness" items={yogaItems} accent={CAT_COLORS.yoga} />
        </div>
      </div>

      {/* Timeline bar */}
      <div className="talks-timeline-section">
        <div className="talks-timeline-header">
          <span className="talks-timeline-label">Activity by year, 2007 to 2026</span>
          <div className="talks-legend">
            {(['talk', 'social', 'yoga', 'giveback'] as const).filter(c => talks.some(t => t.category === c)).map(c => (
              <span key={c} className="talks-legend-item">
                <span className="talks-legend-swatch" style={{ background: CAT_COLORS[c] }} />
                {c}
              </span>
            ))}
          </div>
        </div>
        <TimelineBar />
      </div>
    </div>
  )
}
