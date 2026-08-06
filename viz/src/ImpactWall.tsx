import { useState, useRef, useEffect, useMemo } from 'react'
import impactData from './data/impact.json'

const ERA_COLORS: Record<string, string> = {
  All: '#1a2233',
  IBM: '#2563a8',
  Amazon: '#0d7a52',
  Philips: '#b84c1a',
  'Philips USA': '#c98500',
  'Philips India': '#e6a817',
  Exeter: '#9a6b00',
  Independent: '#6b46b0',
}

const CATEGORY_LABELS: Record<string, string> = {
  professional: 'Professional',
  social: 'Social Impact',
}

interface ImpactItem {
  stat: string
  label: string
  detail: string
  era: string
  category?: string
  evidence_file?: string
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
      .then(text => { setContent(text); setLoading(false) })
      .catch(() => { setContent(null); setLoading(false) })
  }, [evidenceFile])

  return (
    <div className="tl-artifact-overlay" onClick={onClose}>
      <div className="tl-artifact-panel" onClick={e => e.stopPropagation()}>
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

  html = html.replace(/(<li>.*?<\/li>\n?)+/g, match => `<ul>${match}</ul>`)
  html = html.replace(/(<blockquote>.*?<\/blockquote>\n?)+/g, match => `<div class="tl-blockquote-group">${match}</div>`)
  html = html.replace(/```[\s\S]*?```/g, match => {
    const code = match.replace(/^```\w*\n?/, '').replace(/\n?```$/, '')
    return `<pre><code>${code}</code></pre>`
  })
  html = html.replace(/^(?!<[hublipd]|<\/|$)(.+)$/gm, '<p>$1</p>')
  return html
}

// ── Impact Card with Drill-Down ─────────────────────────────────────────────
function ImpactCard({ item, isExpanded, onToggle, onShowFull }: {
  item: ImpactItem
  isExpanded: boolean
  onToggle: () => void
  onShowFull: () => void
}) {
  const detailRef = useRef<HTMLDivElement>(null)
  const color = ERA_COLORS[item.era] ?? '#3987e5'
  const categoryLabel = CATEGORY_LABELS[item.category ?? 'professional'] ?? 'Professional'
  const isSocial = item.category === 'social'

  useEffect(() => {
    const el = detailRef.current
    if (!el) return
    if (isExpanded) {
      el.style.maxHeight = el.scrollHeight + 'px'
      el.style.opacity = '1'
    } else {
      el.style.maxHeight = '0'
      el.style.opacity = '0'
    }
  }, [isExpanded])

  return (
    <div
      className={`impact-card${isExpanded ? ' impact-card-expanded' : ''}`}
      onClick={onToggle}
      role="button"
      tabIndex={0}
      onKeyDown={e => e.key === 'Enter' && onToggle()}
    >
      <div className="impact-badges">
        <span className="impact-category-badge" data-category={isSocial ? 'social' : 'professional'}>
          {categoryLabel}
        </span>
        <span className="impact-era-badge" style={{ background: color + '22', color }}>
          {item.era}
        </span>
        {item.evidence_file && <span className="impact-evidence-dot">●</span>}
      </div>
      <div className="impact-stat" style={{ color }}>{item.stat}</div>
      <div className="impact-label">{item.label}</div>
      <div ref={detailRef} className="impact-detail-wrap">
        <p className="impact-detail-text">{item.detail}</p>
        {item.evidence_file && (
          <div className="impact-detail-evidence">
            <span className="impact-detail-evidence-ref">
              📄 {item.evidence_file.split('/').pop()}
            </span>
            <button
              className="tl-detail-full-btn"
              onClick={e => { e.stopPropagation(); onShowFull() }}
            >
              Explore the full story →
            </button>
          </div>
        )}
      </div>
      <button className="impact-toggle" onClick={e => { e.stopPropagation(); onToggle() }}>
        {isExpanded ? '↑ collapse' : '→ read more'}
      </button>
    </div>
  )
}

export function ImpactWallView() {
  const [filter, setFilter] = useState<'all' | 'professional' | 'social'>('all')
  const [expandedIdx, setExpandedIdx] = useState<number | null>(null)
  const [artifactFile, setArtifactFile] = useState<string | null>(null)

  const filtered = filter === 'all'
    ? (impactData as ImpactItem[])
    : (impactData as ImpactItem[]).filter(item => item.category === filter)

  return (
    <div className="impact-layout">
      <div className="section-header">
        <div className="section-label">Impact</div>
        <h2 className="section-title">Career by the numbers</h2>
        <p className="section-subtitle">
          Quantified outcomes across 20 years, four organizations, and a lifelong commitment to community.
          Click any card to expand. Items with evidence can be explored in full depth.
        </p>
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
          Professional ({(impactData as ImpactItem[]).filter(i => i.category === 'professional').length})
        </button>
        <button
          className={`impact-filter-btn ${filter === 'social' ? 'active' : ''}`}
          onClick={() => setFilter('social')}
        >
          Social Impact ({(impactData as ImpactItem[]).filter(i => i.category === 'social').length})
        </button>
      </div>
      <div className="impact-grid">
        {filtered.map((item, i) => (
          <ImpactCard
            key={i}
            item={item}
            isExpanded={expandedIdx === i}
            onToggle={() => setExpandedIdx(expandedIdx === i ? null : i)}
            onShowFull={() => item.evidence_file && setArtifactFile(item.evidence_file)}
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
