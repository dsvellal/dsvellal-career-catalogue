import { useState, useMemo, useEffect } from 'react'
import timelineData from './data/timeline_full.json'

const ERA_COLORS: Record<string, string> = {
  'Philips USA':   '#c98500',
  'Philips India': '#e6a817',
  IBM:             '#3987e5',
  Exeter:          '#d95926',
  Amazon:          '#199e70',
  Independent:     '#9085e9',
}

const TYPE_ICONS: Record<string, string> = {
  award:         '🏆',
  achievement:   '⚡',
  promotion:     '↑',
  talk:          '🎤',
  publication:   '📄',
  certification: '🎓',
  giveback:      '🤝',
  recognition:   '★',
}

const TYPE_COLORS: Record<string, string> = {
  award:         '#c98500',
  promotion:     '#199e70',
  certification: '#3987e5',
  publication:   '#9085e9',
  talk:          '#d55181',
  giveback:      '#008300',
  achievement:   '#d95926',
  recognition:   '#898781',
}

const ERA_ORDER = ['Philips USA', 'Philips India', 'Amazon', 'Exeter', 'IBM', 'Independent']

interface MilestoneItem {
  title: string
  type: string
  detail: string
  date: string
  pinned?: boolean
  evidence_file?: string
}

interface MonthGroup {
  month: string
  items: MilestoneItem[]
  pinned?: boolean
}

interface YearGroup {
  year: number
  total: number
  months: MonthGroup[]
}

interface EraData {
  era: string
  org: string
  role: string
  start: number
  end: number
  start_date?: string
  end_date?: string
  location?: string
  color_slot: number
  years: YearGroup[]
  total: number
}

const rawEras = timelineData as EraData[]
const eras = ERA_ORDER.map(name => rawEras.find(e => e.era === name)).filter(Boolean) as EraData[]

function flattenYear(yr: YearGroup): MilestoneItem[] {
  const all: MilestoneItem[] = yr.months.flatMap(m => m.items.map(item => ({ ...item, pinned: item.pinned ?? m.pinned })))
  return all.sort((a, b) => (b.date ?? '').localeCompare(a.date ?? ''))
}

