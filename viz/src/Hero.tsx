import { useState, useEffect, useRef } from 'react'

const ERA_COLORS: Record<string, string> = {
  IBM: '#3987e5',
  Exeter: '#d95926',
  Amazon: '#199e70',
  Philips: '#c98500',
}

const STATS = [
  { value: '$3M+',   label: 'Career savings delivered' },
  { value: '20 yrs', label: 'Industry depth' },
  { value: '7,000+', label: 'Engineers reached' },
  { value: '913',    label: 'Knowledge artifacts' },
]

const PHOTO_URL =
  'https://lh3.googleusercontent.com/sitesv/AG8ngQXiNBMCGiZ6lYmNS3Pv54G985-l6aM-8i_iAv3R-L1c-FUMrzYkDeF57IAzjPk9b63Vb8qVzX1Zbb5TLrkvBJoQTbRKZYB08kc7tb8ih7JjJmFNkVw8Dq6yShhbF36W8HQkBZMKqU5P5WBTVJwcUK1B3UyMWrDqm1VI-sFkWbjWSC0qhhVMI3I0s7MDaPHkobZG3JoumfabHYZEIgdOmyAHZQKxT9TlY99TZdMG=w1280'

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
  const cleaned = value.replace(/,/g, '')
  const numMatch = cleaned.match(/[\d.]+/)
  const num = numMatch ? parseFloat(numMatch[0]) : 0
  const prefix = cleaned.match(/^[^0-9]*/)?.[0] ?? ''
  const suffix = cleaned.match(/[^0-9.]+$/)?.[0] ?? ''
  const counted = useCountUp(num, 1400, animate)
  const display = num > 0
    ? `${prefix}${suffix.includes('%') ? counted.toFixed(num % 1 !== 0 ? 3 : 0) : counted.toLocaleString()}${suffix}`
    : value

  return (
    <div className="kpi-tile">
      <div className="kpi-label">{label}</div>
      <div className="kpi-value hero-stat-value">{display}</div>
    </div>
  )
}

export function HeroView() {
  const [visible, setVisible] = useState(false)
  const [photoOk, setPhotoOk] = useState(true)
  const belowRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const t = setTimeout(() => setVisible(true), 80)
    return () => clearTimeout(t)
  }, [])

  const scrollDown = () => {
    belowRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  return (
    <div className="hero-root">
      {/* Two-column: text left, photo right */}
      <div className="hero-cols">
        {/* ── Left: text ── */}
        <div className="hero-left">
          <div className={`hero-text-block${visible ? ' hero-fade-in' : ''}`}>
            <h1 className="hero-name">Datta Vellal</h1>
            <p className="hero-sub">Tech-first. Full human.</p>
            <p className="hero-tagline">
              Global Digital Transformation Leader · IBM → Exeter → Amazon → Philips
            </p>
          </div>

          <div className={`hero-kpi-row${visible ? ' hero-fade-in hero-fade-delay-1' : ''}`}>
            {STATS.map(s => (
              <StatTile key={s.label} value={s.value} label={s.label} animate={visible} />
            ))}
          </div>

          <p className={`hero-bio${visible ? ' hero-fade-in hero-fade-delay-2' : ''}`}>
            Global Digital Transformation Leader leveraging data, AI &amp; Software Craftsmanship
            principles to transform medical device software. Drove $3M+ in savings across IBM,
            Amazon, and Philips — coaching 7,000+ engineers from code to craft.
          </p>

          <div className={`hero-era-chips${visible ? ' hero-fade-in hero-fade-delay-3' : ''}`}>
            {Object.entries(ERA_COLORS).map(([era, color]) => (
              <span key={era} className="hero-era-chip" style={{ borderColor: color, color }}>
                {era}
              </span>
            ))}
          </div>

          <button className="hero-scroll-prompt" onClick={scrollDown} aria-label="Scroll to stats">
            <span className="hero-scroll-text">↓ explore the data</span>
          </button>
        </div>

        {/* ── Right: photo ── */}
        <div className={`hero-right${visible ? ' hero-fade-in hero-fade-delay-1' : ''}`}>
          {photoOk ? (
            <img
              src={PHOTO_URL}
              alt="Datta Vellal"
              className="hero-photo"
              onError={() => setPhotoOk(false)}
            />
          ) : (
            <div className="hero-photo-placeholder">
              <span className="hero-photo-initials">DV</span>
            </div>
          )}
        </div>
      </div>

      {/* ── Below-fold anchor (scroll target) ── */}
      <div ref={belowRef} className="hero-below-fold">
        <div className="hero-below-label">Career Highlights</div>
        <div className="hero-below-grid">
          <div className="hero-below-card">
            <div className="hero-below-stat" style={{ color: '#c98500' }}>Medical Device</div>
            <div className="hero-below-desc">IEC 62304 · ISO 13485 · ISO 14971 — software audit lead at Philips</div>
          </div>
          <div className="hero-below-card">
            <div className="hero-below-stat" style={{ color: '#199e70' }}>AI Pioneer</div>
            <div className="hero-below-desc">Authoring AI-native craftsmanship frameworks; teaching AI integration to engineers and school children</div>
          </div>
          <div className="hero-below-card">
            <div className="hero-below-stat" style={{ color: '#3987e5' }}>Org Transformer</div>
            <div className="hero-below-desc">Built Software Excellence programs from scratch at Philips — 60% delivery time reduction, €2.1M roadmap</div>
          </div>
          <div className="hero-below-card">
            <div className="hero-below-stat" style={{ color: '#d95926' }}>Full Human</div>
            <div className="hero-below-desc">Certified yoga instructor · CSI speaker · social volunteer · community builder across 20+ institutions</div>
          </div>
        </div>
      </div>
    </div>
  )
}
