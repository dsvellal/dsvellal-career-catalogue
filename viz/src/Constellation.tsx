import { useState, useEffect, useRef, useCallback } from 'react'
import * as d3 from 'd3'
import constellationData from './data/constellation.json'

// ── Types ──────────────────────────────────────────────────────────────────
interface BeTalentSkill {
  id: string
  name: string
  betalent_rank: number
  cluster: string
  label: string
  description: string
  ldc_strength: string | null
  ldc_development: string | null
  category: string | null
  overuse_risk: string | null
  used_skill_count: number
  recognized_for_count: number
  sample_achievements: string[]
}

interface OrbitSkill {
  id: string
  name: string
  used_skill_count: number
  category: string | null
  first_seen: string | null
  recognized_for_count: number
}

// ── Palette slots (categorical, validated dark) ────────────────────────────
const CLUSTER_COLORS: Record<string, string> = {
  'How I Interact': '#3987e5',
  'How I Deliver':  '#d95926',
  'How I Lead':     '#199e70',
  'How I Think':    '#c98500',
}

const CLUSTER_ORDER = ['How I Interact', 'How I Deliver', 'How I Lead', 'How I Think']

const CATEGORY_COLORS: Record<string, string> = {
  leadership:           '#199e70',
  engineering_practice: '#3987e5',
  soft_skill:           '#d95926',
  framework:            '#c98500',
  ai_technology:        '#9085e9',
  agile_methodology:    '#d55181',
  devops:               '#e66767',
  domain_expertise:     '#3987e5',
  other:                '#898781',
}

function categoryColor(cat: string | null): string {
  return CATEGORY_COLORS[cat ?? 'other'] ?? CATEGORY_COLORS.other
}

// ── Force layout node/link types ───────────────────────────────────────────
interface SimNode extends d3.SimulationNodeDatum {
  id: string
  name: string
  role: 'cluster-anchor' | 'core' | 'orbit'
  cluster?: string
  rank?: number
  size: number          // circle radius
  color: string
  data?: BeTalentSkill | OrbitSkill
}

interface SimLink extends d3.SimulationLinkDatum<SimNode> {
  source: SimNode | string
  target: SimNode | string
  type: 'cluster' | 'orbit'
}

