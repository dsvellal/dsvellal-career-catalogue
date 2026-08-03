import { useState, useEffect, useRef } from 'react'

const ERA_COLORS: Record<string, string> = {
  IBM: '#3987e5',
  Exeter: '#d95926',
  Amazon: '#199e70',
  Philips: '#c98500',
}

const STATS = [
  { value: '$3M+', label: 'Career savings' },
  { value: '20 yrs', label: 'Industry depth' },
  { value: '7,000+', label: 'Engineers reached' },
  { value: '99.999%', label: 'Service uptime' },
]

function useCountUp(target: number, duration = 1200, start = false) {
  const [count, setCount] = useState(0)
  const raf = useRef<number>(0)

  useEffect(() => {
    if (!start) return
    const startTime = performance.now()
    const tick = (now: number) => {
      const elapsed = now - startTime
      const progress = Math.min(elapsed / duration, 1)
      const eased = 1 - Math.pow(1 - progress, 3)
      setCount(Math.floor(eased * target))
      if (progress < 1) raf.current = requestAnimationFrame(tick)
    }
    raf.current = requestAnimationFrame(tick)
    return () => cancelAnimationFrame(raf.current)
  }, [target, duration, start])

  return count
}

function StatTile({ value, label, animate }: { value: string; label: string; animate: boolean }) {
  // Strip commas so "7,000+" parses as 7000
  const cleaned = value.replace(/,/g, '')
  const numMatch = cleaned.match(/[\d.]+/)
  const num = numMatch ? parseFloat(numMatch[0]) : 0
  const prefix = cleaned.match(/^[^0-9]*/)?.[0] ?? ''
  const suffix = cleaned.match(/[^0-9.]+$/)?.[0] ?? ''
  const counted = useCountUp(num, 1400, animate)
  const display = num > 0 ? `${prefix}${suffix.includes('%') ? counted.toFixed(num % 1 !== 0 ? 3 : 0) : counted.toLocaleString()}${suffix}` : value

  return (
    <div className="kpi-tile">
      <div className="kpi-label">{label}</div>
      <div className="kpi-value hero-stat-value">{display}</div>
    </div>
  )
}

export function HeroView() {
  const [visible, setVisible] = useState(false)

  useEffect(() => {
    const t = setTimeout(() => setVisible(true), 80)
    return () => clearTimeout(t)
  }, [])

  return (
    <div className="hero-root">
      <div className={`hero-text-block${visible ? ' hero-fade-in' : ''}`}>
        <h1 className="hero-name">Datta Vellal</h1>
        <p className="hero-sub">Tech-first. Full human.</p>
        <p className="hero-tagline">
          Principal Software Engineer · 20 Years · IBM → Exeter → Amazon → Philips
        </p>
      </div>

      <div className={`hero-kpi-row${visible ? ' hero-fade-in hero-fade-delay-1' : ''}`}>
        {STATS.map(s => (
          <StatTile key={s.label} value={s.value} label={s.label} animate={visible} />
        ))}
      </div>

      <p className={`hero-bio${visible ? ' hero-fade-in hero-fade-delay-2' : ''}`}>
        Principal software engineer and organizational transformer. Built software excellence programs, led fraud detection at Amazon, authored Philips' State of Craftsmanship report, and coached 50+ engineers from code to craft.
      </p>

      <div className={`hero-era-chips${visible ? ' hero-fade-in hero-fade-delay-3' : ''}`}>
        {Object.entries(ERA_COLORS).map(([era, color]) => (
          <span key={era} className="hero-era-chip" style={{ borderColor: color, color }}>
            {era}
          </span>
        ))}
      </div>

      <div className="hero-scroll-prompt">
        <span className="hero-scroll-text">↓ explore the data</span>
      </div>
    </div>
  )
}
