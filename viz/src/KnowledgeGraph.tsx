import { useState, useRef, useEffect, useCallback, useMemo } from 'react'
import * as d3 from 'd3'
import graphData from './data/graph.json'

// ── Types ────────────────────────────────────────────────────────────────────

type NodeType = 'skill' | 'project' | 'organization' | 'achievement' | 'person'

interface ForceNode {
  id: string
  type: NodeType
  name: string
  degree: number
  properties: Record<string, unknown>
}

interface ForceEdge {
  source: string
  target: string
  type: string
  weight?: number
}

interface OrgNode {
  id: string
  name: string
  type: string
}

interface OrgEdge {
  source: string
  target: string
}

interface HeatmapData {
  skills: string[]
  counts: Record<string, number>
  pairs: Record<string, number>
}

interface RadialProject {
  id: string
  name: string
  year: number
  date: string
  org: string
  description: string
}

interface EgoNeighbor {
  id: string
  name: string
  type: string
  edge: string
}

interface EgoNode {
  id: string
  name: string
  type: string
  neighbors: EgoNeighbor[]
}

type SubView = 'force' | 'org' | 'heatmap' | 'radial' | 'ego'

// ── Color constants ───────────────────────────────────────────────────────────

const NODE_COLORS: Record<string, string> = {
  skill: '#3987e5',
  project: '#d95926',
  organization: '#c98500',
  achievement: '#199e70',
  person: '#d55181',
}

const EDGE_COLORS: Record<string, string> = {
  USED_SKILL: 'rgba(57,135,229,0.25)',
  AT_ORG: 'rgba(201,133,0,0.25)',
  RECOGNIZED_FOR: 'rgba(25,158,112,0.25)',
}

const ORG_ERA_COLORS: Record<string, string> = {
  IBM: '#3987e5',
  Exeter: '#d95926',
  Amazon: '#199e70',
  Philips: '#c98500',
  Other: '#9085e9',
}

// ── Tooltip helper ────────────────────────────────────────────────────────────

function useTooltip() {
  const ref = useRef<HTMLDivElement>(null)

  const show = useCallback((html: string, x: number, y: number) => {
    const el = ref.current
    if (!el) return
    el.innerHTML = html
    el.classList.add('visible')
    const vw = window.innerWidth
    const vh = window.innerHeight
    let left = x + 14
    let top = y - 10
    el.style.opacity = '0'
    el.style.left = `${left}px`
    el.style.top = `${top}px`
    requestAnimationFrame(() => {
      const rect = el.getBoundingClientRect()
      if (left + rect.width > vw - 8) left = x - rect.width - 14
      if (top + rect.height > vh - 8) top = vh - rect.height - 8
      el.style.left = `${left}px`
      el.style.top = `${top}px`
      el.style.opacity = ''
    })
  }, [])

  const hide = useCallback(() => {
    const el = ref.current
    if (el) el.classList.remove('visible')
  }, [])

  return { ref, show, hide }
}

// ── Sub-view 1: Force Graph ───────────────────────────────────────────────────

type NodeFilter = 'all' | 'skill' | 'project' | 'achievement' | 'organization'

interface SimNode extends d3.SimulationNodeDatum {
  id: string
  type: NodeType
  name: string
  degree: number
}

interface SimLink extends d3.SimulationLinkDatum<SimNode> {
  type: string
}

