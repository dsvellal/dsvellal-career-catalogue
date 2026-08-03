import { useState, useMemo } from 'react'
import timelineData from './data/timeline_full.json'

const ERA_COLORS: Record<string, string> = {
  IBM:         '#3987e5',
  Exeter:      '#d95926',
  Amazon:      '#199e70',
  Philips:     '#c98500',
  Independent: '#9085e9',
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

interface MilestoneItem {
  title: string
  type: string
  detail: string
  date: string
  pinned?: boolean
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
  color_slot: number
  years: YearGroup[]
  total: number
}

const eras = timelineData as EraData[]

// ── Expanded detail card ──────────────────────────────────────────────────
function DetailCard({
  item,
  era,
  onClose,
}: {
  item: MilestoneItem
  era: EraData
  onClose: () => void
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
          {item.pinned && (
            <span className="tl-detail-pinned-badge">Highlight</span>
          )}
          <span className="tl-detail-date">{item.date}</span>
          <span className="tl-detail-era" style={{ color }}>{era.era}</span>
        </div>
        <button className="tl-detail-close" onClick={onClose} aria-label="Close">✕</button>
      </div>
      <div className="tl-detail-title">{item.title}</div>
      <p className="tl-detail-body">{item.detail}</p>
    </div>
  )
}

// ── Single milestone row ──────────────────────────────────────────────────
function MilestoneRow({
  item,
  era,
  isActive,
  onClick,
}: {
  item: MilestoneItem
  era: EraData
  isActive: boolean
  onClick: () => void
}) {
  const color = ERA_COLORS[era.era] ?? '#3987e5'
  const typeColor = TYPE_COLORS[item.type] ?? '#898781'
  return (
    <button
      className={`tl-milestone${item.pinned ? ' tl-milestone-pinned' : ''}${isActive ? ' tl-milestone-active' : ''}`}
      onClick={onClick}
      style={isActive ? { borderColor: color, background: color + '12' } : {}}
    >
      <span
        className="tl-milestone-dot"
        style={{ background: item.pinned ? color : typeColor + 'aa', borderColor: item.pinned ? color : typeColor }}
      />
      <span className="tl-milestone-icon">{TYPE_ICONS[item.type] ?? '•'}</span>
      <span className="tl-milestone-title">{item.title}</span>
      {item.pinned && <span className="tl-milestone-highlight-tag">Key moment</span>}
    </button>
  )
}

// ── Month group (collapsible) ─────────────────────────────────────────────
function MonthGroup({
  group,
  era,
  activeKey,
  setActive,
  eraYrKey,
}: {
  group: MonthGroup
  era: EraData
  activeKey: string | null
  setActive: (k: string | null) => void
  eraYrKey: string
}) {
  const [open, setOpen] = useState(group.pinned === true)
  const key = (idx: number) => `${eraYrKey}:${group.month}:${idx}`

  return (
    <div className={`tl-month-group${group.pinned ? ' tl-month-pinned' : ''}`}>
      <button
        className="tl-month-header"
        onClick={() => setOpen(o => !o)}
      >
        <span className="tl-month-arrow">{open ? '▾' : '▸'}</span>
        <span className="tl-month-name">{group.month}</span>
        <span className="tl-month-count">{group.items.length}</span>
      </button>
      {open && (
        <div className="tl-month-items">
          {group.items.map((item, idx) => {
            const k = key(idx)
            return (
              <div key={k}>
                <MilestoneRow
                  item={item}
                  era={era}
                  isActive={activeKey === k}
                  onClick={() => setActive(activeKey === k ? null : k)}
                />
                {activeKey === k && (
                  <DetailCard item={item} era={era} onClose={() => setActive(null)} />
                )}
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}

// ── Year group (collapsible) ──────────────────────────────────────────────
function YearGroup({
  yr,
  era,
  activeKey,
  setActive,
}: {
  yr: YearGroup
  era: EraData
  activeKey: string | null
  setActive: (k: string | null) => void
}) {
  const color = ERA_COLORS[era.era] ?? '#3987e5'
  const hasHighlight = yr.months.some(m => m.pinned)
  const [open, setOpen] = useState(hasHighlight)
  const eraYrKey = `${era.era}:${yr.year}`

  return (
    <div className="tl-year-group">
      <button
        className={`tl-year-header${hasHighlight ? ' tl-year-has-highlight' : ''}`}
        onClick={() => setOpen(o => !o)}
        style={hasHighlight ? { borderLeftColor: color } : {}}
      >
        <span className="tl-year-arrow">{open ? '▾' : '▸'}</span>
        <span className="tl-year-label" style={hasHighlight ? { color } : {}}>{yr.year}</span>
        <span className="tl-year-count">{yr.total} entries</span>
        {hasHighlight && <span className="tl-year-star" style={{ color }}>★ Key year</span>}
      </button>
      {open && (
        <div className="tl-year-body">
          {yr.months.map((group, gi) => (
            <MonthGroup
              key={gi}
              group={group}
              era={era}
              activeKey={activeKey}
              setActive={setActive}
              eraYrKey={eraYrKey}
            />
          ))}
        </div>
      )}
    </div>
  )
}

// ── Era section ──────────────────────────────────────────────────────────
function EraSection({
  era,
  activeKey,
  setActive,
  filterType,
}: {
  era: EraData
  activeKey: string | null
  setActive: (k: string | null) => void
  filterType: string
}) {
  const color = ERA_COLORS[era.era] ?? '#3987e5'
  const [open, setOpen] = useState(true)

  const filteredYears = useMemo(() => {
    if (filterType === 'all') return era.years
    return era.years.map(yr => ({
      ...yr,
      months: yr.months
        .map(m => ({ ...m, items: m.items.filter(i => i.type === filterType) }))
        .filter(m => m.items.length > 0),
      total: yr.months.reduce((acc, m) => acc + m.items.filter(i => i.type === filterType).length, 0),
    })).filter(yr => yr.months.length > 0)
  }, [era, filterType])

  const totalFiltered = filteredYears.reduce((a, yr) => a + yr.total, 0)

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
            <div className="tl-era-org">{era.org}</div>
          </div>
        </div>
        <div className="tl-era-right">
          <span className="tl-era-role">{era.role}</span>
          <span className="tl-era-dates">{era.start} to {era.end}</span>
          <span className="tl-era-total">{totalFiltered} entries</span>
        </div>
      </button>

      {open && (
        <div className="tl-era-body">
          {filteredYears.map(yr => (
            <YearGroup
              key={yr.year}
              yr={yr}
              era={era}
              activeKey={activeKey}
              setActive={setActive}
            />
          ))}
        </div>
      )}
    </div>
  )
}

// ── Main view ────────────────────────────────────────────────────────────
const ALL_TYPES = ['all', 'recognition', 'award', 'certification', 'achievement', 'promotion', 'publication', 'talk', 'giveback']
const ALL_ERAS  = ['All', 'IBM', 'Exeter', 'Amazon', 'Philips', 'Independent']
const TOTAL = eras.reduce((a, e) => a + e.total, 0)

export function TimelineView() {
  const [activeKey, setActiveKey] = useState<string | null>(null)
  const [filterType, setFilterType] = useState('all')
  const [filterEra, setFilterEra] = useState('All')

  const visibleEras = filterEra === 'All' ? eras : eras.filter(e => e.era === filterEra)

  return (
    <div className="tl-layout">
      {/* Header */}
      <div className="section-header">
        <div className="section-label">Career Timeline</div>
        <h2 className="section-title">20 years. Four companies. {TOTAL} recorded moments.</h2>
        <p className="section-subtitle">
          Every achievement, recognition, talk, certification, and promotion across the full career.
          Click any entry to expand its story.
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
          />
        ))}
      </div>
    </div>
  )
}
