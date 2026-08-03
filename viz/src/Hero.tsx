import { useState, useEffect, useRef } from 'react'
import type { Tab } from './App'

const ERA_COLORS: Record<string, string> = {
  IBM: '#3987e5',
  Exeter: '#d95926',
  Amazon: '#199e70',
  Philips: '#c98500',
}

interface StatConfig {
  value: string
  label: string
  sublabel: string
  tab: Tab
  color: string
}

const STATS: StatConfig[] = [
  { value: '$3M+',   label: 'Career savings delivered', sublabel: 'See impact',    tab: 'impact',   color: '#199e70' },
  { value: '20 yrs', label: 'Industry depth',            sublabel: 'See timeline',  tab: 'timeline', color: '#3987e5' },
  { value: '7,000+', label: 'Engineers reached',         sublabel: 'Read voices',   tab: 'voices',   color: '#c98500' },
  { value: '220+',   label: 'Recognitions and quotes',   sublabel: 'Explore graph', tab: 'graph',    color: '#d55181' },
]

function useCountUp(target: number, duration = 1400, start = false) {
  const [count, setCount] = useState(0)
  const raf = useRef<number>(0)
  useEffect(() => {
    if (!start) return
    const t0 = performance.now()
    const tick = (now: number) => {
      const p = Math.min((now - t0) / duration, 1)
      const e = 1 - Math.pow(1 - p, 3)
      setCount(Math.floor(e * target))
      if (p < 1) raf.current = requestAnimationFrame(tick)
    }
    raf.current = requestAnimationFrame(tick)
    return () => cancelAnimationFrame(raf.current)
  }, [target, duration, start])
  return count
}

function StatTile({
  stat,
  animate,
  onNavigate,
}: {
  stat: StatConfig
  animate: boolean
  onNavigate: (tab: Tab) => void
}) {
  const [hovered, setHovered] = useState(false)
  const cleaned = stat.value.replace(/,/g, '')
  const numMatch = cleaned.match(/[\d.]+/)
  const num = numMatch ? parseFloat(numMatch[0]) : 0
  const prefix = cleaned.match(/^[^0-9]*/)?.[0] ?? ''
  const suffix = cleaned.match(/[^0-9.]+$/)?.[0] ?? ''
  const counted = useCountUp(num, 1400, animate)
  const display = num > 0 ? `${prefix}${counted.toLocaleString()}${suffix}` : stat.value

  return (
    <button
      className={`hero-stat-tile${hovered ? ' hero-stat-tile--hovered' : ''}`}
      style={{ '--tile-color': stat.color } as React.CSSProperties}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      onClick={() => onNavigate(stat.tab)}
      aria-label={`${stat.label}: ${stat.sublabel}`}
    >
      <div className="hero-stat-value">{display}</div>
      <div className="hero-stat-label">{stat.label}</div>
      <div className="hero-stat-sub">{stat.sublabel} &rarr;</div>
      <div className="hero-stat-shine" />
    </button>
  )
}

export function HeroView({ onNavigate }: { onNavigate: (tab: Tab) => void }) {
  const [visible, setVisible] = useState(false)
  const belowRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const t = setTimeout(() => setVisible(true), 80)
    return () => clearTimeout(t)
  }, [])

  const scrollDown = () => belowRef.current?.scrollIntoView({ behavior: 'smooth' })

  return (
    <div className="hero-root">
      <div className="hero-cols">
        <div className="hero-left">

          <div className={`hero-text-block${visible ? ' hero-fade-in' : ''}`}>
            <p className="hero-fullname">Dattatreya Subramanya Vellal</p>
            <h1 className="hero-name">Datta Vellal</h1>
            <p className="hero-snazzy">
              Turning regulated complexity into engineering excellence, one org, one standard, one team at a time.
            </p>
            <p className="hero-tagline">
              Global Digital Transformation Leader &nbsp;·&nbsp; IBM &rarr; Exeter &rarr; Amazon &rarr; Philips
            </p>
          </div>

          <div className={`hero-kpi-row${visible ? ' hero-fade-in hero-fade-delay-1' : ''}`}>
            {STATS.map(s => (
              <StatTile key={s.label} stat={s} animate={visible} onNavigate={onNavigate} />
            ))}
          </div>

          <p className={`hero-bio${visible ? ' hero-fade-in hero-fade-delay-2' : ''}`}>
            Global Digital Transformation Leader who harnesses data, AI, and Software Craftsmanship
            to modernize highly regulated medical device software. Works across IEC 62304,
            ISO 13485, ISO 14971, FDA guidances, and INCOSE/EARS systems engineering standards.
            Drove over $3M in savings across IBM, Amazon, and Philips while coaching more than
            7,000 engineers from writing code to mastering craft.
          </p>

          <div className={`hero-era-chips${visible ? ' hero-fade-in hero-fade-delay-3' : ''}`}>
            {Object.entries(ERA_COLORS).map(([era, color]) => (
              <span key={era} className="hero-era-chip" style={{ borderColor: color, color }}>
                {era}
              </span>
            ))}
          </div>

          <button className="hero-scroll-prompt" onClick={scrollDown} aria-label="Scroll to highlights">
            <span className="hero-scroll-text">&#8595; explore the data</span>
          </button>
        </div>

        <div className={`hero-right${visible ? ' hero-fade-in hero-fade-delay-1' : ''}`}>
          <img
            src="/photo.jpg"
            alt="Dattatreya Subramanya Vellal, known as Datta"
            className="hero-photo"
          />
        </div>
      </div>

      <div ref={belowRef} className="hero-below-fold">
        <div className="hero-below-label">Career Highlights</div>
        <div className="hero-below-grid">
          <button className="hero-below-card" onClick={() => onNavigate('constellation')}>
            <div className="hero-below-stat" style={{ color: '#c98500' }}>Medical Device</div>
            <div className="hero-below-desc">IEC 62304, ISO 13485, ISO 14971, and FDA guidances. Software audit authority at Philips.</div>
          </button>
          <button className="hero-below-card" onClick={() => onNavigate('talks')}>
            <div className="hero-below-stat" style={{ color: '#199e70' }}>AI Pioneer</div>
            <div className="hero-below-desc">Authoring AI-native craftsmanship frameworks and teaching AI integration to engineers and school children alike.</div>
          </button>
          <button className="hero-below-card" onClick={() => onNavigate('impact')}>
            <div className="hero-below-stat" style={{ color: '#3987e5' }}>Org Transformer</div>
            <div className="hero-below-desc">Built Software Excellence programs from the ground up at Philips. Delivered a 60% reduction in delivery time and a 2.1M euro transformation roadmap.</div>
          </button>
          <button className="hero-below-card" onClick={() => onNavigate('talks')}>
            <div className="hero-below-stat" style={{ color: '#d95926' }}>Full Human</div>
            <div className="hero-below-desc">Certified yoga instructor, CSI speaker, social volunteer, and community builder across more than 20 institutions.</div>
          </button>
        </div>
      </div>
    </div>
  )
}
