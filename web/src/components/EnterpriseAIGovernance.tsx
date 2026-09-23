import React from 'react';
import { Cpu, ShieldCheck, Network, Binary, CheckCircle2, UserCheck } from 'lucide-react';

export const EnterpriseAIGovernance: React.FC = () => {
  const governanceGuards = [
    {
      id: 'guard-knowledge-graph',
      icon: Network,
      title: 'Deterministic Knowledge Graph Schema (Project SUTRA)',
      description:
        'Replaced fragile relational tables with a graph-indexed semantic network. Links requirements, verification proofs, and risk artifacts deterministically, eliminating hallucination risks in medical device compliance audits.',
      verifiableMetric: '75% Reduction in Release Validation Overhead'
    },
    {
      id: 'guard-ai-harness',
      icon: Binary,
      title: 'AI Validation Harness and Quality Gates',
      description:
        'Engineered automated test harnesses that validate prompt-driven outputs against clinical safety boundaries before deployment. Enforces repeatability and eliminates non-deterministic variance in production pipelines.',
      verifiableMetric: 'Defensible Audit Trail Across 3 Global Divisions'
    },
    {
      id: 'guard-analyst-enablement',
      icon: UserCheck,
      title: 'Workforce Enablement: 150+ Analysts Trained',
      description:
        'Authored and instructed practical prompt engineering curricula for 100 to 150 data analysts across North America. Ranked as top recommended technical enablement curriculum in FY 2026.',
      verifiableMetric: '150+ Analysts Upskilled with Zero Security Breaches'
    }
  ];

  return (
    <section className="enterprise-ai-section" id="enterprise-ai-governance">
      <div className="enterprise-ai-header">
        <div className="ai-badge">
          <Cpu size={16} />
          <span>Responsible Enterprise AI &amp; MedTech Governance</span>
        </div>
        <h2 className="enterprise-ai-title">
          Governing AI in Regulated Healthcare: Zero-Hallucination Engineering
        </h2>
        <p className="enterprise-ai-subtitle">
          Deploying AI in medical technology demands mathematical rigor, audit defensibility, and deterministic validation.
          Here is how I architected enterprise knowledge networks and AI workflows that satisfy both commercial speed and FDA compliance.
        </p>
      </div>

      {/* Architecture Clash: Generative Uncertainty vs. Deterministic Graph */}
      <div className="ai-architecture-comparison">
        <div className="comparison-side legacy-side">
          <div className="side-badge">The Unacceptable Risk</div>
          <h4>Naive Generative AI in Regulated Systems</h4>
          <ul className="comparison-list">
            <li>Non-deterministic outputs and hallucinations in compliance documentation.</li>
            <li>Disconnected legacy relational tables requiring 40+ hours of manual release tracing.</li>
            <li>Lack of verifiable provenance between customer requirements and verification tests.</li>
            <li>Audit failure vulnerability under FDA 21 CFR Part 11 and EU MDR scrutiny.</li>
          </ul>
        </div>

        <div className="comparison-divider">
          <span>VS</span>
        </div>

        <div className="comparison-side modern-side">
          <div className="side-badge resolved-badge">The Deployed Solution: Project SUTRA</div>
          <h4>AI-Indexed Knowledge Graph + Deterministic Validation</h4>
          <ul className="comparison-list">
            <li>Semantic knowledge graph anchoring every node to a verified engineering artifact.</li>
            <li>Automated gap analysis that validates requirements completeness in 10 hours instead of 40 hours.</li>
            <li>Immutable audit provenance with human-in-the-loop verification checkpoints.</li>
            <li>Adopted across 3 global Philips business units with VP-level commendation.</li>
          </ul>
        </div>
      </div>

      {/* 3 Governance Pillars */}
      <div className="governance-cards-grid">
        {governanceGuards.map((guard) => {
          const Icon = guard.icon;
          return (
            <div key={guard.id} className="governance-card">
              <div className="gov-icon-wrapper">
                <Icon size={22} />
              </div>
              <h3 className="gov-title">{guard.title}</h3>
              <p className="gov-desc">{guard.description}</p>
              <div className="gov-metric">
                <CheckCircle2 size={15} />
                <span>{guard.verifiableMetric}</span>
              </div>
            </div>
          );
        })}
      </div>

      {/* Verified Stakeholder Testimonial */}
      <div className="governance-quote-banner">
        <div className="quote-icon-col">
          <ShieldCheck size={28} />
        </div>
        <div className="quote-content-col">
          <p className="quote-body">
            &ldquo;Datta hosted sessions for 100 to 150 analysts across North America on prompt engineering and practical AI adoption.
            His sessions were the top recommended material in the community this year.&rdquo;
          </p>
          <div className="quote-attribution">
            <strong>Claudia Smith</strong> - Data Science and Analytics Lead, North America (WorkDay Formal Stakeholder Review)
          </div>
        </div>
      </div>
    </section>
  );
};
