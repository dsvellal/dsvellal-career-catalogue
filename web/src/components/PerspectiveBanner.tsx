import React from 'react';
import type { LeadershipPerspective } from '../types';
import { ArrowLeft, Briefcase, Users, Compass, Cpu, Award, Layers } from 'lucide-react';

interface StatItem {
  label: string;
  value: string;
}

interface PerspectiveBannerProps {
  index: string;
  title: string;
  subtitle: string;
  stats: StatItem[];
  onNavigate: (perspective: LeadershipPerspective) => void;
}

export const PerspectiveBanner: React.FC<PerspectiveBannerProps> = ({
  index,
  title,
  subtitle,
  stats,
  onNavigate
}) => {
  const perspectives: { id: LeadershipPerspective; label: string; icon: React.ComponentType<{ size?: number }> }[] = [
    { id: 'boardroom', label: '60s Brief', icon: Briefcase },
    { id: 'leadership', label: 'Leadership OS', icon: Users },
    { id: 'architecture', label: 'Architecture', icon: Compass },
    { id: 'governance', label: 'Enterprise AI', icon: Cpu },
    { id: 'career', label: 'Career Lineage', icon: Award },
    { id: 'catalog', label: 'Evidence Catalog', icon: Layers }
  ];

  return (
    <div className="perspective-page-banner">
      <div className="container">
        {/* Navigation Breadcrumb */}
        <div className="perspective-breadcrumb">
          <button
            type="button"
            className="breadcrumb-back-btn"
            onClick={() => onNavigate('boardroom')}
          >
            <ArrowLeft size={13} />
            <span>Boardroom Brief</span>
          </button>
          <span className="breadcrumb-separator">/</span>
          <span className="breadcrumb-current">Perspective {index}</span>
        </div>

        {/* Title and Executive Framing */}
        <div className="perspective-header-content">
          <div className="perspective-index-badge">
            Executive Lens {index} of 06
          </div>
          <h1 className="perspective-page-title">{title}</h1>
          <p className="perspective-page-subtitle">{subtitle}</p>
        </div>

        {/* Executive Stats Ribbon */}
        {stats && stats.length > 0 && (
          <div className="perspective-stats-ribbon">
            {stats.map((s, i) => (
              <div key={i} className="perspective-stat-card">
                <div className="perspective-stat-val">{s.value}</div>
                <div className="perspective-stat-lbl">{s.label}</div>
              </div>
            ))}
          </div>
        )}

        {/* Quick Lens Switcher Strip */}
        <div className="perspective-lens-strip">
          <span className="lens-strip-title">Jump to Lens:</span>
          <div className="lens-strip-pills">
            {perspectives.map((p) => {
              const Icon = p.icon;
              return (
                <button
                  key={p.id}
                  type="button"
                  className="lens-strip-pill"
                  onClick={() => onNavigate(p.id)}
                >
                  <Icon size={12} />
                  <span>{p.label}</span>
                </button>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
};
