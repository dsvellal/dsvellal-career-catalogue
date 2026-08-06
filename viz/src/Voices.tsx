import { useState, useEffect, useRef, useCallback, useMemo } from 'react'
import voicesData from './data/voices.json'

interface Voice {
  quote: string
  company: string
  type: string
  date?: string
  issuer: string
  evidence_file?: string
}

const TYPE_COLORS: Record<string, string> = {
  recognition:     '#3987e5',
  recommendation:  '#199e70',
  certification:   '#c98500',
}

const TYPE_BG: Record<string, string> = {
  recognition:    'rgba(57,135,229,0.10)',
  recommendation: 'rgba(25,158,112,0.10)',
  certification:  'rgba(201,133,0,0.10)',
}

const ERA_COLORS: Record<string, string> = {
  Philips:  '#d95926',
  'Philips USA': '#c98500',
  'Philips India': '#e6a817',
  Amazon:   '#199e70',
  IBM:      '#3987e5',
}

const FILTERS = ['All', 'recognition', 'recommendation', 'certification'] as const

function eraColor(company: string) {
  for (const [k, v] of Object.entries(ERA_COLORS)) {
    if (company.toLowerCase().includes(k.toLowerCase())) return v
  }
  return '#898781'
}

function formatDate(d?: string) {
  if (!d) return ''
  const parts = d.split('-')
  if (parts.length === 3) {
    const date = new Date(d)
    if (!isNaN(date.getTime())) return date.toLocaleDateString('en-US', { month: 'short', year: 'numeric' })
  }
  if (parts.length === 2) return `${new Date(d + '-01').toLocaleDateString('en-US', { month: 'short', year: 'numeric' })}`
  return parts[0]
}

const voices: Voice[] = voicesData as Voice[]

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

// ── Voice Detail Card (Level 2) ──────────────────────────────────────────────
function VoiceDetailCard({ voice, onClose, onShowFull }: { voice: Voice; onClose: () => void; onShowFull: () => void }) {
  const color = eraColor(voice.company)
  const typeColor = TYPE_COLORS[voice.type] ?? '#898781'

  return (
    <div className="voices-detail-card" style={{ borderLeftColor: color }}>
      <div className="voices-detail-top">
        <span className="voices-detail-type" style={{ background: `${typeColor}18`, color: typeColor }}>
          {voice.type}
        </span>
        <span className="voices-detail-company" style={{ color }}>{voice.issuer || voice.company}</span>
        {voice.date && <span className="voices-detail-date">{formatDate(voice.date)}</span>}
        <button className="voices-detail-close" onClick={onClose}>✕</button>
      </div>
      <blockquote className="voices-detail-quote">&ldquo;{voice.quote}&rdquo;</blockquote>
      {voice.evidence_file && (
        <div className="voices-detail-evidence">
          <span className="voices-detail-evidence-ref">
            📄 {voice.evidence_file.split('/').pop()}
          </span>
          <button className="tl-detail-full-btn" onClick={onShowFull}>
            Explore the full story →
          </button>
        </div>
      )}
    </div>
  )
}

