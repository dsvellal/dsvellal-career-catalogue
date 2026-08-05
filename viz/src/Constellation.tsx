import { useState } from 'react'
import constellationData from './data/constellation.json'

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

const CLUSTER_META: Record<string, { color: string; icon: string; subtitle: string }> = {
  'How I Interact': {
    color: '#2563a8',
    icon: 'ROOM A',
    subtitle: 'The way I connect, communicate, and build relationships',
  },
  'How I Deliver': {
    color: '#b84c1a',
    icon: 'ROOM B',
    subtitle: 'The precision, rigor, and quality I bring to every output',
  },
  'How I Lead': {
    color: '#0d7a52',
    icon: 'ROOM C',
    subtitle: 'How I guide, inspire, and set direction for teams and organizations',
  },
  'How I Think': {
    color: '#9a6b00',
    icon: 'ROOM D',
    subtitle: 'The mental models, innovation, and strategy I apply',
  },
}

const CLUSTER_ORDER = ['How I Interact', 'How I Deliver', 'How I Lead', 'How I Think']

function getOrbitSkillsForCluster(
  orbitSkills: OrbitSkill[],
  betalentSkills: BeTalentSkill[],
  cluster: string
): OrbitSkill[] {
  const clusterCategoryMap: Record<string, string[]> = {
    'How I Interact': ['soft_skill', 'hiring'],
    'How I Deliver': ['engineering_practice', 'devops', 'programming_language', 'architecture_pattern'],
    'How I Lead': ['leadership', 'agile_methodology'],
    'How I Think': ['framework', 'innovation'],
  }
  const cats = clusterCategoryMap[cluster] ?? []
  return orbitSkills
    .filter(s => cats.includes(s.category ?? ''))
    .sort((a, b) => b.used_skill_count - a.used_skill_count)
}

function SkillBar({ name, count, maxCount, color, recognized, onClick, isSelected }: {
  name: string
  count: number
  maxCount: number
  color: string
  recognized: number
  onClick: () => void
  isSelected: boolean
}) {
  const pct = (count / maxCount) * 100
  return (
    <button
      className={`fp-skill-bar${isSelected ? ' fp-skill-bar--active' : ''}`}
      onClick={onClick}
      style={{ '--bar-color': color } as React.CSSProperties}
    >
      <span className="fp-skill-name">{name}</span>
      <span className="fp-skill-count">{count}×</span>
      <span className="fp-skill-rec">{recognized > 0 ? `${recognized} rec.` : ''}</span>
      <div className="fp-skill-track">
        <div className="fp-skill-fill" style={{ width: `${pct}%`, background: color }} />
      </div>
    </button>
  )
}

function RoomPanel({ cluster, betalentSkills, orbitSkills, selected, onSelect, maxOrbit }: {
  cluster: string
  betalentSkills: BeTalentSkill[]
  orbitSkills: OrbitSkill[]
  selected: BeTalentSkill | OrbitSkill | null
  onSelect: (s: BeTalentSkill | OrbitSkill) => void
  maxOrbit: number
}) {
  const meta = CLUSTER_META[cluster]
  const coreSkills = betalentSkills.filter(s => s.cluster === cluster)
  const relatedOrbit = getOrbitSkillsForCluster(orbitSkills, betalentSkills, cluster)

  return (
    <div className="fp-room" style={{ '--room-color': meta.color } as React.CSSProperties}>
      <div className="fp-room-header">
        <span className="fp-room-code">{meta.icon}</span>
        <div className="fp-room-title-block">
          <h3 className="fp-room-name">{cluster.replace('How I ', '')}</h3>
          <p className="fp-room-subtitle">{meta.subtitle}</p>
        </div>
      </div>

      <div className="fp-room-core">
        <div className="fp-core-label">Core Strengths (BeTalent Assessed)</div>
        {coreSkills.map(skill => (
          <button
            key={skill.id}
            className={`fp-core-item${selected?.id === skill.id ? ' fp-core-item--active' : ''}`}
            onClick={() => onSelect(skill)}
          >
            <span className="fp-core-rank">#{skill.betalent_rank}</span>
            <span className="fp-core-name">{skill.name}</span>
            <span className="fp-core-label-tag">{skill.label}</span>
          </button>
        ))}
      </div>

      {relatedOrbit.length > 0 && (
        <div className="fp-room-orbit">
          <div className="fp-orbit-label">Applied Skills ({relatedOrbit.length})</div>
          {relatedOrbit.slice(0, 6).map(skill => (
            <SkillBar
              key={skill.id}
              name={skill.name}
              count={skill.used_skill_count}
              maxCount={maxOrbit}
              color={meta.color}
              recognized={skill.recognized_for_count}
              onClick={() => onSelect(skill)}
              isSelected={selected?.id === skill.id}
            />
          ))}
        </div>
      )}
    </div>
  )
}