// ── Full Artifact Viewer (Level 3) ──────────────────────────────────────────
function FullArtifactView({ evidenceFile, onClose }: { evidenceFile: string; onClose: () => void }) {
  const [content, setContent] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    setLoading(true)
    fetch(`/${evidenceFile}`)
      .then(r => {
        if (!r.ok) throw new Error(`${r.status}`)
        return r.text()
      })
      .then(text => {
        setContent(text)
        setLoading(false)
      })
      .catch(() => {
        setContent(null)
        setLoading(false)
      })
  }, [evidenceFile])

  return (
    <div className="tl-artifact-overlay">
      <div className="tl-artifact-panel">
        <div className="tl-artifact-header">
          <span className="tl-artifact-path">{evidenceFile}</span>
          <button className="tl-artifact-close" onClick={onClose}>✕ Close</button>
        </div>
        <div className="tl-artifact-body">
          {loading && <div className="tl-artifact-loading">Loading artifact...</div>}
          {!loading && !content && (
            <div className="tl-artifact-unavailable">
              <p>This artifact is not available for preview.</p>
              <p className="tl-artifact-path-hint">File: <code>{evidenceFile}</code></p>
            </div>
          )}
          {!loading && content && (
            <div className="tl-artifact-content">
              <MarkdownRenderer content={content} />
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

// ── Simple Markdown Renderer ─────────────────────────────────────────────────
function MarkdownRenderer({ content }: { content: string }) {
  const html = useMemo(() => renderMarkdown(content), [content])
  return <div className="tl-markdown" dangerouslySetInnerHTML={{ __html: html }} />
}

function renderMarkdown(md: string): string {
  let html = md
    .replace(/^### (.+)$/gm, '<h3>$1</h3>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/^# (.+)$/gm, '<h1>$1</h1>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/^> (.+)$/gm, '<blockquote>$1</blockquote>')
    .replace(/^- (.+)$/gm, '<li>$1</li>')
    .replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<img src="/$2" alt="$1" class="tl-artifact-img" />')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')

  // Wrap consecutive <li> in <ul>
  html = html.replace(/(<li>.*?<\/li>\n?)+/g, match => `<ul>${match}</ul>`)
  // Wrap consecutive <blockquote>
  html = html.replace(/(<blockquote>.*?<\/blockquote>\n?)+/g, match => `<div class="tl-blockquote-group">${match}</div>`)
  // Code blocks
  html = html.replace(/```[\s\S]*?```/g, match => {
    const code = match.replace(/^```\w*\n?/, '').replace(/\n?```$/, '')
    return `<pre><code>${code}</code></pre>`
  })
  // Paragraphs for remaining lines
  html = html.replace(/^(?!<[hublipd]|<\/|$)(.+)$/gm, '<p>$1</p>')

  return html
}

// ── Rich Summary (Level 2) ───────────────────────────────────────────────────
function RichSummaryCard({
  item,
  era,
  onClose,
  onShowFull,
}: {
  item: MilestoneItem
  era: EraData
  onClose: () => void
  onShowFull: () => void
}) {
  const color = ERA_COLORS[era.era] ?? '#3987e5'
  const typeColor = TYPE_COLORS[item.type] ?? '#898781'

  return (
    <div className="tl-detail-card" style={{ borderLeftColor: color }}>
      <div className="tl-detail-top">
        <span className="tl-detail-icon">{TYPE_ICONS[item.type] ?? '•'}</span>
        <div className="tl-detail-meta">
          <span className="tl-detail-type-badge" style={{ background: typeColor + '22', color: typeColor }}>
            {item.type}
          </span>
          {item.pinned && <span className="tl-detail-pinned-badge">Key moment</span>}
          <span className="tl-detail-date">{item.date}</span>
          <span className="tl-detail-era" style={{ color }}>{era.era}</span>
          {era.location && <span className="tl-detail-location">{era.location}</span>}
        </div>
        <button className="tl-detail-close" onClick={onClose} aria-label="Close">✕</button>
      </div>
      <div className="tl-detail-title">{item.title}</div>
      <p className="tl-detail-body">{item.detail}</p>

      {item.evidence_file && (
        <div className="tl-detail-evidence">
          <div className="tl-detail-evidence-ref">
            <span className="tl-detail-evidence-icon">📄</span>
            <span className="tl-detail-evidence-path">{item.evidence_file.split('/').pop()}</span>
          </div>
          <button className="tl-detail-full-btn" onClick={onShowFull}>
            Explore the full story →
          </button>
        </div>
      )}
    </div>
  )
}

// ── Milestone row ────────────────────────────────────────────────────────────
function MilestoneRow({
  item, era, isActive, onClick, isLast, color, onShowFull,
}: {
  item: MilestoneItem; era: EraData; isActive: boolean; onClick: () => void; isLast: boolean; color: string; onShowFull: () => void
}) {
  const typeColor = TYPE_COLORS[item.type] ?? '#898781'
  const dotColor = item.pinned ? color : typeColor
  return (
    <div className="tl-row-wrap">
      <div className="tl-spine">
        <div className="tl-spine-dot" style={{ background: dotColor, borderColor: dotColor, boxShadow: item.pinned ? `0 0 0 3px ${color}33` : 'none' }} />
        {!isLast && <div className="tl-spine-line" style={{ background: color + '30' }} />}
      </div>

      <div className="tl-row-content">
        <button
          className={`tl-milestone${item.pinned ? ' tl-milestone-pinned' : ''}${isActive ? ' tl-milestone-active' : ''}`}
          onClick={onClick}
          style={isActive ? { borderColor: color, background: color + '12' } : {}}
        >
          <span className="tl-milestone-icon">{TYPE_ICONS[item.type] ?? '•'}</span>
          <span className="tl-milestone-title">{item.title}</span>
          {item.evidence_file && <span className="tl-milestone-evidence-dot" title="Evidence available">●</span>}
          <span className="tl-milestone-date">{item.date?.slice(0, 7)}</span>
        </button>
        {isActive && (
          <RichSummaryCard item={item} era={era} onClose={onClick} onShowFull={onShowFull} />
        )}
      </div>
    </div>
  )
}

// ── Year group ────────────────────────────────────────────────────────────────
function YearGroupSection({
  yr, era, activeKey, setActive, filterType, onShowFull,
}: {
  yr: YearGroup; era: EraData; activeKey: string | null; setActive: (k: string | null) => void; filterType: string; onShowFull: (file: string) => void
}) {
  const color = ERA_COLORS[era.era] ?? '#3987e5'

  const items = useMemo(() => {
    const flat = flattenYear(yr)
    if (filterType === 'all') return flat
    return flat.filter(i => i.type === filterType)
  }, [yr, filterType])

  const hasHighlight = items.some(i => i.pinned)
  const [open, setOpen] = useState(hasHighlight)

  if (items.length === 0) return null

  return (
    <div className="tl-year-group">
      <button
        className="tl-year-header"
        onClick={() => setOpen(o => !o)}
      >
        <span className="tl-year-arrow">{open ? '▾' : '▸'}</span>
        <span className="tl-year-label">{yr.year}</span>
        <span className="tl-year-count">{items.length} entries</span>
      </button>

      {open && (
        <div className="tl-year-body">
          {items.map((item, idx) => {
            const k = `${era.era}:${yr.year}:${idx}`
            return (
              <MilestoneRow
                key={k}
                item={item}
                era={era}
                isActive={activeKey === k}
                onClick={() => setActive(activeKey === k ? null : k)}
                isLast={idx === items.length - 1}
                color={color}
                onShowFull={() => item.evidence_file && onShowFull(item.evidence_file)}
              />
            )
          })}
        </div>
      )}
    </div>
  )
}

// ── Era section ──────────────────────────────────────────────────────────────
function EraSection({
  era, activeKey, setActive, filterType, onShowFull,
}: {
  era: EraData; activeKey: string | null; setActive: (k: string | null) => void; filterType: string; onShowFull: (file: string) => void
}) {
  const color = ERA_COLORS[era.era] ?? '#3987e5'
  const [open, setOpen] = useState(true)

  const reversedYears = useMemo(() => [...era.years].reverse(), [era.years])

  const visibleCount = useMemo(() => {
    if (filterType === 'all') return era.total
    return era.years.flatMap(yr => flattenYear(yr)).filter(i => i.type === filterType).length
  }, [era, filterType])

  if (visibleCount === 0) return null

  const dateRange = era.start_date && era.end_date
    ? `${era.start_date} to ${era.end_date}`
    : `${era.start} to ${era.end}`

  return (
    <div className="tl-era-section" style={{ '--era-color': color } as React.CSSProperties}>
      <button
        className="tl-era-header"
        onClick={() => setOpen(o => !o)}
        style={{ borderLeftColor: color }}
      >
        <div className="tl-era-left">
          <span className="tl-era-arrow">{open ? '▾' : '▸'}</span>
          <div>
            <div className="tl-era-name" style={{ color }}>{era.era}</div>
            <div className="tl-era-org">{era.org}{era.location ? ` · ${era.location}` : ''}</div>
          </div>
        </div>
        <div className="tl-era-right">
          <span className="tl-era-role">{era.role}</span>
          <span className="tl-era-dates">{dateRange}</span>
          <span className="tl-era-total">{visibleCount} entries</span>
        </div>
      </button>

      {open && (
        <div className="tl-era-body">
          {reversedYears.map(yr => (
            <YearGroupSection
              key={yr.year}
              yr={yr}
              era={era}
              activeKey={activeKey}
              setActive={setActive}
              filterType={filterType}
              onShowFull={onShowFull}
            />
          ))}
        </div>
      )}
    </div>
  )
}

// ── Main view ─────────────────────────────────────────────────────────────────
const ALL_TYPES = ['all', 'recognition', 'award', 'certification', 'achievement', 'promotion', 'publication', 'talk', 'giveback']
const TOTAL = eras.reduce((a, e) => a + e.total, 0)

export function TimelineView() {
  const [activeKey, setActiveKey] = useState<string | null>(null)
  const [filterType, setFilterType] = useState('all')
  const [filterEra, setFilterEra] = useState('All')
  const [artifactFile, setArtifactFile] = useState<string | null>(null)

  const visibleEras = filterEra === 'All' ? eras : eras.filter(e => e.era === filterEra)

  return (
    <div className="tl-layout">
      <div className="section-header">
        <div className="section-label">Career Timeline</div>
        <h2 className="section-title">20 years. Five eras. {TOTAL} recorded moments.</h2>
        <p className="section-subtitle">
          Every achievement, recognition, talk, certification, and promotion across the full career,
          newest first. Click any entry to see its story. Items with evidence can be explored in full depth.
        </p>
      </div>

      {/* Era stat tiles */}
      <div className="tl-era-stats">
        {eras.map(e => (
          <div
            key={e.era}
            className={`tl-era-stat${filterEra === e.era ? ' tl-era-stat-active' : ''}`}
            style={{ borderColor: filterEra === e.era ? ERA_COLORS[e.era] : undefined }}
            onClick={() => setFilterEra(filterEra === e.era ? 'All' : e.era)}
          >
            <span className="tl-era-stat-name" style={{ color: ERA_COLORS[e.era] }}>{e.era}</span>
            <span className="tl-era-stat-count">{e.total}</span>
            <span className="tl-era-stat-dates">{e.start} to {e.end}</span>
          </div>
        ))}
      </div>

      {/* Type filters */}
      <div className="tl-filters">
        <span className="tl-filter-label">Filter by type:</span>
        {ALL_TYPES.map(t => (
          <button
            key={t}
            className={`tl-filter-btn${filterType === t ? ' tl-filter-active' : ''}`}
            onClick={() => setFilterType(t)}
          >
            {t === 'all' ? 'All' : `${TYPE_ICONS[t] ?? ''} ${t}`}
          </button>
        ))}
      </div>

      {/* Era sections */}
      <div className="tl-eras">
        {visibleEras.map(era => (
          <EraSection
            key={era.era}
            era={era}
            activeKey={activeKey}
            setActive={setActiveKey}
            filterType={filterType}
            onShowFull={setArtifactFile}
          />
        ))}
      </div>

      {/* Full artifact overlay (Level 3) */}
      {artifactFile && (
        <FullArtifactView
          evidenceFile={artifactFile}
          onClose={() => setArtifactFile(null)}
        />
      )}
    </div>
  )
}
