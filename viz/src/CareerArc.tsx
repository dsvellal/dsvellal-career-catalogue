import { useState, useRef, useMemo } from 'react'
import * as d3 from 'd3'
import careerData from './data/career_arc.json'

// ── Types ──────────────────────────────────────────────────────────────────
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

interface SkillYear {
  name: string
  category: string
  id: string
  year: number
}

// ── Palette slots for eras (validated dark) ───────────────────────────────
const ERA_COLORS = ['#3987e5', '#d95926', '#199e70', '#c98500', '#d55181']
const ACH_TYPE_COLORS: Record<string, string> = {
  recognition:    '#3987e5',
  certification:  '#199e70',
  recommendation: '#d55181',
}
const ACH_TYPE_LABELS: Record<string, string> = {
  recognition:    'Recognition',
  certification:  'Certification',
  recommendation: 'Recommendation',
}
const SKILL_CAT_COLORS: Record<string, string> = {
  leadership:            '#199e70',
  engineering_practice:  '#3987e5',
  soft_skill:            '#d95926',
  framework:             '#c98500',
  ai_technology:         '#9085e9',
  agile_methodology:     '#d55181',
  devops:                '#e66767',
  compliance_standard:   '#e66767',
  domain_expertise:      '#3987e5',
  compliance:            '#d55181',
  other:                 '#898781',
}

function eraForYear(year: number, eras: Era[]): Era | null {
  return eras.find(e => year >= e.start && year <= e.end) ?? null
}