// ── Main component ─────────────────────────────────────────────────────────
export function ConstellationView() {
  const svgRef = useRef<SVGSVGElement>(null)
  const [selected, setSelected] = useState<BeTalentSkill | OrbitSkill | null>(null)
  const [hoveredId, setHoveredId] = useState<string | null>(null)
  const [showTable, setShowTable] = useState(false)
  const [nodes, setNodes] = useState<SimNode[]>([])
  const [links, setLinks] = useState<SimLink[]>([])
  const [tooltip, setTooltip] = useState<{ x: number; y: number; content: string } | null>(null)
  const containerRef = useRef<HTMLDivElement>(null)

  const betalent: BeTalentSkill[] = constellationData.betalent_skills as BeTalentSkill[]
  const orbit: OrbitSkill[] = constellationData.orbit_skills as OrbitSkill[]

  // ── Build force layout ──────────────────────────────────────────────────
  const runLayout = useCallback(() => {
    const W = containerRef.current?.clientWidth ?? 720
    const H = containerRef.current?.clientHeight ?? 560

    const cx = W / 2
    const cy = H / 2

    // Cluster anchors at fixed positions around center
    const clusterAngles: Record<string, number> = {
      'How I Interact': -Math.PI / 4,      // top-right
      'How I Deliver':  Math.PI / 4 * 3,   // bottom-left — was Math.PI * 3/4
      'How I Lead':     Math.PI / 4 * 5,   // bottom-right — was -Math.PI * 3/4
      'How I Think':    Math.PI * 5 / 4,   // top-left
    }
    // Reassign for better layout: TL, TR, BL, BR
    const angles = [
      -Math.PI * 3 / 4,  // TL — How I Interact
       -Math.PI / 4,      // TR — How I Deliver
        Math.PI * 3 / 4,  // BL — How I Lead
        Math.PI / 4,       // BR — How I Think
    ]
    const CLUSTER_R = Math.min(W, H) * 0.28

    const simNodes: SimNode[] = []
    const simLinks: SimLink[] = []

    // Cluster anchors
    CLUSTER_ORDER.forEach((cluster, i) => {
      const angle = angles[i]
      simNodes.push({
        id: `cluster-${cluster}`,
        name: cluster,
        role: 'cluster-anchor',
        cluster,
        size: 0,
        color: CLUSTER_COLORS[cluster],
        x: cx + CLUSTER_R * Math.cos(angle),
        y: cy + CLUSTER_R * Math.sin(angle),
        fx: cx + CLUSTER_R * Math.cos(angle),
        fy: cy + CLUSTER_R * Math.sin(angle),
      })
    })

    // Core BeTalent skills
    const maxCount = Math.max(...betalent.map(s => s.used_skill_count))
    betalent.forEach(skill => {
      const baseR = 14 + (skill.used_skill_count / maxCount) * 12
      simNodes.push({
        id: skill.id,
        name: skill.name,
        role: 'core',
        cluster: skill.cluster,
        rank: skill.betalent_rank,
        size: baseR,
        color: CLUSTER_COLORS[skill.cluster] ?? '#898781',
        data: skill,
      })
      // Link to cluster anchor
      simLinks.push({
        source: `cluster-${skill.cluster}`,
        target: skill.id,
        type: 'cluster',
      })
    })

    // Orbit skills
    const maxOrbitCount = Math.max(...orbit.map(s => s.used_skill_count))
    orbit.forEach(skill => {
      const baseR = 6 + (skill.used_skill_count / maxOrbitCount) * 8
      simNodes.push({
        id: skill.id,
        name: skill.name,
        role: 'orbit',
        size: baseR,
        color: categoryColor(skill.category),
        data: skill,
      })
    })

    // Run simulation
    const simulation = d3.forceSimulation<SimNode>(simNodes)
      .force('link', d3.forceLink<SimNode, SimLink>(simLinks)
        .id(d => d.id)
        .distance(d => d.type === 'cluster' ? CLUSTER_R * 0.55 : 80)
        .strength(d => d.type === 'cluster' ? 0.7 : 0.2)
      )
      .force('charge', d3.forceManyBody().strength(d => d.role === 'cluster-anchor' ? 0 : -80))
      .force('collision', d3.forceCollide<SimNode>().radius(d => d.size + 14))
      .force('center', d3.forceCenter(cx, cy).strength(0.08))
      .force('radial', d3.forceRadial<SimNode>(
        d => {
          if (d.role === 'cluster-anchor') return 0
          if (d.role === 'core') return CLUSTER_R * 0.45
          return CLUSTER_R * 0.95 + Math.random() * 30
        },
        cx, cy
      ).strength(d => d.role === 'orbit' ? 0.15 : 0.08))
      .alphaDecay(0.03)
      .stop()

    for (let i = 0; i < 300; i++) simulation.tick()

    // Clamp to bounds
    simNodes.forEach(n => {
      const r = n.size + 2
      n.x = Math.max(r, Math.min(W - r, n.x ?? cx))
      n.y = Math.max(r, Math.min(H - r, n.y ?? cy))
    })

    setNodes([...simNodes])
    setLinks(simLinks.map(l => ({
      ...l,
      source: simNodes.find(n => n.id === (typeof l.source === 'string' ? l.source : (l.source as SimNode).id))!,
      target: simNodes.find(n => n.id === (typeof l.target === 'string' ? l.target : (l.target as SimNode).id))!,
    })))
  }, [betalent, orbit])

  useEffect(() => {
    const ro = new ResizeObserver(() => runLayout())
    if (containerRef.current) ro.observe(containerRef.current)
    runLayout()
    return () => ro.disconnect()
  }, [runLayout])

  // ── Interaction ─────────────────────────────────────────────────────────
  const handleNodeClick = (node: SimNode) => {
    if (node.role === 'cluster-anchor') return
    if (selected && (selected as BeTalentSkill | OrbitSkill).id === node.id) {
      setSelected(null)
    } else {
      setSelected((node.data as BeTalentSkill | OrbitSkill) ?? null)
    }
  }

  const handleNodeHover = (node: SimNode | null, e?: React.MouseEvent) => {
    setHoveredId(node?.id ?? null)
    if (!node || node.role === 'cluster-anchor') {
      setTooltip(null)
      return
    }
    if (e) {
      const d = node.data as (BeTalentSkill | OrbitSkill)
      const bt = d as BeTalentSkill
      const content = bt.betalent_rank
        ? `Rank ${bt.betalent_rank} · ${bt.cluster}`
        : `${d.used_skill_count} uses · ${d.recognized_for_count} recognitions`
      setTooltip({ x: e.clientX + 12, y: e.clientY - 8, content })
    }
  }

  // ── Highlight logic ─────────────────────────────────────────────────────
  const selectedId = selected ? (selected as BeTalentSkill | OrbitSkill).id : null
  const dim = (node: SimNode) => {
    if (!hoveredId && !selectedId) return false
    const activeId = hoveredId ?? selectedId
    if (node.id === activeId) return false
    if (node.role === 'cluster-anchor') return false
    // Show nodes in same cluster
    const activeNode = nodes.find(n => n.id === activeId)
    if (activeNode?.cluster && node.cluster === activeNode.cluster) return false
    return true
  }

  const highlightLink = (link: SimLink) => {
    const activeId = hoveredId ?? selectedId
    if (!activeId) return false
    const s = link.source as SimNode
    const t = link.target as SimNode
    return s.id === activeId || t.id === activeId
  }

  return (
    <div>
      {/* Section header */}
      <div className="section-header">
        <div className="section-label">Professional Identity</div>
        <h1 className="section-title">Who I Am as a Professional</h1>
        <p className="section-subtitle">
          Core strengths mapped from the BeTalent psychometric assessment — externally validated,
          not self-reported. Size encodes frequency across 20 years. Click any node to explore evidence.
        </p>
      </div>

      {/* KPI row */}
      <div className="kpi-row">
        {[
          { label: 'Assessed strengths', value: '12', sub: 'BeTalent ranked' },
          { label: 'Total recognitions', value: betalent.reduce((a, s) => a + s.recognized_for_count, 0).toString(), sub: 'External, peer, manager' },
          { label: 'Skills in evidence', value: (betalent.length + orbit.length).toString(), sub: 'Across 20 years' },
          { label: 'Top skill', value: 'Communication', sub: 'Rank 1 · How I Interact' },
        ].map(t => (
          <div className="kpi-tile" key={t.label}>
            <div className="kpi-label">{t.label}</div>
            <div className="kpi-value">{t.value}</div>
            <div className="kpi-sub">{t.sub}</div>
          </div>
        ))}
      </div>

      {/* Main layout */}
      <div className="constellation-layout">
        {/* Graph */}
        <div className="graph-panel">
          <div ref={containerRef} className="graph-canvas-wrap" style={{ minHeight: 560 }}>
            {nodes.length > 0 && (
              <svg
                ref={svgRef}
                className="graph-svg"
                style={{ minHeight: 560 }}
                onMouseLeave={() => handleNodeHover(null)}
              >
                {/* Defs */}
                <defs>
                  {CLUSTER_ORDER.map(cl => (
                    <radialGradient key={cl} id={`grd-${cl.replace(/\s/g,'-')}`} cx="50%" cy="50%" r="50%">
                      <stop offset="0%" stopColor={CLUSTER_COLORS[cl]} stopOpacity="0.18" />
                      <stop offset="100%" stopColor={CLUSTER_COLORS[cl]} stopOpacity="0" />
                    </radialGradient>
                  ))}
                </defs>

                {/* Cluster aura circles */}
                {nodes.filter(n => n.role === 'cluster-anchor').map(anchor => (
                  <circle
                    key={`aura-${anchor.id}`}
                    cx={anchor.x} cy={anchor.y}
                    r={120}
                    fill={`url(#grd-${anchor.cluster?.replace(/\s/g,'-')})`}
                    className="cluster-ring"
                    stroke={anchor.color}
                  />
                ))}

                {/* Links */}
                <g>
                  {links.map((link, i) => {
                    const s = link.source as SimNode
                    const t = link.target as SimNode
                    const hl = highlightLink(link)
                    const dm = !hl && (hoveredId != null || selectedId != null)
                    return (
                      <line
                        key={i}
                        x1={s.x} y1={s.y}
                        x2={t.x} y2={t.y}
                        className={`skill-link${hl ? ' highlighted' : ''}${dm ? ' dimmed' : ''}`}
                      />
                    )
                  })}
                </g>

                {/* Nodes */}
                <g>
                  {nodes.filter(n => n.role !== 'cluster-anchor').map(node => {
                    const isDimmed = dim(node)
                    const isSelected = selectedId === node.id
                    const isCore = node.role === 'core'
                    return (
                      <g
                        key={node.id}
                        className={`skill-node${isSelected ? ' selected' : ''}${isDimmed ? ' dimmed' : ''}`}
                        transform={`translate(${node.x},${node.y})`}
                        onClick={() => handleNodeClick(node)}
                        onMouseEnter={e => handleNodeHover(node, e)}
                        onMouseMove={e => handleNodeHover(node, e)}
                      >
                        {/* Surface ring — 2px ring for legibility */}
                        <circle
                          r={node.size + 2}
                          fill="var(--surface-1)"
                          className="node-ring"
                        />
                        <circle
                          r={node.size}
                          fill={node.color}
                          fillOpacity={isCore ? 0.9 : 0.6}
                          stroke={isSelected ? '#fff' : node.color}
                          strokeWidth={isSelected ? 2 : 0}
                          strokeOpacity={0.5}
                          className="node-circle"
                        />
                        {/* Rank badge for core skills */}
                        {isCore && (node as SimNode).rank && (
                          <text
                            textAnchor="middle"
                            dy="0.35em"
                            fontSize={node.size > 18 ? "9" : "8"}
                            fontWeight="700"
                            fill="#fff"
                            fillOpacity="0.9"
                            pointerEvents="none"
                          >
                            {(node as SimNode).rank}
                          </text>
                        )}
                      </g>
                    )
                  })}
                </g>

                {/* Node labels (shown for core + non-dimmed orbit) */}
                <g pointerEvents="none">
                  {nodes.filter(n => n.role !== 'cluster-anchor').map(node => {
                    const isDimmed = dim(node)
                    if (isDimmed && node.role === 'orbit') return null
                    const isCore = node.role === 'core'
                    const labelY = (node.y ?? 0) + node.size + 13
                    return (
                      <text
                        key={`lbl-${node.id}`}
                        x={node.x} y={labelY}
                        className={`node-label${isCore ? ' core' : ''}`}
                        textAnchor="middle"
                        opacity={isDimmed ? 0.25 : 1}
                      >
                        {node.name.length > 18 ? node.name.slice(0, 16) + '…' : node.name}
                      </text>
                    )
                  })}
                </g>

                {/* Cluster anchor labels */}
                <g pointerEvents="none">
                  {nodes.filter(n => n.role === 'cluster-anchor').map(anchor => (
                    <text
                      key={`cl-lbl-${anchor.id}`}
                      x={anchor.x}
                      y={(anchor.y ?? 0) - 14}
                      className="cluster-label"
                      textAnchor="middle"
                      fill={anchor.color}
                    >
                      {anchor.name.toUpperCase()}
                    </text>
                  ))}
                </g>
              </svg>
            )}
          </div>

          {/* Graph legend */}
          <div className="graph-legend">
            <div className="legend-item">
              <div className="legend-dot" style={{ background: '#3987e5' }} />
              <span>BeTalent core</span>
            </div>
            <div className="legend-item">
              <div className="legend-dot" style={{ background: '#898781' }} />
              <span>Supporting skill</span>
            </div>
            <div className="legend-item">
              <span>Size = frequency · Number = rank</span>
            </div>
          </div>
        </div>

        {/* Detail panel */}
        <div className="detail-panel">
          {!selected ? (
            <div className="detail-empty">
              <div className="detail-empty-icon">◎</div>
              <div className="detail-empty-text">
                Click any node to explore assessment data, evidence, and growth edges
              </div>
            </div>
          ) : (
            <SkillDetail skill={selected} />
          )}
        </div>
      </div>

      {/* Orbit chips — accessible table fallback */}
      <div className="orbit-chips">
        <div style={{ display: 'flex', alignItems: 'center', marginBottom: 12 }}>
          <div className="orbit-chips-title">All supporting skills ({orbit.length})</div>
          <button className="table-toggle" onClick={() => setShowTable(v => !v)}>
            {showTable ? 'Hide table' : 'Table view'}
          </button>
        </div>

        {showTable ? (
          <table className="data-table">
            <thead>
              <tr>
                <th>Skill</th>
                <th>Category</th>
                <th>Times used</th>
                <th>Recognitions</th>
                <th>First seen</th>
              </tr>
            </thead>
            <tbody>
              {orbit.map(s => (
                <tr key={s.id}>
                  <td>{s.name}</td>
                  <td>
                    <span className="table-swatch" style={{ background: categoryColor(s.category) }} />
                    {s.category ?? '—'}
                  </td>
                  <td style={{ fontVariantNumeric: 'tabular-nums' }}>{s.used_skill_count}</td>
                  <td style={{ fontVariantNumeric: 'tabular-nums' }}>{s.recognized_for_count}</td>
                  <td>{s.first_seen?.slice(0, 4) ?? '—'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <div className="chips-wrap">
            {orbit.map(s => (
              <div
                key={s.id}
                className={`skill-chip ${selected && (selected as OrbitSkill).id === s.id ? 'selected' : ''}`}
                onClick={() => setSelected(s)}
              >
                <span className="table-swatch" style={{ background: categoryColor(s.category) }} />
                {s.name}
                <span className="chip-count">{s.used_skill_count}</span>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Tooltip */}
      {tooltip && (
        <div
          className="viz-tooltip visible"
          style={{ left: tooltip.x, top: tooltip.y }}
        >
          {tooltip.content}
        </div>
      )}
    </div>
  )
}

// ── Skill detail panel ──────────────────────────────────────────────────────
function SkillDetail({ skill }: { skill: BeTalentSkill | OrbitSkill }) {
  const bt = skill as BeTalentSkill
  const isCore = bt.betalent_rank != null
  const clusterColor = isCore ? CLUSTER_COLORS[bt.cluster] : '#898781'

  return (
    <>
      {isCore && (
        <div
          className="detail-cluster-tag"
          style={{ background: `${clusterColor}22`, color: clusterColor, borderColor: `${clusterColor}44`, border: '1px solid' }}
        >
          {bt.cluster}
        </div>
      )}

      <div className="detail-skill-name">{skill.name}</div>

      {isCore && (
        <>
          {bt.label && <div className="detail-label-badge">"{bt.label}"</div>}
          <div className="betalent-rank">
            <div
              className="rank-badge"
              style={{ color: clusterColor, borderColor: `${clusterColor}66` }}
            >
              #{bt.betalent_rank}
            </div>
            <div className="rank-text">
              <strong>BeTalent Assessment</strong>
              Top {bt.betalent_rank} of all assessed strengths
            </div>
          </div>
        </>
      )}

      <div className="detail-stat-row">
        <div className="detail-stat">
          <div className="detail-stat-value">{skill.used_skill_count}</div>
          <div className="detail-stat-label">Times applied</div>
        </div>
        <div className="detail-stat">
          <div className="detail-stat-value" style={{ color: '#199e70' }}>{skill.recognized_for_count}</div>
          <div className="detail-stat-label">Recognitions</div>
        </div>
      </div>

      {isCore && bt.description && (
        <div className="detail-section">
          <div className="detail-section-title">Assessment description</div>
          <div className="detail-text">{bt.description}</div>
        </div>
      )}

      {isCore && bt.ldc_strength && (
        <>
          <hr className="detail-divider" />
          <div className="detail-section">
            <div className="detail-section-title">LDC strength</div>
            <div className="detail-text strength">{bt.ldc_strength}</div>
          </div>
        </>
      )}

      {isCore && bt.ldc_development && (
        <div className="detail-section">
          <div className="detail-section-title">Growth edge</div>
          <div className="detail-text development">{bt.ldc_development}</div>
        </div>
      )}

      {isCore && bt.overuse_risk && (
        <div className="overuse-section">
          <div className="overuse-label">Overuse risk</div>
          <div className="overuse-text">{bt.overuse_risk}</div>
        </div>
      )}

      {skill.sample_achievements.length > 0 && (
        <>
          <hr className="detail-divider" />
          <div className="detail-section">
            <div className="detail-section-title">Evidence ({skill.recognized_for_count} total)</div>
            <div className="evidence-list">
              {skill.sample_achievements.map((a, i) => (
                <div key={i} className="evidence-item">{a}</div>
              ))}
            </div>
          </div>
        </>
      )}
    </>
  )
}
