import { useState, useEffect } from 'react'

interface TimelineItem {
  id: string
  fileName: string
  fileType: string
  type: string
  date: string | null
  claims: string[]
  skills: string[]
  projects: string[]
  organizations: string[]
  snippet: string
}

interface TimelineData {
  items: TimelineItem[]
  heatmap: Record<string, number>
  career: { org: string; start: string; end: string; role: string }[]
  categories: Record<string, TimelineItem[]>
}

const TYPE_COLORS: Record<string, string> = {
  performance_review: '#f59e0b',
  email_appreciation: '#8b5cf6',
  presentation: '#10b981',
  certificate: '#06b6d4',
  project_doc: '#6366f1',
  recommendation: '#ec4899',
  other: '#64748b',
}

const TYPE_LABELS: Record<string, string> = {
  performance_review: 'Review',
  email_appreciation: 'Recognition',
  presentation: 'Talk',
  certificate: 'Certificate',
  project_doc: 'Project',
  recommendation: 'Recommendation',
  other: 'Other',
}

interface YearGroup {
  year: number
  items: TimelineItem[]
  org: string
  role: string
  typeCounts: Record<string, number>
}

function groupByYear(items: TimelineItem[], career: TimelineData['career']): YearGroup[] {
  const groups: Record<number, TimelineItem[]> = {}
  items.forEach(item => {
    if (item.date) {
      const year = parseInt(item.date.split('-')[0])
      if (year >= 2007 && year <= 2026) {
        if (!groups[year]) groups[year] = []
        groups[year].push(item)
      }
    }
  })

  return Object.entries(groups)
    .map(([yearStr, yearItems]) => {
      const year = parseInt(yearStr)
      const typeCounts: Record<string, number> = {}
      yearItems.forEach(item => {
        typeCounts[item.type] = (typeCounts[item.type] || 0) + 1
      })

      const period = career.find(p => {
        const startYear = parseInt(p.start.split('-')[0])
        const endYear = parseInt(p.end.split('-')[0])
        return year >= startYear && year <= endYear
      })

      return {
        year,
        items: yearItems.sort((a, b) => (b.date || '').localeCompare(a.date || '')),
        org: period?.org || '',
        role: period?.role || '',
        typeCounts,
      }
    })
    .sort((a, b) => b.year - a.year)
}

export default function App() {
  const [data, setData] = useState<TimelineData | null>(null)
  const [yearGroups, setYearGroups] = useState<YearGroup[]>([])
  const [expandedYears, setExpandedYears] = useState<Set<number>>(new Set())
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/timeline')
      .then(r => r.json())
      .then((d: TimelineData) => {
        setData(d)
        const groups = groupByYear(d.items, d.career)
        setYearGroups(groups)
        // Expand the 2 most recent years by default
        const recentYears = groups.slice(0, 2).map(g => g.year)
        setExpandedYears(new Set(recentYears))
        setLoading(false)
      })
  }, [])

  const toggleYear = (year: number) => {
    setExpandedYears(prev => {
      const next = new Set(prev)
      if (next.has(year)) next.delete(year)
      else next.add(year)
      return next
    })
  }

  if (loading || !data) {
    return <div className="loading">Loading timeline...</div>
  }

  const totalArtifacts = data.items.filter(i => i.date).length

  return (
    <div className="app">
      <header className="header">
        <h1>Datta's Career Timeline</h1>
        <div className="stats-bar">
          <span>{totalArtifacts} artifacts</span>
          <span>{yearGroups.length} years</span>
          <span>{data.career.length} roles</span>
        </div>
      </header>

      <main className="timeline">
        <div className="timeline-line" />
        {yearGroups.map(group => (
          <YearSection
            key={group.year}
            group={group}
            expanded={expandedYears.has(group.year)}
            onToggle={() => toggleYear(group.year)}
            maxCount={Math.max(...yearGroups.map(g => g.items.length))}
          />
        ))}
      </main>

      <footer className="legend-bar">
        {Object.entries(TYPE_COLORS).map(([type, color]) => (
          <span key={type} className="legend-item">
            <span className="legend-dot" style={{ background: color }} />
            {TYPE_LABELS[type] || type}
          </span>
        ))}
      </footer>
    </div>
  )
}