// ── Main component ─────────────────────────────────────────────────────────
export function CareerArcView() {
  const years: YearData[] = (careerData.years as YearData[]).filter(d => d.year >= 2007 && d.year <= 2026)
  const eras: Era[] = careerData.eras as Era[]

  const [selectedYear, setSelectedYear] = useState<number | null>(null)
  const [hoveredYear, setHoveredYear] = useState<number | null>(null)
  const [activeEras, setActiveEras] = useState<Set<string>>(new Set(eras.map(e => e.short)))
  const [showTable, setShowTable] = useState(false)
  const [tooltip, setTooltip] = useState<{ x: number; y: number; year: number } | null>(null)
  const svgRef = useRef<SVGSVGElement>(null)

  const selectedData = years.find(d => d.year === selectedYear)
  const highlightYear = hoveredYear ?? selectedYear

  // ── Chart geometry ────────────────────────────────────────────────────
  const MARGIN = { top: 12, right: 24, bottom: 40, left: 44 }
  const SVG_W = 880
  const SVG_H = 260
  const plotW = SVG_W - MARGIN.left - MARGIN.right
  const plotH = SVG_H - MARGIN.top - MARGIN.bottom

  const xScale = d3.scaleBand()
    .domain(years.map(d => String(d.year)))
    .range([0, plotW])
    .padding(0.22)

  const maxTotal = Math.max(...years.map(d => d.total))
  const yScale = d3.scaleLinear()
    .domain([0, Math.ceil(maxTotal / 10) * 10])
    .range([plotH, 0])
    .nice()

  const yTicks = yScale.ticks(5)
  const bandW = xScale.bandwidth()

  // Stacked segments per bar
  const stackKeys: (keyof typeof ACH_TYPE_COLORS)[] = ['recognition', 'certification', 'recommendation']

  // Skills timeline data
  const allSkillYears: SkillYear[] = useMemo(() =>
    years.flatMap(y =>
      y.new_skills.map(s => ({ ...s, year: y.year }))
    ), [years])

  const skillYearRange = [2007, 2026]
  const SKL_SVG_W = 880
  const SKL_SVG_H = 220
  const SKL_MARGIN = { top: 8, right: 24, bottom: 32, left: 44 }
  const sPlotW = SKL_SVG_W - SKL_MARGIN.left - SKL_MARGIN.right
  const sPlotH = SKL_SVG_H - SKL_MARGIN.top - SKL_MARGIN.bottom

  const sXScale = d3.scaleBand()
    .domain(years.map(d => String(d.year)))
    .range([0, sPlotW])
    .padding(0.1)

  // How many new skills per year per category
  const skillByYearCat = useMemo(() => {
    const map: Record<number, Record<string, number>> = {}
    allSkillYears.forEach(s => {
      if (!map[s.year]) map[s.year] = {}
      const cat = s.category || 'other'
      map[s.year][cat] = (map[s.year][cat] ?? 0) + 1
    })
    return map
  }, [allSkillYears])

  const catKeys = Object.keys(SKILL_CAT_COLORS).filter(k => k !== 'other')
  const maxSkillCount = Math.max(...years.map(y => (y.new_skills ?? []).length))
  const sYScale = d3.scaleLinear().domain([0, maxSkillCount]).range([sPlotH, 0]).nice()

  // ── Tooltip ───────────────────────────────────────────────────────────
  const handleBarHover = (year: number, e: React.MouseEvent) => {
    setHoveredYear(year)
    setTooltip({ x: e.clientX, y: e.clientY, year })
  }

  const tooltipYear = tooltip ? years.find(d => d.year === tooltip.year) : null

  // Era toggle
  const toggleEra = (short: string) => {
    setActiveEras(prev => {
      const next = new Set(prev)
      if (next.has(short)) {
        if (next.size === 1) return prev // keep at least one
        next.delete(short)
      } else {
        next.add(short)
      }
      return next
    })
  }

  const totalAchievements = years.reduce((s, d) => s + d.total, 0)
  const totalCerts = years.reduce((s, d) => s + d.certification, 0)
  const totalRecs = years.reduce((s, d) => s + d.recommendation, 0)

  return (
    <div>
      {/* Header */}
      <div className="section-header">
        <div className="section-label">Career Arc</div>
        <h1 className="section-title">20 Years of Impact</h1>
        <p className="section-subtitle">
          Achievements, certifications, and peer recognition plotted across every year of your career.
          Click a bar to see that year's detail.
        </p>
      </div>

      {/* KPI row */}
      <div className="kpi-row">
        {[
          { label: 'Total achievements', value: totalAchievements.toString(), sub: 'Across 20 years' },
          { label: 'Certifications', value: totalCerts.toString(), sub: 'Verified credentials' },
          { label: 'Peer recognitions', value: totalRecs.toString(), sub: 'Recommendations received' },
          { label: 'Peak year', value: String(years.reduce((a, b) => a.total > b.total ? a : b).year), sub: `${years.reduce((a, b) => a.total > b.total ? a : b).total} achievements` },
        ].map(t => (
          <div className="kpi-tile" key={t.label}>
            <div className="kpi-label">{t.label}</div>
            <div className="kpi-value">{t.value}</div>
            <div className="kpi-sub">{t.sub}</div>
          </div>
        ))}
      </div>

      <div className="arc-layout">
        {/* Filter row — era legend */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 16, flexWrap: 'wrap' }}>
          <span style={{ fontSize: 11, color: 'var(--ink-muted)', textTransform: 'uppercase', letterSpacing: '0.06em', fontWeight: 600 }}>
            Eras
          </span>
          <div className="era-legend">
            {eras.map((era, i) => (
              <div
                key={era.short}
                className={`era-pill ${!activeEras.has(era.short) ? 'dimmed' : ''}`}
                onClick={() => toggleEra(era.short)}
              >
                <div className="era-swatch" style={{ background: ERA_COLORS[i] }} />
                <span>{era.short}</span>
                <span style={{ fontSize: 11, color: 'var(--ink-muted)' }}>
                  {era.start}–{era.end}
                </span>
              </div>
            ))}
          </div>
          <div style={{ display: 'flex', gap: 14, marginLeft: 'auto', alignItems: 'center', flexWrap: 'wrap' }}>
            {stackKeys.map(k => (
              <div key={k} className="legend-item">
                <div className="legend-dot" style={{ background: ACH_TYPE_COLORS[k] }} />
                <span style={{ fontSize: 11, color: 'var(--ink-muted)' }}>{ACH_TYPE_LABELS[k]}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Achievement bar chart */}
        <div className="arc-chart-card">
          <div className="arc-chart-header">
            <span className="arc-chart-title">Achievements per year</span>
            <span className="arc-chart-subtitle">Stacked by type</span>
            <button className="table-toggle" onClick={() => setShowTable(v => !v)}>
              {showTable ? 'Hide table' : 'Table view'}
            </button>
          </div>

          {showTable ? (
            <div style={{ padding: '16px 24px' }}>
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Year</th>
                    <th>Era</th>
                    <th>Total</th>
                    <th>Recognition</th>
                    <th>Certification</th>
                    <th>Recommendation</th>
                    <th>Top issuer</th>
                  </tr>
                </thead>
                <tbody>
                  {years.map(d => {
                    const era = eraForYear(d.year, eras)
                    return (
                      <tr key={d.year}>
                        <td style={{ fontVariantNumeric: 'tabular-nums' }}>{d.year}</td>
                        <td>{era?.short ?? '—'}</td>
                        <td style={{ fontVariantNumeric: 'tabular-nums', fontWeight: 600 }}>{d.total}</td>
                        <td style={{ fontVariantNumeric: 'tabular-nums' }}>{d.recognition}</td>
                        <td style={{ fontVariantNumeric: 'tabular-nums' }}>{d.certification}</td>
                        <td style={{ fontVariantNumeric: 'tabular-nums' }}>{d.recommendation}</td>
                        <td>{d.top_issuer}</td>
                      </tr>
                    )
                  })}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="arc-svg-wrap" style={{ overflowX: 'auto', paddingBottom: 16 }}>
              <svg
                ref={svgRef}
                className="arc-svg"
                width={SVG_W}
                height={SVG_H}
                onMouseLeave={() => { setHoveredYear(null); setTooltip(null) }}
              >
                <g transform={`translate(${MARGIN.left},${MARGIN.top})`}>
                  {/* Era bands */}
                  {eras.map((era, i) => {
                    const startX = xScale(String(Math.max(era.start, 2007)))
                    const endX = xScale(String(Math.min(era.end, 2026)))
                    if (startX == null || endX == null) return null
                    return (
                      <rect
                        key={era.short}
                        x={startX}
                        y={0}
                        width={(endX - startX) + bandW}
                        height={plotH}
                        fill={ERA_COLORS[i]}
                        className="era-band"
                        opacity={activeEras.has(era.short) ? 0.07 : 0.02}
                      />
                    )
                  })}

                  {/* Gridlines */}
                  {yTicks.map(tick => (
                    <line
                      key={tick}
                      x1={0} x2={plotW}
                      y1={yScale(tick)} y2={yScale(tick)}
                      className="arc-gridline"
                    />
                  ))}

                  {/* Y axis ticks */}
                  {yTicks.map(tick => (
                    <text
                      key={tick}
                      x={-8} y={yScale(tick)}
                      className="arc-axis-label"
                      textAnchor="end"
                      dominantBaseline="middle"
                    >
                      {tick}
                    </text>
                  ))}

                  {/* Bars */}
                  {years.map(d => {
                    const x = xScale(String(d.year))
                    if (x == null) return null
                    const era = eraForYear(d.year, eras)
                    const isDimmed = era ? !activeEras.has(era.short) : false
                    const isHighlighted = d.year === highlightYear

                    let stackY = plotH
                    return (
                      <g
                        key={d.year}
                        onClick={() => setSelectedYear(d.year === selectedYear ? null : d.year)}
                        onMouseEnter={e => handleBarHover(d.year, e)}
                        onMouseMove={e => handleBarHover(d.year, e)}
                        style={{ cursor: 'pointer' }}
                      >
                        {/* Selection highlight */}
                        {isHighlighted && (
                          <rect
                            x={x - 2} y={0}
                            width={bandW + 4} height={plotH}
                            fill="white"
                            opacity={0.04}
                            rx={4}
                          />
                        )}
                        {stackKeys.map(key => {
                          const val = d[key as keyof YearData] as number
                          if (!val) return null
                          const barH = plotH - yScale(val)
                          const barY = stackY - barH
                          stackY -= barH
                          // 2px surface gap between segments
                          const gapOffset = stackY < plotH - barH ? 1 : 0
                          return (
                            <rect
                              key={key}
                              x={x}
                              y={barY + gapOffset}
                              width={bandW}
                              height={Math.max(0, barH - gapOffset)}
                              fill={ACH_TYPE_COLORS[key]}
                              opacity={isDimmed ? 0.12 : isHighlighted ? 1 : 0.8}
                              rx={key === 'recognition' && stackKeys[0] === 'recognition' ? 4 : 0}
                              className="arc-bar"
                            />
                          )
                        })}
                        {/* Rounded top */}
                        {d.total > 0 && (
                          <rect
                            x={x}
                            y={yScale(d.total)}
                            width={bandW}
                            height={4}
                            rx={4}
                            ry={4}
                            fill={ACH_TYPE_COLORS['recognition']}
                            opacity={isDimmed ? 0.12 : isHighlighted ? 1 : 0.8}
                            pointerEvents="none"
                          />
                        )}
                      </g>
                    )
                  })}

                  {/* X axis labels */}
                  {years.map(d => {
                    const x = xScale(String(d.year))
                    if (x == null) return null
                    const era = eraForYear(d.year, eras)
                    const isActive = era ? activeEras.has(era.short) : true
                    // Show every other year to avoid collision
                    if (d.year % 2 !== 0 && d.year !== 2007) return null
                    return (
                      <text
                        key={d.year}
                        x={(x ?? 0) + bandW / 2}
                        y={plotH + 18}
                        className={`arc-year-label${isActive ? ' era-active' : ''}`}
                        opacity={isActive ? 1 : 0.35}
                      >
                        {d.year}
                      </text>
                    )
                  })}

                  {/* Era labels centered on their band */}
                  {eras.map((era, i) => {
                    if (!activeEras.has(era.short)) return null
                    const startX = xScale(String(Math.max(era.start, 2007)))
                    const endX = xScale(String(Math.min(era.end, 2026)))
                    if (startX == null || endX == null) return null
                    const midX = startX + ((endX - startX) + bandW) / 2
                    return (
                      <text
                        key={era.short}
                        x={midX}
                        y={plotH + 34}
                        textAnchor="middle"
                        fontSize={10}
                        fontWeight={600}
                        fill={ERA_COLORS[i]}
                        opacity={0.8}
                        letterSpacing="0.04em"
                      >
                        {era.short.toUpperCase()}
                      </text>
                    )
                  })}
                </g>
              </svg>
            </div>
          )}
        </div>

        {/* Skills timeline */}
        <div className="skills-row-card">
          <div className="skills-row-title">Skill acquisition over time</div>
          <div className="skills-row-sub">New skills added each year, colored by category</div>

          <div style={{ display: 'flex', gap: 14, flexWrap: 'wrap', marginBottom: 12 }}>
            {catKeys.map(k => (
              <div key={k} className="legend-item">
                <div className="legend-dot" style={{ background: SKILL_CAT_COLORS[k] }} />
                <span style={{ fontSize: 10, color: 'var(--ink-muted)', textTransform: 'capitalize' }}>
                  {k.replace(/_/g, ' ')}
                </span>
              </div>
            ))}
          </div>

          <div className="skills-timeline-wrap">
            <svg className="skills-timeline-svg" width={SKL_SVG_W} height={SKL_SVG_H}>
              <g transform={`translate(${SKL_MARGIN.left},${SKL_MARGIN.top})`}>
                {/* Gridlines */}
                {sYScale.ticks(4).map(tick => (
                  <line
                    key={tick}
                    x1={0} x2={sPlotW}
                    y1={sYScale(tick)} y2={sYScale(tick)}
                    stroke="var(--grid)"
                    strokeWidth={1}
                  />
                ))}

                {/* Y axis labels */}
                {sYScale.ticks(4).map(tick => (
                  <text
                    key={tick}
                    x={-8} y={sYScale(tick)}
                    fontSize={10}
                    fill="var(--ink-muted)"
                    textAnchor="end"
                    dominantBaseline="middle"
                  >
                    {tick}
                  </text>
                ))}

                {/* Stacked skill bars by category */}
                {years.map(d => {
                  const x = sXScale(String(d.year))
                  if (x == null) return null
                  const bw = sXScale.bandwidth()
                  const cats = skillByYearCat[d.year] ?? {}
                  let stackY = sPlotH
                  return (
                    <g key={d.year}>
                      {catKeys.map(cat => {
                        const cnt = cats[cat] ?? 0
                        if (!cnt) return null
                        const bh = sPlotH - sYScale(cnt)
                        const by = stackY - bh
                        stackY -= bh + 1
                        return (
                          <rect
                            key={cat}
                            x={x} y={by}
                            width={bw} height={Math.max(0, bh)}
                            fill={SKILL_CAT_COLORS[cat]}
                            opacity={
                              highlightYear === d.year ? 1
                              : highlightYear != null ? 0.2
                              : 0.75
                            }
                            rx={2}
                          />
                        )
                      })}
                    </g>
                  )
                })}

                {/* X axis labels (every 2 years) */}
                {years.map(d => {
                  if (d.year % 2 !== 0 && d.year !== 2007) return null
                  const x = sXScale(String(d.year))
                  if (x == null) return null
                  return (
                    <text
                      key={d.year}
                      x={(x ?? 0) + sXScale.bandwidth() / 2}
                      y={sPlotH + 18}
                      fontSize={11}
                      fill="var(--ink-muted)"
                      textAnchor="middle"
                      fontVariantNumeric="tabular-nums"
                    >
                      {d.year}
                    </text>
                  )
                })}
              </g>
            </svg>
          </div>
        </div>

        {/* Year detail */}
        {selectedData && (
          <div className={`arc-detail-panel ${selectedData ? 'visible' : ''}`}>
            <div className="arc-detail-header">
              <div className="arc-detail-year">{selectedData.year}</div>
              <div className="arc-detail-org">
                {eraForYear(selectedData.year, eras)?.org ?? ''}
              </div>
              <button
                className="table-toggle"
                style={{ marginLeft: 'auto' }}
                onClick={() => setSelectedYear(null)}
              >
                ✕ Close
              </button>
            </div>

            {/* Stat row */}
            <div style={{ display: 'flex', gap: 12, marginBottom: 20 }}>
              {stackKeys.map(k => {
                const val = selectedData[k as keyof YearData] as number
                return (
                  <div key={k} className="detail-stat" style={{ flex: 1 }}>
                    <div className="detail-stat-value" style={{ color: ACH_TYPE_COLORS[k], fontSize: 20 }}>{val}</div>
                    <div className="detail-stat-label">{ACH_TYPE_LABELS[k]}</div>
                  </div>
                )
              })}
            </div>

            <div className="arc-detail-grid">
              {/* New skills */}
              <div>
                <div className="arc-detail-col-title">
                  New skills added ({selectedData.new_skills.length})
                </div>
                <div className="arc-detail-skills">
                  {selectedData.new_skills.map(s => (
                    <div
                      key={s.id}
                      className="arc-skill-chip"
                      style={{ borderColor: `${SKILL_CAT_COLORS[s.category] ?? '#898781'}44` }}
                    >
                      <span
                        style={{
                          display: 'inline-block',
                          width: 6, height: 6,
                          borderRadius: '50%',
                          background: SKILL_CAT_COLORS[s.category] ?? '#898781',
                          marginRight: 5,
                          verticalAlign: 'middle',
                        }}
                      />
                      {s.name}
                    </div>
                  ))}
                  {selectedData.new_skills.length === 0 && (
                    <span style={{ fontSize: 12, color: 'var(--ink-muted)' }}>No new skills this year</span>
                  )}
                </div>
              </div>

              {/* Top skills used */}
              <div>
                <div className="arc-detail-col-title">
                  Top skills applied
                </div>
                <div className="arc-detail-items">
                  {selectedData.top_skills.slice(0, 6).map((s, i) => (
                    <div key={i} className="arc-detail-item">
                      {s.name}
                      <span style={{ color: 'var(--ink-faint)', marginLeft: 5, fontVariantNumeric: 'tabular-nums', fontSize: 10 }}>
                        ×{s.count}
                      </span>
                    </div>
                  ))}
                  {selectedData.top_skills.length === 0 && (
                    <span style={{ fontSize: 12, color: 'var(--ink-muted)' }}>No skill data for this year</span>
                  )}
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Tooltip */}
      {tooltip && tooltipYear && (
        <div
          className="viz-tooltip visible"
          style={{ left: tooltip.x + 14, top: tooltip.y - 60 }}
        >
          <div className="tooltip-title">{tooltipYear.year}</div>
          {stackKeys.map(k => {
            const val = tooltipYear[k as keyof YearData] as number
            if (!val) return null
            return (
              <div key={k} className="tooltip-row">
                <div className="tooltip-stroke" style={{ background: ACH_TYPE_COLORS[k] }} />
                <span className="tooltip-value">{val}</span>
                <span>{ACH_TYPE_LABELS[k]}</span>
              </div>
            )
          })}
          <div style={{ marginTop: 6, fontSize: 11, color: 'var(--ink-muted)' }}>
            {tooltipYear.top_issuer && `Top: ${tooltipYear.top_issuer}`}
          </div>
        </div>
      )}
    </div>
  )
}
