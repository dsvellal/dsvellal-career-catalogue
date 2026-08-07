"""Build the curated, public-safe dataset for the eight-view Journey Atlas.

This is deliberately not a generic summarizer.  The repository contains private
personal and corporate material, so publication is an editorial boundary: only
reviewed aggregate claims, attributed public recommendations, and opaque source
IDs are emitted.  Raw evidence content and local filenames never enter the browser
bundle.
"""

# Narrative copy and evidence paths are intentionally kept as intact string
# literals so the generated JSON remains easy to review beside this source.
# ruff: noqa: E501

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = REPO_ROOT / "viz" / "src" / "data" / "journey.json"
DEFAULT_REPORT = REPO_ROOT / "data" / "journey-analysis.md"


def _source_id(path: str) -> str:
    """Return a stable public ID without revealing the local evidence filename."""
    return f"src_{hashlib.sha256(path.encode('utf-8')).hexdigest()[:12]}"


def evidence(path: str, tier: str, supports: str) -> dict[str, Any]:
    reference: dict[str, Any] = {
        "evidence_file": path,
        "source_id": _source_id(path),
        "tier": tier,
        "supports": supports,
    }
    year = re.search(r"(?:^|/)((?:19|20)\d{2})(?:/|[-_])", path)
    if year:
        reference["year"] = int(year.group(1))
    return reference


def metric(
    metric_id: str,
    label: str,
    value: str | int | float,
    display: str,
    source: list[dict[str, Any]],
    *,
    unit: str = "",
    period: str = "",
    caveats: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "id": metric_id,
        "label": label,
        "value": value,
        "unit": unit,
        "display": display,
        "period": period,
        "evidence": source,
        "caveat_labels": caveats or [],
    }


RESUME_2026 = "data/evidence/2026/individual/112-resume-2026-latest-authoritative.md"
CAREER_SYNTHESIS = "data/evidence/sessions/resume-career-progression.md"
SESSION_EVIDENCE = "data/evidence/sessions/SESSION-EVIDENCE.md"
SESSION_STATS = "data/evidence/sessions/summary_stats.json"
STUDENT_FEEDBACK = "data/evidence/sessions/student-feedback/STUDENT-FEEDBACK-EVIDENCE.md"
TALKS = "data/evidence/sessions/givebacks-talks-spreadsheet.md"
AWARDS = "data/evidence/sessions/awards-recognition-citations-master.md"
BOOK_PROGRAM = "data/evidence/2025/individual/075-social-giveback-book-distribution-program.md"
CONNECT_2019 = "data/evidence/2019/individual/182-dotconnects-2019-annual-summary.md"
CONNECT_2020 = "data/evidence/2020/individual/089-dotconnects-annual-summary-2020.md"
CONNECT_2021 = "data/evidence/2021/individual/019-connect-annual-summary-2021.md"
AI_2025 = "data/evidence/2025/ai-genai-leadership.md"
SUTRA = "data/evidence/2026/individual/111-xite-special-edition-18k-hours-3-5m-sutra-impact.md"


RECOMMENDATIONS: list[tuple[int, str, str, str]] = [
    (
        2012,
        "Mahesh Paradkar",
        "IBM",
        "data/evidence/2012/individual/001-linkedin-recommendation-mahesh-paradkar.md",
    ),
    (
        2012,
        "Brijesh Krishnan",
        "IBM",
        "data/evidence/2012/individual/002-linkedin-recommendation-brijesh-krishnan.md",
    ),
    (
        2012,
        "Praveen Kumar Vaidyanathan",
        "IBM",
        "data/evidence/2012/individual/003-linkedin-recommendation-praveen-kumar-v.md",
    ),
    (
        2013,
        "Gaurav Gupta",
        "IBM",
        "data/evidence/2013/individual/001-linkedin-recommendation-gaurav-gupta.md",
    ),
    (
        2013,
        "Lohith Ravi Naidu",
        "IBM",
        "data/evidence/2013/individual/002-linkedin-recommendation-lohith-ravi-naidu.md",
    ),
    (
        2014,
        "Rajaraman Hariharan",
        "Exeter",
        "data/evidence/2014/individual/001-linkedin-recommendation-rajaraman-hariharan.md",
    ),
    (
        2014,
        "Dr Arun Kumar B R",
        "Academic community",
        "data/evidence/2014/individual/002-linkedin-recommendation-dr-arun-kumar-br.md",
    ),
    (
        2015,
        "Manohar Veeraiah",
        "Exeter",
        "data/evidence/2015/individual/001-linkedin-recommendation-manohar-veeraiah.md",
    ),
    (
        2015,
        "Vinay S V",
        "Exeter",
        "data/evidence/2015/individual/002-linkedin-recommendation-vinay-sv.md",
    ),
    (
        2015,
        "Robert Parks",
        "Exeter",
        "data/evidence/2015/individual/003-linkedin-recommendation-robert-parks.md",
    ),
    (
        2015,
        "Srisankaraswaminathan J V",
        "Exeter",
        "data/evidence/2015/individual/004-linkedin-recommendation-srisankaraswaminathan-jv.md",
    ),
    (
        2017,
        "Jeffin Manuel",
        "Amazon",
        "data/evidence/2017/individual/001-linkedin-recommendation-jeffin-manuel.md",
    ),
    (
        2019,
        "Rajesh Kumar",
        "Philips",
        "data/evidence/2019/individual/183-linkedin-recommendation-rajesh-kumar.md",
    ),
    (
        2019,
        "Rajesh Manghani",
        "Philips",
        "data/evidence/2019/individual/184-linkedin-recommendation-rajesh-manghani.md",
    ),
    (
        2020,
        "Sannihith Reddy P",
        "Philips",
        "data/evidence/2020/individual/142-linkedin-recommendation-sannihith-reddy.md",
    ),
    (
        2023,
        "NaveenKumar V R",
        "Philips",
        "data/evidence/2023/individual/018-linkedin-recommendation-naveenkumar-vr.md",
    ),
    (
        2024,
        "Rafael Vaz",
        "Philips",
        "data/evidence/2024/individual/010-linkedin-recommendation-rafael-vaz.md",
    ),
    (
        2025,
        "Fernando Vieira",
        "Philips",
        "data/evidence/2025/individual/070-linkedin-recommendation-fernando-vieira.md",
    ),
    (
        2025,
        "Ian Watson",
        "Philips",
        "data/evidence/2025/individual/071-linkedin-recommendation-ian-watson.md",
    ),
    (
        2025,
        "Rob Nicholson",
        "Philips",
        "data/evidence/2025/individual/072-linkedin-recommendation-rob-nicholson.md",
    ),
]


def recommendation_evidence() -> list[dict[str, str]]:
    return [
        evidence(path, "corroborated", f"Dated, attributed recommendation from {name}")
        for _, name, _, path in RECOMMENDATIONS
    ]