function ForceGraphView() {
  const svgRef = useRef<SVGSVGElement>(null)
  const tooltip = useTooltip()
  const [filter, setFilter] = useState<NodeFilter>('all')

  const rawNodes = useMemo(() => graphData.force.nodes as ForceNode[], [])
  const rawEdges = useMemo(() => graphData.force.edges as ForceEdge[], [])

  useEffect(() => {
    const svg = d3.select(svgRef.current!)
    svg.selectAll('*').remove()

    const el = svgRef.current!
    const W = el.clientWidth || 900
    const H = el.clientHeight || 560

    // Filter nodes
    const visibleNodes: SimNode[] = rawNodes
      .filter(n => filter === 'all' || n.type === filter)
      .map(n => ({ ...n }))

    const nodeIds = new Set(visibleNodes.map(n => n.id))
    const visibleLinks: SimLink[] = rawEdges
      .filter(e => nodeIds.has(e.source) && nodeIds.has(e.target))
      .map(e => ({ source: e.source, target: e.target, type: e.type }))

    // Scales
    const maxDegree = d3.max(visibleNodes, n => n.degree) ?? 1
    const rScale = d3.scaleSqrt().domain([0, maxDegree]).range([4, 20])

    // Zoom layer
    const root = svg.append('g').attr('class', 'kg-zoom-root')

    svg.call(
      d3.zoom<SVGSVGElement, unknown>()
        .scaleExtent([0.2, 8])
        .on('zoom', e => root.attr('transform', e.transform))
    )

    // Simulation
    const sim = d3.forceSimulation<SimNode>(visibleNodes)
      .force('link', d3.forceLink<SimNode, SimLink>(visibleLinks)
        .id(d => d.id)
        .distance(60)
        .strength(0.4))
      .force('charge', d3.forceManyBody().strength(-80))
      .force('center', d3.forceCenter(W / 2, H / 2))
      .force('collide', d3.forceCollide<SimNode>(d => rScale(d.degree) + 2))

    // Links
    const linkSel = root.append('g')
      .selectAll<SVGLineElement, SimLink>('line')
      .data(visibleLinks)
      .join('line')
      .attr('stroke', d => EDGE_COLORS[d.type] ?? 'rgba(255,255,255,0.1)')
      .attr('stroke-width', 1)
      .attr('class', 'kg-link')

    // Nodes
    const nodeSel = root.append('g')
      .selectAll<SVGCircleElement, SimNode>('circle')
      .data(visibleNodes)
      .join('circle')
      .attr('r', d => rScale(d.degree))
      .attr('fill', d => NODE_COLORS[d.type] ?? '#888')
      .attr('stroke', 'rgba(0,0,0,0.3)')
      .attr('stroke-width', 1)
      .attr('class', 'kg-node')
      .style('cursor', 'pointer')

    // Drag
    nodeSel.call(
      d3.drag<SVGCircleElement, SimNode>()
        .on('start', (event, d) => {
          if (!event.active) sim.alphaTarget(0.3).restart()
          d.fx = d.x; d.fy = d.y
        })
        .on('drag', (event, d) => { d.fx = event.x; d.fy = event.y })
        .on('end', (event, d) => {
          if (!event.active) sim.alphaTarget(0)
          d.fx = null; d.fy = null
        })
    )

    // Hover
    nodeSel
      .on('mousemove', (event, d) => {
        tooltip.show(
          `<div class="tooltip-title">${d.name}</div>
           <div class="tooltip-row"><span class="tooltip-value">${d.type}</span></div>
           <div class="tooltip-row">Degree: <span class="tooltip-value">${d.degree}</span></div>`,
          event.clientX, event.clientY
        )
      })
      .on('mouseleave', () => tooltip.hide())

    // Click highlight
    let selected: string | null = null
    nodeSel.on('click', (_, d) => {
      if (selected === d.id) {
        selected = null
        nodeSel.attr('opacity', 1)
        linkSel.attr('opacity', 1)
        return
      }
      selected = d.id
      const neighborIds = new Set<string>([d.id])
      visibleLinks.forEach(l => {
        const s = typeof l.source === 'object' ? (l.source as SimNode).id : l.source as string
        const t = typeof l.target === 'object' ? (l.target as SimNode).id : l.target as string
        if (s === d.id) neighborIds.add(t)
        if (t === d.id) neighborIds.add(s)
      })
      nodeSel.attr('opacity', nd => neighborIds.has(nd.id) ? 1 : 0.1)
      linkSel.attr('opacity', l => {
        const s = typeof l.source === 'object' ? (l.source as SimNode).id : l.source as string
        const t = typeof l.target === 'object' ? (l.target as SimNode).id : l.target as string
        return neighborIds.has(s) && neighborIds.has(t) ? 0.8 : 0.05
      })
    })

    // Tick
    sim.on('tick', () => {
      linkSel
        .attr('x1', d => (d.source as SimNode).x ?? 0)
        .attr('y1', d => (d.source as SimNode).y ?? 0)
        .attr('x2', d => (d.target as SimNode).x ?? 0)
        .attr('y2', d => (d.target as SimNode).y ?? 0)
      nodeSel
        .attr('cx', d => d.x ?? 0)
        .attr('cy', d => d.y ?? 0)
    })

    return () => { sim.stop() }
  }, [filter, rawNodes, rawEdges, tooltip])

  const filters: { key: NodeFilter; label: string }[] = [
    { key: 'all', label: 'All' },
    { key: 'skill', label: 'Skills' },
    { key: 'project', label: 'Projects' },
    { key: 'achievement', label: 'Achievements' },
    { key: 'organization', label: 'Orgs' },
  ]

  return (
    <div className="kg-subview">
      <div className="kg-toolbar">
        <div className="kg-filter-row">
          {filters.map(f => (
            <button
              key={f.key}
              className={`kg-filter-btn${filter === f.key ? ' active' : ''}`}
              onClick={() => setFilter(f.key)}
            >
              {f.label}
            </button>
          ))}
        </div>
        <div className="kg-legend">
          {Object.entries(NODE_COLORS).map(([type, color]) => (
            <span key={type} className="kg-legend-item">
              <span className="kg-legend-dot" style={{ background: color }} />
              {type}
            </span>
          ))}
        </div>
      </div>
      <div className="kg-svg-wrap">
        <svg ref={svgRef} className="kg-svg" />
      </div>
      <div ref={tooltip.ref} className="viz-tooltip" />
    </div>
  )
}

// ── Sub-view 2: Org Subgraph ──────────────────────────────────────────────────

type OrgKey = 'IBM' | 'Exeter' | 'Amazon' | 'Philips'

interface OrgSimNode extends d3.SimulationNodeDatum {
  id: string
  name: string
  type: string
}

