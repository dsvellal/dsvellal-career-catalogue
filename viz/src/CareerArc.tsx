import { useState, useMemo } from 'react'
import careerData from './data/career_arc.json'

interface YearData {
  year: number
  recognition: number
  certification: number
  recommendation: number
  total: number
  top_issuer: string
  issuers: Record<string, number>
  new_skills: { name: string; category: string; id: string }[]
  top_skills: { name: string; count: number }[]
}

interface Era {
  short: string
  org: string
  start: number
  end: number
  color_slot: number
}

const ERA_COLORS = ['#2563a8', '#b84c1a', '#0d7a52', '#9a6b00', '#6b46b0']

type SubView = 'load' | 'chapters' | 'cumulative' | 'skills'

function eraColor(era: Era): string {
  return ERA_COLORS[era.color_slot] ?? '#1a2233'
}

function LoadDiagramView({ years, eras }: { years: YearData[]; eras: Era[] }) {
  const [selectedYear, setSelectedYear] = useState<number | null>(null)
  const maxTotal = Math.max(...years.map(d => d.total))
  const cumulative = years.reduce<{ year: number; cum: number; total: number }[]>((acc, y) => {
    const prev = acc.length > 0 ? acc[acc.length - 1].cum : 0
    acc.push({ year: y.year, cum: prev + y.total, total: y.total })
    return acc
  }, [])
  const maxCum = cumulative[cumulative.length - 1]?.cum ?? 1

  const selectedData = years.find(d => d.year === selectedYear)
  const selectedEra = selectedYear ? eras.find(e => selectedYear >= e.start && selectedYear <= e.end) : null

  return (
    <div className="ca-load-view">
      <div className="ca-load-diagram">
        <div className="ca-load-header">
          <span className="ca-load-title">Structural Load Over Time</span>
          <span className="ca-load-subtitle">Each year adds weight (recognitions); capacity (skills) grows to support it</span>
        </div>
        <div className="ca-load-bars">
          {cumulative.map(({ year, cum, total }) => {
            const era = eras.find(e => year >= e.start && year <= e.end)
            const heightPct = (cum / maxCum) * 100
            const yearPct = (total / maxTotal) * 100
            const isSelected = year === selectedYear
            return (
              <button
                key={year}
                className={`ca-load-col${isSelected ? ' ca-load-col--active' : ''}`}
                onClick={() => setSelectedYear(year === selectedYear ? null : year)}
              >
                <div className="ca-load-bar-wrap">
                  <div
                    className="ca-load-bar-cum"
                    style={{ height: `${heightPct}%`, background: era ? eraColor(era) : '#1a2233', opacity: 0.15 }}
                  />
                  <div
                    className="ca-load-bar-year"
                    style={{ height: `${yearPct}%`, background: era ? eraColor(era) : '#1a2233' }}
                  />
                </div>
                <span className="ca-load-year-label">{year}</span>
              </button>
            )
          })}
        </div>
        <div className="ca-load-legend">
          {eras.map(era => (
            <span key={era.short} className="ca-load-legend-item">
              <span className="ca-load-legend-swatch" style={{ background: eraColor(era) }} />
              {era.short}
            </span>
          ))}
          <span className="ca-load-legend-note">Solid = year's load · Faded = cumulative capacity</span>
        </div>
      </div>

      {selectedData && (
        <div className="ca-load-detail">
          <div className="ca-load-detail-header">
            <span className="ca-load-detail-year">{selectedYear}</span>
            <span className="ca-load-detail-era" style={{ color: selectedEra ? eraColor(selectedEra) : undefined }}>
              {selectedEra?.org}
            </span>
          </div>
          <div className="ca-load-detail-metrics">
            <div className="ca-load-metric">
              <span className="ca-load-metric-val">{selectedData.recognition}</span>
              <span className="ca-load-metric-lbl">RECOGNITIONS</span>
            </div>
            <div className="ca-load-metric">
              <span className="ca-load-metric-val">{selectedData.certification}</span>
              <span className="ca-load-metric-lbl">CERTIFICATIONS</span>
            </div>
            <div className="ca-load-metric">
              <span className="ca-load-metric-val">{selectedData.recommendation}</span>
              <span className="ca-load-metric-lbl">RECOMMENDATIONS</span>
            </div>
          </div>
          {selectedData.new_skills.length > 0 && (
            <div className="ca-load-detail-skills">
              <div className="ca-load-detail-skills-title">New skills acquired</div>
              <div className="ca-load-detail-skills-list">
                {selectedData.new_skills.map(s => (
                  <span key={s.id} className="ca-load-skill-chip">{s.name}</span>
                ))}
              </div>
            </div>
          )}
          {selectedData.top_skills.length > 0 && (
            <div className="ca-load-detail-skills">
              <div className="ca-load-detail-skills-title">Top skills by usage</div>
              <div className="ca-load-detail-skills-list">
                {selectedData.top_skills.slice(0, 5).map(s => (
                  <span key={s.name} className="ca-load-skill-chip">{s.name} ({s.count})</span>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  )
}

function ChaptersView({ years, eras }: { years: YearData[]; eras: Era[] }) {
  return (
    <div className="ca-chapters">
      {eras.map(era => {
        const eraYears = years.filter(y => y.year >= era.start && y.year <= era.end)
        const totalAch = eraYears.reduce((s, y) => s + y.total, 0)
        const totalSkills = eraYears.reduce((s, y) => s + y.new_skills.length, 0)
        const topSkill = eraYears.flatMap(y => y.top_skills).sort((a, b) => b.count - a.count)[0]
        return (
          <div key={era.short} className="ca-chapter" style={{ '--chapter-color': eraColor(era) } as React.CSSProperties}>
            <div className="ca-chapter-header">
              <span className="ca-chapter-era" style={{ color: eraColor(era) }}>{era.short}</span>
              <span className="ca-chapter-org">{era.org}</span>
              <span className="ca-chapter-dates">{era.start}–{era.end}</span>
            </div>
            <div className="ca-chapter-stats">
              <div className="ca-chapter-stat">
                <span className="ca-chapter-stat-val">{totalAch}</span>
                <span className="ca-chapter-stat-lbl">ACHIEVEMENTS</span>
              </div>
              <div className="ca-chapter-stat">
                <span className="ca-chapter-stat-val">{totalSkills}</span>
                <span className="ca-chapter-stat-lbl">NEW SKILLS</span>
              </div>
              <div className="ca-chapter-stat">
                <span className="ca-chapter-stat-val">{eraYears.length}</span>
                <span className="ca-chapter-stat-lbl">YEARS</span>
              </div>
              {topSkill && (
                <div className="ca-chapter-stat">
                  <span className="ca-chapter-stat-val ca-chapter-stat-val--text">{topSkill.name}</span>
                  <span className="ca-chapter-stat-lbl">TOP SKILL</span>
                </div>
              )}
            </div>
          </div>
        )
      })}
    </div>
  )
}

function CumulativeView({ years, eras }: { years: YearData[]; eras: Era[] }) {
  const cumData = years.reduce<{ year: number; cum: number; era: Era | undefined }[]>((acc, y) => {
    const prev = acc.length > 0 ? acc[acc.length - 1].cum : 0
    const era = eras.find(e => y.year >= e.start && y.year <= e.end)
    acc.push({ year: y.year, cum: prev + y.total, era })
    return acc
  }, [])
  const maxCum = cumData[cumData.length - 1]?.cum ?? 1

  return (
    <div className="ca-cumulative">
      <div className="ca-cum-header">
        <span className="ca-cum-title">Evidence Accumulated</span>
        <span className="ca-cum-total">{maxCum} total achievements by 2026</span>
      </div>
      <div className="ca-cum-bars">
        {cumData.map(({ year, cum, era }) => (
          <div key={year} className="ca-cum-col">
            <div className="ca-cum-bar-wrap">
              <div
                className="ca-cum-bar"
                style={{ height: `${(cum / maxCum) * 100}%`, background: era ? eraColor(era) : '#1a2233' }}
              />
            </div>
            <span className="ca-cum-year">{year}</span>
            <span className="ca-cum-val">{cum}</span>
          </div>
        ))}
      </div>
    </div>
  )
}

function SkillsTimelineView({ years, eras }: { years: YearData[]; eras: Era[] }) {
  const allSkills = useMemo(() =>
    years.flatMap(y => y.new_skills.map(s => ({ ...s, year: y.year }))),
    [years]
  )

  const categories = useMemo(() => {
    const catMap: Record<string, { name: string; skills: typeof allSkills }> = {}
    allSkills.forEach(s => {
      const cat = s.category || 'other'
      if (!catMap[cat]) catMap[cat] = { name: cat, skills: [] }
      catMap[cat].skills.push(s)
    })
    return Object.values(catMap).sort((a, b) => b.skills.length - a.skills.length)
  }, [allSkills])

  return (
    <div className="ca-skills-tl">
      <div className="ca-skills-tl-header">
        <span className="ca-skills-tl-title">Skill Acquisition Timeline</span>
        <span className="ca-skills-tl-sub">{allSkills.length} skills learned across {years.length} years</span>
      </div>
      <div className="ca-skills-tl-grid">
        {categories.slice(0, 8).map(cat => (
          <div key={cat.name} className="ca-skills-tl-row">
            <span className="ca-skills-tl-cat">{cat.name.replace(/_/g, ' ')}</span>
            <div className="ca-skills-tl-track">
              {cat.skills.map(s => {
                const era = eras.find(e => s.year >= e.start && s.year <= e.end)
                const pos = ((s.year - 2007) / (2026 - 2007)) * 100
                return (
                  <span
                    key={s.id}
                    className="ca-skills-tl-dot"
                    style={{ left: `${pos}%`, background: era ? eraColor(era) : '#1a2233' }}
                    title={`${s.name} (${s.year})`}
                  />
                )
              })}
            </div>
            <span className="ca-skills-tl-count">{cat.skills.length}</span>
          </div>
        ))}
        <div className="ca-skills-tl-axis">
          {[2007, 2010, 2013, 2016, 2019, 2022, 2025].map(y => (
            <span key={y} className="ca-skills-tl-axis-label" style={{ left: `${((y - 2007) / (2026 - 2007)) * 100}%` }}>{y}</span>
          ))}
        </div>
      </div>
    </div>
  )
}

export function CareerArcView() {
  const years: YearData[] = (careerData.years as unknown as YearData[]).filter(d => d.year >= 2007 && d.year <= 2026)
  const eras: Era[] = careerData.eras as Era[]
  const [view, setView] = useState<SubView>('load')

  const totalAch = years.reduce((s, d) => s + d.total, 0)
  const peakYear = years.reduce((a, b) => a.total > b.total ? a : b)

  return (
    <div className="ca-layout">
      <div className="section-header">
        <div className="section-label">Career Arc</div>
        <h2 className="section-title">20 Years of Building</h2>
        <p className="section-subtitle">
          {totalAch} achievements across {eras.length} organizations. Peak year: {peakYear.year} with {peakYear.total} achievements.
        </p>
      </div>

      <div className="ca-sub-tabs">
        <button className={`ca-sub-tab${view === 'load' ? ' ca-sub-tab--active' : ''}`} onClick={() => setView('load')}>
          Load Diagram
        </button>
        <button className={`ca-sub-tab${view === 'chapters' ? ' ca-sub-tab--active' : ''}`} onClick={() => setView('chapters')}>
          Chapters
        </button>
        <button className={`ca-sub-tab${view === 'cumulative' ? ' ca-sub-tab--active' : ''}`} onClick={() => setView('cumulative')}>
          Cumulative
        </button>
        <button className={`ca-sub-tab${view === 'skills' ? ' ca-sub-tab--active' : ''}`} onClick={() => setView('skills')}>
          Skills Timeline
        </button>
      </div>

      <div className="ca-view-content">
        {view === 'load' && <LoadDiagramView years={years} eras={eras} />}
        {view === 'chapters' && <ChaptersView years={years} eras={eras} />}
        {view === 'cumulative' && <CumulativeView years={years} eras={eras} />}
        {view === 'skills' && <SkillsTimelineView years={years} eras={eras} />}
      </div>
    </div>
  )
}