def build_journey_data() -> dict[str, Any]:
    resume_ref = [evidence(RESUME_2026, "self-reported", "Employment chronology and role history")]
    session_ref = [
        evidence(
            SESSION_EVIDENCE,
            "corroborated",
            "Aggregate of 90 session workbooks and participant feedback",
        ),
        evidence(SESSION_STATS, "corroborated", "Machine-readable aggregate statistics"),
    ]
    sutra_ref = [evidence(SUTRA, "documented", "Team-authored 2026 delivery and showcase metrics")]

    eras = [
        {
            "id": "ibm",
            "label": "Builder becomes a technical citizen",
            "organization": "IBM",
            "role": "Application Developer · Technical Community Leader",
            "start": 2007,
            "end": 2013,
            "summary": "Built deep middleware and integration craft while stepping beyond delivery into patents, papers, HackDays, technical community leadership, and teaching.",
            "capabilities": [
                "software engineering",
                "integration",
                "technical writing",
                "community leadership",
            ],
            "impact_claims": [
                "Led end-to-end delivery early in career",
                "Won IBM India HackDay 8 in Pune",
                "Co-invented two US patents",
            ],
            "evidence": resume_ref
            + [
                evidence(
                    "data/evidence/2008/individual/004-ibm-bravo-internship-management.md",
                    "documented",
                    "Early end-to-end ownership and internship leadership",
                ),
                evidence(
                    "data/evidence/2010/individual/001-ibm-hackday8-winner.md",
                    "corroborated",
                    "IBM India HackDay 8 first-place record",
                ),
                evidence(AWARDS, "documented", "Patent, award, and public-citation index"),
            ],
            "caveat_labels": ["employment_dates_self_reported"],
        },
        {
            "id": "exeter",
            "label": "Technical anchor becomes team enabler",
            "organization": "Exeter Group",
            "role": "Senior Lead — Software Development",
            "start": 2013,
            "end": 2015,
            "summary": "Took responsibility for complex healthcare software, releases, engineering practices, and a roughly twenty-person delivery group while creating learning rituals around the work.",
            "capabilities": [
                "healthcare software",
                "delivery leadership",
                "quality systems",
                "facilitation",
            ],
            "impact_claims": [
                "Became the team's linchpin for high-complexity work",
                "Combined release ownership with coaching and technical forums",
            ],
            "evidence": resume_ref
            + [
                evidence(
                    "data/evidence/2015/individual/006-exeter-ppm-q1-2015-performance-review.md",
                    "corroborated",
                    "Manager assessment of complexity, quality, and team role",
                ),
                evidence(
                    "data/evidence/2014/individual/002-exeter-texeter-6months-letter.md",
                    "documented",
                    "Internal technical learning community continuity",
                ),
            ],
            "caveat_labels": ["employment_dates_self_reported"],
        },
        {
            "id": "amazon",
            "label": "Scale sharpens product judgment",
            "organization": "Amazon",
            "role": "Software Development Engineer II",
            "start": 2016,
            "end": 2018,
            "summary": "Worked at marketplace scale, improved operational mechanisms, raised the hiring bar, and turned hard-won delivery knowledge into onboarding and workshop systems for others.",
            "capabilities": [
                "distributed systems",
                "operational excellence",
                "product ownership",
                "hiring",
            ],
            "impact_claims": [
                "Contributed to a 1.9-billion-ASIN backfill across 12 marketplaces",
                "Conducted 68 interviews in 18 months",
                "Reduced onboarding from one week to two days",
            ],
            "evidence": [
                evidence(
                    "data/evidence/2018/individual/019-resume-2018-amazon-work-examples.md",
                    "self-reported",
                    "Detailed first-party work examples and scale metrics",
                ),
                evidence(
                    "data/evidence/2018/individual/005-amazon-hwefficiency-dollars-saved.md",
                    "documented",
                    "Hardware-efficiency savings record",
                ),
                evidence(
                    "data/evidence/2017/individual/009-amazon-on-boarding-guide.md",
                    "documented",
                    "Reusable onboarding mechanism",
                ),
            ],
            "caveat_labels": ["employment_dates_self_reported", "mixed_attribution"],
        },
        {
            "id": "philips-india",
            "label": "Practice scales into transformation",
            "organization": "Philips India",
            "role": "Competency Specialist — Software Excellence",
            "start": 2018,
            "end": 2021,
            "summary": "Moved from improving code to improving the system around code: quality programs, communities, standards, mentoring, and a demand-driven network across roles, departments, and geographies.",
            "capabilities": [
                "software excellence",
                "organizational change",
                "regulated quality",
                "influence without authority",
            ],
            "impact_claims": [
                "Built a broad one-to-one influence network",
                "Scaled code-quality and Bar Raiser practices",
                "Received the CTO Outstanding Achievement Award",
            ],
            "evidence": [
                evidence(
                    "data/evidence/2021/individual/044-resume-2021-philips-competency-lead.md",
                    "self-reported",
                    "Role, transformation scope, and business metrics",
                ),
                evidence(CONNECT_2020, "documented", "Annual .connect reach and demand record"),
                evidence(
                    "data/evidence/2021/individual/001-outstanding-achievement-award-cto-2021.md",
                    "corroborated",
                    "Formal CTO recognition",
                ),
            ],
            "caveat_labels": ["employment_dates_self_reported", "mixed_attribution"],
        },
        {
            "id": "philips-na",
            "label": "Enterprise multiplier enters the AI era",
            "organization": "Philips North America",
            "role": "Software Competency Lead — Innovation Engineering",
            "start": 2021,
            "end": 2026,
            "summary": "Connected global platform reliability, regulated-software rigor, DORA and continuous value delivery, AI enablement, and AI-native traceability into an enterprise transformation portfolio.",
            "capabilities": [
                "enterprise platforms",
                "digital transformation",
                "AI-native engineering",
                "executive translation",
            ],
            "impact_claims": [
                "Served a global software community",
                "Led AI and continuous-delivery capability programs",
                "Helped build a quality-gated AI traceability platform",
            ],
            "evidence": resume_ref
            + [
                evidence(
                    "data/evidence/2025/individual/071-linkedin-recommendation-ian-watson.md",
                    "corroborated",
                    "Peer testimony on transformation through influence",
                ),
                evidence(
                    "data/evidence/2025/individual/072-linkedin-recommendation-rob-nicholson.md",
                    "corroborated",
                    "Direct-manager testimony on global leadership and engineering depth",
                ),
                evidence(
                    SUTRA, "documented", "AI-native traceability outcomes and quality controls"
                ),
            ],
            "caveat_labels": ["employment_dates_self_reported", "team_attribution"],
        },
    ]

    service_lane = {
        "label": "Teaching, community, and stewardship",
        "start": 2010,
        "summary": "A parallel practice of teaching and service has continued across employers, locations, and life transitions—evidence that contribution is a personal operating principle, not a job-title artifact.",
        "milestones": [
            {
                "id": "yoga-2010",
                "year": 2010,
                "title": "First recorded community talk: practical yoga",
                "summary": "A non-technical college session established the service lane.",
                "metrics": [],
                "evidence": [evidence(TALKS, "documented", "First dated giveback session")],
                "caveat_labels": [],
            },
            {
                "id": "t2e-2011",
                "year": 2011,
                "title": "Technical education workshops",
                "summary": "Hands-on T2E workshops brought industry craft into colleges.",
                "metrics": [],
                "evidence": [evidence(TALKS, "documented", "Dated participant and venue records")],
                "caveat_labels": [],
            },
            {
                "id": "college-2013",
                "year": 2013,
                "title": "College teaching expands",
                "summary": "Technical, career, and yoga sessions developed into a long-running feedback-backed practice.",
                "metrics": [],
                "evidence": [
                    evidence(STUDENT_FEEDBACK, "corroborated", "Student response archive begins")
                ],
                "caveat_labels": [],
            },
            {
                "id": "books-2014",
                "year": 2014,
                "title": "Rural book-distribution program begins",
                "summary": "A personal initiative grew into a recurring, network-supported education program.",
                "metrics": [],
                "evidence": [evidence(BOOK_PROGRAM, "documented", "Ten annual program ledgers")],
                "caveat_labels": ["public_safe_aggregate"],
            },
            {
                "id": "conference-2019",
                "year": 2019,
                "title": "Teaching reaches enterprise scale",
                "summary": "Software excellence talks, workshops, and .connect translated practice across teams.",
                "metrics": [],
                "evidence": [
                    evidence(TALKS, "documented", "Conference and workshop records"),
                    evidence(CONNECT_2019, "documented", "Annual connection record"),
                ],
                "caveat_labels": [],
            },
            {
                "id": "virtual-2021",
                "year": 2021,
                "title": "Global virtual reach",
                "summary": "Observability, shift-left, interviews, and community sessions crossed geographic boundaries.",
                "metrics": [],
                "evidence": [
                    evidence(TALKS, "documented", "Virtual and global conference sessions"),
                    evidence(CONNECT_2021, "documented", "Global participant touchpoints"),
                ],
                "caveat_labels": ["touchpoints_not_unique_people"],
            },
            {
                "id": "ai-teaching-2025",
                "year": 2025,
                "title": "AI literacy becomes the teaching frontier",
                "summary": "Copilot, prompt engineering, DORA, and continuous value delivery became repeatable learning programs.",
                "metrics": [],
                "evidence": [
                    evidence(AI_2025, "documented", "AI enablement program evidence"),
                    evidence(
                        SESSION_EVIDENCE, "corroborated", "Session feedback and topic evolution"
                    ),
                ],
                "caveat_labels": [],
            },
            {
                "id": "service-2026",
                "year": 2026,
                "title": "Professional and social programs keep compounding",
                "summary": "AI teaching and the book program both reached new documented peaks.",
                "metrics": [],
                "evidence": [
                    evidence(SUTRA, "documented", "AI platform showcase"),
                    evidence(BOOK_PROGRAM, "documented", "2026 aggregate program record"),
                ],
                "caveat_labels": ["public_safe_aggregate"],
            },
        ],
        "metrics": [
            metric(
                "talks",
                "Recorded giveback talks",
                50,
                "50",
                [evidence(TALKS, "documented", "Complete dated talks spreadsheet")],
                period="2010–2021",
            ),
            metric(
                "talk-reach",
                "Recorded participants",
                3732,
                "3,732",
                [evidence(TALKS, "documented", "Participant counts by session")],
                period="2010–2021",
                caveats=["participant_counts_not_unique"],
            ),
            metric(
                "service-years",
                "Book-program years active",
                10,
                "10 years",
                [evidence(BOOK_PROGRAM, "documented", "Annual program ledgers")],
                period="2014–2026",
                caveats=["public_safe_aggregate"],
            ),
        ],
        "evidence": [
            evidence(TALKS, "documented", "Eleven-year giveback record"),
            evidence(BOOK_PROGRAM, "documented", "Ten active years of social service"),
        ],
        "caveat_labels": ["curated_milestones"],
    }

    capability_sources = {
        "ibm": eras[0]["evidence"],
        "exeter": eras[1]["evidence"],
        "amazon": eras[2]["evidence"],
        "philips-india": eras[3]["evidence"],
        "philips-na": eras[4]["evidence"],
    }

    def stage(
        era_id: str, level: int, label: str, caveats: list[str] | None = None
    ) -> dict[str, Any]:
        return {
            "era_id": era_id,
            "level": level,
            "label": label,
            "evidence": capability_sources[era_id][:2],
            "caveat_labels": caveats or [],
        }

    capability_streams = [
        {
            "id": "engineering",
            "label": "Engineering craft",
            "color": "#2563a8",
            "stages": [
                stage("ibm", 2, "Hands-on foundation"),
                stage("exeter", 3, "Technical anchor"),
                stage("amazon", 4, "Scale and operations"),
                stage("philips-india", 4, "Craft as a system"),
                stage("philips-na", 5, "AI-native, quality-gated craft"),
            ],
        },
        {
            "id": "systems",
            "label": "Systems & platforms",
            "color": "#0d7a52",
            "stages": [
                stage("ibm", 2, "Enterprise integration"),
                stage("exeter", 3, "Healthcare delivery systems"),
                stage("amazon", 5, "Marketplace-scale systems"),
                stage("philips-india", 4, "Reusable engineering platforms"),
                stage("philips-na", 5, "Global regulated platforms"),
            ],
        },
        {
            "id": "quality",
            "label": "Quality & regulation",
            "color": "#b84c1a",
            "stages": [
                stage("ibm", 1, "Disciplined delivery"),
                stage("exeter", 3, "Quality ownership"),
                stage("amazon", 4, "Operational mechanisms"),
                stage("philips-india", 5, "Quality transformation"),
                stage("philips-na", 5, "Compliance as continuous evidence"),
            ],
        },
        {
            "id": "transformation",
            "label": "Transformation leadership",
            "color": "#b57b00",
            "stages": [
                stage("ibm", 2, "Community initiative"),
                stage("exeter", 3, "Team practice change"),
                stage("amazon", 3, "Mechanism building"),
                stage("philips-india", 5, "Organization-wide programs"),
                stage("philips-na", 5, "Enterprise portfolio influence"),
            ],
        },
        {
            "id": "people",
            "label": "Coaching & influence",
            "color": "#6b46b0",
            "stages": [
                stage("ibm", 2, "Interns and technical community"),
                stage("exeter", 4, "Twenty-person leadership"),
                stage("amazon", 4, "Hiring and onboarding"),
                stage("philips-india", 5, "Demand-driven .connect network"),
                stage("philips-na", 5, "Executive-to-developer translation"),
            ],
        },
        {
            "id": "ai",
            "label": "AI-native engineering",
            "color": "#b83d6b",
            "stages": [
                stage("amazon", 1, "Automation mindset"),
                stage("philips-india", 2, "Data-led engineering systems"),
                stage(
                    "philips-na", 5, "AI delivery with traceability and gates", ["team_attribution"]
                ),
            ],
        },
    ]

    impact_ledger = [
        {
            "id": "amazon-scale",
            "scope": "individual",
            "category": "individual-to-team engineering",
            "title": "Marketplace-scale migration",
            "statement": "Contributed engineering and operational mechanisms to a backfill spanning 1.9 billion ASINs across 12 marketplaces.",
            "metrics": [
                metric(
                    "asins",
                    "ASINs processed",
                    1_900_000_000,
                    "1.9B",
                    [
                        evidence(
                            "data/evidence/2018/individual/019-resume-2018-amazon-work-examples.md",
                            "self-reported",
                            "Detailed work-example scale",
                        )
                    ],
                    period="Amazon era",
                    caveats=["self_reported", "team_attribution"],
                )
            ],
            "evidence": [
                evidence(
                    "data/evidence/2018/individual/019-resume-2018-amazon-work-examples.md",
                    "self-reported",
                    "First-party work example",
                )
            ],
            "caveat_labels": ["team_attribution"],
        },
        {
            "id": "hiring-onboarding",
            "scope": "team",
            "category": "team capability",
            "title": "Hiring judgment becomes a reusable system",
            "statement": "Conducted 68 interviews in 18 months and converted onboarding knowledge from a one-week path into a two-day guide-led experience.",
            "metrics": [
                metric(
                    "interviews",
                    "Interviews",
                    68,
                    "68",
                    [
                        evidence(
                            "data/evidence/2018/individual/019-resume-2018-amazon-work-examples.md",
                            "self-reported",
                            "Interview count and period",
                        )
                    ],
                    period="18 months",
                    caveats=["self_reported"],
                )
            ],
            "evidence": [
                evidence(
                    "data/evidence/2017/individual/009-amazon-on-boarding-guide.md",
                    "documented",
                    "Onboarding mechanism",
                ),
                evidence(
                    "data/evidence/2018/individual/019-resume-2018-amazon-work-examples.md",
                    "self-reported",
                    "Before/after and interview count",
                ),
            ],
            "caveat_labels": ["mixed_evidence_tiers"],
        },
        {
            "id": "philips-value",
            "scope": "organization",
            "category": "organizational business impact",
            "title": "Engineering excellence tied to business value",
            "statement": "Career documents attribute more than €2.1M in realized savings to the Philips India transformation portfolio.",
            "metrics": [
                metric(
                    "savings",
                    "Realized savings",
                    2.1,
                    "€2.1M+",
                    [
                        evidence(
                            CAREER_SYNTHESIS, "self-reported", "Resume-derived cumulative impact"
                        )
                    ],
                    period="Philips India",
                    caveats=["self_reported", "portfolio_attribution", "currency_context"],
                )
            ],
            "evidence": [
                evidence(
                    "data/evidence/2021/individual/044-resume-2021-philips-competency-lead.md",
                    "self-reported",
                    "First-party business-impact claims",
                )
            ],
            "caveat_labels": ["portfolio_attribution", "self_reported"],
        },
        {
            "id": "global-platform",
            "scope": "ecosystem",
            "category": "enterprise platform",
            "title": "Global platforms as an engineering product",
            "statement": "Resume records describe platforms serving 7,000+ engineers with 99.999% availability.",
            "metrics": [
                metric(
                    "engineers",
                    "Engineers served",
                    7000,
                    "7,000+",
                    [
                        evidence(
                            CAREER_SYNTHESIS,
                            "self-reported",
                            "Resume-derived global platform reach",
                        )
                    ],
                    caveats=["self_reported", "population_not_active_users"],
                )
            ],
            "evidence": resume_ref,
            "caveat_labels": ["self_reported", "population_not_active_users"],
        },
        {
            "id": "learning-system",
            "scope": "organization",
            "category": "organizational people capability",
            "title": "Learning measured at the point of experience",
            "statement": "Ninety facilitated sessions generated 1,183 responses and a normalized 4.3/5 average across eight years.",
            "metrics": [
                metric(
                    "responses",
                    "Participant responses",
                    1183,
                    "1,183",
                    session_ref,
                    period="2018–2026",
                )
            ],
            "evidence": session_ref,
            "caveat_labels": ["responses_not_attendance"],
        },
        {
            "id": "connect-system",
            "scope": "ecosystem",
            "category": "enterprise influence",
            "title": "Influence made observable through .connect",
            "statement": "A one-to-one engagement practice reached 778 unique people across 26 cities and 74 departments in 2020 alone.",
            "metrics": [
                metric(
                    "connect-people",
                    "Unique people",
                    778,
                    "778",
                    [evidence(CONNECT_2020, "documented", "Annual unique-participant rollup")],
                    period="2020",
                )
            ],
            "evidence": [
                evidence(
                    CONNECT_2020,
                    "documented",
                    "Annual interaction, role, department, and city rollups",
                )
            ],
            "caveat_labels": ["period_specific"],
        },
        {
            "id": "sutra",
            "scope": "ecosystem",
            "category": "enterprise AI transformation",
            "title": "AI speed held behind quality gates",
            "statement": "The Sutra team reported 90%+ traceability improvement, 3× development speed, roughly 80% AI-generated code, and a 400+ attendee showcase while enforcing continuous quality gates.",
            "metrics": [
                metric(
                    "traceability",
                    "Traceability improvement",
                    90,
                    "90%+",
                    sutra_ref,
                    period="2026",
                    caveats=["team_attribution"],
                )
            ],
            "evidence": sutra_ref,
            "caveat_labels": ["team_attribution", "initiative_specific"],
        },
        {
            "id": "book-program",
            "scope": "community",
            "category": "community service",
            "title": "Trust mobilized for rural education",
            "statement": "A personally organized book-distribution program sustained ten active years and grew annual contributions 13.3× while keeping donor details private.",
            "metrics": [
                metric(
                    "book-total",
                    "Funds mobilized",
                    1_972_381,
                    "₹19.72L",
                    [evidence(BOOK_PROGRAM, "documented", "Aggregate of ten annual ledgers")],
                    period="2014–2026",
                    caveats=["public_safe_aggregate", "currency_context"],
                )
            ],
            "evidence": [
                evidence(BOOK_PROGRAM, "documented", "Program totals, continuity, and growth")
            ],
            "caveat_labels": ["public_safe_aggregate"],
        },
    ]

    recommendation_manifest = [
        {
            "id": f"recommendation-{index:02d}",
            "year": year,
            "person": name,
            "organization": organization,
            "evidence": [evidence(path, "corroborated", "Dated, attributed recommendation")],
            "caveat_labels": ["selected_evidence"],
        }
        for index, (year, name, organization, path) in enumerate(RECOMMENDATIONS, start=1)
    ]

    quotes = [
        {
            "id": "early-leadership",
            "year": 2012,
            "person": "Brijesh Krishnan",
            "role": "IBM colleague",
            "organization": "IBM",
            "quote": "He had, in a very early stage of his career, started getting involved in project initiatives, mentoring interns and technical vitality activities, which showed his leadership capabilities.",
            "evidence": [
                evidence(
                    "data/evidence/2012/individual/002-linkedin-recommendation-brijesh-krishnan.md",
                    "corroborated",
                    "Public attributed recommendation",
                )
            ],
            "caveat_labels": ["light_grammar_edit"],
        },
        {
            "id": "linchpin",
            "year": 2015,
            "person": "Exeter performance reviewer",
            "role": "Manager review",
            "organization": "Exeter",
            "quote": "Handling complexity is now an expectation from Datta and … the key reason for him being a linchpin in the team.",
            "evidence": [
                evidence(
                    "data/evidence/2015/individual/006-exeter-ppm-q1-2015-performance-review.md",
                    "corroborated",
                    "Direct manager-review quotation",
                )
            ],
            "caveat_labels": ["excerpted_quote"],
        },
        {
            "id": "improvement",
            "year": 2020,
            "person": "Robert Van Lieshout",
            "role": "Product Owner",
            "organization": "Philips",
            "quote": "I cannot think of an improvement area for Datta.",
            "evidence": [
                evidence(
                    "data/evidence/2020/individual/077-comprehensive-impact-2018-2020-quantified.md",
                    "corroborated",
                    "Attributed peer quotation retained in impact record",
                )
            ],
            "caveat_labels": ["selected_evidence"],
        },
        {
            "id": "values",
            "year": 2020,
            "person": "Sannihith Reddy P",
            "role": "Mentee and colleague",
            "organization": "Philips",
            "quote": "Best part about Datta is he teaches skills with values.",
            "evidence": [
                evidence(
                    "data/evidence/2020/individual/142-linkedin-recommendation-sannihith-reddy.md",
                    "corroborated",
                    "Public attributed recommendation",
                )
            ],
            "caveat_labels": ["light_grammar_edit"],
        },
        {
            "id": "changed",
            "year": 2023,
            "person": "NaveenKumar V R",
            "role": "Mentee and colleague",
            "organization": "Philips",
            "quote": "Your technical and personal advice and support have been invaluable to me. I can't say how much it changed me as a person.",
            "evidence": [
                evidence(
                    "data/evidence/2023/individual/018-linkedin-recommendation-naveenkumar-vr.md",
                    "corroborated",
                    "Public attributed recommendation",
                )
            ],
            "caveat_labels": ["selected_evidence"],
        },
        {
            "id": "influence",
            "year": 2025,
            "person": "Ian Watson",
            "role": "Transformation peer",
            "organization": "Philips",
            "quote": "Datta is a master of leading digital transformation through influence.",
            "evidence": [
                evidence(
                    "data/evidence/2025/individual/071-linkedin-recommendation-ian-watson.md",
                    "corroborated",
                    "Public attributed recommendation",
                )
            ],
            "caveat_labels": ["selected_evidence"],
        },
        {
            "id": "natural-leader",
            "year": 2025,
            "person": "Rob Nicholson",
            "role": "Direct manager",
            "organization": "Philips",
            "quote": "Datta is a natural leader who inspires and motivates people across all levels, regardless of reporting lines, seniority, or team boundaries.",
            "evidence": [
                evidence(
                    "data/evidence/2025/individual/072-linkedin-recommendation-rob-nicholson.md",
                    "corroborated",
                    "Public attributed direct-manager recommendation",
                )
            ],
            "caveat_labels": ["selected_evidence"],
        },
    ]

    respect = {
        "recommendation_count": len(recommendation_manifest),
        "recommendation_manifest": recommendation_manifest,
        "quotes": quotes,
        "recognitions": [
            {
                "id": "hackday",
                "year": 2010,
                "title": "IBM India HackDay 8 — Pune first place",
                "evidence": [
                    evidence(
                        "data/evidence/2010/individual/001-ibm-hackday8-winner.md",
                        "corroborated",
                        "Award record",
                    )
                ],
                "caveat_labels": [],
            },
            {
                "id": "rtle",
                "year": 2010,
                "title": "Most influential member, IBM Technical Experts Council India",
                "evidence": [
                    evidence(
                        "data/evidence/2010/individual/005-ibm-rtle-2010-award.md",
                        "corroborated",
                        "Award record",
                    )
                ],
                "caveat_labels": [],
            },
            {
                "id": "amazon",
                "year": 2017,
                "title": "TRMS Spot and Zeus awards",
                "evidence": [
                    evidence(
                        "data/evidence/2017/individual/001-amazon-trms-spot-award.md",
                        "corroborated",
                        "Award record",
                    ),
                    evidence(
                        "data/evidence/2017/individual/002-amazon-trms-zeus-award.md",
                        "corroborated",
                        "Team award record",
                    ),
                ],
                "caveat_labels": ["team_attribution"],
            },
            {
                "id": "cto",
                "year": 2021,
                "title": "Philips CTO Outstanding Achievement Award",
                "evidence": [
                    evidence(
                        "data/evidence/2021/individual/001-outstanding-achievement-award-cto-2021.md",
                        "corroborated",
                        "Formal award record",
                    )
                ],
                "caveat_labels": [],
            },
            {
                "id": "impact-makers",
                "year": 2026,
                "title": "Sutra team recognized as Impact Makers",
                "evidence": [
                    evidence(
                        "data/evidence/2026/individual/088-sutra-team-recognized-as-impact-makers-at-ien-global-town-hall.md",
                        "corroborated",
                        "Team recognition record",
                    )
                ],
                "caveat_labels": ["team_attribution"],
            },
        ],
        "evidence": recommendation_evidence()
        + [evidence(AWARDS, "documented", "Master recognition index")],
        "caveat_labels": ["selected_evidence"],
    }

    influence = {
        "annual_connects": [
            {
                "id": "connect-2019",
                "year": 2019,
                "connects": 341,
                "unique_people": 236,
                "display": "236 unique people",
                "evidence": [evidence(CONNECT_2019, "documented", "Annual program rollup")],
                "caveat_labels": ["period_specific"],
            },
            {
                "id": "connect-2020",
                "year": 2020,
                "connects": 2731,
                "unique_people": 778,
                "display": "778 unique people",
                "evidence": [evidence(CONNECT_2020, "documented", "Annual program rollup")],
                "caveat_labels": ["period_specific"],
            },
            {
                "id": "connect-2021",
                "year": 2021,
                "connects": 575,
                "people": 2975,
                "display": "2,975 touchpoints",
                "evidence": [
                    evidence(CONNECT_2021, "documented", "Annual participant-touchpoint rollup")
                ],
                "caveat_labels": ["touchpoints_not_unique_people"],
            },
        ],
        "reach_dimensions": [
            {
                "id": "cities",
                "label": "Cities reached in 2020",
                "value": 26,
                "evidence": [evidence(CONNECT_2020, "documented", "Geographic rollup")],
                "caveat_labels": ["period_specific"],
            },
            {
                "id": "departments",
                "label": "Departments reached in 2020",
                "value": 74,
                "evidence": [evidence(CONNECT_2020, "documented", "Department rollup")],
                "caveat_labels": ["period_specific"],
            },
            {
                "id": "roles",
                "label": "Role categories reached in 2020",
                "value": 45,
                "evidence": [evidence(CONNECT_2020, "documented", "Role rollup")],
                "caveat_labels": ["period_specific"],
            },
            {
                "id": "demand",
                "label": "Average share initiated by others",
                "value": 79,
                "evidence": [
                    evidence(CONNECT_2021, "documented", "Monthly demand-origin measures")
                ],
                "caveat_labels": ["derived_average"],
            },
            {
                "id": "enterprise",
                "label": "Global software community",
                "value": 7000,
                "evidence": [
                    evidence(
                        "data/evidence/2025/individual/072-linkedin-recommendation-rob-nicholson.md",
                        "corroborated",
                        "Direct-manager description of community scale",
                    )
                ],
                "caveat_labels": ["population_not_active_users"],
            },
        ],
        "stories": [
            {
                "id": "one-to-one",
                "mechanism": "Listen one-to-one",
                "summary": "Use structured conversations to discover friction and earn permission to help.",
                "evidence": [evidence(CONNECT_2020, "documented", "Sustained one-to-one program")],
                "caveat_labels": [],
            },
            {
                "id": "co-create",
                "mechanism": "Deliver early together",
                "summary": "Build credibility with hands-on contribution before asking teams to change.",
                "evidence": [
                    evidence(
                        "data/evidence/2025/individual/071-linkedin-recommendation-ian-watson.md",
                        "corroborated",
                        "Peer description of influence mechanism",
                    )
                ],
                "caveat_labels": [],
            },
            {
                "id": "teach",
                "mechanism": "Teach for independence",
                "summary": "Coach people to reason and own the practice rather than depend on the coach.",
                "evidence": [
                    evidence(
                        "data/evidence/2020/individual/142-linkedin-recommendation-sannihith-reddy.md",
                        "corroborated",
                        "Mentee description of teaching method",
                    )
                ],
                "caveat_labels": [],
            },
            {
                "id": "system",
                "mechanism": "Leave a reusable system",
                "summary": "Turn recurring lessons into standards, platforms, communities, and guardrails.",
                "evidence": [
                    evidence(SESSION_EVIDENCE, "corroborated", "Repeated learning system"),
                    evidence(SUTRA, "documented", "Reusable quality-gated platform"),
                ],
                "caveat_labels": ["narrative_synthesis"],
            },
            {
                "id": "translate",
                "mechanism": "Translate across levels",
                "summary": "Make strategy and engineering reality understandable from executive rooms to developer teams.",
                "evidence": [
                    evidence(
                        "data/evidence/2025/individual/071-linkedin-recommendation-ian-watson.md",
                        "corroborated",
                        "Peer testimony across organizational levels",
                    )
                ],
                "caveat_labels": [],
            },
        ],
        "evidence": [
            evidence(CONNECT_2019, "documented", "2019 influence network"),
            evidence(CONNECT_2020, "documented", "2020 influence network"),
            evidence(CONNECT_2021, "documented", "2021 demand and reach"),
        ],
        "caveat_labels": ["cooccurrence_not_influence", "period_specific"],
    }

    teaching_service = {
        "session_metrics": [
            metric(
                "facilitated-sessions",
                "Facilitated sessions",
                90,
                "90",
                session_ref,
                period="2018–2026",
            ),
            metric(
                "feedback-responses",
                "Feedback responses",
                1183,
                "1,183",
                session_ref,
                period="2018–2026",
                caveats=["responses_not_attendance"],
            ),
            metric(
                "average-rating",
                "Normalized average",
                4.3,
                "4.3/5",
                session_ref,
                period="2018–2026",
            ),
        ],
        "college_program": {
            "id": "college-teaching",
            "year": 2013,
            "period": "2013–2020",
            "title": "Voluntary college teaching with direct student feedback",
            "category": "Teaching",
            "summary": "Thirteen weekend and community sessions across seven institutions produced 494 student responses on technical craft, careers, communication, and yoga.",
            "metrics": [
                metric(
                    "college-sessions",
                    "Feedback-backed sessions",
                    13,
                    "13",
                    [evidence(STUDENT_FEEDBACK, "corroborated", "Raw survey aggregate")],
                ),
                metric(
                    "student-responses",
                    "Student responses",
                    494,
                    "494",
                    [evidence(STUDENT_FEEDBACK, "corroborated", "Raw survey aggregate")],
                ),
                metric(
                    "presenter-five",
                    "Presenter rating",
                    4.58,
                    "4.58/5",
                    [evidence(STUDENT_FEEDBACK, "corroborated", "149 presenter ratings")],
                ),
                metric(
                    "presenter-ten",
                    "Presenter rating",
                    9.12,
                    "9.12/10",
                    [evidence(STUDENT_FEEDBACK, "corroborated", "128 presenter ratings")],
                ),
            ],
            "evidence": [
                evidence(STUDENT_FEEDBACK, "corroborated", "Thirteen feedback-form datasets")
            ],
            "caveat_labels": ["feedback_respondents_only"],
        },
        "service_programs": [
            {
                "id": "giveback-talks",
                "year": 2010,
                "period": "2010–2021",
                "title": "Giveback talks and workshops",
                "category": "Teaching",
                "summary": "Fifty recorded seminars, workshops, panels, and talks reached 3,732 participant instances across 25 venues.",
                "metrics": [
                    metric(
                        "giveback-count",
                        "Recorded sessions",
                        50,
                        "50",
                        [evidence(TALKS, "documented", "Dated talks spreadsheet")],
                    ),
                    metric(
                        "giveback-reach",
                        "Participant instances",
                        3732,
                        "3,732",
                        [evidence(TALKS, "documented", "Per-session participant counts")],
                        caveats=["participant_counts_not_unique"],
                    ),
                ],
                "evidence": [evidence(TALKS, "documented", "Complete session list")],
                "caveat_labels": ["participant_counts_not_unique"],
            },
            {
                "id": "book-distribution",
                "year": 2014,
                "period": "2014–2026",
                "title": "Rural education book program",
                "category": "Service",
                "summary": "Ten active years of organizing sustained an education giveback program through relocation and a pandemic pause.",
                "metrics": [
                    metric(
                        "book-years",
                        "Active years",
                        10,
                        "10",
                        [evidence(BOOK_PROGRAM, "documented", "Annual ledgers")],
                    ),
                    metric(
                        "book-growth",
                        "Annual growth factor",
                        13.3,
                        "13.3×",
                        [evidence(BOOK_PROGRAM, "documented", "2014-to-2026 aggregate")],
                        caveats=["public_safe_aggregate"],
                    ),
                ],
                "evidence": [evidence(BOOK_PROGRAM, "documented", "Aggregate program history")],
                "caveat_labels": ["public_safe_aggregate"],
            },
            {
                "id": "ai-learning",
                "year": 2024,
                "period": "2024–2026",
                "title": "AI and continuous-delivery learning system",
                "category": "Teaching",
                "summary": "Copilot, prompt engineering, context engineering, DORA, and agent-building sessions show the teaching portfolio moving with the engineering frontier.",
                "metrics": [
                    metric(
                        "ai-sessions",
                        "AI/GenAI sessions",
                        24,
                        "24",
                        session_ref,
                        period="2024–2026",
                    )
                ],
                "evidence": [
                    evidence(AI_2025, "documented", "AI leadership and enablement record"),
                    evidence(
                        SESSION_EVIDENCE, "corroborated", "Session topic and response aggregate"
                    ),
                ],
                "caveat_labels": [],
            },
        ],
        "evidence": session_ref
        + [
            evidence(STUDENT_FEEDBACK, "corroborated", "Student feedback archive"),
            evidence(BOOK_PROGRAM, "documented", "Social program aggregate"),
        ],
        "caveat_labels": ["participant_counts_not_unique", "public_safe_aggregate"],
    }

    momentum = {
        "ai_session_metrics": [
            metric(
                "ai-genai-sessions", "AI/GenAI sessions", 24, "24", session_ref, period="2024–2026"
            ),
            metric(
                "ai-feedback",
                "Approx. feedback responses",
                450,
                "~450",
                session_ref,
                period="2024–2026",
                caveats=["category_estimate"],
            ),
            metric(
                "copilot-class",
                "Train-the-trainer attendees",
                34,
                "34",
                [
                    evidence(
                        "data/evidence/2025/individual/002-copilot-family-class-for-hssap-team-34-ppl-joined-and-went-well.md",
                        "documented",
                        "Dated class record",
                    )
                ],
                period="2025",
            ),
        ],
        "frontier_projects": [
            {
                "id": "traceability",
                "year": 2026,
                "title": "AI-assisted end-to-end traceability",
                "summary": "A team platform connects requirements, tests, and evidence while quality gates remain non-negotiable.",
                "evidence": sutra_ref,
                "caveat_labels": ["team_attribution"],
            },
            {
                "id": "requirements",
                "year": 2026,
                "title": "AI-assisted requirements and test generation",
                "summary": "Active experiments use domain context to accelerate specifications and tests without presenting pilots as completed enterprise outcomes.",
                "evidence": [
                    evidence(
                        "data/evidence/2026/individual/017-fyi-xite-cohort-5-proposal-submission-sutra-extension-test-case-generation-for-a.md",
                        "documented",
                        "Dated pilot proposal",
                    )
                ],
                "caveat_labels": ["pilot_not_scaled_outcome", "team_attribution"],
            },
            {
                "id": "patient-safety",
                "year": 2026,
                "title": "AI applied to patient-safety and quality work",
                "summary": "The direction extends AI-native engineering into regulated quality workflows where traceability matters most.",
                "evidence": [
                    evidence(
                        "data/evidence/2026/individual/105-viva-engage-reqspec-patient-safety-quality-341-views.md",
                        "documented",
                        "Public internal-community post and engagement",
                    )
                ],
                "caveat_labels": ["initiative_specific"],
            },
            {
                "id": "copilot-enablement",
                "year": 2025,
                "title": "Enterprise AI capability enablement",
                "summary": "Structured learning, train-the-trainer work, and practical sessions turn tool adoption into engineering judgment.",
                "evidence": [evidence(AI_2025, "documented", "Multi-program AI enablement record")],
                "caveat_labels": [],
            },
        ],
        "quality_guardrails": [
            {
                "id": "ci-gates",
                "year": 2026,
                "title": "Quality rules block broken commits",
                "summary": "The reported AI-native delivery system disallowed commits that broke quality rules and used independent analyzers in CI/CD.",
                "evidence": sutra_ref,
                "caveat_labels": ["team_attribution", "initiative_specific"],
            },
            {
                "id": "traceability-gate",
                "year": 2026,
                "title": "Traceability treated as a product capability",
                "summary": "Evidence continuity is designed into delivery rather than assembled only at the end.",
                "evidence": [
                    evidence(
                        "data/evidence/2026/sutra-xite-ai-platform.md",
                        "documented",
                        "Thematic platform evidence",
                    )
                ],
                "caveat_labels": ["team_attribution"],
            },
            {
                "id": "dora",
                "year": 2025,
                "title": "Flow measured with DORA and continuous value delivery",
                "summary": "Leadership sessions and coaching connect delivery speed to stability and value rather than optimizing velocity alone.",
                "evidence": [
                    evidence(
                        "data/evidence/2025/skill-building-philips-university.md",
                        "documented",
                        "DORA and CVD learning-program evidence",
                    ),
                    evidence(
                        "data/evidence/2025/individual/072-linkedin-recommendation-rob-nicholson.md",
                        "corroborated",
                        "Direct-manager outcome testimony",
                    ),
                ],
                "caveat_labels": ["mixed_evidence_tiers"],
            },
        ],
        "next_horizon": [
            {
                "id": "evidence-native",
                "year": 2026,
                "title": "Evidence-native AI engineering",
                "summary": "Make requirements, decisions, tests, code, risk, and validation continuously traceable as one living system.",
                "evidence": [
                    evidence(
                        "data/evidence/2026/sutra-xite-ai-platform.md",
                        "derived",
                        "Current platform direction supports this horizon",
                    )
                ],
                "caveat_labels": ["future_direction"],
            },
            {
                "id": "quality-first",
                "year": 2026,
                "title": "Quality-first code generation",
                "summary": "Scale AI assistance only when automated gates, review, observability, and engineering judgment scale with it.",
                "evidence": [
                    evidence(
                        SUTRA,
                        "derived",
                        "Current quality-gated AI delivery supports this direction",
                    )
                ],
                "caveat_labels": ["future_direction"],
            },
            {
                "id": "context-systems",
                "year": 2026,
                "title": "Context systems for regulated work",
                "summary": "Turn fragmented organizational knowledge into governed context that people and agents can use safely.",
                "evidence": [
                    evidence(
                        "data/evidence/2026/individual/017-fyi-xite-cohort-5-proposal-submission-sutra-extension-test-case-generation-for-a.md",
                        "derived",
                        "Current context-rich pilot supports this direction",
                    )
                ],
                "caveat_labels": ["future_direction"],
            },
            {
                "id": "human-multiplier",
                "year": 2026,
                "title": "Human capability remains the multiplier",
                "summary": "Pair AI-native systems with coaching and communities so adoption increases judgment, ownership, and agency.",
                "evidence": [
                    evidence(SESSION_EVIDENCE, "derived", "Longitudinal teaching record"),
                    evidence(
                        "data/evidence/2025/individual/071-linkedin-recommendation-ian-watson.md",
                        "corroborated",
                        "Observed transformation-through-influence pattern",
                    ),
                ],
                "caveat_labels": ["future_direction", "narrative_synthesis"],
            },
        ],
        "evidence": [
            evidence(AI_2025, "documented", "2025 AI program portfolio"),
            evidence(SUTRA, "documented", "2026 AI-native delivery evidence"),
        ],
        "caveat_labels": ["future_direction", "team_attribution"],
    }

    data = {
        "meta": {
            "schema_version": 1,
            "generated_at": "2026-08-06",
            "title": "Datta Vellal — Evidence-backed Journey Atlas",
            "audience": "Public professional audience",
            "privacy": "Curated aggregates and attributed public recommendations only; raw evidence remains local.",
            "views": [
                {
                    "id": "portrait",
                    "label": "Executive Portrait",
                    "description": "Begin with a concise identity and high-trust proof points.",
                    "data_keys": ["thesis", "headline_metrics"],
                },
                {
                    "id": "journey",
                    "label": "Twenty-Year Journey",
                    "description": "Read work, service, and learning as parallel reinforcing strands.",
                    "data_keys": ["eras", "service_lane", "capability_streams"],
                },
                {
                    "id": "capabilities",
                    "label": "Capability Compounder",
                    "description": "Show how craft was reinvested into wider forms of leverage.",
                    "data_keys": ["capability_streams", "eras"],
                },
                {
                    "id": "outcomes",
                    "label": "Outcome Ledger",
                    "description": "Separate individual, team, organizational, enterprise, and community value.",
                    "data_keys": ["impact_ledger"],
                },
                {
                    "id": "respect",
                    "label": "Trust & Respect",
                    "description": "Let attributable third-party voices establish character and credibility.",
                    "data_keys": ["respect"],
                },
                {
                    "id": "influence",
                    "label": "Influence Web",
                    "description": "Explain the mechanisms that turn credibility into reusable reach.",
                    "data_keys": ["influence", "capability_streams"],
                },
                {
                    "id": "service",
                    "label": "Teaching & Service Ripple",
                    "description": "Show that teaching and stewardship persist beyond job boundaries.",
                    "data_keys": ["teaching_service", "service_lane"],
                },
                {
                    "id": "momentum",
                    "label": "Momentum & Next Horizon",
                    "description": "Ground future direction in recent work without presenting aspiration as delivery.",
                    "data_keys": ["momentum"],
                },
            ],
        },
        "thesis": {
            "headline": "Engineering excellence that compounds through people",
            "statement": "Across five professional eras, Datta's consistent move has been to understand complexity deeply, make it legible, build a reusable mechanism, and help other people own it—while sustaining a parallel commitment to teaching and service.",
            "role": "Digital transformation leader · Regulated software · AI-native engineering",
            "evidence": [
                evidence(CAREER_SYNTHESIS, "derived", "Longitudinal career synthesis"),
                evidence(
                    "data/evidence/2025/individual/071-linkedin-recommendation-ian-watson.md",
                    "corroborated",
                    "Observed influence pattern",
                ),
                evidence(
                    "data/evidence/2020/individual/142-linkedin-recommendation-sannihith-reddy.md",
                    "corroborated",
                    "Observed mentoring pattern",
                ),
                evidence(BOOK_PROGRAM, "documented", "Long-horizon service continuity"),
            ],
            "caveat_labels": ["narrative_synthesis"],
        },
        "headline_metrics": [
            metric(
                "career-span",
                "Professional journey",
                20,
                "20 years",
                resume_ref,
                period="2007–2026",
                caveats=["inclusive_year_count", "employment_dates_self_reported"],
            ),
            metric(
                "responses",
                "Session feedback responses",
                1183,
                "1,183",
                session_ref,
                period="2018–2026",
                caveats=["responses_not_attendance"],
            ),
            metric(
                "recommendations",
                "Attributed recommendations",
                len(RECOMMENDATIONS),
                "20",
                recommendation_evidence(),
                period="2012–2025",
                caveats=["selected_evidence"],
            ),
            metric(
                "patents",
                "US patents",
                2,
                "2",
                [evidence(AWARDS, "documented", "Patent and citation index")],
                caveats=["public_citation_index"],
            ),
        ],
        "eras": eras,
        "service_lane": service_lane,
        "capability_streams": capability_streams,
        "impact_ledger": impact_ledger,
        "influence": influence,
        "respect": respect,
        "teaching_service": teaching_service,
        "momentum": momentum,
        "caveats": {
            "category_estimate": "The category total is an approximate rollup from session records.",
            "cooccurrence_not_influence": "Knowledge-graph co-occurrence is not treated as proof of social influence.",
            "currency_context": "Currency values retain their original period and are not inflation- or exchange-rate-adjusted.",
            "curated_milestones": "The narrative selects representative milestones rather than every archived event.",
            "derived_average": "Calculated from the monthly values in the cited annual source.",
            "employment_dates_self_reported": "Employment dates come from first-party career documents.",
            "excerpted_quote": "The quote is shortened for display without changing its meaning.",
            "feedback_respondents_only": "Ratings describe respondents, not every attendee.",
            "future_direction": "This describes an active direction, not a promised or completed outcome.",
            "inclusive_year_count": "The span counts calendar years inclusively from 2007 through 2026.",
            "initiative_specific": "The metric belongs to the cited initiative and should not be generalized to all work.",
            "light_grammar_edit": "Minor grammar was normalized for display; the source preserves the original wording.",
            "mixed_attribution": "The record combines personal contribution with shared delivery context.",
            "mixed_evidence_tiers": "The claim combines sources with different evidentiary strength.",
            "narrative_synthesis": "This is an interpretation across multiple sources, not a single source claim.",
            "participant_counts_not_unique": "Participant totals are session instances and may include repeat attendees.",
            "period_specific": "The value applies only to the stated year or period.",
            "pilot_not_scaled_outcome": "A pilot or proposal demonstrates direction, not enterprise-scale adoption.",
            "population_not_active_users": "The figure describes the addressable software community, not measured active users.",
            "portfolio_attribution": "The outcome belongs to a portfolio of initiatives rather than one project or person alone.",
            "public_citation_index": "Patent counts and citations are based on the archived public-reference index.",
            "public_safe_aggregate": "Names, personal contribution amounts, account details, and identifiers are intentionally excluded.",
            "responses_not_attendance": "Feedback responses are not the same as total attendance.",
            "selected_evidence": "Recommendations and quotations are curated, not an unbiased survey.",
            "self_reported": "The figure is reported in a first-party resume or work narrative.",
            "team_attribution": "The result is a team outcome; Datta's role is contribution and leadership, not sole credit.",
            "touchpoints_not_unique_people": "Participant touchpoints may include the same person more than once.",
        },
    }
    _validate_source_journey_data(data, REPO_ROOT)
    public_data = _public_projection(data)
    validate_journey_data(public_data, REPO_ROOT)
    return public_data