function YearSection({ group, expanded, onToggle, maxCount }: {
  group: YearGroup
  expanded: boolean
  onToggle: () => void
  maxCount: number
}) {
  const total = group.items.length
  const ringSegments = Object.entries(group.typeCounts)
    .sort((a, b) => b[1] - a[1])

  return (
    <div className={`year-section ${expanded ? 'expanded' : ''}`}>
      <div className="year-header" onClick={onToggle}>
        <div className="year-ring-container">
          <RingChart segments={ringSegments} total={total} />
        </div>
        <div className="year-info">
          <div className="year-label">{group.year}</div>
          <div className="year-meta">
            {group.org && <span className="year-org">{group.org}</span>}
            {group.role && <span className="year-role">{group.role}</span>}
          </div>
        </div>
        <div className="year-summary">
          {ringSegments.slice(0, 3).map(([type, count]) => (
            <span key={type} className="type-pill" style={{ borderColor: TYPE_COLORS[type] || '#666' }}>
              {count} {TYPE_LABELS[type] || type}
            </span>
          ))}
        </div>
        <span className="expand-icon">{expanded ? '−' : '+'}</span>
      </div>

      {expanded && (
        <div className="year-cards">
          {group.items.map(item => (
            <ArtifactCard key={item.id} item={item} />
          ))}
        </div>
      )}
    </div>
  )
}

function RingChart({ segments, total }: { segments: [string, number][]; total: number }) {
  const radius = 20
  const strokeWidth = 5
  const circumference = 2 * Math.PI * radius
  let offset = 0

  return (
    <svg width="50" height="50" viewBox="0 0 50 50">
      <circle cx="25" cy="25" r={radius} fill="none" stroke="#1e1e2e" strokeWidth={strokeWidth} />
      {segments.map(([type, count]) => {
        const fraction = count / total
        const dashLength = fraction * circumference
        const segment = (
          <circle
            key={type}
            cx="25"
            cy="25"
            r={radius}
            fill="none"
            stroke={TYPE_COLORS[type] || '#666'}
            strokeWidth={strokeWidth}
            strokeDasharray={`${dashLength} ${circumference - dashLength}`}
            strokeDashoffset={-offset}
            transform="rotate(-90 25 25)"
          />
        )
        offset += dashLength
        return segment
      })}
      <text x="25" y="25" textAnchor="middle" dy="0.35em" fontSize="11" fontWeight="600" fill="#e0e0e0">
        {total}
      </text>
    </svg>
  )
}

function ArtifactCard({ item }: { item: TimelineItem }) {
  return (
    <div className="card">
      <div className="card-top">
        <span
          className="type-badge"
          style={{ backgroundColor: TYPE_COLORS[item.type] || TYPE_COLORS.other }}
        >
          {TYPE_LABELS[item.type] || item.type}
        </span>
        {item.date && <span className="card-date">{item.date}</span>}
        {item.organizations.length > 0 && (
          <span className="card-org">{item.organizations[0]}</span>
        )}
      </div>
      <h3 className="card-title">{cleanFileName(item.fileName)}</h3>
      {item.claims.length > 0 && (
        <ul className="card-claims">
          {item.claims.map((c, i) => <li key={i}>{c}</li>)}
        </ul>
      )}
      {item.skills.length > 0 && (
        <div className="card-skills">
          {item.skills.slice(0, 6).map(s => <span key={s} className="skill-tag">{s}</span>)}
        </div>
      )}
      {item.snippet && !item.snippet.startsWith('[') && item.snippet.length > 30 && (
        <p className="card-snippet">{item.snippet.slice(0, 120)}...</p>
      )}
    </div>
  )
}

function cleanFileName(name: string): string {
  return name
    .replace(/\.(pdf|docx|xlsx|pptx|png|jpg|jpeg|txt|md|csv|doc|ppt)$/i, '')
    .replace(/_/g, ' ')
    .replace(/([a-z])([A-Z])/g, '$1 $2')
}