function DetailPanel({ skill }: { skill: BeTalentSkill | OrbitSkill | null }) {
  if (!skill) {
    return (
      <div className="fp-detail fp-detail--empty">
        <p className="fp-detail-prompt">Select any strength or skill to see its full specification.</p>
      </div>
    )
  }

  const isBeTalent = 'betalent_rank' in skill
  const bt = skill as BeTalentSkill

  return (
    <div className="fp-detail">
      <div className="fp-detail-header">
        {isBeTalent && <span className="fp-detail-rank">RANK #{bt.betalent_rank}</span>}
        <h3 className="fp-detail-name">{skill.name}</h3>
        {isBeTalent && <span className="fp-detail-label">{bt.label}</span>}
      </div>

      {isBeTalent && (
        <>
          <div className="fp-detail-section">
            <div className="fp-detail-section-title">Description</div>
            <p className="fp-detail-text">{bt.description}</p>
          </div>

          <div className="fp-detail-metrics">
            <div className="fp-detail-metric">
              <span className="fp-detail-metric-val">{skill.used_skill_count}</span>
              <span className="fp-detail-metric-label">TIMES DEMONSTRATED</span>
            </div>
            <div className="fp-detail-metric">
              <span className="fp-detail-metric-val">{skill.recognized_for_count}</span>
              <span className="fp-detail-metric-label">PEER RECOGNITIONS</span>
            </div>
          </div>

          {bt.ldc_strength && (
            <div className="fp-detail-section">
              <div className="fp-detail-section-title">Assessed Strength</div>
              <p className="fp-detail-text">{bt.ldc_strength}</p>
            </div>
          )}

          {bt.overuse_risk && (
            <div className="fp-detail-section fp-detail-section--caution">
              <div className="fp-detail-section-title">Overuse Risk</div>
              <p className="fp-detail-text">{bt.overuse_risk}</p>
            </div>
          )}

          {bt.sample_achievements.length > 0 && (
            <div className="fp-detail-section">
              <div className="fp-detail-section-title">Evidence ({bt.sample_achievements.length})</div>
              <ul className="fp-detail-evidence">
                {bt.sample_achievements.map((a, i) => (
                  <li key={i}>{a}</li>
                ))}
              </ul>
            </div>
          )}
        </>
      )}

      {!isBeTalent && (
        <>
          <div className="fp-detail-metrics">
            <div className="fp-detail-metric">
              <span className="fp-detail-metric-val">{skill.used_skill_count}</span>
              <span className="fp-detail-metric-label">TIMES USED</span>
            </div>
            <div className="fp-detail-metric">
              <span className="fp-detail-metric-val">{skill.recognized_for_count}</span>
              <span className="fp-detail-metric-label">RECOGNITIONS</span>
            </div>
          </div>
          {(skill as OrbitSkill).first_seen && (
            <div className="fp-detail-section">
              <div className="fp-detail-section-title">First Observed</div>
              <p className="fp-detail-text">{(skill as OrbitSkill).first_seen}</p>
            </div>
          )}
        </>
      )}
    </div>
  )
}

export function ConstellationView() {
  const [selected, setSelected] = useState<BeTalentSkill | OrbitSkill | null>(null)
  const betalent: BeTalentSkill[] = constellationData.betalent_skills as BeTalentSkill[]
  const orbit: OrbitSkill[] = constellationData.orbit_skills as OrbitSkill[]
  const maxOrbit = Math.max(...orbit.map(s => s.used_skill_count))

  const totalRecognitions = betalent.reduce((sum, s) => sum + s.recognized_for_count, 0) +
    orbit.reduce((sum, s) => sum + s.recognized_for_count, 0)

  return (
    <div className="fp-layout">
      <div className="section-header">
        <div className="section-label">Professional Identity</div>
        <h2 className="section-title">Who I Am as a Professional</h2>
        <p className="section-subtitle">
          Core strengths mapped from the BeTalent psychometric assessment — externally validated,
          not self-reported. Applied skills measured across 20 years of evidence.
        </p>
      </div>

      <div className="fp-stats-row">
        <div className="fp-stat-cell">
          <span className="fp-stat-value">12</span>
          <span className="fp-stat-label">ASSESSED STRENGTHS</span>
          <span className="fp-stat-sub">BeTalent ranked</span>
        </div>
        <div className="fp-stat-cell">
          <span className="fp-stat-value">{totalRecognitions}</span>
          <span className="fp-stat-label">TOTAL RECOGNITIONS</span>
          <span className="fp-stat-sub">External, peer, manager</span>
        </div>
        <div className="fp-stat-cell">
          <span className="fp-stat-value">{betalent.length + orbit.length}</span>
          <span className="fp-stat-label">SKILLS IN EVIDENCE</span>
          <span className="fp-stat-sub">Across 20 years</span>
        </div>
        <div className="fp-stat-cell">
          <span className="fp-stat-value">Communication</span>
          <span className="fp-stat-label">TOP SKILL</span>
          <span className="fp-stat-sub">Rank 1 · How I Interact</span>
        </div>
      </div>

      <div className="fp-content">
        <div className="fp-floor-plan">
          <div className="fp-rooms-grid">
            {CLUSTER_ORDER.map(cluster => (
              <RoomPanel
                key={cluster}
                cluster={cluster}
                betalentSkills={betalent}
                orbitSkills={orbit}
                selected={selected}
                onSelect={setSelected}
                maxOrbit={maxOrbit}
              />
            ))}
          </div>
        </div>
        <DetailPanel skill={selected} />
      </div>
    </div>
  )
}
