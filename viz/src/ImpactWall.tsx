import { useState, useRef, useEffect } from 'react'
import impactData from './data/impact.json'

const ERA_COLORS: Record<string, string> = {
  All: '#3987e5',
  IBM: '#3987e5',
  Amazon: '#199e70',
  Philips: '#d95926',
  Exeter: '#c98500',
}

function ImpactCard({ item }: { item: typeof impactData[number] }) {
  const [open, setOpen] = useState(false)
  const detailRef = useRef<HTMLDivElement>(null)
  const color = ERA_COLORS[item.era] ?? '#3987e5'

  useEffect(() => {
    const el = detailRef.current
    if (!el) return
    if (open) {
      el.style.maxHeight = el.scrollHeight + 'px'
      el.style.opacity = '1'
    } else {
      el.style.maxHeight = '0'
      el.style.opacity = '0'
    }
  }, [open])

  return (
    <div
      className="impact-card"
      onClick={() => setOpen(o => !o)}
      role="button"
      tabIndex={0}
      onKeyDown={e => e.key === 'Enter' && setOpen(o => !o)}
    >
      <span className="impact-era-badge" style={{ background: color + '22', color }}>
        {item.era}
      </span>
      <div className="impact-stat" style={{ color }}>{item.stat}</div>
      <div className="impact-label">{item.label}</div>
      <div
        ref={detailRef}
        className="impact-detail-wrap"
      >
        <p className="impact-detail-text">{item.detail}</p>
      </div>
      <button className="impact-toggle" onClick={e => { e.stopPropagation(); setOpen(o => !o) }}>
        {open ? '↑ collapse' : '→ read more'}
      </button>
    </div>
  )
}

export function ImpactWallView() {
  return (
    <div className="impact-layout">
      <div className="section-header">
        <div className="section-label">Impact</div>
        <h2 className="section-title">Career by the numbers</h2>
        <p className="section-subtitle">Quantified outcomes across 20 years and four organizations.</p>
      </div>
      <div className="impact-grid">
        {impactData.map((item, i) => (
          <ImpactCard key={i} item={item} />
        ))}
      </div>
    </div>
  )
}
