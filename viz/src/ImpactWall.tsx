import { useState, useRef, useEffect } from 'react'
import impactData from './data/impact.json'

const ERA_COLORS: Record<string, string> = {
  All: '#1a2233',
  IBM: '#2563a8',
  Amazon: '#0d7a52',
  Philips: '#b84c1a',
  Exeter: '#9a6b00',
  Independent: '#6b46b0',
}

const CATEGORY_LABELS: Record<string, string> = {
  professional: 'Professional',
  social: 'Social Impact',
}

function ImpactCard({ item }: { item: typeof impactData[number] }) {
  const [open, setOpen] = useState(false)
  const detailRef = useRef<HTMLDivElement>(null)
  const color = ERA_COLORS[item.era] ?? '#3987e5'
  const categoryLabel = CATEGORY_LABELS[(item as any).category] ?? 'Professional'
  const isSocial = (item as any).category === 'social'

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
      <div className="impact-badges">
        <span className="impact-category-badge" data-category={isSocial ? 'social' : 'professional'}>
          {categoryLabel}
        </span>
        <span className="impact-era-badge" style={{ background: color + '22', color }}>
          {item.era}
        </span>
      </div>
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
  const [filter, setFilter] = useState<'all' | 'professional' | 'social'>('all')

  const filtered = filter === 'all'
    ? impactData
    : impactData.filter(item => (item as any).category === filter)

  return (
    <div className="impact-layout">
      <div className="section-header">
        <div className="section-label">Impact</div>
        <h2 className="section-title">Career by the numbers</h2>
        <p className="section-subtitle">Quantified outcomes across 20 years, four organizations, and a lifelong commitment to community.</p>
      </div>
      <div className="impact-filters">
        <button
          className={`impact-filter-btn ${filter === 'all' ? 'active' : ''}`}
          onClick={() => setFilter('all')}
        >
          All ({impactData.length})
        </button>
        <button
          className={`impact-filter-btn ${filter === 'professional' ? 'active' : ''}`}
          onClick={() => setFilter('professional')}
        >
          Professional ({impactData.filter(i => (i as any).category === 'professional').length})
        </button>
        <button
          className={`impact-filter-btn ${filter === 'social' ? 'active' : ''}`}
          onClick={() => setFilter('social')}
        >
          Social Impact ({impactData.filter(i => (i as any).category === 'social').length})
        </button>
      </div>
      <div className="impact-grid">
        {filtered.map((item, i) => (
          <ImpactCard key={i} item={item} />
        ))}
      </div>
    </div>
  )
}