function OrgSubgraphView() {
  const svgRef = useRef<SVGSVGElement>(null)
  const tooltip = useTooltip()
  const [org, setOrg] = useState<OrgKey>('IBM')

  useEffect(() => {
    const svg = d3.select(svgRef.current!)
    svg.selectAll('*').remove()

    const el = svgRef.current!
    const W = el.clientWidth || 900
    const H = el.clientHeight || 560

    const data = (graphData.org_subgraphs as Record<string, { nodes: OrgNode[]; edges: OrgEdge[] }>)[org]
    if (!data) return

    const allNodes: OrgSimNode[] = data.nodes.map(n => ({ ...n }))
    const projects = allNodes.filter(n => n.type === 'project')
    const skills = allNodes.filter(n => n.type === 'skill')

    const nodeMap = new Map(allNodes.map(n => [n.id, n]))
    const edges = data.edges

    const root = svg.append('g').attr('class', 'kg-zoom-root')
    svg.call(
      d3.zoom<SVGSVGElement, unknown>()
        .scaleExtent([0.1, 8])
        .on('zoom', e => root.attr('transform', e.transform))
    )

    const sim = d3.forceSimulation<OrgSimNode>(allNodes)
      .force('link', d3.forceLink<OrgSimNode, { source: string; target: string }>(
        edges.map(e => ({ source: e.source, target: e.target }))
      ).id(d => d.id).distance(80).strength(0.5))
      .force('charge', d3.forceManyBody().strength(-60))
      .force('x', d3.forceX<OrgSimNode>(d =>
        d.type === 'project' ? W * 0.25 : W * 0.75
      ).strength(0.6))
      .force('y', d3.forceY(H / 2).strength(0.05))
      .force('collide', d3.forceCollide(14))

    const linkSel = root.append('g')
      .selectAll<SVGLineElement, { source: OrgSimNode; target: OrgSimNode }>('line')
      .data(edges)
      .join('line')
      .attr('stroke', 'rgba(255,255,255,0.12)')
      .attr('stroke-width', 1)
      .style('cursor', 'default')

    linkSel
      .on('mousemove', (event, d) => {
        const src = nodeMap.get(d.source)
        const tgt = nodeMap.get(d.target)
        if (src && tgt) {
          tooltip.show(
            `<div class="tooltip-title">${src.name}</div>
             <div class="tooltip-row" style="color:var(--ink-muted)">→ ${tgt.name}</div>`,
            event.clientX, event.clientY
          )
        }
      })
      .on('mouseleave', () => tooltip.hide())

    const nodeSel = root.append('g')
      .selectAll<SVGCircleElement, OrgSimNode>('circle')
      .data(allNodes)
      .join('circle')
      .attr('r', 7)
      .attr('fill', d => d.type === 'project' ? NODE_COLORS.project : NODE_COLORS.skill)
      .attr('stroke', 'rgba(0,0,0,0.3)')
      .attr('stroke-width', 1)
      .style('cursor', 'pointer')

    nodeSel
      .on('mousemove', (event, d) => {
        tooltip.show(
          `<div class="tooltip-title">${d.name}</div>
           <div class="tooltip-row"><span class="tooltip-value">${d.type}</span></div>`,
          event.clientX, event.clientY
        )
      })
      .on('mouseleave', () => tooltip.hide())

    sim.on('tick', () => {
      linkSel
        .attr('x1', d => (nodeMap.get((d as unknown as { source: string }).source) as OrgSimNode)?.x ?? 0)
        .attr('y1', d => (nodeMap.get((d as unknown as { source: string }).source) as OrgSimNode)?.y ?? 0)
        .attr('x2', d => (nodeMap.get((d as unknown as { target: string }).target) as OrgSimNode)?.x ?? 0)
        .attr('y2', d => (nodeMap.get((d as unknown as { target: string }).target) as OrgSimNode)?.y ?? 0)
      nodeSel
        .attr('cx', d => d.x ?? 0)
        .attr('cy', d => d.y ?? 0)
    })

    // Column labels
    svg.append('text')
      .attr('x', W * 0.25)
      .attr('y', 28)
      .attr('text-anchor', 'middle')
      .attr('fill', NODE_COLORS.project)
      .attr('font-size', 11)
      .attr('font-weight', 600)
      .attr('letter-spacing', '0.07em')
      .text(`PROJECTS (${projects.length})`)

    svg.append('text')
      .attr('x', W * 0.75)
      .attr('y', 28)
      .attr('text-anchor', 'middle')
      .attr('fill', NODE_COLORS.skill)
      .attr('font-size', 11)
      .attr('font-weight', 600)
      .attr('letter-spacing', '0.07em')
      .text(`SKILLS (${skills.length})`)

    return () => { sim.stop() }
  }, [org, tooltip])

  const orgs: OrgKey[] = ['IBM', 'Exeter', 'Amazon', 'Philips']
  const data = (graphData.org_subgraphs as Record<string, { nodes: OrgNode[]; edges: OrgEdge[] }>)[org]
  const projectCount = data?.nodes.filter(n => n.type === 'project').length ?? 0
  const skillCount = data?.nodes.filter(n => n.type === 'skill').length ?? 0

  return (
    <div className="kg-subview">
      <div className="kg-toolbar">
        <div className="kg-filter-row">
          {orgs.map(o => (
            <button
              key={o}
              className={`kg-filter-btn${org === o ? ' active' : ''}`}
              style={org === o ? { borderColor: ORG_ERA_COLORS[o], color: ORG_ERA_COLORS[o] } : {}}
              onClick={() => setOrg(o)}
            >
              {o}
            </button>
          ))}
        </div>
        <span className="kg-info-text">{projectCount} projects → {skillCount} skills</span>
      </div>
      <div className="kg-svg-wrap">
        <svg ref={svgRef} className="kg-svg" />
      </div>
      <div ref={tooltip.ref} className="viz-tooltip" />
    </div>
  )
}