def _walk(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk(child)


def _public_projection(value: Any) -> Any:
    """Strip private local paths while preserving stable public provenance IDs."""
    if isinstance(value, dict):
        return {
            key: _public_projection(child) for key, child in value.items() if key != "evidence_file"
        }
    if isinstance(value, list):
        return [_public_projection(child) for child in value]
    return value


def _validate_core(data: dict[str, Any]) -> None:
    required = {
        "meta",
        "thesis",
        "headline_metrics",
        "eras",
        "service_lane",
        "capability_streams",
        "impact_ledger",
        "influence",
        "respect",
        "teaching_service",
        "momentum",
        "caveats",
    }
    if set(data) != required:
        raise ValueError(f"Journey top-level keys differ: {sorted(set(data) ^ required)}")
    view_ids = [view["id"] for view in data["meta"]["views"]]
    expected_views = [
        "portrait",
        "journey",
        "capabilities",
        "outcomes",
        "respect",
        "influence",
        "service",
        "momentum",
    ]
    if view_ids != expected_views:
        raise ValueError(f"Expected exact journey views {expected_views}, got {view_ids}")
    if data["respect"]["recommendation_count"] != len(data["respect"]["recommendation_manifest"]):
        raise ValueError("Recommendation count does not match its manifest")
    if not data["eras"] or data["eras"][0]["start"] != 2007 or data["eras"][-1]["end"] != 2026:
        raise ValueError("Career chronology must span 2007 through 2026")

    metrics = [item for item in _walk(data) if {"label", "display", "value"} <= set(item)]
    without_sources = [
        item.get("id", item.get("label")) for item in metrics if not item.get("evidence")
    ]
    if without_sources:
        raise ValueError(f"Displayed metrics without evidence: {without_sources}")


def _validate_source_journey_data(data: dict[str, Any], repo_root: Path) -> None:
    """Validate the private path-bearing model before producing its public copy."""
    _validate_core(data)
    evidence_refs: list[dict[str, Any]] = []
    source_paths: dict[str, str] = {}
    for item in _walk(data):
        if "evidence_file" in item:
            allowed = {"evidence_file", "source_id", "tier", "supports", "year"}
            required = {"evidence_file", "source_id", "tier", "supports"}
            if not required <= set(item) or set(item) - allowed or not item.get("supports"):
                raise ValueError(f"Malformed evidence reference: {item}")
            if item.get("source_id") != _source_id(item["evidence_file"]):
                raise ValueError(f"Evidence source ID does not match its path: {item}")
            existing_path = source_paths.setdefault(item["source_id"], item["evidence_file"])
            if existing_path != item["evidence_file"]:
                raise ValueError(f"Opaque source ID collision: {item['source_id']}")
            evidence_refs.append(item)
    if not evidence_refs:
        raise ValueError("Journey data has no evidence references")
    missing = sorted(
        {
            ref["evidence_file"]
            for ref in evidence_refs
            if not (repo_root / ref["evidence_file"]).is_file()
        }
    )
    if missing:
        raise FileNotFoundError(f"Journey evidence paths do not exist: {missing}")


def validate_journey_data(data: dict[str, Any], repo_root: Path) -> None:
    """Validate the exact public contract after private paths have been removed."""
    if not repo_root.is_dir():
        raise FileNotFoundError(f"Repository root does not exist: {repo_root}")
    _validate_core(data)

    evidence_refs: list[dict[str, Any]] = []
    for item in _walk(data):
        if "evidence_file" in item:
            raise ValueError("Public journey data contains a private evidence path")
        if "source_id" in item:
            allowed = {"source_id", "tier", "supports", "year"}
            required = {"source_id", "tier", "supports"}
            if not required <= set(item) or set(item) - allowed or not item.get("supports"):
                raise ValueError(f"Malformed public evidence reference: {item}")
            if not re.fullmatch(r"src_[0-9a-f]{12}", str(item["source_id"])):
                raise ValueError(f"Malformed public source ID: {item['source_id']}")
            if item.get("tier") not in {
                "corroborated",
                "documented",
                "self-reported",
                "derived",
            }:
                raise ValueError(f"Unknown evidence tier: {item.get('tier')}")
            evidence_refs.append(item)
    if not evidence_refs:
        raise ValueError("Public journey data has no evidence references")

    serialized = json.dumps(data, ensure_ascii=False).lower()
    forbidden = [
        "data/evidence/",
        "@philips.com",
        "http://",
        "https://",
        "pan card",
        "account number",
    ]
    found = [token for token in forbidden if token in serialized]
    if found:
        raise ValueError(f"Public journey data contains forbidden private/link material: {found}")


def analysis_markdown(data: dict[str, Any]) -> str:
    return f"""# Journey analysis — 2007–2026

Generated from the curated public-safe journey model. The canonical evidence and raw relationship
stores remain local; this report records the editorial interpretation used by the Journey Atlas.

## Central thesis

**{data["thesis"]["headline"]}.** {data["thesis"]["statement"]}

The journey is best understood as a progression from **hands-on builder**, to **team enabler**, to
**organizational multiplier**, to **AI-era transformation leader**. The constant operating pattern is:
understand complexity deeply, make it understandable, build a reusable mechanism, and enable other
people to own it. A parallel teaching and service lane demonstrates that the pattern survives changes
in employer, title, geography, and technology.

## Evidence picture

- Five employment eras from 2007 through 2026, using the latest resume for chronology.
- {len(data["respect"]["recommendation_manifest"])} dated, attributed recommendations from 2012–2025.
- 90 facilitated professional sessions with 1,183 responses and a normalized 4.3/5 average.
- 13 voluntary college sessions with 494 responses, including presenter averages of 4.58/5 and 9.12/10.
- A three-year .connect record that shows both reach and demand, while separating unique people from touchpoints.
- 50 recorded giveback talks reaching 3,732 participant instances across 25 venues.
- A ten-active-year rural education program, published only as privacy-safe aggregates.
- Recent AI-native delivery evidence with explicit team attribution and quality guardrails.

## Why these eight views are the strongest projection

1. **Executive Portrait** earns attention with a concise identity and high-trust proof, not a claim dump.
2. **Twenty-Year Journey** proves continuity by braiding work, capability, and service rather than treating life as job titles.
3. **Capability Compounder** shows that technical depth was reinvested into systems, people, and transformation.
4. **Outcome Ledger** makes value concrete while keeping attribution, currency, audience, and period caveats visible.
5. **Trust & Respect** lets other people's attributed words demonstrate the respect the work earned.
6. **Influence Web** explains the repeatable mechanism—credibility, co-creation, teaching, and systems—without mislabeling graph co-occurrence as influence.
7. **Teaching & Service Ripple** reveals values and generosity beyond formal organizational authority.
8. **Momentum & Next Horizon** shows an active direction grounded in recent evidence without presenting aspiration as a forecast.

This sequence moves the audience from identity → chronology → capability → value → independent validation →
influence mechanism → character → future relevance. It projects ambition confidently while remaining credible.

## Important interpretation boundaries

- Resume-originated financial, scale, and employment claims are explicitly marked self-reported.
- Team and portfolio outcomes are never presented as sole-person attribution.
- Participant instances, feedback responses, touchpoints, and unique people remain distinct measures.
- The raw NetworkX graph represents extracted entity relationships and co-occurrence, not social causality.
- Recommendations are curated evidence, not an unbiased survey.
- Future-horizon entries are direction, not delivered outcomes.
- Donor identities, personal contribution amounts, emails, internal URLs, and financial identifiers are excluded.

## Data-store findings that affect confidence

The relationship export contains 49,614 DuckDB rows, 17,190 edges, 21,356 Chroma records, and a
3,471-node NetworkX graph. Cross-store validation found no missing graph endpoints, Chroma extras,
or document/metadata mismatches. It also records 4,411 DuckDB chunks without embeddings and 13 soft
edge-provenance links whose source artifact is absent. Those gaps matter for retrieval completeness,
but they do not invalidate the curated claims above because every displayed claim points to a reviewed
evidence file.
"""


def write_outputs(data: dict[str, Any], output: Path, report: Path) -> None:
    validate_journey_data(data, REPO_ROOT)
    output.parent.mkdir(parents=True, exist_ok=True)
    report.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    report.write_text(analysis_markdown(data), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    data = build_journey_data()
    write_outputs(data, args.output, args.report)
    print(f"Wrote {args.output} ({len(json.dumps(data, ensure_ascii=False)):,} JSON characters)")
    print(f"Wrote {args.report}")


if __name__ == "__main__":
    main()
