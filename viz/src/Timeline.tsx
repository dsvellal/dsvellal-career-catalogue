import { useState } from 'react'
import timelineData from './data/timeline.json'

const ERA_COLORS = ['#3987e5', '#d95926', '#199e70', '#c98500']

const TYPE_ICONS: Record<string, string> = {
  award: '🏆',
  achievement: '⚡',
  promotion: '↑',
  talk: '🎤',
  publication: '📄',
  certification: '🎓',
  giveback: '🤝',
}

const MIN_YEAR = Math.min(...timelineData.map(e => e.start))
const MAX_YEAR = Math.max(...timelineData.map(e => e.end))
const TOTAL_YEARS = MAX_YEAR - MIN_YEAR

export function TimelineView() {
  const [selected, setSelected] = useState<{ eraIdx: number; milestoneIdx: number } | null>(null)

  const selectedMilestone =
    selected !== null
      ? timelineData[selected.eraIdx].milestones[selected.milestoneIdx]
      : null

  const handleDot = (eraIdx: number, milestoneIdx: number) => {
    setSelected(prev =>
      prev?.eraIdx === eraIdx && prev?.milestoneIdx === milestoneIdx ? null : { eraIdx, milestoneIdx }
    )
  }

  return (
    <div className="timeline-layout">
      <div className="section-header">
        <div className="section-label">Career Timeline</div>
        <h2 className="section-title">20 years, four eras</h2>
        <p className="section-subtitle">Click a milestone to expand its story.</p>
      </div>

      <div className="timeline-scroll-outer">
        <div className="timeline-scroll-inner">
          {timelineData.map((era, eraIdx) => {
            const color = ERA_COLORS[era.color_slot]
            const eraWidth = ((era.end - era.start) / TOTAL_YEARS) * 100
            const eraLeft = ((era.start - MIN_YEAR) / TOTAL_YEARS) * 100

            return (
              <div
                key={era.era}
                className="timeline-era-column"
                style={{ left: `${eraLeft}%`, width: `${eraWidth}%` }}
              >
                <div className="timeline-era-bar" style={{ background: color + '22', borderColor: color }}>
                  <span className="timeline-era-name" style={{ color }}>{era.org}</span>
                  <span className="timeline-era-role">{era.role}</span>
                  <span className="timeline-era-dates">{era.start} to {era.end}</span>
                </div>

                <div className="timeline-track">
                  <div className="timeline-track-line" style={{ background: color + '44' }} />
                  {era.milestones.map((m, mIdx) => {
                    const posLeft = ((m.year - era.start) / Math.max(era.end - era.start, 1)) * 100
                    const isActive = selected?.eraIdx === eraIdx && selected?.milestoneIdx === mIdx
                    return (
                      <button
                        key={mIdx}
                        className={`timeline-dot${isActive ? ' timeline-dot-active' : ''}`}
                        style={{
                          left: `${posLeft}%`,
                          background: isActive ? color : color + '55',
                          borderColor: color,
                        }}
                        onClick={() => handleDot(eraIdx, mIdx)}
                        title={m.title}
                      >
                        <span className="timeline-dot-icon">{TYPE_ICONS[m.type] ?? '•'}</span>
                      </button>
                    )
                  })}
                </div>

                <div className="timeline-year-labels">
                  {[era.start, era.end].map(yr => (
                    <span
                      key={yr}
                      className="timeline-year-label"
                      style={{ left: yr === era.start ? '0' : '100%' }}
                    >
                      {yr}
                    </span>
                  ))}
                </div>
              </div>
            )
          })}
        </div>
      </div>

      {selectedMilestone && selected !== null && (
        <div className="timeline-detail-card" style={{ borderLeftColor: ERA_COLORS[timelineData[selected.eraIdx].color_slot] }}>
          <div className="timeline-detail-header">
            <span className="timeline-detail-icon">{TYPE_ICONS[selectedMilestone.type] ?? '•'}</span>
            <div>
              <div className="timeline-detail-title">{selectedMilestone.title}</div>
              <div className="timeline-detail-meta">
                <span className="timeline-detail-year">{selectedMilestone.year}</span>
                <span className="timeline-detail-type">{selectedMilestone.type}</span>
                <span className="timeline-detail-era" style={{ color: ERA_COLORS[timelineData[selected.eraIdx].color_slot] }}>
                  {timelineData[selected.eraIdx].era}
                </span>
              </div>
            </div>
            <button className="timeline-detail-close" onClick={() => setSelected(null)}>✕</button>
          </div>
          <p className="timeline-detail-body">{selectedMilestone.detail}</p>
        </div>
      )}
    </div>
  )
}