// ── Sub-view 3: Skill Heatmap ─────────────────────────────────────────────────

function SkillHeatmapView() {
  const containerRef = useRef<HTMLDivElement>(null)
  const tooltip = useTooltip()
  const heatmap = graphData.heatmap as HeatmapData

  useEffect(() => {
    const el = containerRef.current!
    el.innerHTML = ''

    const skills = heatmap.skills
    const N = skills.length
    const margin = { top: 20, right: 20, bottom: 140, left: 140 }
    const containerW = el.clientWidth || 700
    const cellSize = Math.floor(Math.min((containerW - margin.left - margin.right) / N, 36))
    const gridW = cellSize * N
    const gridH = cellSize * N
    const W = gridW + margin.left + margin.right
    const H = gridH + margin.top + margin.bottom

    const svg = d3.select(el).append('svg')
      .attr('width', W)
      .attr('height', H)

    const g = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`)

    // Color scales
    const maxPair = d3.max(Object.values(heatmap.pairs)) ?? 1
    const maxCount = d3.max(Object.values(heatmap.counts)) ?? 1
    const pairColor = d3.scaleSequential(d3.interpolate('#0d1f3c', '#3987e5')).domain([0, maxPair])
    const diagColor = d3.scaleSequential(d3.interpolate('#1a1a19', '#c98500')).domain([0, maxCount])

    // Cells
    for (let row = 0; row < N; row++) {
      for (let col = 0; col < N; col++) {
        const sk1 = skills[row]
        const sk2 = skills[col]
        let value: number
        let isDiag = false

        if (row === col) {
          value = heatmap.counts[sk1] ?? 0
          isDiag = true
        } else {
          const key1 = `${sk1}|${sk2}`
          const key2 = `${sk2}|${sk1}`
          value = heatmap.pairs[key1] ?? heatmap.pairs[key2] ?? 0
        }

        const cellEl = g.append('rect')
          .attr('x', col * cellSize)
          .attr('y', row * cellSize)
          .attr('width', cellSize - 1)
          .attr('height', cellSize - 1)
          .attr('rx', 2)
          .attr('fill', isDiag ? diagColor(value) : pairColor(value))
          .style('cursor', 'pointer')

        cellEl
          .on('mousemove', (event) => {
            const text = row === col
              ? `<div class="tooltip-title">${sk1}</div><div class="tooltip-row">Used in <span class="tooltip-value">${value}</span> projects</div>`
              : `<div class="tooltip-title">${sk1} + ${sk2}</div><div class="tooltip-row">Co-occurrence: <span class="tooltip-value">${value}</span> projects</div>`
            tooltip.show(text, event.clientX, event.clientY)
          })
          .on('mouseleave', () => tooltip.hide())
      }
    }

    // X axis labels
    g.selectAll('.kg-hm-xlabel')
      .data(skills)
      .join('text')
      .attr('class', 'kg-hm-xlabel')
      .attr('x', (_, i) => i * cellSize + cellSize / 2)
      .attr('y', gridH + 10)
      .attr('text-anchor', 'end')
      .attr('dominant-baseline', 'middle')
      .attr('transform', (_, i) => `rotate(-45, ${i * cellSize + cellSize / 2}, ${gridH + 10})`)
      .attr('fill', 'var(--ink-muted)')
      .attr('font-size', Math.min(cellSize * 0.45, 11))
      .text(d => d)

    // Y axis labels
    g.selectAll('.kg-hm-ylabel')
      .data(skills)
      .join('text')
      .attr('class', 'kg-hm-ylabel')
      .attr('x', -8)
      .attr('y', (_, i) => i * cellSize + cellSize / 2)
      .attr('text-anchor', 'end')
      .attr('dominant-baseline', 'middle')
      .attr('fill', 'var(--ink-muted)')
      .attr('font-size', Math.min(cellSize * 0.45, 11))
      .text(d => d)

    // Legend ramp
    const legendW = 120
    const legendH = 10
    const lgX = gridW - legendW
    const lgY = gridH + 110

    const defs = svg.append('defs')
    const gradId = 'kg-hm-grad'
    const grad = defs.append('linearGradient').attr('id', gradId)
    grad.append('stop').attr('offset', '0%').attr('stop-color', '#0d1f3c')
    grad.append('stop').attr('offset', '100%').attr('stop-color', '#3987e5')

    const lg = g.append('g').attr('transform', `translate(${lgX},${lgY})`)
    lg.append('rect')
      .attr('width', legendW).attr('height', legendH)
      .attr('rx', 2)
      .attr('fill', `url(#${gradId})`)
    lg.append('text').attr('x', 0).attr('y', legendH + 12)
      .attr('fill', 'var(--ink-muted)').attr('font-size', 9).text('0')
    lg.append('text').attr('x', legendW).attr('y', legendH + 12)
      .attr('text-anchor', 'end')
      .attr('fill', 'var(--ink-muted)').attr('font-size', 9).text(`${maxPair}`)
    lg.append('text').attr('x', legendW / 2).attr('y', -4)
      .attr('text-anchor', 'middle')
      .attr('fill', 'var(--ink-muted)').attr('font-size', 9).text('co-occurrence')
  }, [heatmap, tooltip])

  return (
    <div className="kg-subview">
      <div className="kg-svg-wrap" style={{ overflowX: 'auto', height: 'auto', minHeight: 540 }}>
        <div ref={containerRef} style={{ minWidth: 500 }} />
      </div>
      <div ref={tooltip.ref} className="viz-tooltip" />
    </div>
  )
}

// ── Sub-view 4: Timeline Radial ───────────────────────────────────────────────

const ERA_RANGES: { org: string; start: number; end: number }[] = [
  { org: 'IBM', start: 2007, end: 2013 },
  { org: 'Exeter', start: 2013, end: 2016 },
  { org: 'Amazon', start: 2016, end: 2020 },
  { org: 'Philips', start: 2020, end: 2026 },
]

function TimelineRadialView() {
  const svgRef = useRef<SVGSVGElement>(null)
  const tooltip = useTooltip()
  const projects = useMemo(() => graphData.radial as RadialProject[], [])

  useEffect(() => {
    const svg = d3.select(svgRef.current!)
    svg.selectAll('*').remove()

    const el = svgRef.current!
    const W = el.clientWidth || 800
    const H = el.clientHeight || 560
    const cx = W / 2
    const cy = H / 2
    const outerR = Math.min(cx, cy) - 40
    const innerR = outerR * 0.3
    const dotR = outerR * 0.72

    const minYear = 2007
    const maxYear = 2026
    const totalYears = maxYear - minYear

    // Angle scale: 0 = top, clockwise
    const angleForYear = (year: number) => {
      const frac = (year - minYear) / totalYears
      return frac * 2 * Math.PI - Math.PI / 2
    }

    // Era arcs
    ERA_RANGES.forEach(era => {
      const startAngle = angleForYear(era.start)
      const endAngle = angleForYear(era.end)
      const arcR = outerR + 16
      const arcInner = outerR + 8

      const arcGen = d3.arc<{ startAngle: number; endAngle: number; innerRadius: number; outerRadius: number }>()
        .innerRadius(d => d.innerRadius)
        .outerRadius(d => d.outerRadius)
        .startAngle(d => d.startAngle)
        .endAngle(d => d.endAngle)

      const arcDatum = {
        startAngle: startAngle + Math.PI / 2,
        endAngle: endAngle + Math.PI / 2,
        innerRadius: arcInner,
        outerRadius: arcR,
      }

      svg.append('path')
        .attr('d', arcGen(arcDatum) as string)
        .attr('fill', ORG_ERA_COLORS[era.org] ?? '#888')
        .attr('opacity', 0.7)
        .attr('transform', `translate(${cx},${cy})`)
    })

    // Year rings + labels
    for (let y = minYear; y <= maxYear; y++) {
      const angle = angleForYear(y)
      const labelR = outerR + 30
      const lx = cx + Math.cos(angle) * labelR
      const ly = cy + Math.sin(angle) * labelR

      // tick
      const tickInner = outerR - 4
      const tx1 = cx + Math.cos(angle) * tickInner
      const ty1 = cy + Math.sin(angle) * tickInner
      const tx2 = cx + Math.cos(angle) * (outerR + 2)
      const ty2 = cy + Math.sin(angle) * (outerR + 2)
      svg.append('line')
        .attr('x1', tx1).attr('y1', ty1)
        .attr('x2', tx2).attr('y2', ty2)
        .attr('stroke', 'rgba(255,255,255,0.15)')
        .attr('stroke-width', 1)

      svg.append('text')
        .attr('x', lx).attr('y', ly)
        .attr('text-anchor', 'middle')
        .attr('dominant-baseline', 'middle')
        .attr('fill', 'var(--ink-faint)')
        .attr('font-size', 9)
        .text(y)
    }

    // Outer circle ring
    svg.append('circle')
      .attr('cx', cx).attr('cy', cy)
      .attr('r', outerR)
      .attr('fill', 'none')
      .attr('stroke', 'rgba(255,255,255,0.08)')
      .attr('stroke-width', 1)

    // Inner circle
    svg.append('circle')
      .attr('cx', cx).attr('cy', cy)
      .attr('r', innerR)
      .attr('fill', 'var(--surface-2)')
      .attr('stroke', 'rgba(255,255,255,0.06)')
      .attr('stroke-width', 1)

    // Center text
    svg.append('text')
      .attr('x', cx).attr('y', cy - 10)
      .attr('text-anchor', 'middle')
      .attr('fill', 'var(--ink-primary)')
      .attr('font-size', 18)
      .attr('font-weight', 700)
      .text('913')
    svg.append('text')
      .attr('x', cx).attr('y', cy + 8)
      .attr('text-anchor', 'middle')
      .attr('fill', 'var(--ink-muted)')
      .attr('font-size', 9)
      .attr('letter-spacing', '0.06em')
      .text('ARTIFACTS')
    svg.append('text')
      .attr('x', cx).attr('y', cy + 22)
      .attr('text-anchor', 'middle')
      .attr('fill', 'var(--ink-muted)')
      .attr('font-size', 9)
      .attr('letter-spacing', '0.06em')
      .text('20 YEARS')

    // Project dots
    // Spread multiple dots at same year with small random angular offset
    const yearBuckets = new Map<number, RadialProject[]>()
    projects.forEach(p => {
      const yr = p.year || minYear
      if (!yearBuckets.has(yr)) yearBuckets.set(yr, [])
      yearBuckets.get(yr)!.push(p)
    })

    projects.forEach((p, idx) => {
      const yr = p.year || minYear
      const bucket = yearBuckets.get(yr) ?? [p]
      const posInBucket = bucket.indexOf(p)
      const spread = (bucket.length > 1) ? (posInBucket / (bucket.length - 1) - 0.5) * 0.15 : 0
      const baseAngle = angleForYear(yr)
      const angle = baseAngle + spread
      const jitter = ((idx * 17 + 3) % 7) - 3 // deterministic small radial jitter
      const r = dotR + jitter

      const dx = cx + Math.cos(angle) * r
      const dy = cy + Math.sin(angle) * r
      const orgColor = ORG_ERA_COLORS[p.org] ?? '#9085e9'

      svg.append('circle')
        .attr('cx', dx).attr('cy', dy)
        .attr('r', 5)
        .attr('fill', orgColor)
        .attr('stroke', 'rgba(0,0,0,0.4)')
        .attr('stroke-width', 1)
        .style('cursor', 'pointer')
        .on('mousemove', event => {
          tooltip.show(
            `<div class="tooltip-title">${p.name}</div>
             <div class="tooltip-row"><span class="tooltip-value">${p.org}</span> · ${p.year}</div>
             ${p.description ? `<div class="tooltip-row" style="color:var(--ink-muted);margin-top:4px;font-size:11px">${p.description.slice(0, 100)}${p.description.length > 100 ? '…' : ''}</div>` : ''}`,
            event.clientX, event.clientY
          )
        })
        .on('mouseleave', () => tooltip.hide())
    })

    // Era legend at bottom
    const legendItems = Object.entries(ORG_ERA_COLORS).filter(([k]) => k !== 'Other')
    const lgY = H - 18
    const lgStartX = cx - (legendItems.length * 80) / 2
    legendItems.forEach(([org, color], i) => {
      const lx = lgStartX + i * 80
      svg.append('rect')
        .attr('x', lx).attr('y', lgY - 6)
        .attr('width', 10).attr('height', 10)
        .attr('rx', 2)
        .attr('fill', color)
      svg.append('text')
        .attr('x', lx + 14).attr('y', lgY + 1)
        .attr('fill', 'var(--ink-muted)')
        .attr('font-size', 10)
        .attr('dominant-baseline', 'middle')
        .text(org)
    })
  }, [projects, tooltip])

  return (
    <div className="kg-subview">
      <div className="kg-svg-wrap">
        <svg ref={svgRef} className="kg-svg" />
      </div>
      <div ref={tooltip.ref} className="viz-tooltip" />
    </div>
  )
}

// ── Sub-view 5: Ego Explorer ──────────────────────────────────────────────────

interface EgoSimNode extends d3.SimulationNodeDatum {
  id: string
  name: string
  type: string
  isCenter: boolean
  degree?: number
  edgeLabel?: string
}

const MENTORING_ID = 'skill_2d5da182-de4a-5adc-becd-79e99003def6'

function EgoExplorerView() {
  const svgRef = useRef<SVGSVGElement>(null)
  const tooltip = useTooltip()
  const egoIndex = useMemo(() => graphData.ego_index as Record<string, EgoNode>, [])

  const [query, setQuery] = useState('')
  const [suggestions, setSuggestions] = useState<EgoNode[]>([])
  const [selectedId, setSelectedId] = useState<string>(MENTORING_ID)
  const [breadcrumb, setBreadcrumb] = useState<{ id: string; name: string }[]>([
    { id: MENTORING_ID, name: 'Mentoring' },
  ])

  const navigateTo = useCallback((id: string, name: string) => {
    setSelectedId(id)
    setBreadcrumb(prev => {
      const existing = prev.findIndex(b => b.id === id)
      if (existing >= 0) return prev.slice(0, existing + 1)
      return [...prev, { id, name }]
    })
    setQuery('')
    setSuggestions([])
  }, [])

  useEffect(() => {
    if (!query.trim()) { setSuggestions([]); return }
    const q = query.toLowerCase()
    const results = Object.values(egoIndex)
      .filter(n => n.name.toLowerCase().includes(q))
      .slice(0, 8)
    setSuggestions(results)
  }, [query, egoIndex])

  useEffect(() => {
    const svg = d3.select(svgRef.current!)
    svg.selectAll('*').remove()

    const el = svgRef.current!
    const W = el.clientWidth || 900
    const H = el.clientHeight || 500

    const center = egoIndex[selectedId]
    if (!center) return

    const forceNodes: EgoSimNode[] = [
      { id: center.id, name: center.name, type: center.type, isCenter: true },
      ...center.neighbors.map(nb => ({
        id: nb.id,
        name: nb.name,
        type: nb.type,
        isCenter: false,
        edgeLabel: nb.edge,
        degree: (graphData.force.nodes as ForceNode[]).find(n => n.id === nb.id)?.degree ?? 10,
      })),
    ]

    const forceLinks = center.neighbors.map(nb => ({
      source: center.id,
      target: nb.id,
      label: nb.edge,
    }))

    const nodeMap = new Map(forceNodes.map(n => [n.id, n]))
    const degreeScale = d3.scaleSqrt()
      .domain([0, d3.max(forceNodes, n => n.degree ?? 10) ?? 10])
      .range([5, 16])

    const root = svg.append('g').attr('class', 'kg-zoom-root')
    svg.call(
      d3.zoom<SVGSVGElement, unknown>()
        .scaleExtent([0.2, 8])
        .on('zoom', e => root.attr('transform', e.transform))
    )

    const sim = d3.forceSimulation<EgoSimNode>(forceNodes)
      .force('link', d3.forceLink<EgoSimNode, { source: string; target: string }>(forceLinks)
        .id(d => d.id).distance(100).strength(0.5))
      .force('charge', d3.forceManyBody().strength(-200))
      .force('center', d3.forceCenter(W / 2, H / 2))
      .force('collide', d3.forceCollide<EgoSimNode>(d => (d.isCenter ? 40 : degreeScale(d.degree ?? 10)) + 4))

    // Fix center
    forceNodes[0].fx = W / 2
    forceNodes[0].fy = H / 2

    // Links
    const linkGroup = root.append('g')
    const linkSel = linkGroup.selectAll<SVGLineElement, typeof forceLinks[0]>('line')
      .data(forceLinks)
      .join('line')
      .attr('stroke', 'rgba(255,255,255,0.15)')
      .attr('stroke-width', 1.5)

    // Edge labels
    const edgeLabelSel = linkGroup.selectAll<SVGTextElement, typeof forceLinks[0]>('text')
      .data(forceLinks)
      .join('text')
      .attr('fill', 'var(--ink-faint)')
      .attr('font-size', 8)
      .attr('text-anchor', 'middle')
      .attr('dominant-baseline', 'middle')
      .attr('pointer-events', 'none')
      .text(d => d.label.replace('_', ' '))

    // Node circles
    const nodeSel = root.append('g')
      .selectAll<SVGCircleElement, EgoSimNode>('circle')
      .data(forceNodes)
      .join('circle')
      .attr('r', d => d.isCenter ? 26 : degreeScale(d.degree ?? 10))
      .attr('fill', d => d.isCenter
        ? (NODE_COLORS[d.type as NodeType] ?? '#888')
        : (NODE_COLORS[d.type as NodeType] ?? '#888'))
      .attr('stroke', d => d.isCenter ? 'rgba(255,255,255,0.4)' : 'rgba(0,0,0,0.3)')
      .attr('stroke-width', d => d.isCenter ? 2 : 1)
      .attr('opacity', d => d.isCenter ? 1 : 0.85)
      .style('cursor', d => d.isCenter ? 'default' : 'pointer')

    // Node labels
    const labelSel = root.append('g')
      .selectAll<SVGTextElement, EgoSimNode>('text')
      .data(forceNodes)
      .join('text')
      .attr('fill', d => d.isCenter ? 'var(--ink-primary)' : 'var(--ink-secondary)')
      .attr('font-size', d => d.isCenter ? 11 : 9)
      .attr('font-weight', d => d.isCenter ? 600 : 400)
      .attr('text-anchor', 'middle')
      .attr('dominant-baseline', d => d.isCenter ? 'middle' : 'auto')
      .attr('pointer-events', 'none')
      .text(d => d.name.length > 20 ? d.name.slice(0, 18) + '…' : d.name)

    // Hover + click on neighbor nodes
    nodeSel
      .on('mousemove', (event, d) => {
        if (d.isCenter) return
        const neighborData = egoIndex[d.id]
        tooltip.show(
          `<div class="tooltip-title">${d.name}</div>
           <div class="tooltip-row"><span class="tooltip-value">${d.type}</span></div>
           ${neighborData ? `<div class="tooltip-row" style="color:var(--ink-muted)">${neighborData.neighbors.length} connections</div>` : ''}
           <div class="tooltip-row" style="color:var(--ink-faint);font-size:10px">Click to explore</div>`,
          event.clientX, event.clientY
        )
      })
      .on('mouseleave', () => tooltip.hide())
      .on('click', (_, d) => {
        if (d.isCenter || !egoIndex[d.id]) return
        tooltip.hide()
        navigateTo(d.id, d.name)
      })

    sim.on('tick', () => {
      linkSel
        .attr('x1', d => (nodeMap.get((d as unknown as { source: string }).source) as EgoSimNode)?.x ?? 0)
        .attr('y1', d => (nodeMap.get((d as unknown as { source: string }).source) as EgoSimNode)?.y ?? 0)
        .attr('x2', d => (nodeMap.get((d as unknown as { target: string }).target) as EgoSimNode)?.x ?? 0)
        .attr('y2', d => (nodeMap.get((d as unknown as { target: string }).target) as EgoSimNode)?.y ?? 0)

      edgeLabelSel
        .attr('x', d => {
          const src = nodeMap.get((d as unknown as { source: string }).source) as EgoSimNode
          const tgt = nodeMap.get((d as unknown as { target: string }).target) as EgoSimNode
          return ((src?.x ?? 0) + (tgt?.x ?? 0)) / 2
        })
        .attr('y', d => {
          const src = nodeMap.get((d as unknown as { source: string }).source) as EgoSimNode
          const tgt = nodeMap.get((d as unknown as { target: string }).target) as EgoSimNode
          return ((src?.y ?? 0) + (tgt?.y ?? 0)) / 2
        })

      nodeSel
        .attr('cx', d => d.x ?? 0)
        .attr('cy', d => d.y ?? 0)

      labelSel
        .attr('x', d => d.x ?? 0)
        .attr('y', d => d.isCenter ? (d.y ?? 0) : (d.y ?? 0) + degreeScale(d.degree ?? 10) + 10)
    })

    return () => { sim.stop() }
  }, [selectedId, egoIndex, tooltip, navigateTo])

  const currentNode = egoIndex[selectedId]

  return (
    <div className="kg-subview">
      <div className="kg-toolbar" style={{ flexDirection: 'column', alignItems: 'flex-start', gap: 10 }}>
        {/* Breadcrumb */}
        <div className="kg-breadcrumb">
          {breadcrumb.map((b, i) => (
            <span key={b.id}>
              {i > 0 && <span className="kg-breadcrumb-sep">→</span>}
              <button
                className={`kg-breadcrumb-btn${i === breadcrumb.length - 1 ? ' active' : ''}`}
                onClick={() => navigateTo(b.id, b.name)}
              >
                {b.name}
              </button>
            </span>
          ))}
        </div>

        {/* Search */}
        <div className="kg-ego-search-wrap">
          <input
            className="kg-ego-search"
            placeholder="Search nodes (e.g. Agile, Amazon, DXR…)"
            value={query}
            onChange={e => setQuery(e.target.value)}
          />
          {suggestions.length > 0 && (
            <div className="kg-ego-suggestions">
              {suggestions.map(s => (
                <button
                  key={s.id}
                  className="kg-ego-suggestion-item"
                  onClick={() => navigateTo(s.id, s.name)}
                >
                  <span className="kg-ego-sug-dot" style={{ background: NODE_COLORS[s.type as NodeType] ?? '#888' }} />
                  <span className="kg-ego-sug-name">{s.name}</span>
                  <span className="kg-ego-sug-type">{s.type}</span>
                </button>
              ))}
            </div>
          )}
        </div>

        {currentNode && (
          <div className="kg-ego-meta">
            <span className="kg-ego-meta-dot" style={{ background: NODE_COLORS[currentNode.type as NodeType] ?? '#888' }} />
            <strong>{currentNode.name}</strong>
            <span className="kg-ego-meta-type">{currentNode.type}</span>
            <span className="kg-ego-meta-count">{currentNode.neighbors.length} direct connections</span>
          </div>
        )}
      </div>

      <div className="kg-svg-wrap">
        <svg ref={svgRef} className="kg-svg" />
      </div>
      <div ref={tooltip.ref} className="viz-tooltip" />
    </div>
  )
}

// ── Main KnowledgeGraph Component ─────────────────────────────────────────────

const SUB_VIEWS: { key: SubView; label: string }[] = [
  { key: 'force', label: 'Force Graph' },
  { key: 'org', label: 'Org Subgraph' },
  { key: 'heatmap', label: 'Skill Heatmap' },
  { key: 'radial', label: 'Timeline Radial' },
  { key: 'ego', label: 'Ego Explorer' },
]

export function KnowledgeGraphView() {
  const [activeView, setActiveView] = useState<SubView>('force')

  return (
    <div className="kg-container">
      <div className="kg-header">
        <h2 className="kg-title">Knowledge Graph</h2>
        <p className="kg-subtitle">148 nodes · 1,619 edges · 20 years of career data</p>
      </div>

      <div className="kg-sub-tabs">
        {SUB_VIEWS.map(sv => (
          <button
            key={sv.key}
            className={`kg-sub-tab${activeView === sv.key ? ' active' : ''}`}
            onClick={() => setActiveView(sv.key)}
          >
            {sv.label}
          </button>
        ))}
      </div>

      <div className="kg-view">
        {activeView === 'force' && <ForceGraphView />}
        {activeView === 'org' && <OrgSubgraphView />}
        {activeView === 'heatmap' && <SkillHeatmapView />}
        {activeView === 'radial' && <TimelineRadialView />}
        {activeView === 'ego' && <EgoExplorerView />}
      </div>
    </div>
  )
}