export function VoicesView() {
  const [filter, setFilter] = useState<string>('All')
  const [featured, setFeatured] = useState<Voice>(voices[0])
  const [fadeKey, setFadeKey] = useState(0)
  const [idle, setIdle] = useState(true)
  const [selectedIdx, setSelectedIdx] = useState<number | null>(null)
  const [artifactFile, setArtifactFile] = useState<string | null>(null)
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null)
  const idleTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null)

  const filtered = filter === 'All' ? voices : voices.filter(v => v.type === filter)

  const setFeaturedAnimated = useCallback((v: Voice) => {
    setFeatured(v)
    setFadeKey(k => k + 1)
  }, [])

  const resetIdleTimer = useCallback(() => {
    setIdle(false)
    if (idleTimerRef.current) clearTimeout(idleTimerRef.current)
    idleTimerRef.current = setTimeout(() => setIdle(true), 3000)
  }, [])

  useEffect(() => {
    if (!idle) {
      if (timerRef.current) clearInterval(timerRef.current)
      return
    }
    const pool = filter === 'All' ? voices : voices.filter(v => v.type === filter)
    if (pool.length === 0) return
    timerRef.current = setInterval(() => {
      setFeaturedAnimated(pool[Math.floor(Math.random() * pool.length)])
    }, 5000)
    return () => { if (timerRef.current) clearInterval(timerRef.current) }
  }, [idle, filter, setFeaturedAnimated])

  useEffect(() => {
    const pool = filter === 'All' ? voices : voices.filter(v => v.type === filter)
    if (pool.length > 0) setFeaturedAnimated(pool[0])
  }, [filter, setFeaturedAnimated])

  const handleCardClick = (v: Voice, idx: number) => {
    setFeaturedAnimated(v)
    setSelectedIdx(selectedIdx === idx ? null : idx)
    resetIdleTimer()
  }

  const typeColor = (t: string) => TYPE_COLORS[t] ?? '#898781'
  const typeBg = (t: string) => TYPE_BG[t] ?? 'rgba(137,135,129,0.1)'

  const availableFilters = FILTERS.filter(f => {
    if (f === 'All') return true
    return voices.some(v => v.type === f)
  })

  return (
    <div className="voices-view">
      <div className="section-header">
        <div className="section-label">Voices</div>
        <h2 className="section-title">What others say</h2>
        <p className="section-subtitle">
          Recognition, recommendations, and certifications across a 20-year career. {voices.length} voices.
          Click any card to expand. Items with evidence can be explored in full depth.
        </p>
      </div>

      {/* Featured quote */}
      <div className="voices-featured-wrap">
        <div
          className="voices-featured-card"
          key={fadeKey}
          onMouseEnter={() => { setIdle(false) }}
          onMouseLeave={() => setIdle(true)}
        >
          <div className="voices-featured-quote">
            &ldquo;{featured.quote}&rdquo;
          </div>
          <div className="voices-featured-meta">
            <span
              className="voices-era-pill"
              style={{ background: `${eraColor(featured.company)}22`, color: eraColor(featured.company), borderColor: `${eraColor(featured.company)}44` }}
            >
              {featured.issuer || featured.company}
            </span>
            <span
              className="voices-type-badge"
              style={{ background: typeBg(featured.type), color: typeColor(featured.type), borderColor: `${typeColor(featured.type)}44` }}
            >
              {featured.type}
            </span>
            {featured.date && (
              <span className="voices-date">{formatDate(featured.date)}</span>
            )}
            {featured.evidence_file && (
              <button
                className="tl-detail-full-btn"
                style={{ marginLeft: 'auto' }}
                onClick={() => setArtifactFile(featured.evidence_file!)}
              >
                Explore the full story →
              </button>
            )}
          </div>
        </div>
      </div>

      {/* Filter pills + grid */}
      <div className="voices-grid-section">
        <div className="voices-filter-row">
          {availableFilters.map(f => (
            <button
              key={f}
              className={`voices-filter-pill ${filter === f ? 'active' : ''}`}
              style={filter === f && f !== 'All' ? { borderColor: typeColor(f), color: typeColor(f) } : undefined}
              onClick={() => { setFilter(f); resetIdleTimer(); setSelectedIdx(null) }}
            >
              {f === 'All' ? 'All' : f.charAt(0).toUpperCase() + f.slice(1)}
              <span className="voices-filter-count">
                {f === 'All' ? voices.length : voices.filter(v => v.type === f).length}
              </span>
            </button>
          ))}
        </div>

        <div className="voices-grid">
          {filtered.map((v, i) => {
            const isActive = v === featured
            const isExpanded = selectedIdx === i
            return (
              <div key={i} className="voices-card-wrap">
                <div
                  className={`voices-card ${isActive ? 'active' : ''}`}
                  style={{ '--type-color': typeColor(v.type), '--type-bg': typeBg(v.type) } as React.CSSProperties}
                  onClick={() => handleCardClick(v, i)}
                >
                  <div className="voices-card-quote">{v.quote}</div>
                  <div className="voices-card-footer">
                    <span className="voices-card-company" style={{ color: eraColor(v.company) }}>
                      {v.company.length > 22 ? v.company.slice(0, 22) + '…' : v.company}
                    </span>
                    <span className="voices-card-type" style={{ background: typeBg(v.type), color: typeColor(v.type) }}>
                      {v.type}
                    </span>
                    {v.evidence_file && <span className="voices-card-evidence-dot">●</span>}
                  </div>
                </div>
                {isExpanded && (
                  <VoiceDetailCard
                    voice={v}
                    onClose={() => setSelectedIdx(null)}
                    onShowFull={() => v.evidence_file && setArtifactFile(v.evidence_file)}
                  />
                )}
              </div>
            )
          })}
        </div>
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
