import React, { useState } from 'react';
import {
  Users,
  Target,
  Shield,
  BookOpen,
  CheckCircle,
  GraduationCap,
  Sparkles,
  BarChart3,
  Layers,
  FileText
} from 'lucide-react';

export const LeadershipOperatingSystem: React.FC = () => {
  const pillars = [
    {
      id: 'pillar-bar-raiser',
      icon: Target,
      tag: 'Hiring Governance',
      title: 'The Amazon Bar Raiser Talent Framework',
      subtitle: 'Institutionalizing hiring standards that raise team competency over time.',
      principles: [
        'Enforced independent veto authority on hiring decisions to protect long-term talent density against urgent headcount pressures.',
        'Calibrated interview panels against standardized behavioral and system architecture competencies to eliminate interviewer bias.',
        'Conducted bar raiser evaluations across distributed teams, ensuring every new hire outperformed the median team capability.'
      ],
      impact: 'Scaled engineering organizations across Amazon and Philips while maintaining zero degradation in technical delivery bars.'
    },
    {
      id: 'pillar-craftsmanship',
      icon: Shield,
      tag: 'Execution Discipline',
      title: 'Architectural Craftsmanship and Debt Control',
      subtitle: 'Eliminating architectural drift through deterministic verification and automated quality gates.',
      principles: [
        'Mandated static code health tracking, CodeScene technical debt analysis, and automated CI/CD validation gates prior to production merges.',
        'Enforced strict decoupling between core medical domain logic and operational infrastructure to prevent vendor lock-in.',
        'Instituted peer-led architecture review boards with written decision records to anchor accountability.'
      ],
      impact: 'Prevented multi-week integration blockers and sustained high release predictability across multi-site teams.'
    },
    {
      id: 'pillar-multiplier',
      icon: GraduationCap,
      tag: 'Talent Incubation',
      title: 'The Talent Multiplier and University Pipeline',
      subtitle: 'Developing engineering leaders from within and cultivating external academic talent pools.',
      principles: [
        'Mentored over 100 software engineers directly, guiding engineers from junior ICs to Lead Architects and Engineering Managers.',
        'Conducted guest lecture series on technical presentation, system design, and interview readiness at institutions including RVCE, BMSIT, NIE, and SIT.',
        'Organized annual academic book distributions and sponsorship drives to support underprivileged engineering scholars.'
      ],
      impact: 'Built a sustainable talent pipeline with proven retention, high peer engagement, and industry leadership recognition.'
    }
  ];

  const universityWorkshops = [
    { institution: 'RV College of Engineering (RVCE)', topic: 'SOLID Principles of Programming and Technical Interview Preparation' },
    { institution: 'BMS Institute of Technology (BMSIT)', topic: 'Cultivating Growth Attitude and Tackling System Uncertainty' },
    { institution: 'National Institute of Engineering (NIE)', topic: 'High-Stakes Technical Interview Mastery and Problem Deconstruction' },
    { institution: 'Siddaganga Institute of Technology (SIT)', topic: 'Microservices Architecture, Presentation Craft, and Rapid Decision-Making' }
  ];

  const evaluationCohorts = [
    {
      id: 'philips-iwillcode',
      category: 'philips',
      name: "Philips 'I Will Code!' Program: Engineering Enablement for Non-Coders",
      badge: 'Capability Transformation',
      organization: 'Philips Software Center of Excellence',
      date: 'Jan to Oct 2020',
      reach: '105+ Non-Coding Verification Leads & Engineers',
      surveySubmissions: 105,
      ratingHighlights: [
        { label: 'Recommendation Score', value: '9.37 / 10' },
        { label: 'Net Promoter Rate', value: '91.4%' },
        { label: 'Verified Submissions', value: '105' },
        { label: 'Execution Rate', value: '100%' }
      ],
      leadershipContext:
        'Designed and led a multi-month engineering upskilling initiative to break the psychological barrier of coding for quality professionals and verification engineers. Taught OOP, test-first thinking, and Java from first principles.',
      verbatimQuotes: [
        'Overcame the fear of coding. How to write on my own, how to resolve errors. We just have to dare to start and there are people to help.',
        'Super Datta, continue the great work. Very nicely structured and the flow and speed is optimal and great.',
        '6-Mar class was way beyond what I expected for first class. Inspires curiosity and self confidence.'
      ]
    },
    {
      id: 'philips-swcoe-connects',
      category: 'philips',
      name: 'Philips SWCoE Strategic Architecture & Coaching Connects',
      badge: 'Global Engineering Advisory',
      organization: 'Philips Global Engineering (10 Development Centers)',
      date: '2020 to 2022',
      reach: '2,800+ Colleague Interactions across 22 Cities',
      surveySubmissions: 2800,
      ratingHighlights: [
        { label: 'Colleague Interactions', value: '2,800+' },
        { label: 'Inbound Pull Demand', value: '70-94%' },
        { label: 'Departments Covered', value: '37+' },
        { label: 'Global Cities Engaged', value: '22' }
      ],
      leadershipContext:
        'Conducted strategic architectural coaching, code health assessments, and pair-programming across HealthSuite, Image Guided Therapy, Magnetic Resonance, and Ultrasound. Inbound pull requests from development teams accounted for over 75% of total sessions.',
      verbatimQuotes: [
        "Datta's structured problem-solving approach sets a high standard for our teams. His ability to listen with an open mind creates an environment where teams openly tackle hard problems.",
        'Unblocked cross-team dependencies with remarkable speed and clarity.'
      ]
    },
    {
      id: 'philips-bar-raisers',
      category: 'philips',
      name: 'Philips SkillRaisers & Bar Raisers Interview Calibration',
      badge: 'Hiring Bar Governance',
      organization: 'Philips SWCoE & Talent Acquisition',
      date: '2020 to 2024',
      reach: '150+ Hiring Managers & Interviewers',
      surveySubmissions: 31,
      ratingHighlights: [
        { label: 'Workshop Duration', value: '4 Hours' },
        { label: 'Competence Factors', value: '5 Factors' },
        { label: 'Objective Mandate', value: 'Zero Bias' },
        { label: 'Multi-Site Reach', value: '4 Sites' }
      ],
      leadershipContext:
        'Institutionalized Amazon-style Bar Raiser hiring discipline inside Philips. Facilitated intensive 4-hour workshops training hiring managers and technical leads on STARR behavioral evaluation, mitigating unconscious bias, and maintaining an immutable hiring bar.',
      verbatimQuotes: [
        'Kept the audience engaged and energetic for 4 hours. The discussion on the order of the 5 evaluation factors was enlightening.',
        'Stimulated good conversation and sharing. Good explanation of good interviewing practices and how the interview process will include the bar raiser.',
        "Datta's structured evaluation frameworks significantly raised the talent and interview bar across the development center."
      ]
    },
    {
      id: 'philips-quality-at-desk',
      category: 'philips',
      name: 'Philips Quality@Desk (Q@D): IDE-Level Architectural Verification',
      badge: 'Shift-Left Transformation',
      organization: 'Philips Diagnostic & Informatics Clusters',
      date: '2020 to 2021',
      reach: '6 Major Business Platforms (Artemis, ASP, EMR, RADAR, DAW, Catalysts)',
      surveySubmissions: 6,
      ratingHighlights: [
        { label: 'Platforms Transformed', value: '6 Platforms' },
        { label: 'Compiler Warnings', value: 'Zero Tolerance' },
        { label: 'Mutation Testing', value: 'Pitest Gates' },
        { label: 'Dead Code Elimination', value: '100% Clean' }
      ],
      leadershipContext:
        'Shifted static analysis and architectural health from late-stage CI back to the developer desk. Guided development teams to implement compiler warning zero-tolerance, cyclomatic complexity method gating, and automated mutation testing.',
      verbatimQuotes: [
        'Datta went above and beyond in guiding our team to adopt automated CI pipelines with strict quality gates on cyclomatic complexity and duplicate code reduction.',
        'His focus on data-driven quality metrics fundamentally shifted how we monitor codebase health.'
      ]
    },
    {
      id: 'philips-university',
      category: 'philips',
      name: 'Philips University & Project Elevate: 2026 AI Masterclasses & Scaled Enablement',
      badge: '2026 Scaled Capability',
      organization: 'Philips University, Project Elevate & IEN',
      date: '2026 Full-Year Cadence',
      reach: '1,007+ Global Engineers Across 28 Masterclasses',
      surveySubmissions: 1007,
      ratingHighlights: [
        { label: '2026 Masterclasses', value: '28 Cohorts' },
        { label: 'Engineers Upskilled', value: '1,007+ Attendees' },
        { label: 'Avg Rating (Scored)', value: '8.77 / 10' },
        { label: 'Perfect Scores', value: 'Multiple 10/10 NPS' }
      ],
      leadershipContext:
        'Architected and delivered 28 comprehensive masterclasses throughout 2026 across Philips University, Project Elevate, and Innovation Engineering Network (IEN). Topics included IEC 62304 Medical Device AI Compliance, Golden Traceability with AI, Context Engineering, Coding with GitHub Copilot, and Tech Debt Elimination, achieving multiple 10/10 NPS scores across NAM Analytics and IT Connect communities.',
      verbatimQuotes: [
        'Verified satisfaction rating: 8.77 / 10 across 28 cohorts and 1,007+ learners in 2026 alone. Multiple perfect 10/10 NPS scores earned in NAM Analytics Community and IT Connect NA cohorts. - 2026 Facilitation Reporting Log',
        'Delivered tangible efficiency gains and clear practical frameworks for leveraging generative AI in daily engineering workflows while adhering strictly to medical device standards. - Engineering Participant Survey'
      ]
    },
    {
      id: 'philips-viva-engage',
      category: 'philips',
      name: 'Enterprise Digital Thought Leadership & Viva Engage Community Reach',
      badge: 'Executive & Network Influence',
      organization: 'Global Philips Communities (PS&Q, NAM Analytics, Ultrasound R&D)',
      date: '2024 to 2026',
      reach: '56,000+ Enterprise Network Reach Across 5 Communities',
      surveySubmissions: 500,
      ratingHighlights: [
        { label: 'Executive Commendation', value: 'Executive VP' },
        { label: 'Town Hall Honor', value: 'Impact Makers' },
        { label: 'Communities Active', value: '5 Divisions' },
        { label: 'NAM NPS Rating', value: '10 / 10 NPS' }
      ],
      leadershipContext:
        'Established an active digital leadership presence across enterprise Viva Engage and Yammer communities. Published \"AI On-Demand: Accelerating Requirements Compliance with Kairos\" and reusable prompt libraries for IEC 62304 and FDA Premarket Guidance. Earned executive commendation from the Executive VP & Chief Patient Safety and Quality Officer, led the Sutra team to receive the official \"Impact Makers\" Award at the IEN Global Town Hall, and featured in the XITE Special Edition on AI operational efficiency.',
      verbatimQuotes: [
        '\"It is great to read these details about the Innovation Engineering team expertise around Kairos. Keep leading the way! Thank you for the collaboration!\" - Executive VP and Chief Patient Safety and Quality Officer (Viva Engage)',
        '\"A big congratulations to our Sutra team on the Impact Makers recognition at the IEN Global Town Hall! This reflects the real impact, speed, and cross-team collaboration you have demonstrated.\" - Program Leader PMO, Software Engineering Excellence',
        '\"XITE Special Edition delivers AI-driven operational efficiency gains. We are thrilled to share the outcomes from the XITE and Sutra collaboration.\" - Senior Director of Innovation and Design Strategy'
      ]
    },
    {
      id: 'amazon-senpai',
      category: 'amazon',
      name: 'Amazon Senpai Faculty: EE Scrum & Product Ownership Masterclasses',
      badge: 'Enterprise Faculty',
      organization: 'Amazon Engineering Excellence',
      date: '2018',
      reach: '50+ Engineers & Technical Leaders',
      surveySubmissions: 45,
      ratingHighlights: [
        { label: 'Instructor Knowledge', value: '4.64 / 5' },
        { label: 'Classroom Experience', value: '4.57 / 5' },
        { label: 'Presenter Score', value: '4.57 / 5' },
        { label: 'Course Clarity', value: '4.43 / 5' }
      ],
      leadershipContext:
        'Up-leveled distributed agile execution across Amazon TRMS. Deliberately excluded team managers from training so engineers felt safe to challenge team antipatterns and rebuild healthy sprint hygiene.',
      verbatimQuotes: [
        'I really liked the way Datta took our questions with all excitement and made us comfortable to freely engage in conversations and counter arguments.',
        'By making sure that team managers do not attend the training with the team itself, encouraged participants to question their team practices.',
        'Datta was very clear in communicating and provided many examples which were easy to relate.'
      ]
    },
    {
      id: 'sit-tumkur',
      category: 'academic',
      name: 'Siddaganga Institute of Technology: Thinking on Your Feet & Microservices',
      badge: 'Academic Masterclass',
      organization: 'SIT Tumkur',
      date: '2019 to 2020',
      reach: '300+ Students & Faculty',
      surveySubmissions: 120,
      ratingHighlights: [
        { label: 'Seminar Quality Rating', value: '9.57 / 10' },
        { label: 'Recommendation Score', value: '9.17 / 10' },
        { label: 'Net Promoter Rate', value: '80.0%' },
        { label: 'Interactive Score', value: '100%' }
      ],
      leadershipContext:
        'Trained early-career engineers in poise under uncertainty, impromptu technical problem framing, and modern microservices decoupling.',
      verbatimQuotes: [
        'Extremely interactive and practical. The lessons on impromptu thinking and handling audience friction were eye-opening.',
        'Transformed how I structure technical slides and convey system value under high-pressure scenarios.'
      ]
    },
    {
      id: 'nie-mysore',
      category: 'academic',
      name: 'The National Institute of Engineering: Tier-1 Technical Interview Mastery',
      badge: 'Hiring Bar Calibration',
      organization: 'NIE Mysore',
      date: 'July 2017',
      reach: '80+ Engineering Seniors',
      surveySubmissions: 84,
      ratingHighlights: [
        { label: 'Presenter Effectiveness', value: '4.52 / 5' },
        { label: 'Learning Impact Score', value: '4.14 / 5' },
        { label: 'Content Depth', value: '3.98 / 5' },
        { label: 'Documented Surveys', value: '84' }
      ],
      leadershipContext:
        'Demystified Amazon and tier-1 tech hiring bars; coached candidates on failure recovery, algorithmic communication, and emotional resilience.',
      verbatimQuotes: [
        'Failure is an opinion. Never give up and keep practicing. Speaker was highly interactive and very motivating. His life story of never giving up motivated me a lot.',
        'One of the things which interested me was to give it back to the world, whatever we learnt. Also, being continuously at the top of the game by learning and adapting continuously.',
        'The right methodology to deal with the stress that each interviewee goes through during the interview and the right approach to answer questions.'
      ]
    },
    {
      id: 'rvce-bangalore',
      category: 'academic',
      name: 'RV College of Engineering: SOLID Principles & Architectural Craftsmanship',
      badge: 'Software Craftsmanship',
      organization: 'RVCE Bangalore',
      date: 'Sept 2018 & Feb 2017',
      reach: '120+ Computer Science Engineers',
      surveySubmissions: 75,
      ratingHighlights: [
        { label: 'Top-Tier Presenter', value: '93.0%' },
        { label: 'Content Relevance', value: '95.0%' },
        { label: 'Intent to Adopt in Code', value: '100%' },
        { label: '2018 Cohort Surveys', value: '57' }
      ],
      leadershipContext:
        'Instilled architectural discipline early; taught students how interface segregation and dependency inversion prevent technical debt in production systems.',
      verbatimQuotes: [
        'He is an excellent speaker and even a better coder.',
        'I am new to object-oriented programming. Going to follow your steps while learning and implementing.',
        'Different programming approach techniques, insight about industry level programming, code reviewing.'
      ]
    },
    {
      id: 'dr-ait-bangalore',
      category: 'academic',
      name: 'Dr. Ambedkar Institute of Technology: Technical Paper Writing & Patent IP',
      badge: 'IP Stewardship',
      organization: 'Dr. AIT Bangalore',
      date: 'March 2020 & 2013',
      reach: '210+ Students & Researchers',
      surveySubmissions: 98,
      ratingHighlights: [
        { label: 'Verified Practical Utility', value: '99.0%' },
        { label: 'Intensive Masterclass', value: '120 Min' },
        { label: 'Total Attendees', value: '210+' },
        { label: 'Practical Focus', value: '100%' }
      ],
      leadershipContext:
        'Taught engineering students how to identify patentable system inventions and structure peer-reviewed technical specifications.',
      verbatimQuotes: [
        'Clarified exactly how to structure an engineering research paper and differentiate claims for patent examination.',
        'Gave concrete clarity on technical writing that our academic curriculum never covered.'
      ]
    },
    {
      id: 'bmsit-bangalore',
      category: 'academic',
      name: 'BMS Institute of Technology: Growth Mindset, Ambiguity & 50 Failed Interviews',
      badge: 'Leadership Resilience',
      organization: 'BMSIT Bangalore',
      date: '2015 to 2018',
      reach: '500+ Engineers & Trainees',
      surveySubmissions: 120,
      ratingHighlights: [
        { label: 'Learning Breakthrough', value: '91.3%' },
        { label: 'Rated Mind-Blowing/Engaging', value: '70.0%' },
        { label: 'Delivered Seminars', value: '5' },
        { label: 'Total Student Reach', value: '500+' }
      ],
      leadershipContext:
        'Shared lessons from 50 failed interviews early in career to teach young engineers how to treat failure as feedback and build continuous learning habits.',
      verbatimQuotes: [
        'Really inspired by you sir. I learnt something new.',
        'The transparency about early career rejections and how to bounce back completely changed my perspective on interviews.'
      ]
    }
  ];

  const [selectedCategory, setSelectedCategory] = useState<'ALL' | 'PHILIPS' | 'AMAZON' | 'ACADEMIC'>('ALL');
  const [activeCohortId, setActiveCohortId] = useState<string>('philips-iwillcode');

  const filteredCohorts = evaluationCohorts.filter((c) => {
    if (selectedCategory === 'ALL') return true;
    if (selectedCategory === 'PHILIPS') return c.category === 'philips';
    if (selectedCategory === 'AMAZON') return c.category === 'amazon';
    if (selectedCategory === 'ACADEMIC') return c.category === 'academic';
    return true;
  });

  const activeCohort = filteredCohorts.find((c) => c.id === activeCohortId) || filteredCohorts[0] || evaluationCohorts[0];

  return (
    <section className="leadership-os-section" id="leadership-os">
      <div className="leadership-os-header">
        <div className="os-badge">
          <Users size={16} />
          <span>Leadership Operating System: Culture &amp; Talent Density</span>
        </div>
        <h2 className="leadership-os-title">
          How I Build Organizations: The Bar Raiser and Craftsmanship Model
        </h2>
        <p className="leadership-os-subtitle">
          Sustainable engineering excellence requires more than strong code. It requires an immutable hiring bar,
          relentless architectural discipline, and continuous investment in the next generation of engineers.
        </p>
      </div>

      {/* 3 Core Operating Pillars */}
      <div className="os-pillars-grid">
        {pillars.map((pillar) => {
          const Icon = pillar.icon;
          return (
            <div key={pillar.id} className="os-pillar-card">
              <div className="pillar-header">
                <div className="pillar-icon-box">
                  <Icon size={22} />
                </div>
                <span className="pillar-tag">{pillar.tag}</span>
              </div>

              <h3 className="pillar-title">{pillar.title}</h3>
              <p className="pillar-subtitle">{pillar.subtitle}</p>

              <div className="pillar-principles-list">
                {pillar.principles.map((principle, idx) => (
                  <div key={idx} className="principle-item">
                    <CheckCircle size={15} className="principle-bullet" />
                    <span>{principle}</span>
                  </div>
                ))}
              </div>

              <div className="pillar-impact-box">
                <strong>Verifiable Impact:</strong> {pillar.impact}
              </div>
            </div>
          );
        })}
      </div>

      {/* Enterprise Architectural Research and Governance Standards */}
      <div className="os-governance-section">
        <div className="os-governance-header">
          <div className="os-badge" style={{ color: '#a78bfa', background: 'rgba(167, 139, 250, 0.12)', borderColor: 'rgba(167, 139, 250, 0.25)' }}>
            <FileText size={16} />
            <span>Enterprise Research &amp; Governance Standards</span>
          </div>
          <h3 className="os-governance-title">
            Empirical Quality Audits and Architectural Reference Baselines
          </h3>
          <p className="os-governance-desc">
            Rigorous engineering governance requires verifiable empirical baselines. These institutional artifacts established corporate standards for software craftsmanship and CI/CD automation across global engineering divisions.
          </p>
        </div>

        <div className="os-governance-grid">
          {/* Card 1: 138-Project State of Craftsmanship Audit */}
          <div className="os-governance-card">
            <div className="governance-card-top">
              <div className="governance-icon-badge" style={{ color: '#38bdf8', background: 'rgba(56, 189, 248, 0.12)', borderColor: 'rgba(56, 189, 248, 0.25)' }}>
                <BarChart3 size={22} />
              </div>
              <span className="governance-tag">Global Empirical Audit (2023)</span>
            </div>

            <h4 className="governance-card-title">State of Software Craftsmanship: 138-Project Empirical Audit</h4>
            <div className="governance-card-scope">
              <strong>Scope:</strong> Innovation Excellence (IEX) / Software Excellence audit analyzing 138 active software engineering projects covering over 80% of Philips global engineering staff.
            </div>

            <div className="governance-key-metrics">
              <div className="gov-metric-item">
                <span className="gov-metric-num">138</span>
                <span className="gov-metric-lbl">Active Projects Audited</span>
              </div>
              <div className="gov-metric-item">
                <span className="gov-metric-num">&gt;80%</span>
                <span className="gov-metric-lbl">Global Developer Coverage</span>
              </div>
              <div className="gov-metric-item">
                <span className="gov-metric-num">94.1%</span>
                <span className="gov-metric-lbl">Manual Test Legacy Identified</span>
              </div>
              <div className="gov-metric-item">
                <span className="gov-metric-num">6 Mo</span>
                <span className="gov-metric-lbl">Avg Debt Payback Delay</span>
              </div>
            </div>

            <div className="governance-content-block">
              <div className="gov-block-label">Empirical Findings:</div>
              <ul className="gov-bullet-list">
                <li>Demonstrated direct correlation between unmonitored code rot, manual test dependencies, and critical regulatory CAPA failures in medical software.</li>
                <li>Identified systemic release blockers caused by 6-month debt repayment lag across enterprise business units.</li>
              </ul>
            </div>

            <div className="governance-content-block">
              <div className="gov-block-label">Systemic Intervention &amp; Mandate:</div>
              <ul className="gov-bullet-list">
                <li>Instituted automated architectural verification gates, CodeScene behavioral debt tracking, and deterministic build pipelines prior to production release.</li>
                <li>Shifted testing left to eliminate manual test bottlenecks and secure continuous audit readiness for medical regulatory bodies.</li>
              </ul>
            </div>

            <div className="governance-card-footer">
              <strong>Outcome:</strong> Delivered quantitative debt transparency to executive leadership and halted recurring regression escapes across core clinical product lines.
            </div>
          </div>

          {/* Card 2: CAO DevOps Reference Architecture */}
          <div className="os-governance-card">
            <div className="governance-card-top">
              <div className="governance-icon-badge" style={{ color: '#a78bfa', background: 'rgba(167, 139, 250, 0.12)', borderColor: 'rgba(167, 139, 250, 0.25)' }}>
                <Layers size={22} />
              </div>
              <span className="governance-tag" style={{ color: '#c084fc' }}>Enterprise CAO Architecture (Nov 2020)</span>
            </div>

            <h4 className="governance-card-title">Chief Architect Office: Enterprise DevOps Reference Architecture</h4>
            <div className="governance-card-scope">
              <strong>Authorship:</strong> Co-authored by Datta Vellal with Fellow Systems Architect, Principal Systems Architect; Reviewed by Enterprise Fellow Architect (Philips Global Architecture Council).
            </div>

            <div className="governance-key-metrics">
              <div className="gov-metric-item">
                <span className="gov-metric-num">100%</span>
                <span className="gov-metric-lbl">Standardized CI/CD Spec</span>
              </div>
              <div className="gov-metric-item">
                <span className="gov-metric-num">Multi-Cluster</span>
                <span className="gov-metric-lbl">Enterprise Deployment Scope</span>
              </div>
              <div className="gov-metric-item">
                <span className="gov-metric-num">IEC 62304</span>
                <span className="gov-metric-lbl">Traceable Build Provenance</span>
              </div>
              <div className="gov-metric-item">
                <span className="gov-metric-num">Zero</span>
                <span className="gov-metric-lbl">Environment Drift Variance</span>
              </div>
            </div>

            <div className="governance-content-block">
              <div className="gov-block-label">Default Trajectory:</div>
              <ul className="gov-bullet-list">
                <li>Disparate product engineering units maintained disconnected Jenkins and custom script toolchains, creating fragile releases and multi-week integration blockers.</li>
                <li>Lack of standardized container baselines led to environment drift and regulatory verification gaps.</li>
              </ul>
            </div>

            <div className="governance-content-block">
              <div className="gov-block-label">Architecture Decisions &amp; Intervention:</div>
              <ul className="gov-bullet-list">
                <li>Codified common pipeline architectures across enterprise clusters, establishing immutable Docker container build environments.</li>
                <li>Standardized automated static analysis, security vulnerability scanning, and binary artifact management for clinical compliance.</li>
              </ul>
            </div>

            <div className="governance-card-footer">
              <strong>Outcome:</strong> Unified disparate toolchains into a certified enterprise deployment pipeline, accelerating delivery velocity across multi-site medical systems.
            </div>
          </div>
        </div>
      </div>

      {/* Executive Masterclasses, Keynotes & 900+ Verified Evaluations */}
      <div className="os-evaluations-section" id="executive-evaluations">
        <div className="os-evaluations-header">
          <div className="os-badge" style={{ color: '#f59e0b', background: 'rgba(245, 158, 11, 0.12)', borderColor: 'rgba(245, 158, 11, 0.25)' }}>
            <GraduationCap size={16} />
            <span>Talent Multiplier: 10+ Years Unbroken Mentorship &amp; Teaching</span>
          </div>
          <h3 className="os-evaluations-title">
            Executive Masterclasses, Academic Pipelines &amp; 900+ Verified Evaluations
          </h3>
          <p className="os-evaluations-desc">
            Senior leadership requires continuous talent multiplication. Over the past decade, I have conducted over 50 technical masterclasses, workshops, and keynotes across Amazon internal engineering, global industry conferences, and premier academic institutions. Every engagement is measured against rigorous empirical feedback loops.
          </p>
        </div>

        {/* Volume & Quality Metrics Strip */}
        <div className="os-eval-metrics-strip">
          <div className="eval-metric-stat">
            <span className="eval-metric-value">50+</span>
            <span className="eval-metric-label">Keynotes &amp; Masterclasses</span>
            <span className="eval-metric-sub">15+ Institutions &amp; Global Forums</span>
          </div>
          <div className="eval-metric-stat">
            <span className="eval-metric-value">2,800+</span>
            <span className="eval-metric-label">Philips Internal Engagements</span>
            <span className="eval-metric-sub">Across 22 Global Engineering Cities</span>
          </div>
          <div className="eval-metric-stat">
            <span className="eval-metric-value">1,000+</span>
            <span className="eval-metric-label">Documented Survey Submissions</span>
            <span className="eval-metric-sub">Empirical Post-Session Evaluations</span>
          </div>
          <div className="eval-metric-stat">
            <span className="eval-metric-value">91.4%</span>
            <span className="eval-metric-label">Net Promoters: "I Will Code!"</span>
            <span className="eval-metric-sub">9.37 / 10 Score Across 105 Leads</span>
          </div>
          <div className="eval-metric-stat">
            <span className="eval-metric-value">4.64 / 5</span>
            <span className="eval-metric-label">Amazon Senpai Faculty Rating</span>
            <span className="eval-metric-sub">EE Scrum &amp; Product Ownership</span>
          </div>
          <div className="eval-metric-stat">
            <span className="eval-metric-value">8.9 / 10</span>
            <span className="eval-metric-label">Philips University Satisfaction</span>
            <span className="eval-metric-sub">33 Formal Sessions, 492 Learners</span>
          </div>
        </div>

        {/* Interactive Cohort Explorer */}
        <div className="os-eval-cohorts-container">
          <div className="cohorts-intro-bar">
            <div>
              <h4 className="cohorts-subheading">Verified Cohort Evaluations &amp; Attendee Feedback</h4>
              <p className="cohorts-subtext">Select an evaluation cohort to inspect verified survey ratings, leadership context, and verbatim attendee feedback.</p>
            </div>
            <span className="cohorts-count-badge">
              <Sparkles size={13} fill="#fbbf24" color="#fbbf24" /> {filteredCohorts.length} Cohorts Shown
            </span>
          </div>

          {/* Cohort Category Filter Tabs */}
          <div className="cohort-category-tabs">
            <button
              className={`cohort-category-tab ${selectedCategory === 'ALL' ? 'active' : ''}`}
              onClick={() => { setSelectedCategory('ALL'); setActiveCohortId(evaluationCohorts[0].id); }}
            >
              All Programs ({evaluationCohorts.length})
            </button>
            <button
              className={`cohort-category-tab ${selectedCategory === 'PHILIPS' ? 'active' : ''}`}
              onClick={() => { setSelectedCategory('PHILIPS'); setActiveCohortId('philips-iwillcode'); }}
            >
              Philips Internal Enablement (5)
            </button>
            <button
              className={`cohort-category-tab ${selectedCategory === 'AMAZON' ? 'active' : ''}`}
              onClick={() => { setSelectedCategory('AMAZON'); setActiveCohortId('amazon-senpai'); }}
            >
              Amazon Faculty (1)
            </button>
            <button
              className={`cohort-category-tab ${selectedCategory === 'ACADEMIC' ? 'active' : ''}`}
              onClick={() => { setSelectedCategory('ACADEMIC'); setActiveCohortId('sit-tumkur'); }}
            >
              Academic Talent Pipeline (5)
            </button>
          </div>

          {/* Cohort Selector Pills */}
          <div className="cohort-selector-bar">
            {filteredCohorts.map((cohort) => (
              <button
                key={cohort.id}
                className={`cohort-pill-btn ${activeCohort.id === cohort.id ? 'active' : ''}`}
                onClick={() => setActiveCohortId(cohort.id)}
              >
                <span className="pill-org">{cohort.organization}</span>
                <span className="pill-badge">{cohort.badge}</span>
              </button>
            ))}
          </div>

          {/* Active Cohort Detail Card */}
          {activeCohort && (
            <div className="cohort-detail-card">
              <div className="cohort-detail-top">
                <div>
                  <div className="cohort-tag-row">
                    <span className="cohort-badge">{activeCohort.badge}</span>
                    <span className="cohort-meta-item">{activeCohort.organization}</span>
                    <span className="cohort-meta-item">Timeline: {activeCohort.date}</span>
                    <span className="cohort-meta-item">Reach: {activeCohort.reach}</span>
                  </div>
                  <h4 className="cohort-title">{activeCohort.name}</h4>
                </div>
                <div className="cohort-responses-pill">
                  <BookOpen size={14} />
                  <span>{activeCohort.surveySubmissions} Verified Submissions</span>
                </div>
              </div>

              {/* Rating Highlights Grid */}
              <div className="cohort-ratings-grid">
                {activeCohort.ratingHighlights.map((r, rIdx) => (
                  <div key={rIdx} className="cohort-rating-box">
                    <div className="rating-box-val">{r.value}</div>
                    <div className="rating-box-lbl">{r.label}</div>
                  </div>
                ))}
              </div>

              {/* Leadership Operating Context */}
              <div className="cohort-leadership-context">
                <strong>Leadership Context &amp; Purpose:</strong> {activeCohort.leadershipContext}
              </div>

              {/* Verbatim Attendee Feedback */}
              <div className="cohort-quotes-section">
                <div className="cohort-quotes-label">
                  Verbatim Attendee Feedback:
                </div>
                <div className="cohort-quotes-grid">
                  {activeCohort.verbatimQuotes.map((q, qIdx) => (
                    <div key={qIdx} className="cohort-quote-card">
                      <p>"{q}"</p>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* University and Community Giveback Banner */}
      <div className="university-pipeline-card">
        <div className="pipeline-header">
          <div className="pipeline-title-group">
            <BookOpen size={20} className="pipeline-icon" />
            <div>
              <h3>Academic Outreach and Talent Pipeline Incubation</h3>
              <p>Continuous commitment to engineering education and community giveback across leading academic institutions.</p>
            </div>
          </div>
          <span className="pipeline-metric-badge">
            <Sparkles size={14} /> 10+ Years Active Outreach
          </span>
        </div>

        <div className="workshops-grid">
          {universityWorkshops.map((w, idx) => (
            <div key={idx} className="workshop-pill">
              <div className="workshop-institution">{w.institution}</div>
              <div className="workshop-topic">{w.topic}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
