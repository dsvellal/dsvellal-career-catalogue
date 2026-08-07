"""Build the public, auditable dataset for Datta's executive portfolio.

The repository contains private personal and corporate evidence.  This builder is
the publication boundary: it calculates reviewable aggregates from the held
sources, emits only approved excerpts, and models every claim as a traceable edge
to evidence.  Local paths are intentionally absent from the browser bundle.
"""

# Narrative copy is kept beside the provenance declarations for editorial review.
# ruff: noqa: E501

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = REPO_ROOT / "viz" / "src" / "data" / "portfolio.json"
AS_OF = "2026-08-07"

SESSION_CORPUS = "data/evidence/sessions/all_sessions_data.json"
SESSION_NARRATIVE = "data/evidence/sessions/SESSION-EVIDENCE.md"
SESSION_SUMMARY = "data/evidence/sessions/summary_stats.json"
STUDENT_FEEDBACK_SUMMARY = "data/evidence/sessions/student-feedback/STUDENT-FEEDBACK-EVIDENCE.md"
STUDENT_FEEDBACK_CORPUS = "data/evidence/sessions/student-feedback/all_sessions_raw.json"
RESUME_2026 = "data/evidence/2026/individual/112-resume-2026-latest-authoritative.md"
FEEDBACK_360 = "data/evidence/2020/individual/069a-philips-360-degree-feedback-2020.md"
STRENGTHS_2020 = "data/evidence/2020/individual/069c-philips-betalent-strengths-2020.md"
IBM_EARLY_LEADERSHIP = "data/evidence/2008/individual/004-ibm-bravo-internship-management.md"
IBM_PATENT_AWARD = "data/evidence/2010/individual/004-ibm-first-patent-award.md"
IBM_TECHNICAL_INFLUENCE = "data/evidence/2010/individual/005-ibm-rtle-2010-award.md"
AWARDS_INDEX = "data/evidence/sessions/awards-recognition-citations-master.md"
EXETER_REVIEW = "data/evidence/2015/individual/006-exeter-ppm-q1-2015-performance-review.md"
EXETER_RECOMMENDATION = (
    "data/evidence/2015/individual/004-linkedin-recommendation-srisankaraswaminathan-jv.md"
)
AMAZON_PROCESS = "data/evidence/2017/individual/026-amazon-trms-spot-award-process-improvement.md"
AMAZON_DELIVERY = "data/evidence/2017/individual/002-amazon-trms-zeus-award.md"
AMAZON_WORK = "data/evidence/2018/individual/019-resume-2018-amazon-work-examples.md"
CONNECT_2021 = "data/evidence/2021/individual/019-connect-annual-summary-2021.md"
CTO_RECOGNITION = "data/evidence/2021/individual/001-outstanding-achievement-award-cto-2021.md"
TALKS_LEDGER = "data/evidence/sessions/givebacks-talks-spreadsheet.md"
BOOK_LEDGER = "data/evidence/2025/individual/075-social-giveback-book-distribution-program.md"
SERVICE_PHOTOS = "data/evidence/2025/individual/074-social-giving-back-presentation.md"
RECOMMENDATION_SANNIHITH = (
    "data/evidence/2020/individual/142-linkedin-recommendation-sannihith-reddy.md"
)
RECOMMENDATION_NAVEEN = (
    "data/evidence/2023/individual/018-linkedin-recommendation-naveenkumar-vr.md"
)
RECOMMENDATION_IAN = "data/evidence/2025/individual/071-linkedin-recommendation-ian-watson.md"
RECOMMENDATION_ROB = "data/evidence/2025/individual/072-linkedin-recommendation-rob-nicholson.md"
XITE_SUTRA = "data/evidence/2026/individual/111-xite-special-edition-18k-hours-3-5m-sutra-impact.md"
SUTRA_RECOGNITION = (
    "data/evidence/2026/individual/099-recognition-learning-collaboration-sutra-q2-2026.md"
)
RELATIONSHIP_QUALITY = "data/exports/relationships/quality/consistency-report.md"
EVIDENCE_INDEX = "data/evidence/INDEX.md"

ALLOWED_EXTERNAL_HOSTS = frozenset({"patents.google.com"})
FORBIDDEN_PUBLIC_TOKENS = (
    "/users/",
    "data/evidence/",
    "data/exports/",
    "file://",
    "@philips.com",
    "teams.microsoft.com",
    "engage.cloud.microsoft",
    "account number",
    "pan card",
    "evidence pending",
)
FORBIDDEN_INTERNAL_DOMAINS = (
    "docs.philips.com",
    "philips.sharepoint.com",
    "sharepoint.com",
    "w.amazon.com",
    "tfsemea1.ta.philips.com",
    "caoapps.htce.nl",
    "engage.cloud.microsoft",
    "teams.microsoft.com",
)
EMAIL_PATTERN = re.compile(r"\b[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}\b", re.IGNORECASE)
INTERNATIONAL_PHONE_PATTERN = re.compile(r"\+\d[\d\s().\-]{7,}\d")
SEPARATED_PHONE_PATTERN = re.compile(r"\b\d{3}[\s.)\-]\d{3}[\s.\-]\d{4}\b")
CONTIGUOUS_PHONE_PATTERN = re.compile(r"(?<!\d)\d{10}(?!\d)")
URL_PATTERN = re.compile(r"https?://[^\s\"<>]+", re.IGNORECASE)


SOURCE_SPECS: tuple[dict[str, str], ...] = (
    {
        "id": "source-session-response-corpus-2018-2026",
        "path": SESSION_CORPUS,
        "title": "Structured feedback-file corpus, 2018–2026",
        "source_type": "structured_aggregate",
        "source_date": "2018–2026",
        "publisher": "Datta Vellal — compiled feedback records",
        "access_state": "aggregate_only",
        "approved_excerpt": "The corpus distinguishes a post-event/interaction analysis population from pre-session audience surveys and stores response-row, rating-observation, qualitative-entry, date, and filename-derived category fields.",
    },
    {
        "id": "source-participant-improvement-relevant-examples-2019",
        "path": SESSION_CORPUS,
        "title": "Anonymous participant improvement excerpt — relevant examples, 2019",
        "source_type": "selected_anonymous_feedback",
        "source_date": "2019-09-26",
        "publisher": "Anonymous participant",
        "access_state": "public_excerpt",
        "excerpt_kind": "verbatim",
        "approved_excerpt": "It could be better if you can give examples related to the technology which we are working on.",
    },
    {
        "id": "source-participant-takeaway-ai-guardrails-2024",
        "path": SESSION_CORPUS,
        "title": "Anonymous participant takeaway — prompting and guardrails, 2024",
        "source_type": "selected_anonymous_feedback",
        "source_date": "2024-12-18",
        "publisher": "Anonymous participant",
        "access_state": "public_excerpt",
        "excerpt_kind": "verbatim",
        "approved_excerpt": "Setting up IDE with copilot and how to interface with agent there as well as triggering agents on github.com\nHow to write better prompts to get the results I want \nUnderstanding the importance of setting up guide rails through things like copilot-instructions to get quality output",
    },
    {
        "id": "source-participant-improvement-hands-on-agents-2026",
        "path": SESSION_CORPUS,
        "title": "Anonymous participant improvement excerpt — hands-on agents, 2026",
        "source_type": "selected_anonymous_feedback",
        "source_date": "2026-06-25",
        "publisher": "Anonymous participant",
        "access_state": "public_excerpt",
        "excerpt_kind": "verbatim",
        "approved_excerpt": "Would like to have hands-on sessions (multiple), on building agents and optimal use of them.",
    },
    {
        "id": "source-session-corrected-narrative-2026",
        "path": SESSION_NARRATIVE,
        "title": "Corrected session evidence narrative, 2026",
        "source_type": "editorial_summary",
        "source_date": "2026-08-05",
        "publisher": "Datta Vellal — evidence synthesis",
        "access_state": "aggregate_only",
        "approved_excerpt": "The corrected narrative defines mutually exclusive source, duplicate, pre-survey, and post-event/interaction populations and explicitly documents the earlier population-accounting error.",
    },
    {
        "id": "source-session-corrected-summary-2026",
        "path": SESSION_SUMMARY,
        "title": "Corrected reproducible feedback aggregate, 2026",
        "source_type": "structured_aggregate",
        "source_date": "2026-08-05",
        "publisher": "Datta Vellal — generated summary",
        "access_state": "aggregate_only",
        "approved_excerpt": "The reproducible aggregate reports 92 source files, 2 duplicates, 2 pre-session surveys, and 88 post-event/interaction analysis files, with field-specific units.",
    },
    {
        "id": "source-student-feedback-aggregate-2013-2020",
        "path": STUDENT_FEEDBACK_SUMMARY,
        "title": "Audited student-feedback aggregate, 2013–2020",
        "source_type": "audited_aggregate",
        "source_date": "2013–2020",
        "publisher": "Datta Vellal — community-teaching feedback archive",
        "access_state": "aggregate_only",
        "approved_excerpt": "The separate community-teaching tracker contains 13 feedback forms and 494 response rows across six educational institutions plus one Exeter corporate yoga context. Presenter ratings retain their original 5-point and 10-point scales; recommendation likelihood is reported as an 8.87/10 source-scale mean.",
    },
    {
        "id": "source-student-feedback-structured-corpus-2013-2020",
        "path": STUDENT_FEEDBACK_CORPUS,
        "title": "Structured student-feedback corpus, 2013–2020",
        "source_type": "structured_private_feedback",
        "source_date": "2013–2020",
        "publisher": "Datta Vellal — compiled feedback records",
        "access_state": "private_held",
        "approved_excerpt": "The held corpus stores one record per feedback form, response-row counts, per-question aggregates, contexts, and qualitative fields. Raw rows are not published.",
    },
    {
        "id": "source-student-takeaway-interview-resilience-2017",
        "path": STUDENT_FEEDBACK_CORPUS,
        "title": "Anonymous student takeaway — interview resilience, 2017",
        "source_type": "selected_anonymous_feedback",
        "source_date": "2017-07-08",
        "publisher": "Anonymous NIE participant",
        "access_state": "public_excerpt",
        "excerpt_kind": "verbatim",
        "approved_excerpt": "I will try to learn application of ds and improve my soft skills! And its ok to fail",
    },
    {
        "id": "source-student-takeaway-uncertainty-2020",
        "path": STUDENT_FEEDBACK_CORPUS,
        "title": "Anonymous student takeaway — moving through uncertainty, 2020",
        "source_type": "selected_anonymous_feedback",
        "source_date": "2020-08-08",
        "publisher": "Anonymous SIT participant",
        "access_state": "public_excerpt",
        "excerpt_kind": "verbatim",
        "approved_excerpt": "Accept the uncertainty , think differently and move forward.",
    },
    {
        "id": "source-career-resume-2026",
        "path": RESUME_2026,
        "title": "2026 comprehensive career record",
        "source_type": "resume",
        "source_date": "2026-03-29",
        "publisher": "Datta Vellal",
        "access_state": "public_excerpt",
        "approved_excerpt": "The career chronology begins at IBM in July 2007 and records roles at Exeter, Amazon, Philips India, and Philips North America through 2026.",
    },
    {
        "id": "source-leadership-award-2008",
        "path": IBM_EARLY_LEADERSHIP,
        "title": "IBM early-career leadership award, 2008",
        "source_type": "award_artifact",
        "source_date": "2008-06-01",
        "publisher": "IBM",
        "access_state": "public_excerpt",
        "approved_excerpt": "The award recognizes end-to-end leadership of a complex internship project early in Datta's career.",
    },
    {
        "id": "source-patent-award-2010",
        "path": IBM_PATENT_AWARD,
        "title": "IBM first-patent invention achievement award, 2010",
        "source_type": "award_artifact",
        "source_date": "2010-12-28",
        "publisher": "IBM",
        "access_state": "public_excerpt",
        "approved_excerpt": "IBM recognized Datta's first patent application, Determining and Conveying User Availability.",
    },
    {
        "id": "source-technical-community-recognition-2010",
        "path": IBM_TECHNICAL_INFLUENCE,
        "title": "IBM technical community recognition, 2010",
        "source_type": "award_artifact",
        "source_date": "2010-09",
        "publisher": "IBM Regional Technical Leadership Exchange — India",
        "access_state": "public_excerpt",
        "approved_excerpt": "The certificate recognizes Datta's contribution to IBM's India technical community exchange.",
    },
    {
        "id": "source-us-patent-8560487",
        "path": AWARDS_INDEX,
        "title": "US Patent 8,560,487 — public registry record",
        "source_type": "public_registry",
        "source_date": "2013",
        "publisher": "Google Patents",
        "access_state": "public_external",
        "approved_excerpt": "The public registry lists Datta among the inventors of Determining and Conveying User Availability.",
        "external_url": "https://patents.google.com/patent/US8560487B2/en",
    },
    {
        "id": "source-exeter-performance-review-2015",
        "path": EXETER_REVIEW,
        "title": "Exeter manager performance review, 2015",
        "source_type": "performance_review",
        "source_date": "2015-04-01",
        "publisher": "Exeter",
        "access_state": "private_held",
        "approved_excerpt": "The review describes high-complexity, high-impact work, quality due diligence, collaborative partnerships, and a linchpin role; it also records improvement areas.",
    },
    {
        "id": "source-cross-team-recommendation-2015",
        "path": EXETER_RECOMMENDATION,
        "title": "Cross-team professional recommendation, 2015",
        "source_type": "attributed_recommendation",
        "source_date": "2015-10-28",
        "publisher": "Professional colleague",
        "access_state": "public_excerpt",
        "approved_excerpt": "A cross-team colleague describes a combination of technical depth, people leadership, teaching, and organization-wide bridge building. Identity is withheld in this portfolio view.",
    },
    {
        "id": "source-amazon-process-recognition-2017",
        "path": AMAZON_PROCESS,
        "title": "Amazon team-process improvement recognition, 2017",
        "source_type": "award_artifact",
        "source_date": "2017-11-01",
        "publisher": "Amazon TRMS Tech",
        "access_state": "public_excerpt",
        "approved_excerpt": "The award explicitly recognizes contributions to team process improvement.",
    },
    {
        "id": "source-amazon-delivery-recognition-2017",
        "path": AMAZON_DELIVERY,
        "title": "Amazon project-delivery recognition, 2017",
        "source_type": "award_artifact",
        "source_date": "2017-10",
        "publisher": "Amazon TRMS Tech",
        "access_state": "public_excerpt",
        "approved_excerpt": "The award recognizes exceptional work related to project delivery.",
    },
    {
        "id": "source-amazon-work-examples-2018",
        "path": AMAZON_WORK,
        "title": "Amazon work-examples record, 2016–2018",
        "source_type": "self_assessment",
        "source_date": "2018",
        "publisher": "Datta Vellal",
        "access_state": "public_excerpt",
        "approved_excerpt": "The record describes self-service tools, reusable guides, workshops, hiring contributions, delivery outcomes, and lessons captured through reflective delivery reviews.",
    },
    {
        "id": "source-360-feedback-2020",
        "path": FEEDBACK_360,
        "title": "DDI 360-degree leadership feedback, 2020",
        "source_type": "multi_rater_assessment",
        "source_date": "2020-12-01",
        "publisher": "DDI in partnership with Philips",
        "access_state": "private_held",
        "approved_excerpt": "Fourteen raters scored five leadership behaviors. The report also records a development request to broaden influence with senior executives beyond software.",
    },
    {
        "id": "source-strengths-assessment-2020",
        "path": STRENGTHS_2020,
        "title": "BeTalent strengths profile, 2020",
        "source_type": "psychometric_assessment",
        "source_date": "2020-10-29",
        "publisher": "BeTalent Ltd",
        "access_state": "private_held",
        "approved_excerpt": "The ranked profile names Articulate, Meticulous, Evaluative, Genuine, Achiever, Networker, and Self-Aware as the top seven strengths.",
    },
    {
        "id": "source-mentoring-recommendation-2020",
        "path": RECOMMENDATION_SANNIHITH,
        "title": "Mentee recommendation on independent-thinking mentorship, 2020",
        "source_type": "attributed_recommendation",
        "source_date": "2020-04-29",
        "publisher": "Former mentee",
        "access_state": "public_excerpt",
        "approved_excerpt": "A former mentee says Datta helps people think through solutions independently and teaches skills together with values.",
    },
    {
        "id": "source-connect-program-2021",
        "path": CONNECT_2021,
        "title": "Connect program annual ledger, 2021",
        "source_type": "program_ledger",
        "source_date": "2021",
        "publisher": "Datta Vellal — program record",
        "access_state": "aggregate_only",
        "approved_excerpt": "The monthly ledger records 575 connect conversations; 454 were set up by other people seeking a conversation.",
    },
    {
        "id": "source-philips-cto-recognition-2021",
        "path": CTO_RECOGNITION,
        "title": "Philips CTO outstanding achievement recognition, 2021",
        "source_type": "award_artifact",
        "source_date": "2021-02-24",
        "publisher": "Philips CTO Annual Address",
        "access_state": "public_excerpt",
        "approved_excerpt": "A company-wide CTO event artifact includes Datta among thirty outstanding-achievement recipients.",
    },
    {
        "id": "source-purpose-first-mentoring-recommendation-2023",
        "path": RECOMMENDATION_NAVEEN,
        "title": "Recommendation on calm, purpose-first mentoring, 2023",
        "source_type": "attributed_recommendation",
        "source_date": "2023-02-03",
        "publisher": "Professional colleague and mentee",
        "access_state": "public_excerpt",
        "approved_excerpt": "A peer mentored outside formal reporting lines describes calmness, kindness, purpose and outcome context, openness to input, and availability.",
    },
    {
        "id": "source-influence-recommendation-2025",
        "path": RECOMMENDATION_IAN,
        "title": "Recommendation on transformation through influence, 2025",
        "source_type": "attributed_recommendation",
        "source_date": "2025-02-25",
        "publisher": "Software Excellence colleague",
        "access_state": "public_excerpt",
        "approved_excerpt": "A colleague independently observes relationship-led credibility, communication from executives to developers, coaching, roadmap execution, and use of data.",
    },
    {
        "id": "source-manager-recommendation-2025",
        "path": RECOMMENDATION_ROB,
        "title": "Direct-manager recommendation on cross-boundary leadership, 2025",
        "source_type": "manager_recommendation",
        "source_date": "2025-02-20",
        "publisher": "Former direct manager",
        "access_state": "public_excerpt",
        "approved_excerpt": "A former direct manager observes leadership across reporting lines, seniority, and team boundaries, alongside empathetic communication, coaching, craftsmanship, and DORA improvement.",
    },
    {
        "id": "source-community-talks-ledger-2010-2021",
        "path": TALKS_LEDGER,
        "title": "Community and professional talks ledger, 2010–2021",
        "source_type": "activity_ledger",
        "source_date": "2010–2021",
        "publisher": "Datta Vellal — compiled activity record",
        "access_state": "aggregate_only",
        "approved_excerpt": "The ledger records 50 sessions and 3,732 participant instances, spanning wellness, software craft, career learning, uncertainty, and observability.",
    },
    {
        "id": "source-book-program-ledger-2014-2026",
        "path": BOOK_LEDGER,
        "title": "Book-distribution program aggregate ledger, 2014–2026",
        "source_type": "financial_aggregate",
        "source_date": "2014–2026",
        "publisher": "Datta Vellal — private program records",
        "access_state": "aggregate_only",
        "approved_excerpt": "Reviewed aggregates record ten active years and ₹1,972,381 raised in total, with a 13.3× 2014-to-2026 endpoint ratio. The active-year ledger distinguishes the recorded 2014–2019, 2022–2023, and 2025–2026 program years while protecting names, account data, and individual amounts.",
    },
    {
        "id": "source-community-service-photo-record-2007-2015",
        "path": SERVICE_PHOTOS,
        "title": "Social giving-back photo record, 2007–2015",
        "source_type": "documentary_photo_album",
        "source_date": "2007–2015",
        "publisher": "Datta Vellal — personal archive",
        "access_state": "public_excerpt",
        "approved_excerpt": "Dated images document teaching, yoga instruction, rural-school visits, and distribution of educational materials across multiple years.",
    },
    {
        "id": "source-xite-portfolio-outcomes-2026",
        "path": XITE_SUTRA,
        "title": "XITE portfolio potential-value announcement, 2026",
        "source_type": "internal_program_announcement",
        "source_date": "2026-05-28",
        "publisher": "XITE program",
        "access_state": "private_held",
        "approved_excerpt": "Across eight AI initiatives, the announcement describes potential annual value of about 18,000 productivity hours and €3.5 million in efficiencies. These are portfolio-level potential estimates.",
    },
    {
        "id": "source-sutra-initiative-outcomes-2026",
        "path": XITE_SUTRA,
        "title": "Sutra initiative traceability and AI-delivery record, 2026",
        "source_type": "internal_program_announcement",
        "source_date": "2026-04-30",
        "publisher": "Inside XITE and Sutra team commentary",
        "access_state": "private_held",
        "approved_excerpt": "The initiative record reports 90%+ traceability improvement; a team comment reports 3× development speed, about 80% AI-generated code, and commit-level quality gates measured by external tools.",
    },
    {
        "id": "source-sutra-recognition-2026",
        "path": SUTRA_RECOGNITION,
        "title": "Sutra learning and collaboration recognition, 2026",
        "source_type": "award_artifact",
        "source_date": "2026-07-28",
        "publisher": "Philips Recognition",
        "access_state": "public_excerpt",
        "approved_excerpt": "The recognition artifact credits conscious application of AI and delivery of the XITE-funded Sutra program to business units.",
    },
    {
        "id": "source-relationship-export-quality-2026",
        "path": RELATIONSHIP_QUALITY,
        "title": "Relationship export consistency report, 2026",
        "source_type": "machine_quality_report",
        "source_date": "2026-08-07",
        "publisher": "Knowledge-context export pipeline",
        "access_state": "aggregate_only",
        "approved_excerpt": "The report records row counts, referential checks, graph coverage, and retrieval-index alignment, including explicit provenance and embedding gaps.",
    },
    {
        "id": "source-evidence-inventory-2026",
        "path": EVIDENCE_INDEX,
        "title": "Evidence repository inventory, 2026",
        "source_type": "repository_inventory",
        "source_date": "2026-08-07",
        "publisher": "Knowledge-context repository",
        "access_state": "aggregate_only",
        "approved_excerpt": "The public-safe inventory method counts held evidence documents and media without publishing their filenames or contents.",
    },
)


CAVEATS: tuple[dict[str, str], ...] = (
    {
        "id": "caveat-calendar-span-not-tenure",
        "label": "Calendar span, not tenure",
        "description": "The inclusive 2007–2026 calculation describes calendar-year coverage. It is not elapsed duration, continuous tenure, or a claim of twenty completed years of experience.",
    },
    {
        "id": "caveat-response-unit",
        "label": "Responses are records",
        "description": "A response is a submitted row in a source dataset, not a unique person and not total attendance.",
    },
    {
        "id": "caveat-rating-observation-unit",
        "label": "Rating observations are question-level",
        "description": "One respondent may answer multiple rating questions. The count is the sum of question-level rating observations, not respondents or sessions.",
    },
    {
        "id": "caveat-qualitative-entry-unit",
        "label": "Qualitative entries are field values",
        "description": "The count is populated qualitative field values; a single response can contribute multiple entries.",
    },
    {
        "id": "caveat-surveys-separated",
        "label": "Audience surveys separated",
        "description": "Two pre-session surveys and their responses are disclosed separately and excluded from post-session feedback metrics.",
    },
    {
        "id": "caveat-category-labels",
        "label": "Topic labels are curated",
        "description": "Each file has one filename-pattern-derived category label. Counts describe the current rule set, not an independently hand-coded or exhaustive lexical analysis of overlapping themes.",
    },
    {
        "id": "caveat-private-held-source",
        "label": "Private-held source",
        "description": "The underlying record is retained for audit but cannot be opened publicly; only its approved excerpt, hash, and locator are published.",
    },
    {
        "id": "caveat-self-authored-source",
        "label": "Self-authored evidence",
        "description": "The source records Datta's own account. It is useful first-party evidence but is not independent corroboration.",
    },
    {
        "id": "caveat-team-attribution",
        "label": "Team attribution",
        "description": "The outcome belongs to a team or program. Datta's contribution is evidenced, but the result is not represented as his individual output.",
    },
    {
        "id": "caveat-potential-not-realized",
        "label": "Potential, not realized value",
        "description": "The announced hours and euro values are estimates of potential annual portfolio value, not audited realized savings.",
    },
    {
        "id": "caveat-initiative-scope",
        "label": "Initiative-specific metric",
        "description": "Sutra metrics describe one initiative and must not be conflated with the aggregate XITE portfolio estimate.",
    },
    {
        "id": "caveat-non-causal-synthesis",
        "label": "Non-causal synthesis",
        "description": "Evidence ordered over time can show recurrence, concordance, or a plausible lineage; it cannot prove that an earlier event caused a later outcome.",
    },
    {
        "id": "caveat-assessment-not-performance",
        "label": "Assessment is not performance proof",
        "description": "A psychometric profile describes assessed preferences. Later similar language is concordance, not validation or proof of capability.",
    },
    {
        "id": "caveat-selected-evidence",
        "label": "Selected evidence path",
        "description": "A relationship path uses reviewed representative sources. It does not claim that every relevant record is included.",
    },
    {
        "id": "caveat-patent-scope",
        "label": "Patent lineage, not commercial impact",
        "description": "The evidence links a 2010 first-application recognition to a later public grant for the same named invention and identifies Datta as one of three inventors. It does not establish sole inventorship, commercialization, adoption, revenue, or current legal status.",
    },
    {
        "id": "caveat-touchpoints-not-people",
        "label": "Touchpoints, not unique people",
        "description": "Conversation and participant totals may include repeat people and should not be presented as unique reach.",
    },
    {
        "id": "caveat-active-years-with-gaps",
        "label": "Recorded years are non-contiguous",
        "description": "The book program has ten recorded active years across 2014–2026. No program is recorded for 2020–2021, and no reviewed 2024 program record is present; absence of a record is not converted into a zero amount or an unqualified claim of inactivity.",
    },
    {
        "id": "caveat-currency-not-normalized",
        "label": "Nominal currency",
        "description": "Rupee values are nominal annual amounts and are not adjusted for inflation or exchange rates.",
    },
    {
        "id": "caveat-identity-withheld",
        "label": "Identity withheld",
        "description": "The matched identity and individual contribution amounts are deliberately suppressed. The public claim is limited to cross-record continuity.",
    },
    {
        "id": "caveat-inference-not-motive",
        "label": "No motive inferred",
        "description": "Cross-context participation is a trust signal, but the records do not establish why someone recommended or contributed.",
    },
    {
        "id": "caveat-export-gap",
        "label": "Export coverage gap",
        "description": "Retrieval or provenance gaps limit graph completeness; they do not invalidate the separately source-linked portfolio claims.",
    },
    {
        "id": "caveat-source-label-conflict",
        "label": "Source labels conflict",
        "description": "Legacy summaries use incompatible units or labels. The conflict is shown and the current method is versioned rather than silently choosing a number.",
    },
    {
        "id": "caveat-feedback-not-longitudinal",
        "label": "Feedback is not a panel study",
        "description": "Feedback at different dates generally comes from different participants and sessions; changes in comments cannot be treated as individual longitudinal change.",
    },
    {
        "id": "caveat-session-tracker-boundary",
        "label": "Tracker boundary",
        "description": "Counts cover only records present in the reviewed trackers. They are lower bounds for activity, not a complete career attendance ledger.",
    },
    {
        "id": "caveat-student-tracker-separate",
        "label": "Separate student-feedback tracker",
        "description": "The 13-form community-teaching tracker is not part of the professional feedback corpus and is not added to the talks ledger's approximate participant instances.",
    },
    {
        "id": "caveat-student-response-rows",
        "label": "Student responses are rows",
        "description": "The 494 figure counts submitted response rows, not verified unique people, total attendance, or participant instances from the separate talks ledger.",
    },
    {
        "id": "caveat-student-context-boundary",
        "label": "Six institutions plus one corporate context",
        "description": "Six contexts are educational institutions; the seventh is one Exeter corporate yoga session and is not relabeled as an educational institution.",
    },
    {
        "id": "caveat-student-rating-scales",
        "label": "Rating scales stay separate",
        "description": "Presenter ratings on 5-point and 10-point scales cover different response populations and are never normalized or merged. Weighted means use stored per-form means that are already rounded.",
    },
    {
        "id": "caveat-recommendation-not-nps",
        "label": "Recommendation likelihood is not NPS",
        "description": "The 8.87/10 value is an arithmetic mean of recommendation-likelihood ratings. No promoter, passive, or detractor classification exists, so no Net Promoter Score is calculated.",
    },
    {
        "id": "caveat-360-benchmark-scope",
        "label": "Company benchmark scope",
        "description": "Deltas compare other-rater averages with the company-average column in one 2020 assessment; they are not an external executive benchmark or a current score.",
    },
)


def _read_text(root: Path, relative_path: str) -> str:
    return (root / relative_path).read_text(encoding="utf-8")


def _sha256(root: Path, relative_path: str) -> str:
    return hashlib.sha256((root / relative_path).read_bytes()).hexdigest()


def _string_values(value: Any):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from _string_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from _string_values(child)


def _verbatim_excerpt_exists(path: Path, excerpt: str) -> bool:
    if path.suffix.lower() == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        return any(excerpt in value for value in _string_values(payload))
    return excerpt in path.read_text(encoding="utf-8")


def _sources(root: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for spec in SOURCE_SPECS:
        path = root / spec["path"]
        if not path.is_file():
            raise ValueError(f"Evidence source does not exist: {spec['id']}")
        if spec.get("excerpt_kind") == "verbatim" and not _verbatim_excerpt_exists(
            path, spec["approved_excerpt"]
        ):
            raise ValueError(
                f"Verbatim excerpt is not present in its canonical source: {spec['id']}"
            )
        record = {key: value for key, value in spec.items() if key != "path"}
        record.setdefault("excerpt_kind", "editorial_summary")
        record["sha256"] = _sha256(root, spec["path"])
        record["checksum_scope"] = "held_canonical_artifact"
        if record["access_state"] == "public_external":
            record["checksum_note"] = (
                "SHA-256 covers the held catalog/evidence artifact used by this "
                "publication boundary, not live external page content."
            )
        else:
            record["checksum_note"] = (
                "SHA-256 covers the held canonical artifact used by this publication boundary."
            )
        records.append(record)
    return records


def _session_metrics(root: Path) -> dict[str, Any]:
    datasets = json.loads(_read_text(root, SESSION_CORPUS))
    unique = [item for item in datasets if not item["is_duplicate"]]
    post = [item for item in unique if not item["is_pre_session_survey"]]
    surveys = [item for item in unique if item["is_pre_session_survey"]]

    rating_observations = sum(
        rating["count"] for item in post for rating in item["ratings"].values()
    )
    qualitative_entries = sum(len(item["text_feedback"]) for item in post)
    category_datasets = Counter(item["category"] for item in post)
    category_responses: Counter[str] = Counter()
    for item in post:
        category_responses[item["category"]] += item["response_count"]

    return {
        "raw_files": len(datasets),
        "post_session_datasets": len(post),
        "post_session_responses": sum(item["response_count"] for item in post),
        "audience_surveys": len(surveys),
        "audience_survey_responses": sum(item["response_count"] for item in surveys),
        "rating_observations": rating_observations,
        "qualitative_entries": qualitative_entries,
        "category_datasets": dict(sorted(category_datasets.items())),
        "category_responses": dict(sorted(category_responses.items())),
    }


def _student_feedback_metrics(root: Path) -> dict[str, Any]:
    forms = json.loads(_read_text(root, STUDENT_FEEDBACK_CORPUS))
    educational_institutions = sorted(
        {item["college"] for item in forms if item["college"] != "Exeter"}
    )
    corporate_contexts = [item for item in forms if item["college"] == "Exeter"]

    def weighted_rating(metric: str, scale: int) -> tuple[float, int]:
        aggregates = []
        for item in forms:
            rating = item["ratings"].get(metric)
            if not rating:
                continue
            rating_scale = 5 if rating["max"] <= 5 else 10
            if rating_scale == scale:
                aggregates.append((rating["mean"], rating["n"]))
        observations = sum(count for _, count in aggregates)
        mean = round(
            sum(value * count for value, count in aggregates) / observations,
            2,
        )
        return mean, observations

    presenter_5_mean, presenter_5_n = weighted_rating("presenter", 5)
    presenter_10_mean, presenter_10_n = weighted_rating("presenter", 10)
    recommendation_mean, recommendation_n = weighted_rating("recommend", 10)
    metrics = {
        "feedback_forms": len(forms),
        "response_rows": sum(item["responses"] for item in forms),
        "educational_institutions": educational_institutions,
        "educational_institution_count": len(educational_institutions),
        "corporate_context_count": len(corporate_contexts),
        "presenter_5_mean": presenter_5_mean,
        "presenter_5_n": presenter_5_n,
        "presenter_10_mean": presenter_10_mean,
        "presenter_10_n": presenter_10_n,
        "recommendation_mean": recommendation_mean,
        "recommendation_n": recommendation_n,
    }
    expected = {
        "feedback_forms": 13,
        "response_rows": 494,
        "educational_institution_count": 6,
        "corporate_context_count": 1,
        "presenter_5_mean": 4.58,
        "presenter_5_n": 149,
        "presenter_10_mean": 9.12,
        "presenter_10_n": 128,
        "recommendation_mean": 8.87,
        "recommendation_n": 98,
    }
    actual = {key: metrics[key] for key in expected}
    if actual != expected:
        raise ValueError(f"Student-feedback aggregate changed: {actual}")
    return metrics


def _table_row_numbers(markdown: str, label: str) -> list[int]:
    pattern = rf"^\|\s*{re.escape(label)}\s*\|(?P<cells>.+)\|$"
    match = re.search(pattern, markdown, flags=re.MULTILINE)
    if not match:
        raise ValueError(f"Could not find table row: {label}")
    values = []
    for cell in match.group("cells").split("|"):
        token = cell.strip().replace(",", "")
        if re.fullmatch(r"\d+", token):
            values.append(int(token))
    return values


def _connect_metrics(root: Path) -> dict[str, int | float]:
    markdown = _read_text(root, CONNECT_2021)
    connects = _table_row_numbers(markdown, "Connects")
    requested = _table_row_numbers(markdown, "Setup by Others")
    total = sum(connects)
    requested_total = sum(requested)
    return {
        "total_connects": total,
        "requested_by_others": requested_total,
        "requested_share": round(100 * requested_total / total),
    }


def _book_metrics(root: Path) -> dict[str, Any]:
    markdown = _read_text(root, BOOK_LEDGER)
    rows = re.findall(
        r"^\|\s*(20\d{2})\s*\|[^|]*\|\s*\d+\s*\|\s*([\d,]+)\s*\|",
        markdown,
        flags=re.MULTILINE,
    )
    annual = {int(year): int(amount.replace(",", "")) for year, amount in rows}
    if len(annual) != 10:
        raise ValueError(f"Expected 10 annual book-program rows, found {len(annual)}")
    first_year = min(annual)
    last_year = max(annual)
    unrecorded_years = [year for year in range(first_year, last_year + 1) if year not in annual]
    if unrecorded_years != [2020, 2021, 2024]:
        raise ValueError(f"Unexpected unrecorded book-program years: {unrecorded_years}")
    return {
        "annual": {str(year): annual[year] for year in sorted(annual)},
        "active_years": len(annual),
        "total_raised_inr": sum(annual.values()),
        "first_year": first_year,
        "first_year_amount_inr": annual[first_year],
        "last_year": last_year,
        "last_year_amount_inr": annual[last_year],
        "growth_factor": round(annual[last_year] / annual[first_year], 1),
        "unrecorded_years": unrecorded_years,
        "unrecorded_years_display": "2020–2021 and 2024",
    }


def _career_metrics(root: Path) -> dict[str, int]:
    markdown = _read_text(root, RESUME_2026)
    start = re.search(r"IBM \(July (20\d{2})", markdown)
    end = re.search(r"\*\*Date:\*\* (20\d{2})", markdown)
    if not start or not end:
        raise ValueError("Could not resolve career boundary years")
    start_year = int(start.group(1))
    end_year = int(end.group(1))
    return {
        "start_year": start_year,
        "end_year": end_year,
        "inclusive_calendar_years": end_year - start_year + 1,
    }


def _assessment_metrics(root: Path) -> dict[str, Any]:
    markdown = _read_text(root, FEEDBACK_360)
    rows = re.findall(
        r"^\|\s*([^|]+?)\s*\|\s*[\d.]+\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*([+\-][\d.]+)\s*\|$",
        markdown,
        flags=re.MULTILINE,
    )
    if len(rows) != 5:
        raise ValueError(f"Expected five 360 behavior rows, found {len(rows)}")
    deltas = {name.strip(): float(delta) for name, _, _, delta in rows}
    return {
        "behavior_deltas": deltas,
        "all_above_company_average": all(value > 0 for value in deltas.values()),
        "minimum_delta": min(deltas.values()),
        "maximum_delta": max(deltas.values()),
        "mean_delta": round(sum(deltas.values()) / len(deltas), 2),
    }


def _inventory_metrics(root: Path) -> dict[str, int]:
    evidence_root = root / "data" / "evidence"
    markdown = list(evidence_root.rglob("*.md"))
    individual = [
        path for path in evidence_root.glob("*/individual/*.md") if path.name != "_INDEX.md"
    ]
    informal = [
        path
        for path in (evidence_root / "informal-feedbacks").rglob("*.md")
        if path.name != "INDEX.md"
    ]
    image_extensions = {".gif", ".jpeg", ".jpg", ".png", ".svg", ".webp"}
    images = [
        path
        for path in evidence_root.rglob("*")
        if path.is_file() and path.suffix.lower() in image_extensions
    ]
    frontmatter = sum(
        1
        for path in markdown
        if path.read_text(encoding="utf-8", errors="ignore").startswith("---\n")
    )
    quality = _read_text(root, RELATIONSHIP_QUALITY)

    def report_value(label: str) -> int:
        match = re.search(rf"^\| `{re.escape(label)}` \| ([\d,]+) \|$", quality, re.MULTILINE)
        if not match:
            raise ValueError(f"Could not find quality-report value: {label}")
        return int(match.group(1).replace(",", ""))

    def check_value(label: str) -> int:
        match = re.search(rf"^\| `{re.escape(label)}` \| ([\d,]+) \|$", quality, re.MULTILINE)
        if not match:
            raise ValueError(f"Could not find quality-check value: {label}")
        return int(match.group(1).replace(",", ""))

    return {
        "evidence_markdown": len(markdown),
        "individual_evidence_records": len(individual),
        "informal_feedback_records": len(informal),
        "documentary_images": len(images),
        "frontmatter_records": frontmatter,
        "evidence_index_rows": report_value("evidence_index"),
        "artifacts": report_value("artifacts"),
        "chunks": report_value("chunks"),
        "edges": report_value("edges"),
        "nodes": report_value("nodes"),
        "orphan_edge_artifact_provenance": check_value("orphan_edge_artifact_provenance"),
        "missing_in_chroma": check_value("missing_in_chroma"),
    }


def _support(
    source_id: str,
    locator: str,
    directness: str,
    grade: str,
    rationale: str,
    relationship: str = "supports",
) -> dict[str, str]:
    return {
        "source_id": source_id,
        "relationship": relationship,
        "locator": locator,
        "directness": directness,
        "grade": grade,
        "rationale": rationale,
    }


def _claim(
    claim_id: str,
    title: str,
    statement: str,
    kind: str,
    category: str,
    scope: str,
    attribution: str,
    supports: list[dict[str, str]],
    *,
    status: str = "published",
    period: str | None = None,
    metric: dict[str, str | int | float] | None = None,
    method_id: str | None = None,
    caveat_ids: list[str] | None = None,
    conflict_ids: list[str] | None = None,
    confidence_level: str = "supported",
    confidence_rationale: str = "The claim is bounded to the linked sources and stated method.",
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "id": claim_id,
        "title": title,
        "statement": statement,
        "kind": kind,
        "category": category,
        "scope": scope,
        "attribution": attribution,
        "status": status,
        "support_specs": supports,
        "caveat_ids": caveat_ids or [],
        "conflict_ids": conflict_ids or [],
        "confidence": {
            "level": confidence_level,
            "rationale": confidence_rationale,
        },
    }
    if period is not None:
        record["period"] = period
    if metric is not None:
        record["metric"] = metric
    if method_id is not None:
        record["method_id"] = method_id
    return record


def _method(
    method_id: str,
    title: str,
    kind: str,
    description: str,
    inputs: list[dict[str, Any]],
    inclusion_rules: list[str],
    exclusion_rules: list[str],
    deduplication: str,
    rounding: str,
    result: str,
    caveat_ids: list[str],
    formula: str | None = None,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "id": method_id,
        "title": title,
        "kind": kind,
        "version": "1.0.0",
        "description": description,
        "inputs": inputs,
        "inclusion_rules": inclusion_rules,
        "exclusion_rules": exclusion_rules,
        "deduplication": deduplication,
        "rounding": rounding,
        "result": result,
        "caveat_ids": caveat_ids,
    }
    if formula is not None:
        record["formula"] = formula
    return record


def _input(
    input_id: str,
    label: str,
    *,
    source_id: str | None = None,
    claim_id: str | None = None,
    locator: str | None = None,
    value: str | int | float | None = None,
    unit: str | None = None,
) -> dict[str, Any]:
    record: dict[str, Any] = {"id": input_id, "label": label}
    if source_id is not None:
        record["source_id"] = source_id
    if claim_id is not None:
        record["claim_id"] = claim_id
    if locator is not None:
        record["locator"] = locator
    if value is not None:
        record["value"] = value
    if unit is not None:
        record["unit"] = unit
    return record


def _methods(
    sessions: dict[str, Any],
    student: dict[str, Any],
    connect: dict[str, int | float],
    books: dict[str, Any],
    career: dict[str, int],
    assessment: dict[str, Any],
    inventory: dict[str, int],
) -> list[dict[str, Any]]:
    category_result = ", ".join(
        f"{category}: {count} files / {sessions['category_responses'][category]} response rows"
        for category, count in sessions["category_datasets"].items()
    )
    delta_result = ", ".join(
        f"{name}: +{value:.2f}" for name, value in assessment["behavior_deltas"].items()
    )
    return [
        _method(
            "method-session-composition-v1",
            "Session composition and unit reconciliation",
            "deterministic_aggregation",
            "Recompute public feedback metrics from the file-level structured corpus while separating the post-event/interaction analysis population from pre-session audience surveys.",
            [
                _input(
                    "input-session-corpus",
                    "Structured response corpus",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="All dataset objects",
                ),
                _input(
                    "input-session-post-datasets",
                    "Eligible post-event/interaction analysis files",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="is_duplicate=false and is_pre_session_survey=false",
                    value=sessions["post_session_datasets"],
                    unit="files",
                ),
                _input(
                    "input-session-post-responses",
                    "Post-event/interaction response rows",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="Sum of response_count for eligible post-event/interaction files",
                    value=sessions["post_session_responses"],
                    unit="response rows",
                ),
                _input(
                    "input-session-rating-observations",
                    "Question-level rating observations",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="Sum of ratings[*].count for eligible post-event/interaction files",
                    value=sessions["rating_observations"],
                    unit="rating observations",
                ),
                _input(
                    "input-session-qualitative-entries",
                    "Populated qualitative values",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="Sum of text_feedback array lengths for eligible post-event/interaction files",
                    value=sessions["qualitative_entries"],
                    unit="qualitative entries",
                ),
                _input(
                    "input-session-audience-surveys",
                    "Pre-session audience surveys",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="is_duplicate=false and is_pre_session_survey=true",
                    value=sessions["audience_surveys"],
                    unit="surveys",
                ),
                _input(
                    "input-session-audience-responses",
                    "Pre-session survey responses",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="Sum of response_count for eligible pre-session surveys",
                    value=sessions["audience_survey_responses"],
                    unit="responses",
                ),
            ],
            [
                "Include only files explicitly marked non-duplicate.",
                "Partition files by the is_pre_session_survey flag before summing.",
                "Use response_count for response rows, rating.count for rating observations, and text_feedback length for qualitative entries.",
            ],
            [
                "Exclude duplicate records.",
                "Exclude pre-session survey rows from post-session totals.",
                "Do not infer attendance or unique people.",
            ],
            "The source's explicit is_duplicate flag is authoritative; no fuzzy deduplication is applied.",
            "Counts are integers; no rounding.",
            f"88 post-event/interaction analysis files / {sessions['post_session_responses']:,} response rows; {sessions['rating_observations']:,} rating observations; {sessions['qualitative_entries']:,} qualitative entries; 2 pre-session surveys / {sessions['audience_survey_responses']} response rows.",
            [
                "caveat-response-unit",
                "caveat-rating-observation-unit",
                "caveat-qualitative-entry-unit",
                "caveat-surveys-separated",
                "caveat-session-tracker-boundary",
                "caveat-source-label-conflict",
            ],
            formula="Filter → partition → sum field-specific units",
        ),
        _method(
            "method-session-topic-themes-v1",
            "Session topic composition",
            "deterministic_aggregation",
            "Count the single filename-pattern-derived category assigned to each eligible post-event/interaction file and sum response rows within each category.",
            [
                _input(
                    "input-topic-corpus",
                    "Eligible post-event/interaction files",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="category on non-duplicate post-event/interaction files",
                    value=sessions["post_session_datasets"],
                    unit="files",
                ),
                _input(
                    "input-topic-ai-datasets",
                    "AI/GenAI files",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="category=ai-genai",
                    value=sessions["category_datasets"]["ai-genai"],
                    unit="files",
                ),
                _input(
                    "input-topic-ai-responses",
                    "AI/GenAI response rows",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="category=ai-genai · sum response_count",
                    value=sessions["category_responses"]["ai-genai"],
                    unit="responses",
                ),
                _input(
                    "input-topic-dora-datasets",
                    "DORA files",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="category=dora",
                    value=sessions["category_datasets"]["dora"],
                    unit="files",
                ),
                _input(
                    "input-topic-dora-responses",
                    "DORA response rows",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="category=dora · sum response_count",
                    value=sessions["category_responses"]["dora"],
                    unit="responses",
                ),
            ],
            [
                "Use the existing filename-pattern-derived category field.",
                "Include only non-duplicate post-event/interaction files.",
            ],
            [
                "Do not double-count a file across categories.",
                "Do not claim that category file counts are counts of distinct facilitated sessions or that the categories capture every concept in free text.",
            ],
            "Each eligible file has one category; the explicit duplicate flag is applied first.",
            "Counts are integers; no rounding.",
            category_result,
            ["caveat-category-labels", "caveat-response-unit", "caveat-session-tracker-boundary"],
            formula="Count(dataset by category); sum(response_count by category)",
        ),
        _method(
            "method-student-feedback-aggregate-v1",
            "Student-feedback aggregate with separate rating scales",
            "deterministic_aggregation",
            "Recompute the privacy-safe community-teaching aggregate from thirteen structured feedback-form records while keeping context types, rating scales, and recommendation likelihood separate from one another and from the professional-feedback and talks trackers.",
            [
                _input(
                    "input-student-audit-summary",
                    "Audited student-feedback summary",
                    source_id="source-student-feedback-aggregate-2013-2020",
                    locator="Aggregate Statistics and Rating Averages",
                ),
                _input(
                    "input-student-corpus",
                    "Held structured form records",
                    source_id="source-student-feedback-structured-corpus-2013-2020",
                    locator="All form objects",
                ),
                _input(
                    "input-student-forms",
                    "Feedback forms",
                    source_id="source-student-feedback-structured-corpus-2013-2020",
                    locator="Count of form objects",
                    value=student["feedback_forms"],
                    unit="feedback forms",
                ),
                _input(
                    "input-student-responses",
                    "Submitted response rows",
                    source_id="source-student-feedback-structured-corpus-2013-2020",
                    locator="Sum of responses across form objects",
                    value=student["response_rows"],
                    unit="response rows",
                ),
                _input(
                    "input-student-institutions",
                    "Educational institutions",
                    source_id="source-student-feedback-structured-corpus-2013-2020",
                    locator="Distinct college values excluding Exeter",
                    value=student["educational_institution_count"],
                    unit="educational institutions",
                ),
                _input(
                    "input-student-corporate-context",
                    "Exeter corporate yoga context",
                    source_id="source-student-feedback-structured-corpus-2013-2020",
                    locator="college=Exeter",
                    value=student["corporate_context_count"],
                    unit="corporate contexts",
                ),
                _input(
                    "input-student-presenter-5",
                    "Presenter mean on 5-point forms",
                    source_id="source-student-feedback-structured-corpus-2013-2020",
                    locator="presenter aggregates with source scale /5",
                    value=student["presenter_5_mean"],
                    unit=f"/5, n={student['presenter_5_n']}",
                ),
                _input(
                    "input-student-presenter-10",
                    "Presenter mean on 10-point forms",
                    source_id="source-student-feedback-structured-corpus-2013-2020",
                    locator="presenter aggregates with source scale /10",
                    value=student["presenter_10_mean"],
                    unit=f"/10, n={student['presenter_10_n']}",
                ),
                _input(
                    "input-student-recommendation",
                    "Recommendation-likelihood mean",
                    source_id="source-student-feedback-structured-corpus-2013-2020",
                    locator="recommend aggregates on /10 forms",
                    value=student["recommendation_mean"],
                    unit=f"/10, n={student['recommendation_n']}",
                ),
            ],
            [
                "Include all thirteen form records in the separate student/community tracker.",
                "Count response rows using each form's responses field.",
                "Count six distinct educational-institution codes after explicitly separating the one Exeter corporate yoga context.",
                "Compute weighted presenter means independently for the source 5-point and 10-point scale populations.",
                "Compute recommendation likelihood only from the two forms that contain the recommend field.",
            ],
            [
                "Do not add these response rows to the professional-feedback corpus or the talks ledger's participant instances.",
                "Do not normalize or merge the 5-point and 10-point presenter populations.",
                "Preserve recommendation likelihood on its source scale; NPS classification requires separate promoter, passive, and detractor fields.",
                "Do not publish raw rows or unapproved qualitative content.",
            ],
            "Each structured object represents one source feedback form. Distinct dated forms are retained; qualitative strings are not used to inflate the form or response-row counts.",
            "Counts are integers. Weighted means use stored per-form means and n values and are rounded to two decimals; those per-form means are already rounded in the held corpus.",
            f"{student['feedback_forms']} feedback forms / {student['response_rows']} response rows; {student['educational_institution_count']} educational institutions + {student['corporate_context_count']} Exeter corporate yoga context; presenter {student['presenter_5_mean']:.2f}/5 (n={student['presenter_5_n']}) and {student['presenter_10_mean']:.2f}/10 (n={student['presenter_10_n']}) as separate populations; recommendation likelihood {student['recommendation_mean']:.2f}/10 (n={student['recommendation_n']}) on its source scale.",
            [
                "caveat-student-tracker-separate",
                "caveat-student-response-rows",
                "caveat-student-context-boundary",
                "caveat-student-rating-scales",
                "caveat-recommendation-not-nps",
                "caveat-private-held-source",
            ],
            formula="weighted_mean_by_scale = Σ(form_mean × form_n) ÷ Σ(form_n)",
        ),
        _method(
            "method-career-calendar-span-v1",
            "Career calendar-span calculation",
            "calendar_arithmetic",
            "Calculate the number of calendar years touched by the held chronology, including both boundary years.",
            [
                _input(
                    "input-career-start",
                    "First recorded career year",
                    source_id="source-career-resume-2026",
                    locator="Career history · IBM begins July 2007",
                    value=career["start_year"],
                    unit="year",
                ),
                _input(
                    "input-career-end",
                    "Portfolio as-of career year",
                    source_id="source-career-resume-2026",
                    locator="Resume source date and current role through 2026",
                    value=career["end_year"],
                    unit="year",
                ),
            ],
            [
                "Use the earliest and latest years in the selected authoritative chronology.",
                "Include both boundary calendar years.",
            ],
            [
                "Do not convert the result into completed years of tenure.",
                "Do not resolve resume headline labels by arithmetic.",
            ],
            "One authoritative career chronology is used; overlapping roles are not separately counted.",
            "Integer calendar years; no rounding.",
            f"{career['start_year']} through {career['end_year']} touches {career['inclusive_calendar_years']} calendar years inclusively.",
            [
                "caveat-calendar-span-not-tenure",
                "caveat-source-label-conflict",
                "caveat-self-authored-source",
            ],
            formula="end_year − start_year + 1",
        ),
        _method(
            "method-patent-award-registry-match-v1",
            "First-patent award to public-grant match",
            "deterministic_record_match",
            "Match the employer-issued first-patent application certificate to the later public patent grant using the full invention title and Datta's explicitly named recipient/inventor identity.",
            [
                _input(
                    "input-patent-award-title",
                    "Awarded invention title",
                    claim_id="claim-2010-first-patent-achievement",
                    source_id="source-patent-award-2010",
                    locator="Metadata · Invention title and certificate quotation",
                    value="Determining and Conveying User Availability",
                    unit="title",
                ),
                _input(
                    "input-patent-award-recipient",
                    "Named award recipient",
                    claim_id="claim-2010-first-patent-achievement",
                    source_id="source-patent-award-2010",
                    locator="Certificate quotation · recipient",
                    value="Dattatreya S. Vellal",
                    unit="person name",
                ),
                _input(
                    "input-patent-award-date",
                    "First-application recognition date",
                    source_id="source-patent-award-2010",
                    locator="Metadata · Date on certificate",
                    value="2010-12-28",
                    unit="date",
                ),
                _input(
                    "input-patent-registry-title",
                    "Granted-patent title",
                    claim_id="claim-public-patent-record",
                    source_id="source-us-patent-8560487",
                    locator="Public registry · title",
                    value="Determining and conveying user availability",
                    unit="title",
                ),
                _input(
                    "input-patent-registry-inventor",
                    "Named co-inventor",
                    claim_id="claim-public-patent-record",
                    source_id="source-us-patent-8560487",
                    locator="Public registry · Inventor list",
                    value="Dattatreya S. Vellal",
                    unit="person name",
                ),
                _input(
                    "input-patent-registry-grant",
                    "Later public grant",
                    claim_id="claim-public-patent-record",
                    source_id="source-us-patent-8560487",
                    locator="Public registry · publication number and grant date",
                    value="US8560487B2 · 2013-10-15",
                    unit="grant record",
                ),
            ],
            [
                "Normalize Unicode case and whitespace in both full titles, then require exact equality.",
                "Require the certificate recipient to appear in the public registry's inventor list.",
                "Preserve the sequence as a 2010 application-recognition artifact followed by a 2013 grant record.",
            ],
            [
                "Do not match on a shortened title alone.",
                "Do not infer that the award itself was a grant.",
                "Do not infer sole inventorship, commercial impact, adoption, revenue, citation impact, or current legal status.",
            ],
            "One employer certificate and one uniquely identified public grant record are compared; no patent-family records are added to the count.",
            "No numeric rounding; title comparison uses case-folded, whitespace-normalized text.",
            "The normalized full titles match exactly, and Dattatreya S. Vellal is named as the 2010 certificate recipient and as one of three inventors on US8560487B2, granted in 2013.",
            ["caveat-patent-scope", "caveat-selected-evidence"],
            formula="normalize(award_title) = normalize(registry_title) AND award_recipient ∈ registry_inventors",
        ),
        _method(
            "method-connect-demand-v1",
            "Connect-demand share",
            "deterministic_aggregation",
            "Sum the twelve monthly connect counts and the twelve monthly 'set up by others' counts, then divide the latter by the former.",
            [
                _input(
                    "input-connect-total",
                    "All 2021 connects",
                    source_id="source-connect-program-2021",
                    locator="Raw Data Per Month · Connects",
                    value=connect["total_connects"],
                    unit="connects",
                ),
                _input(
                    "input-connect-requested",
                    "Connects set up by others",
                    source_id="source-connect-program-2021",
                    locator="Raw Data Per Month · Setup by Others",
                    value=connect["requested_by_others"],
                    unit="connects",
                ),
            ],
            [
                "Include every month from January through December 2021.",
                "Use the ledger's explicit setup attribution.",
            ],
            [
                "Do not infer unique people, motive, satisfaction, or business outcome from a request."
            ],
            "Monthly rows are mutually exclusive within each ledger metric; no additional deduplication.",
            "Round the percentage to the nearest whole percent; retain raw numerator and denominator.",
            f"{connect['requested_by_others']} of {connect['total_connects']} connects = {connect['requested_by_others'] / connect['total_connects'] * 100:.2f}%, displayed as {connect['requested_share']}%.",
            [
                "caveat-touchpoints-not-people",
                "caveat-inference-not-motive",
                "caveat-private-held-source",
            ],
            formula="round(100 × requested_by_others ÷ total_connects)",
        ),
        _method(
            "method-book-totals-growth-v1",
            "Book-program totals and endpoint ratio",
            "deterministic_aggregation",
            "Parse the ten published annual aggregate rows, sum nominal rupees, and compare the final recorded year with the first recorded year.",
            [
                _input(
                    "input-book-active-years",
                    "Recorded active years",
                    source_id="source-book-program-ledger-2014-2026",
                    locator="Financial Summary · annual rows",
                    value=books["active_years"],
                    unit="active years",
                ),
                _input(
                    "input-book-total",
                    "Sum of annual aggregates",
                    source_id="source-book-program-ledger-2014-2026",
                    locator="Financial Summary · Total Raised",
                    value=books["total_raised_inr"],
                    unit="INR",
                ),
                _input(
                    "input-book-first",
                    "First recorded annual amount",
                    source_id="source-book-program-ledger-2014-2026",
                    locator=f"Financial Summary · {books['first_year']}",
                    value=books["first_year_amount_inr"],
                    unit="INR",
                ),
                _input(
                    "input-book-last",
                    "Latest recorded annual amount",
                    source_id="source-book-program-ledger-2014-2026",
                    locator=f"Financial Summary · {books['last_year']}",
                    value=books["last_year_amount_inr"],
                    unit="INR",
                ),
                _input(
                    "input-book-unrecorded-years",
                    "Calendar years without a reviewed program record",
                    source_id="source-book-program-ledger-2014-2026",
                    locator="Financial Summary · explicit gap rows and annual-year complement",
                    value=books["unrecorded_years_display"],
                    unit="calendar years without records",
                ),
            ],
            [
                "Include only year rows with a numeric annual total.",
                "Compute missing calendar years between the first and final recorded years and preserve 2020–2021 and 2024 as unrecorded rather than interpolating them.",
                "Treat the 2024 condition as absence of a reviewed program record, not a verified zero amount.",
            ],
            [
                "Exclude contributor identities, individual amounts, bank details, currency conversion, inflation adjustment, and beneficiary estimates.",
                "Do not imply uninterrupted activity after the 2022 resumption or calculate CAGR from non-contiguous recorded years.",
            ],
            "One aggregate row per active year; no donor-level data enters the method.",
            "Total is exact to the rupee in the aggregate source; the endpoint ratio is rounded to one decimal place.",
            f"₹{books['total_raised_inr']:,} across {books['active_years']} recorded active years; ₹{books['first_year_amount_inr']:,} in {books['first_year']} to ₹{books['last_year_amount_inr']:,} in {books['last_year']} = a {books['growth_factor']}× endpoint ratio. Years without reviewed program records: {books['unrecorded_years_display']}.",
            [
                "caveat-active-years-with-gaps",
                "caveat-currency-not-normalized",
                "caveat-private-held-source",
            ],
            formula="total = Σ annual_amount; endpoint_ratio = final_amount ÷ first_amount",
        ),
        _method(
            "method-360-company-deltas-v1",
            "2020 360 company-average deltas",
            "deterministic_comparison",
            "For each of five behaviors, subtract the company-average column from the average score given by other raters, then calculate the mean and range of those five deltas.",
            [
                *[
                    _input(
                        f"input-360-{index}",
                        f"{name} delta vs company average",
                        source_id="source-360-feedback-2020",
                        locator=f"Behavior Scores Summary · {name} · Difference vs Company",
                        value=value,
                        unit="rating points",
                    )
                    for index, (name, value) in enumerate(assessment["behavior_deltas"].items(), 1)
                ]
            ],
            [
                "Use the AVG (Others) and Company Average columns from the same report.",
                "Include all five listed behaviors.",
            ],
            [
                "Exclude self ratings from the comparison.",
                "Do not compare against the universal or digital-ready benchmark where row-level values are not published in the evidence summary.",
            ],
            "Each behavior appears once; no rater-level records are republished.",
            "Source deltas have two decimals; their arithmetic mean is rounded to two decimals.",
            f"All five deltas are positive; range +{assessment['minimum_delta']:.2f} to +{assessment['maximum_delta']:.2f}; mean +{assessment['mean_delta']:.2f}. Detail: {delta_result}.",
            ["caveat-360-benchmark-scope", "caveat-private-held-source"],
            formula="delta_behavior = others_average − company_average; mean = Σ delta ÷ 5",
        ),
        _method(
            "method-corpus-coverage-v1",
            "Evidence-corpus and export coverage",
            "repository_inventory",
            "Inventory held Markdown and documentary image files and compare them with the generated evidence-index and retrieval-export quality report.",
            [
                _input(
                    "input-inventory-markdown",
                    "Evidence Markdown files",
                    source_id="source-evidence-inventory-2026",
                    locator="Repository inventory · all held evidence Markdown",
                    value=inventory["evidence_markdown"],
                    unit="files",
                ),
                _input(
                    "input-inventory-individual",
                    "Individual evidence records excluding year indexes",
                    source_id="source-evidence-inventory-2026",
                    locator="Repository inventory · year/individual records",
                    value=inventory["individual_evidence_records"],
                    unit="files",
                ),
                _input(
                    "input-inventory-informal",
                    "Informal-feedback records excluding index",
                    source_id="source-evidence-inventory-2026",
                    locator="Repository inventory · informal feedback records",
                    value=inventory["informal_feedback_records"],
                    unit="files",
                ),
                _input(
                    "input-inventory-images",
                    "Documentary images",
                    source_id="source-evidence-inventory-2026",
                    locator="Repository inventory · supported image extensions",
                    value=inventory["documentary_images"],
                    unit="files",
                ),
                _input(
                    "input-inventory-index",
                    "Evidence-index rows",
                    source_id="source-relationship-export-quality-2026",
                    locator="DuckDB tables · evidence_index",
                    value=inventory["evidence_index_rows"],
                    unit="rows",
                ),
                _input(
                    "input-inventory-missing-embeddings",
                    "Chunks absent from retrieval index",
                    source_id="source-relationship-export-quality-2026",
                    locator="ChromaDB alignment · missing_in_chroma",
                    value=inventory["missing_in_chroma"],
                    unit="chunks",
                ),
                _input(
                    "input-inventory-orphan-provenance",
                    "Edges with orphan artifact provenance",
                    source_id="source-relationship-export-quality-2026",
                    locator="Referential and graph checks · orphan_edge_artifact_provenance",
                    value=inventory["orphan_edge_artifact_provenance"],
                    unit="edges",
                ),
            ],
            [
                "Count held files at build time using explicit extensions.",
                "Exclude index Markdown from individual and informal-feedback record counts.",
                "Use generated quality-report values for database and retrieval coverage.",
            ],
            [
                "Do not interpret a file count as verified claim count.",
                "Do not publish local filenames or raw records.",
            ],
            "Filesystem paths are counted once; quality-report rows use their canonical generated counts.",
            "Counts are integers; no rounding.",
            f"{inventory['evidence_markdown']:,} evidence Markdown files, including {inventory['individual_evidence_records']:,} individual records and {inventory['informal_feedback_records']:,} informal-feedback records; {inventory['documentary_images']:,} documentary images; {inventory['evidence_index_rows']:,} indexed evidence rows; {inventory['missing_in_chroma']:,} chunks absent from the retrieval index; {inventory['orphan_edge_artifact_provenance']} provenance gaps.",
            ["caveat-export-gap", "caveat-private-held-source"],
            formula="Count reviewed filesystem classes; join generated export-quality counts",
        ),
        _method(
            "method-feedback-executive-observation-v1",
            "Development signal to later executive-influence observation",
            "qualitative_synthesis",
            "Link a specific 2020 development request with independent 2025 observations that describe the requested behavior. The method tests recurrence in language and context; it does not score growth or infer causality.",
            [
                _input(
                    "input-executive-development",
                    "2020 development request",
                    claim_id="claim-2020-executive-influence-development-signal",
                    source_id="source-360-feedback-2020",
                    locator="Greatest Development Area · broaden senior-executive influence",
                ),
                _input(
                    "input-executive-observation",
                    "2025 independent colleague observation",
                    claim_id="claim-2025-executive-influence-observation",
                    source_id="source-influence-recommendation-2025",
                    locator="Recommendation · executives-to-developers communication, influence, roadmap execution, data",
                ),
                _input(
                    "input-cross-boundary-observation",
                    "2025 manager observation",
                    claim_id="claim-2025-cross-boundary-leadership",
                    source_id="source-manager-recommendation-2025",
                    locator="Recommendation · reporting lines, seniority, team boundaries",
                ),
            ],
            [
                "Require a dated development statement and later independently attributed behavioral observations.",
                "Preserve the source relationship and wording context.",
            ],
            [
                "Do not claim a before/after score, completed development, promotion readiness, or causal effect."
            ],
            "One assessment and two independently attributed 2025 recommendations are used; duplicated source narratives are excluded.",
            "No numeric rounding; the output is a bounded qualitative relationship.",
            "The requested executive-influence behavior is present in later independent observations, supporting a non-causal development-to-observation concordance.",
            [
                "caveat-non-causal-synthesis",
                "caveat-selected-evidence",
                "caveat-private-held-source",
            ],
        ),
        _method(
            "method-strengths-observation-concordance-v1",
            "Strengths profile to later observed behavior",
            "qualitative_synthesis",
            "Map named 2020 assessment strengths to semantically corresponding behaviors in two independent 2025 recommendations.",
            [
                _input(
                    "input-strengths-profile",
                    "2020 ranked strengths",
                    claim_id="claim-2020-strengths-profile",
                    source_id="source-strengths-assessment-2020",
                    locator="Top 7 Strengths",
                ),
                _input(
                    "input-strengths-ian",
                    "2025 colleague observations",
                    claim_id="claim-2025-executive-influence-observation",
                    source_id="source-influence-recommendation-2025",
                    locator="Relationships, multi-level communication, data",
                ),
                _input(
                    "input-strengths-rob",
                    "2025 manager observations",
                    claim_id="claim-2025-cross-boundary-leadership",
                    source_id="source-manager-recommendation-2025",
                    locator="Meticulous, organized, empathetic, collaborative",
                ),
            ],
            [
                "Map only explicit assessment labels to explicit later behavioral descriptions.",
                "Require the later record to be independently attributed.",
            ],
            [
                "Do not treat a psychometric profile as performance proof.",
                "Do not claim every strength was independently observed.",
            ],
            "Two distinct 2025 recommenders are used; repeated editorial analysis within source files is ignored.",
            "No numeric rounding; five named correspondences are reported.",
            "Articulate ↔ multi-level communication; Meticulous ↔ meticulous detail; Evaluative ↔ data underpinning; Networker ↔ relationship building; Genuine ↔ approachable, empathetic collaboration.",
            [
                "caveat-assessment-not-performance",
                "caveat-non-causal-synthesis",
                "caveat-selected-evidence",
            ],
        ),
        _method(
            "method-quality-before-ai-lineage-v1",
            "Quality-before-AI engineering-control lineage",
            "qualitative_synthesis",
            "Trace a dated sequence in which quality due diligence, process improvement, delivery recognition, quality-as-speed framing, DORA/craft observations, and commit-level AI quality gates recur across roles.",
            [
                _input(
                    "input-quality-2015",
                    "2015 quality discipline",
                    claim_id="claim-2015-quality-discipline",
                    source_id="source-exeter-performance-review-2015",
                    locator="Behavioral Competencies and Key Quotes",
                ),
                _input(
                    "input-quality-2017",
                    "2017 process and delivery recognition",
                    claim_id="claim-2017-process-delivery-recognition",
                    source_id="source-amazon-process-recognition-2017",
                    locator="Award reason",
                ),
                _input(
                    "input-delivery-2017",
                    "2017 exceptional delivery recognition",
                    source_id="source-amazon-delivery-recognition-2017",
                    locator="Award reason",
                ),
                _input(
                    "input-quality-2020",
                    "2020 quality/speed framing",
                    claim_id="claim-2020-quality-speed-framing",
                    source_id="source-360-feedback-2020",
                    locator="Line manager comments · quality in context",
                ),
                _input(
                    "input-quality-2025",
                    "2025 craftsmanship and DORA observation",
                    claim_id="claim-2025-cross-boundary-leadership",
                    source_id="source-manager-recommendation-2025",
                    locator="Craftsmanship, pipelines, DORA",
                ),
                _input(
                    "input-quality-2026",
                    "2026 AI-native gated delivery",
                    claim_id="claim-sutra-ai-delivery",
                    source_id="source-sutra-initiative-outcomes-2026",
                    locator="Datta team comment · 3× speed, AI code, commit gates",
                ),
            ],
            [
                "Require dated evidence from 2015, 2017, 2020, 2025, and 2026.",
                "Distinguish independent observations and awards from team-authored delivery commentary.",
            ],
            [
                "Do not claim that the earlier practices caused the later speed claim.",
                "Do not generalize Sutra's initiative metrics to the XITE portfolio or other teams.",
            ],
            "Each time point is represented once; the two complementary 2017 award artifacts are retained as distinct process and delivery observations.",
            "No numeric rounding; chronology and source grades remain visible.",
            "The sequence supports the interpretation that 2026 AI adoption sits on a pre-existing engineering control system, not novelty alone; causality and individual attribution remain unproven.",
            [
                "caveat-non-causal-synthesis",
                "caveat-team-attribution",
                "caveat-self-authored-source",
                "caveat-selected-evidence",
                "caveat-initiative-scope",
            ],
        ),
        _method(
            "method-title-independent-leadership-v1",
            "Title-independent leadership continuity",
            "qualitative_synthesis",
            "Compare leadership evidence from an early individual-contributor period with later cross-team, informal-mentoring, and manager observations that explicitly cross formal reporting boundaries.",
            [
                _input(
                    "input-title-2008",
                    "Early-career end-to-end leadership",
                    claim_id="claim-2008-early-leadership",
                    source_id="source-leadership-award-2008",
                    locator="Award citation",
                ),
                _input(
                    "input-title-2015",
                    "Cross-team bridge building",
                    claim_id="claim-2015-cross-team-leadership",
                    source_id="source-cross-team-recommendation-2015",
                    locator="Recommendation · organization-wide and cross-location work",
                ),
                _input(
                    "input-title-2023",
                    "Mentoring without a reporting line",
                    claim_id="claim-2023-purpose-first-mentoring",
                    source_id="source-purpose-first-mentoring-recommendation-2023",
                    locator="Relationship and recommendation",
                ),
                _input(
                    "input-title-2025",
                    "Leadership across boundaries",
                    claim_id="claim-2025-cross-boundary-leadership",
                    source_id="source-manager-recommendation-2025",
                    locator="Recommendation · reporting lines, seniority, team boundaries",
                ),
            ],
            [
                "Use evidence that describes behavior or influence, not title alone.",
                "Include sources from multiple organizations and relationship types.",
            ],
            [
                "Do not infer formal people-management scope where the source describes informal or cross-boundary leadership."
            ],
            "One representative source per time point is used; source relationship is preserved.",
            "No numeric rounding; the result is a continuity proposition.",
            "Leadership behavior is documented before senior titles and later explicitly outside reporting lines, supporting a title-independent leadership pattern.",
            ["caveat-non-causal-synthesis", "caveat-selected-evidence"],
        ),
        _method(
            "method-learn-build-teach-systemize-v1",
            "Learn → build → teach → systemize operating pattern",
            "qualitative_synthesis",
            "Trace recurring conversion of personal learning or building into reusable artifacts, teaching, and mechanisms across IBM, Exeter, Amazon, and Philips evidence.",
            [
                _input(
                    "input-lbts-ibm",
                    "IBM invention and technical community contribution",
                    claim_id="claim-public-patent-record",
                    source_id="source-us-patent-8560487",
                    locator="Public patent record",
                ),
                _input(
                    "input-lbts-exeter",
                    "Exeter technical teaching and cross-team initiatives",
                    claim_id="claim-2015-cross-team-leadership",
                    source_id="source-cross-team-recommendation-2015",
                    locator="Technology sessions and organization-wide initiatives",
                ),
                _input(
                    "input-lbts-amazon",
                    "Amazon self-service tools, guides, and workshops",
                    source_id="source-amazon-work-examples-2018",
                    locator="Hire & Develop the Best and reusable delivery examples",
                ),
                _input(
                    "input-lbts-philips",
                    "Philips structured feedback corpus",
                    claim_id="claim-session-post-datasets",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="Eligible post-event/interaction files",
                ),
                _input(
                    "input-lbts-sutra",
                    "AI system delivery and learning recognition",
                    claim_id="claim-sutra-delivery-recognition",
                    source_id="source-sutra-recognition-2026",
                    locator="Recognition reason",
                ),
            ],
            [
                "Require evidence of at least two stages of the pattern at each represented employer.",
                "Preserve self-authored versus independently documented source grades.",
            ],
            [
                "Do not imply that every project followed every stage or that teaching caused delivery outcomes."
            ],
            "Representative artifacts are selected by employer and stage; duplicate summaries are excluded.",
            "No numeric rounding; the output is a recurring operating-pattern interpretation.",
            "Across employers, the record repeatedly moves from learning/building to reusable teaching or systems, with varying evidence strength at each stage.",
            [
                "caveat-non-causal-synthesis",
                "caveat-selected-evidence",
                "caveat-self-authored-source",
            ],
        ),
        _method(
            "method-topic-frontier-teaching-continuity-v1",
            "Topic-frontier shift with practical teaching continuity",
            "mixed_method_synthesis",
            "Combine the dated talks ledger with filename-pattern-derived post-event topic counts to compare subject evolution while checking whether practical, feedback-seeking delivery remains present.",
            [
                _input(
                    "input-frontier-talks",
                    "2010–2021 talks ledger",
                    claim_id="claim-community-talks-reach",
                    source_id="source-community-talks-ledger-2010-2021",
                    locator="Complete Talks List · first and last entries",
                    value=50,
                    unit="recorded sessions",
                ),
                _input(
                    "input-frontier-ai",
                    "AI/GenAI post-event files",
                    claim_id="claim-session-ai-feedback",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="category=ai-genai",
                    value=sessions["category_datasets"]["ai-genai"],
                    unit="files",
                ),
                _input(
                    "input-frontier-quality",
                    "Code-quality post-event files",
                    source_id="source-session-response-corpus-2018-2026",
                    locator="category=code-quality",
                    value=sessions["category_datasets"]["code-quality"],
                    unit="files",
                ),
                _input(
                    "input-frontier-practice",
                    "Practical AI takeaway",
                    claim_id="claim-2024-practical-ai-takeaway",
                    source_id="source-participant-takeaway-ai-guardrails-2024",
                    locator="Key-takeaways response field",
                ),
                _input(
                    "input-frontier-depth",
                    "Continuing hands-on request",
                    claim_id="claim-2026-hands-on-depth-request",
                    source_id="source-participant-improvement-hands-on-agents-2026",
                    locator="Facilitator-improvement response field",
                ),
            ],
            [
                "Use dated ledger endpoints and explicit reviewed topic labels.",
                "Retain both positive takeaways and improvement requests.",
            ],
            [
                "Do not treat approximate participant instances as unique people.",
                "Do not infer that older topics stopped or that category counts equal all teaching activity.",
            ],
            "The talks ledger and feedback corpus have different scopes and are not merged into one count.",
            "Counts are integers; narrative comparison is not rounded.",
            f"The recorded frontier moves from wellness and foundational software topics toward observability and AI; the post-event corpus includes {sessions['category_datasets']['ai-genai']} AI-category files / {sessions['category_responses']['ai-genai']} response rows, while practical examples, guardrails, and hands-on depth remain recurring teaching concerns.",
            [
                "caveat-category-labels",
                "caveat-touchpoints-not-people",
                "caveat-session-tracker-boundary",
                "caveat-feedback-not-longitudinal",
                "caveat-non-causal-synthesis",
            ],
        ),
        _method(
            "method-service-continuity-growth-v1",
            "Service recurrence and endpoint ratio",
            "mixed_method_synthesis",
            "Combine dated documentary evidence of direct service with the privacy-safe annual financial aggregates while explicitly preserving all unrecorded years and the non-contiguous post-2022 sequence.",
            [
                _input(
                    "input-service-photos",
                    "Dated teaching and distribution record",
                    claim_id="claim-community-service-photo-record",
                    source_id="source-community-service-photo-record-2007-2015",
                    locator="Timeline and slides 20, 27, 30–32, 38–39",
                ),
                _input(
                    "input-service-total",
                    "Program aggregate total",
                    claim_id="claim-book-program-total",
                    source_id="source-book-program-ledger-2014-2026",
                    locator="Financial Summary",
                    value=books["total_raised_inr"],
                    unit="INR",
                ),
                _input(
                    "input-service-growth",
                    "Program endpoint ratio",
                    claim_id="claim-book-program-growth",
                    source_id="source-book-program-ledger-2014-2026",
                    locator="2014 and 2026 annual aggregates",
                    value=books["growth_factor"],
                    unit="times",
                ),
                _input(
                    "input-service-unrecorded-years",
                    "Unrecorded calendar years",
                    source_id="source-book-program-ledger-2014-2026",
                    locator="Financial Summary · 2020–2021 gap and no 2024 record",
                    value=books["unrecorded_years_display"],
                    unit="calendar years without records",
                ),
            ],
            [
                "Require dated direct-service documentation and separate annual aggregate records.",
                "Show that no program is recorded for 2020–2021 and no reviewed 2024 program record is present.",
                "Represent 2022 as a resumption and 2025 as the next recorded year, not as proof of uninterrupted post-2022 activity.",
            ],
            [
                "Exclude identities, individual amounts, bank records, beneficiary estimates, and claims of uninterrupted annual activity.",
                "Do not infer a zero amount or verified inactivity solely from the absence of a 2024 record.",
            ],
            "Photo and ledger evidence remain separate; annual aggregates have one row per active year.",
            "Financial total is exact to the rupee; the endpoint ratio is rounded to one decimal place.",
            f"Direct service is documented before and during the program's early years. The ledger resumes in 2022 after no program recorded for 2020–2021, contains no reviewed 2024 program record, then records 2025 and the highest annual endpoint in 2026. The sequence is explicitly non-contiguous; years without records are {books['unrecorded_years_display']}.",
            [
                "caveat-active-years-with-gaps",
                "caveat-currency-not-normalized",
                "caveat-private-held-source",
                "caveat-non-causal-synthesis",
            ],
        ),
        _method(
            "method-professional-community-trust-bridge-v1",
            "Privacy-safe professional/community trust bridge",
            "identity_redacted_record_linkage",
            "Use a reviewed identity match held behind the publication boundary to establish that one person appears in both a professional recommendation and multi-year service-program contribution records.",
            [
                _input(
                    "input-trust-professional",
                    "2015 professional recommendation",
                    claim_id="claim-2015-cross-team-leadership",
                    source_id="source-cross-team-recommendation-2015",
                    locator="Identity-held recommendation record",
                ),
                _input(
                    "input-trust-community",
                    "Multi-year contribution continuity",
                    claim_id="claim-book-program-total",
                    source_id="source-book-program-ledger-2014-2026",
                    locator="Identity-held contributor records; public output suppresses identity and amounts",
                ),
            ],
            [
                "Require an exact reviewed identity match across the two held records.",
                "Publish only the existence of continuity.",
            ],
            [
                "Exclude the person's identity, contribution amounts, contact data, and any inference about motive."
            ],
            "One matched identity is counted once; no fuzzy identity resolution is exposed.",
            "No numeric amount or frequency is published.",
            "One identity-redacted person appears in both contexts, supporting a bounded cross-context trust signal.",
            [
                "caveat-identity-withheld",
                "caveat-inference-not-motive",
                "caveat-private-held-source",
                "caveat-non-causal-synthesis",
            ],
        ),
        _method(
            "method-feedback-adaptation-tension-v1",
            "Feedback-to-adaptation tension",
            "qualitative_synthesis",
            "Compare selected, dated participant feedback about practical relevance, examples, prompting guardrails, and requests for deeper hands-on work without treating different cohorts as a panel.",
            [
                _input(
                    "input-adaptation-2019",
                    "2019 request for relevant examples and hands-on depth",
                    claim_id="claim-2019-practical-feedback-request",
                    source_id="source-participant-improvement-relevant-examples-2019",
                    locator="Facilitator-improvement response field",
                ),
                _input(
                    "input-adaptation-2024",
                    "2024 takeaway on prompting and guardrails",
                    claim_id="claim-2024-practical-ai-takeaway",
                    source_id="source-participant-takeaway-ai-guardrails-2024",
                    locator="Key-takeaways response field",
                ),
                _input(
                    "input-adaptation-2026",
                    "2026 request for more hands-on agent sessions",
                    claim_id="claim-2026-hands-on-depth-request",
                    source_id="source-participant-improvement-hands-on-agents-2026",
                    locator="Facilitator-improvement response field",
                ),
            ],
            [
                "Use dated feedback that contains a concrete learning takeaway or delivery improvement request.",
                "Retain both evidence of adaptation and continuing unmet demand.",
            ],
            [
                "Do not claim the same people were followed over time.",
                "Do not label the improvement request solved or infer causality from the sequence.",
            ],
            "Each selected feedback entry represents a distinct source row; no sentiment averaging is applied.",
            "No numeric rounding; the result is a bounded tension statement.",
            "Later feedback praises practical prompting and guardrails, while recent participants still request more hands-on depth: an ongoing adaptation signal, not a solved trajectory.",
            [
                "caveat-feedback-not-longitudinal",
                "caveat-non-causal-synthesis",
                "caveat-selected-evidence",
                "caveat-session-tracker-boundary",
            ],
        ),
    ]


def _claims(
    sessions: dict[str, Any],
    student: dict[str, Any],
    connect: dict[str, int | float],
    books: dict[str, Any],
    career: dict[str, int],
    assessment: dict[str, Any],
    inventory: dict[str, int],
) -> list[dict[str, Any]]:
    session_support = _support(
        "source-session-response-corpus-2018-2026",
        "Non-duplicate post-event/interaction analysis population",
        "aggregate",
        "documented",
        "The structured fields permit deterministic, field-specific aggregation.",
    )
    return [
        _claim(
            "claim-career-calendar-span",
            "A career record spanning twenty calendar years",
            f"The selected chronology touches {career['inclusive_calendar_years']} calendar years from {career['start_year']} through {career['end_year']}, inclusive.",
            "calculated",
            "journey",
            "individual",
            "Datta career chronology",
            [
                _support(
                    "source-career-resume-2026",
                    "Career chronology · IBM through current role",
                    "direct",
                    "self_reported",
                    "The held resume supplies both boundary years.",
                )
            ],
            period=f"{career['start_year']}–{career['end_year']}",
            metric={
                "value": career["inclusive_calendar_years"],
                "display": f"{career['inclusive_calendar_years']} calendar years",
                "unit": "inclusive calendar years",
            },
            method_id="method-career-calendar-span-v1",
            caveat_ids=[
                "caveat-calendar-span-not-tenure",
                "caveat-source-label-conflict",
                "caveat-self-authored-source",
            ],
            conflict_ids=["conflict-career-duration-labels"],
            confidence_level="high",
            confidence_rationale="The boundary years are explicit and the inclusive arithmetic is deterministic; the semantic limitation is prominent.",
        ),
        _claim(
            "claim-session-post-datasets",
            "Eighty-eight post-event/interaction analysis files",
            f"After excluding two duplicate files and separating two pre-session surveys, the corpus contains {sessions['post_session_datasets']} post-event or interaction feedback files. This is not asserted to be the number of facilitated sessions.",
            "calculated",
            "learning",
            "program_evidence",
            "Compiled feedback corpus",
            [session_support],
            period="2018–2026",
            metric={
                "value": sessions["post_session_datasets"],
                "display": f"{sessions['post_session_datasets']} analysis files",
                "unit": "files",
            },
            method_id="method-session-composition-v1",
            caveat_ids=[
                "caveat-surveys-separated",
                "caveat-session-tracker-boundary",
                "caveat-source-label-conflict",
            ],
            conflict_ids=["conflict-session-population-accounting", "conflict-session-year-count"],
            confidence_level="high",
            confidence_rationale="The explicit duplicate and pre-survey flags reproduce the corrected aggregate exactly.",
        ),
        _claim(
            "claim-session-post-responses",
            "1,050 post-event/interaction response rows",
            f"The {sessions['post_session_datasets']}-file analysis population contains {sessions['post_session_responses']:,} submitted response rows.",
            "calculated",
            "learning",
            "program_evidence",
            "Compiled feedback corpus",
            [session_support],
            period="2018–2026",
            metric={
                "value": sessions["post_session_responses"],
                "display": f"{sessions['post_session_responses']:,} response rows",
                "unit": "response rows",
            },
            method_id="method-session-composition-v1",
            caveat_ids=[
                "caveat-response-unit",
                "caveat-surveys-separated",
                "caveat-session-tracker-boundary",
            ],
            conflict_ids=["conflict-session-population-accounting"],
            confidence_level="high",
            confidence_rationale="The figure is the deterministic sum of response_count in the eligible files.",
        ),
        _claim(
            "claim-session-rating-observations",
            "2,149 question-level rating observations",
            f"The analysis population contains {sessions['rating_observations']:,} rating observations after summing each rating question's recorded count.",
            "calculated",
            "learning",
            "program_evidence",
            "Compiled feedback corpus",
            [session_support],
            period="2018–2026",
            metric={
                "value": sessions["rating_observations"],
                "display": f"{sessions['rating_observations']:,} rating observations",
                "unit": "rating observations",
            },
            method_id="method-session-composition-v1",
            caveat_ids=[
                "caveat-rating-observation-unit",
                "caveat-surveys-separated",
                "caveat-session-tracker-boundary",
            ],
            conflict_ids=["conflict-session-rating-units"],
            confidence_level="high",
            confidence_rationale="The count is reproducible from the stored per-question count field; it is not relabeled as respondents.",
        ),
        _claim(
            "claim-session-qualitative-entries",
            "1,811 qualitative feedback entries",
            f"The analysis population contains {sessions['qualitative_entries']:,} populated qualitative field values.",
            "calculated",
            "learning",
            "program_evidence",
            "Compiled feedback corpus",
            [session_support],
            period="2018–2026",
            metric={
                "value": sessions["qualitative_entries"],
                "display": f"{sessions['qualitative_entries']:,} qualitative entries",
                "unit": "qualitative entries",
            },
            method_id="method-session-composition-v1",
            caveat_ids=[
                "caveat-qualitative-entry-unit",
                "caveat-surveys-separated",
                "caveat-session-tracker-boundary",
            ],
            conflict_ids=["conflict-session-population-accounting"],
            confidence_level="high",
            confidence_rationale="The figure is the sum of text_feedback array lengths for eligible files.",
        ),
        _claim(
            "claim-session-audience-surveys",
            "Audience research is disclosed separately",
            f"Two pre-session surveys contain {sessions['audience_survey_responses']} response rows; they are useful audience research and excluded from post-event feedback totals.",
            "calculated",
            "learning",
            "program_evidence",
            "Compiled feedback corpus",
            [session_support],
            period="2025",
            metric={
                "value": sessions["audience_survey_responses"],
                "display": f"2 surveys · {sessions['audience_survey_responses']} rows",
                "unit": "response rows",
            },
            method_id="method-session-composition-v1",
            caveat_ids=["caveat-response-unit", "caveat-surveys-separated"],
            conflict_ids=["conflict-session-population-accounting"],
            confidence_level="high",
            confidence_rationale="The source explicitly flags both pre-session surveys and their response counts.",
        ),
        _claim(
            "claim-session-ai-feedback",
            "AI/GenAI became a measured learning frontier",
            f"The filename-derived AI/GenAI category contains {sessions['category_datasets']['ai-genai']} post-event files and {sessions['category_responses']['ai-genai']} response rows.",
            "calculated",
            "innovation",
            "program_evidence",
            "Compiled feedback corpus",
            [session_support],
            period="2024–2026",
            metric={
                "value": sessions["category_datasets"]["ai-genai"],
                "display": f"{sessions['category_datasets']['ai-genai']} files · {sessions['category_responses']['ai-genai']} rows",
                "unit": "files",
            },
            method_id="method-session-topic-themes-v1",
            caveat_ids=[
                "caveat-category-labels",
                "caveat-response-unit",
                "caveat-session-tracker-boundary",
            ],
            conflict_ids=["conflict-session-category-counts"],
            confidence_level="high",
            confidence_rationale="Counts are reproducible from the explicit category and response_count fields; the filename-rule limitation is disclosed.",
        ),
        _claim(
            "claim-session-dora-feedback",
            "DORA learning has eleven measured feedback files",
            f"The filename-derived DORA category contains {sessions['category_datasets']['dora']} post-event files and {sessions['category_responses']['dora']} response rows.",
            "calculated",
            "impact",
            "program_evidence",
            "Compiled feedback corpus",
            [session_support],
            period="2025",
            metric={
                "value": sessions["category_datasets"]["dora"],
                "display": f"{sessions['category_datasets']['dora']} files · {sessions['category_responses']['dora']} rows",
                "unit": "files",
            },
            method_id="method-session-topic-themes-v1",
            caveat_ids=[
                "caveat-category-labels",
                "caveat-response-unit",
                "caveat-session-tracker-boundary",
            ],
            conflict_ids=["conflict-session-category-counts"],
            confidence_level="high",
            confidence_rationale="Counts are reproducible from the explicit category and response_count fields; the filename-rule limitation is disclosed.",
        ),
        _claim(
            "claim-student-feedback-coverage",
            "A separate community-teaching tracker contains 494 response rows",
            f"A privacy-safe tracker covers {student['feedback_forms']} feedback forms and {student['response_rows']} submitted response rows across {student['educational_institution_count']} educational institutions plus {student['corporate_context_count']} Exeter corporate yoga context. It is not combined with the professional-feedback corpus or the talks ledger.",
            "calculated",
            "community_learning",
            "community_teaching",
            "Separate student/community feedback tracker",
            [
                _support(
                    "source-student-feedback-aggregate-2013-2020",
                    "Aggregate Statistics · form, response-row, and context counts",
                    "aggregate",
                    "documented",
                    "The audited summary states the tracker boundary and the three aggregate units explicitly.",
                )
            ],
            period="2013–2020",
            metric={
                "value": student["response_rows"],
                "display": f"{student['feedback_forms']} forms · {student['response_rows']} response rows",
                "unit": "response rows",
            },
            method_id="method-student-feedback-aggregate-v1",
            caveat_ids=[
                "caveat-student-tracker-separate",
                "caveat-student-response-rows",
                "caveat-student-context-boundary",
                "caveat-private-held-source",
            ],
            confidence_level="high",
            confidence_rationale="The form and response-row counts are deterministically recomputed from the held structured form records; the tracker boundary and context split are explicit.",
        ),
        _claim(
            "claim-student-presenter-ratings",
            "Presenter ratings remain visible on their original scales",
            f"The student/community tracker records a weighted presenter mean of {student['presenter_5_mean']:.2f}/5 across n={student['presenter_5_n']} ratings and {student['presenter_10_mean']:.2f}/10 across a separate n={student['presenter_10_n']} ratings. The populations are neither normalized nor merged.",
            "calculated",
            "community_learning",
            "community_teaching",
            "Separate student/community feedback tracker",
            [
                _support(
                    "source-student-feedback-aggregate-2013-2020",
                    "Rating Averages · Presenter rows on /5 and /10 scales",
                    "aggregate",
                    "documented",
                    "The audited summary publishes both source-scale populations and their response counts separately.",
                )
            ],
            period="2017–2020",
            metric={
                "value": student["presenter_5_mean"],
                "display": f"{student['presenter_5_mean']:.2f}/5 (n={student['presenter_5_n']}) · {student['presenter_10_mean']:.2f}/10 (n={student['presenter_10_n']})",
                "unit": "separate source-scale populations",
            },
            method_id="method-student-feedback-aggregate-v1",
            caveat_ids=[
                "caveat-student-tracker-separate",
                "caveat-student-rating-scales",
                "caveat-student-response-rows",
                "caveat-private-held-source",
            ],
            confidence_level="supported",
            confidence_rationale="The weighted means and n values are reproducible from per-form aggregates, while the source-scale and already-rounded-input limitations remain visible.",
        ),
        _claim(
            "claim-student-recommendation-likelihood",
            "Recommendation likelihood averaged 8.87/10",
            f"Two student/community forms record an arithmetic mean recommendation likelihood of {student['recommendation_mean']:.2f}/10 across n={student['recommendation_n']} ratings on the original source scale.",
            "calculated",
            "community_learning",
            "community_teaching",
            "Separate student/community feedback tracker",
            [
                _support(
                    "source-student-feedback-aggregate-2013-2020",
                    "Rating Averages · Recommend to friend row and source-scale definition",
                    "aggregate",
                    "documented",
                    "The audited summary reports the arithmetic mean, its population, and its source-scale definition.",
                )
            ],
            period="2020",
            metric={
                "value": student["recommendation_mean"],
                "display": f"{student['recommendation_mean']:.2f}/10 · n={student['recommendation_n']}",
                "unit": "recommendation-likelihood ratings",
            },
            method_id="method-student-feedback-aggregate-v1",
            caveat_ids=[
                "caveat-student-tracker-separate",
                "caveat-student-rating-scales",
                "caveat-recommendation-not-nps",
                "caveat-student-response-rows",
                "caveat-private-held-source",
            ],
            confidence_level="supported",
            confidence_rationale="The weighted arithmetic mean is reproducible from two stored form aggregates, and its distinction from NPS is explicit.",
        ),
        _claim(
            "claim-student-takeaway-interview-resilience-2017",
            "A 2017 interview-preparation takeaway links learning with resilience",
            "The approved anonymous NIE key-takeaways field contains this verbatim response: “I will try to learn application of ds and improve my soft skills! And its ok to fail”. No respondent identity is present, and the repeated text is not treated as a unique-person count.",
            "observed",
            "participant_takeaway",
            "community_feedback",
            "Anonymous NIE feedback field",
            [
                _support(
                    "source-student-takeaway-interview-resilience-2017",
                    "2017-07-08 NIE HowToPrepareForTechInterviews form · feedback.key_takeaways[0] (same text also at [1])",
                    "direct",
                    "documented",
                    "The excerpt is an exact string from the documented key-takeaways field, and the public record preserves respondent anonymity.",
                )
            ],
            period="2017-07-08",
            caveat_ids=[
                "caveat-student-tracker-separate",
                "caveat-student-response-rows",
                "caveat-selected-evidence",
                "caveat-private-held-source",
            ],
            confidence_level="high",
            confidence_rationale="The text and field classification are exact; no identity, uniqueness, representativeness, or causal outcome is inferred.",
        ),
        _claim(
            "claim-student-takeaway-uncertainty-2020",
            "A 2020 uncertainty-session takeaway emphasizes adaptive action",
            "The approved anonymous SIT key-takeaways field contains this verbatim response: “Accept the uncertainty , think differently and move forward.” No respondent identity is present, and the selected response is not generalized to every participant.",
            "observed",
            "participant_takeaway",
            "community_feedback",
            "Anonymous SIT feedback field",
            [
                _support(
                    "source-student-takeaway-uncertainty-2020",
                    "2020-08-08 SIT HowToDealWithUncertainity form · feedback.key_takeaways[31]",
                    "direct",
                    "documented",
                    "The excerpt is an exact sequence within the documented key-takeaways string; source whitespace is preserved in the held record, and the public record preserves respondent anonymity.",
                )
            ],
            period="2020-08-08",
            caveat_ids=[
                "caveat-student-tracker-separate",
                "caveat-student-response-rows",
                "caveat-selected-evidence",
                "caveat-private-held-source",
            ],
            confidence_level="high",
            confidence_rationale="The text and field classification are exact; no identity, representativeness, or causal outcome is inferred.",
        ),
        _claim(
            "claim-community-talks-reach",
            "A long-running record of public teaching",
            "A held activity ledger records 50 community and professional sessions and 3,732 participant instances across 2010–2021.",
            "observed",
            "community",
            "community_program",
            "Datta-maintained talks ledger",
            [
                _support(
                    "source-community-talks-ledger-2010-2021",
                    "Metadata and Complete Talks List",
                    "aggregate",
                    "self_reported",
                    "The ledger publishes session-level dates, topics, formats, venues, and approximate participant counts.",
                )
            ],
            period="2010–2021",
            metric={
                "value": 50,
                "display": "50 sessions · 3,732 participant instances",
                "unit": "recorded sessions",
            },
            caveat_ids=[
                "caveat-touchpoints-not-people",
                "caveat-session-tracker-boundary",
                "caveat-self-authored-source",
            ],
            confidence_level="supported",
            confidence_rationale="The figures are documented in a session-level first-party ledger; reach is approximate and not independently audited.",
        ),
        _claim(
            "claim-connect-volume-2021",
            "A 575-conversation program ledger",
            f"The 2021 monthly ledger records {connect['total_connects']} connect conversations across twelve months.",
            "calculated",
            "influence",
            "program",
            "Connect program ledger",
            [
                _support(
                    "source-connect-program-2021",
                    "Raw Data Per Month · Connects",
                    "aggregate",
                    "documented",
                    "Twelve monthly counts sum to the annual program volume.",
                )
            ],
            period="2021",
            metric={
                "value": connect["total_connects"],
                "display": f"{connect['total_connects']} connects",
                "unit": "conversation records",
            },
            method_id="method-connect-demand-v1",
            caveat_ids=["caveat-touchpoints-not-people", "caveat-private-held-source"],
            confidence_level="high",
            confidence_rationale="The total is a deterministic sum of twelve published monthly aggregates.",
        ),
        _claim(
            "claim-connect-demand-share",
            "Most 2021 connect conversations were requested by others",
            f"Other people set up {connect['requested_by_others']} of {connect['total_connects']} recorded connects, or {connect['requested_by_others'] / connect['total_connects'] * 100:.2f}%, displayed as {connect['requested_share']}%.",
            "calculated",
            "trust",
            "program",
            "Connect program ledger",
            [
                _support(
                    "source-connect-program-2021",
                    "Raw Data Per Month · Connects and Setup by Others",
                    "aggregate",
                    "documented",
                    "The numerator and denominator are explicit monthly program totals.",
                )
            ],
            period="2021",
            metric={
                "value": connect["requested_share"],
                "display": f"{connect['requested_share']}% requested by others",
                "unit": "percent",
            },
            method_id="method-connect-demand-v1",
            caveat_ids=[
                "caveat-touchpoints-not-people",
                "caveat-inference-not-motive",
                "caveat-private-held-source",
            ],
            confidence_level="high",
            confidence_rationale="The composition is deterministic; its interpretation is bounded to demonstrated demand for a conversation, not outcome or motive.",
        ),
        _claim(
            "claim-book-program-total",
            "A decade-scale education-support ledger",
            f"Ten recorded active years sum to ₹{books['total_raised_inr']:,} in nominal contributions for the education-material program.",
            "calculated",
            "community",
            "community_program",
            "Book-distribution program aggregate",
            [
                _support(
                    "source-book-program-ledger-2014-2026",
                    "Financial Summary · annual Total Raised column",
                    "aggregate",
                    "documented",
                    "The public calculation uses privacy-safe annual aggregates while protecting identities and banking fields.",
                )
            ],
            period="2014–2026",
            metric={
                "value": books["total_raised_inr"],
                "display": f"₹{books['total_raised_inr']:,}",
                "unit": "INR",
            },
            method_id="method-book-totals-growth-v1",
            caveat_ids=[
                "caveat-active-years-with-gaps",
                "caveat-currency-not-normalized",
                "caveat-private-held-source",
            ],
            confidence_level="supported",
            confidence_rationale="The arithmetic is deterministic from reviewed annual aggregates; underlying financial records remain private-held.",
        ),
        _claim(
            "claim-book-program-growth",
            "The 2014 and 2026 recorded annual totals have a 13.3× endpoint ratio",
            f"The recorded annual total increased from ₹{books['first_year_amount_inr']:,} in {books['first_year']} to ₹{books['last_year_amount_inr']:,} in {books['last_year']}, a {books['growth_factor']}× endpoint ratio.",
            "calculated",
            "community",
            "community_program",
            "Book-distribution program aggregate",
            [
                _support(
                    "source-book-program-ledger-2014-2026",
                    "Financial Summary · first and final recorded annual rows plus unrecorded-year disclosures",
                    "aggregate",
                    "documented",
                    "The source provides both endpoint aggregates and distinguishes the ten recorded program years from years outside the reviewed ledger.",
                )
            ],
            period=f"{books['first_year']}–{books['last_year']}",
            metric={
                "value": books["growth_factor"],
                "display": f"{books['growth_factor']}× endpoint ratio",
                "unit": "times",
            },
            method_id="method-book-totals-growth-v1",
            caveat_ids=[
                "caveat-active-years-with-gaps",
                "caveat-currency-not-normalized",
                "caveat-private-held-source",
            ],
            confidence_level="supported",
            confidence_rationale="The endpoint ratio is reproducible; it is not represented as smooth annual growth or inflation-adjusted impact.",
        ),
        _claim(
            "claim-community-service-photo-record",
            "Direct service predates the financial ledger",
            "Dated documentary images show teaching, yoga instruction, rural-school engagement, and educational-material distribution from 2007 through 2015.",
            "observed",
            "community",
            "individual_and_family",
            "Documentary photo record",
            [
                _support(
                    "source-community-service-photo-record-2007-2015",
                    "Timeline; slides 20, 27, 30–32, and 38–39",
                    "direct",
                    "documented",
                    "The photographs and dated artifacts document multiple forms and years of direct service.",
                )
            ],
            period="2007–2015",
            caveat_ids=["caveat-selected-evidence", "caveat-self-authored-source"],
            confidence_level="supported",
            confidence_rationale="The record contains dated documentary artifacts; scale estimates and motives are deliberately excluded from this claim.",
        ),
        _claim(
            "claim-xite-potential-hours",
            "18,000 hours is an XITE portfolio estimate",
            "Across eight AI initiatives, the XITE announcement estimates potential annual productivity capacity of about 18,000 hours. It is not a Sutra-only or realized-savings claim.",
            "observed",
            "impact",
            "portfolio",
            "XITE program across eight teams",
            [
                _support(
                    "source-xite-portfolio-outcomes-2026",
                    "Portfolio announcement · eight initiatives and potential annual value",
                    "direct",
                    "documented",
                    "The announcement explicitly scopes the figure to the eight-initiative portfolio and uses potential-value language.",
                )
            ],
            period="2026",
            metric={
                "value": 18000,
                "display": "~18,000 potential hours/year",
                "unit": "potential annual productivity hours",
            },
            caveat_ids=[
                "caveat-potential-not-realized",
                "caveat-team-attribution",
                "caveat-private-held-source",
            ],
            confidence_level="supported",
            confidence_rationale="The estimate is directly stated, but realized value and initiative allocation are not established.",
        ),
        _claim(
            "claim-xite-potential-efficiency",
            "€3.5 million is an XITE portfolio estimate",
            "Across eight AI initiatives, the XITE announcement estimates potential annual efficiencies of €3.5 million. It is not attributed to Sutra or Datta individually.",
            "observed",
            "impact",
            "portfolio",
            "XITE program across eight teams",
            [
                _support(
                    "source-xite-portfolio-outcomes-2026",
                    "Portfolio announcement · eight initiatives and potential annual value",
                    "direct",
                    "documented",
                    "The announcement explicitly scopes the figure to the portfolio and describes potential efficiencies.",
                )
            ],
            period="2026",
            metric={
                "value": 3.5,
                "display": "€3.5M potential/year",
                "unit": "million EUR potential annual efficiencies",
            },
            caveat_ids=[
                "caveat-potential-not-realized",
                "caveat-team-attribution",
                "caveat-private-held-source",
            ],
            confidence_level="supported",
            confidence_rationale="The estimate is directly stated, but realized value and initiative allocation are not established.",
        ),
        _claim(
            "claim-sutra-traceability",
            "Sutra reports a 90%+ traceability improvement",
            "An Inside XITE initiative record reports more than 90% improvement in automated traceability for Sutra's requirements, tests, and risk workflow.",
            "observed",
            "innovation",
            "team_initiative",
            "Sutra team and Inside XITE",
            [
                _support(
                    "source-sutra-initiative-outcomes-2026",
                    "Inside XITE · Sutra impact bullets",
                    "direct",
                    "documented",
                    "The traceability figure is stated specifically for the Sutra initiative.",
                )
            ],
            period="2026",
            metric={
                "value": 90,
                "display": "90%+ traceability improvement",
                "unit": "percent improvement",
            },
            caveat_ids=[
                "caveat-initiative-scope",
                "caveat-team-attribution",
                "caveat-private-held-source",
            ],
            confidence_level="supported",
            confidence_rationale="The initiative announcement states the metric; the underlying measurement protocol is not available in the public evidence summary.",
        ),
        _claim(
            "claim-sutra-ai-delivery",
            "Sutra paired AI-native speed with commit-level controls",
            "A Sutra team comment reports 3× development speed and about 80% AI-generated code while disallowing commits that broke quality rules and using external quality tools in continuous delivery.",
            "observed",
            "innovation",
            "team_initiative",
            "Datta's attributed Sutra team comment",
            [
                _support(
                    "source-sutra-initiative-outcomes-2026",
                    "Datta team comment · AI use, speed, generated code, and quality gates",
                    "direct",
                    "self_reported",
                    "The same attributed comment states both the speed claim and the engineering controls.",
                )
            ],
            period="2026",
            metric={"value": 3, "display": "3× stated development speed", "unit": "times"},
            caveat_ids=[
                "caveat-initiative-scope",
                "caveat-team-attribution",
                "caveat-self-authored-source",
                "caveat-private-held-source",
            ],
            conflict_ids=[
                "conflict-sutra-onboarding-arithmetic",
                "conflict-sutra-zero-quality-boundary",
            ],
            confidence_level="limited",
            confidence_rationale="The implementation controls are specific and attributable, but the speed and AI-code shares are team-reported rather than independently audited.",
        ),
        _claim(
            "claim-sutra-delivery-recognition",
            "Sutra delivery received documented organizational recognition",
            "A 2026 recognition artifact credits conscious AI application and delivery of the XITE-funded Sutra program to business units.",
            "observed",
            "trust",
            "team_initiative",
            "Philips Recognition",
            [
                _support(
                    "source-sutra-recognition-2026",
                    "Recognition reason",
                    "direct",
                    "documented",
                    "The award artifact specifically names conscious AI application and delivery to business units.",
                )
            ],
            period="2026",
            caveat_ids=["caveat-team-attribution", "caveat-private-held-source"],
            confidence_level="high",
            confidence_rationale="A dated recognition artifact directly states the basis of recognition.",
        ),
        _claim(
            "claim-2010-first-patent-achievement",
            "IBM recognized a first patent application in 2010",
            "An IBM certificate dated December 28, 2010 names Dattatreya S. Vellal as recipient of a First Patent Application Invention Achievement Award for Determining and Conveying User Availability.",
            "observed",
            "innovation",
            "individual_invention",
            "IBM award certificate",
            [
                _support(
                    "source-patent-award-2010",
                    "Metadata and certificate quotation · recipient, award type, invention title, and date",
                    "direct",
                    "documented",
                    "The employer-issued artifact directly names the recipient, application milestone, invention, and date.",
                )
            ],
            period="2010-12-28",
            metric={
                "value": 1,
                "display": "1 first-application award",
                "unit": "employer recognition artifacts",
            },
            caveat_ids=["caveat-patent-scope", "caveat-selected-evidence"],
            confidence_level="high",
            confidence_rationale="The dated employer certificate directly supports the bounded application-recognition claim; grant and impact are treated separately.",
        ),
        _claim(
            "claim-public-patent-record",
            "Innovation with a public registry trail",
            "The public registry for US Patent 8,560,487 lists Datta among the inventors of Determining and Conveying User Availability; a dated IBM artifact records the first-patent achievement.",
            "observed",
            "innovation",
            "co_inventor",
            "Public patent registry and IBM award",
            [
                _support(
                    "source-us-patent-8560487",
                    "Public registry · inventors and patent title",
                    "direct",
                    "corroborated",
                    "The external registry provides a publicly openable record.",
                ),
                _support(
                    "source-patent-award-2010",
                    "IBM award citation",
                    "direct",
                    "documented",
                    "The award artifact independently records the first patent application milestone.",
                ),
            ],
            period="2010–2013",
            metric={"value": 1, "display": "US Patent 8,560,487", "unit": "public patent record"},
            caveat_ids=["caveat-patent-scope", "caveat-selected-evidence"],
            confidence_level="high",
            confidence_rationale="The claim is corroborated by an external public registry and an employer award artifact.",
        ),
        _claim(
            "claim-2008-early-leadership",
            "Leadership evidence appears in the first career year",
            "A 2008 employer award recognizes end-to-end leadership of a complex internship project early in Datta's career.",
            "observed",
            "leadership",
            "individual",
            "IBM award citation",
            [
                _support(
                    "source-leadership-award-2008",
                    "Award citation",
                    "direct",
                    "documented",
                    "The citation explicitly uses leadership and end-to-end delivery language.",
                )
            ],
            period="2008",
            caveat_ids=["caveat-selected-evidence"],
            confidence_level="high",
            confidence_rationale="A dated employer-issued artifact directly supports the bounded early-leadership claim.",
        ),
        _claim(
            "claim-2010-technical-community-recognition",
            "Technical-community contribution was recognized in 2010",
            "An IBM Regional Technical Leadership Exchange artifact recognizes Datta's contribution to the India technical community exchange.",
            "observed",
            "leadership",
            "technical_community",
            "IBM technical leadership forum",
            [
                _support(
                    "source-technical-community-recognition-2010",
                    "Certificate citation",
                    "direct",
                    "documented",
                    "The artifact directly records technical-community contribution.",
                )
            ],
            period="2010",
            caveat_ids=["caveat-selected-evidence"],
            confidence_level="high",
            confidence_rationale="A dated employer-issued certificate directly supports the claim.",
        ),
        _claim(
            "claim-2015-quality-discipline",
            "Quality discipline under high complexity",
            "A 2015 manager review describes due diligence across quality, high-complexity and high-impact work, collaborative partnerships, and a linchpin role, while retaining improvement feedback.",
            "observed",
            "leadership",
            "team",
            "Exeter manager review",
            [
                _support(
                    "source-exeter-performance-review-2015",
                    "Behavioral Competencies, Key Quotes, and scores",
                    "direct",
                    "corroborated",
                    "The manager review provides a balanced assessment of demonstrated strengths and development opportunities.",
                )
            ],
            period="2015",
            caveat_ids=["caveat-private-held-source"],
            confidence_level="high",
            confidence_rationale="The bounded claim comes from a formal manager assessment with explicit behavioral detail.",
        ),
        _claim(
            "claim-2015-cross-team-leadership",
            "Cross-team bridge building was observed in 2015",
            "A cross-team colleague describes technical depth, people leadership, teaching, and activity across technology, project, and location boundaries.",
            "observed",
            "leadership",
            "organization",
            "Cross-team colleague",
            [
                _support(
                    "source-cross-team-recommendation-2015",
                    "Recommendation · team scale, teaching, and barrier crossing",
                    "direct",
                    "corroborated",
                    "The recommender worked on a different team and describes directly observed cross-organizational behavior.",
                )
            ],
            period="2015",
            caveat_ids=["caveat-selected-evidence", "caveat-identity-withheld"],
            confidence_level="supported",
            confidence_rationale="The attributed recommendation is independent but remains one colleague's observation.",
        ),
        _claim(
            "claim-2017-process-delivery-recognition",
            "Process improvement and delivery were both recognized in 2017",
            "Two adjacent Amazon award artifacts recognize team-process improvement and exceptional project delivery.",
            "observed",
            "impact",
            "team",
            "Amazon TRMS Tech",
            [
                _support(
                    "source-amazon-process-recognition-2017",
                    "Award reason · team process improvement",
                    "direct",
                    "documented",
                    "The first artifact directly names process improvement.",
                ),
                _support(
                    "source-amazon-delivery-recognition-2017",
                    "Award reason · exceptional project delivery",
                    "direct",
                    "documented",
                    "The second artifact directly names delivery.",
                ),
            ],
            period="2017",
            caveat_ids=["caveat-selected-evidence"],
            confidence_level="high",
            confidence_rationale="Both bounded observations come from dated employer award artifacts.",
        ),
        _claim(
            "claim-2020-quality-speed-framing",
            "Quality was explicitly framed as an enabler of speed",
            "A 2020 line-manager comment says Datta puts quality in the context of benefits in speed, defects, and predictability.",
            "observed",
            "leadership",
            "individual",
            "Line-manager feedback in a multi-rater assessment",
            [
                _support(
                    "source-360-feedback-2020",
                    "Line Manager Comments · quality in context",
                    "direct",
                    "corroborated",
                    "The assessment preserves the manager's explicit quality-speed-defect-predictability framing.",
                )
            ],
            period="2020",
            caveat_ids=["caveat-private-held-source"],
            confidence_level="high",
            confidence_rationale="The claim closely paraphrases a specific attributed manager comment.",
        ),
        _claim(
            "claim-2020-360-company-deltas",
            "All five 360 behaviors were above the company-average column",
            f"Other-rater averages exceeded the company-average column for all five behaviors; deltas range from +{assessment['minimum_delta']:.2f} to +{assessment['maximum_delta']:.2f}, with a mean of +{assessment['mean_delta']:.2f} rating points.",
            "calculated",
            "leadership",
            "individual",
            "Fourteen-rater 2020 assessment",
            [
                _support(
                    "source-360-feedback-2020",
                    "Behavior Scores Summary · AVG (Others), Company Average, and Difference",
                    "aggregate",
                    "corroborated",
                    "The five source rows expose the compared values and deltas.",
                )
            ],
            period="2020",
            metric={
                "value": assessment["mean_delta"],
                "display": f"+{assessment['mean_delta']:.2f} mean delta",
                "unit": "rating points vs company average",
            },
            method_id="method-360-company-deltas-v1",
            caveat_ids=["caveat-360-benchmark-scope", "caveat-private-held-source"],
            confidence_level="high",
            confidence_rationale="The five comparisons are explicit and the mean is deterministic; benchmark scope is bounded to the source column.",
        ),
        _claim(
            "claim-2020-executive-influence-development-signal",
            "The 2020 assessment names a concrete executive-influence development edge",
            "The line-manager development feedback asks Datta to broaden influence with senior executives outside software and frames a transition from humble coach toward business transformer.",
            "observed",
            "leadership",
            "individual",
            "Line-manager feedback in a multi-rater assessment",
            [
                _support(
                    "source-360-feedback-2020",
                    "Greatest Development Area and Line Manager Comments",
                    "direct",
                    "corroborated",
                    "The assessment directly records the development request in its original 2020 context.",
                )
            ],
            period="2020",
            caveat_ids=["caveat-private-held-source", "caveat-selected-evidence"],
            confidence_level="high",
            confidence_rationale="The development edge is directly stated by the line manager in a formal multi-rater report.",
        ),
        _claim(
            "claim-2020-strengths-profile",
            "A 2020 assessment supplies a testable strengths hypothesis",
            "The BeTalent profile ranks Articulate, Meticulous, Evaluative, Genuine, Achiever, Networker, and Self-Aware as Datta's top seven assessed strengths.",
            "observed",
            "leadership",
            "individual",
            "BeTalent psychometric assessment",
            [
                _support(
                    "source-strengths-assessment-2020",
                    "Top 7 Strengths · rank order",
                    "direct",
                    "documented",
                    "The held assessment lists the seven labels in rank order.",
                )
            ],
            period="2020",
            caveat_ids=["caveat-assessment-not-performance", "caveat-private-held-source"],
            confidence_level="supported",
            confidence_rationale="The ranked labels are documented; their interpretation is limited to the assessment construct.",
        ),
        _claim(
            "claim-2020-mentoring-method",
            "Mentoring is described as building independent thinking",
            "A former mentee describes a method of guiding people to think through solutions themselves and teaching skills together with values.",
            "observed",
            "learning",
            "individual",
            "Former mentee recommendation",
            [
                _support(
                    "source-mentoring-recommendation-2020",
                    "Recommendation · independent thinking and skills with values",
                    "direct",
                    "corroborated",
                    "The recommender grounds the endorsement in observable mentoring behaviors.",
                )
            ],
            period="2020",
            caveat_ids=["caveat-selected-evidence"],
            confidence_level="supported",
            confidence_rationale="The behavior is specific and independently attributed, but it remains one mentee's perspective.",
        ),
        _claim(
            "claim-2021-cto-recognition",
            "Company-wide technical recognition in 2021",
            "A Philips CTO Annual Address artifact includes Datta among thirty outstanding-achievement recipients.",
            "observed",
            "trust",
            "individual",
            "Philips CTO Annual Address",
            [
                _support(
                    "source-philips-cto-recognition-2021",
                    "Outstanding Achievement Awards artifact",
                    "direct",
                    "documented",
                    "The event artifact visibly lists the recipients.",
                )
            ],
            period="2021",
            metric={"value": 30, "display": "1 of 30 listed recipients", "unit": "recipients"},
            caveat_ids=["caveat-selected-evidence"],
            confidence_level="high",
            confidence_rationale="A dated company event artifact directly records inclusion among the award recipients.",
        ),
        _claim(
            "claim-2023-purpose-first-mentoring",
            "Purpose-first mentoring is observed outside a reporting line",
            "A colleague whom Datta did not manage describes calmness, kindness, clarity on purpose and expected outcomes, openness to input, and availability.",
            "observed",
            "leadership",
            "informal_mentoring",
            "Informally mentored colleague",
            [
                _support(
                    "source-purpose-first-mentoring-recommendation-2023",
                    "Relationship metadata and behavioral recommendation",
                    "direct",
                    "corroborated",
                    "The relationship metadata establishes peer mentoring outside a direct reporting line and records concrete behaviors.",
                )
            ],
            period="2023",
            caveat_ids=["caveat-selected-evidence"],
            confidence_level="supported",
            confidence_rationale="The behavior is specific and independently attributed, but it remains one colleague's perspective.",
        ),
        _claim(
            "claim-2025-executive-influence-observation",
            "A 2025 colleague observes executive-to-developer influence",
            "A Software Excellence colleague describes relationship-led credibility, communication from senior executives to developers, coaching, roadmap contribution and execution, and work underpinned by data.",
            "observed",
            "leadership",
            "organization",
            "Software Excellence colleague",
            [
                _support(
                    "source-influence-recommendation-2025",
                    "Recommendation · influence, communication, coaching, execution, and data",
                    "direct",
                    "corroborated",
                    "The later observation is independently attributed and behaviorally specific.",
                )
            ],
            period="2025",
            caveat_ids=["caveat-selected-evidence"],
            confidence_level="supported",
            confidence_rationale="The recommendation directly describes multiple behaviors but remains one colleague's observation.",
        ),
        _claim(
            "claim-2025-cross-boundary-leadership",
            "A direct manager observes leadership across formal boundaries",
            "A former direct manager describes leadership across reporting lines, seniority, and team boundaries, together with empathetic communication, coaching, craftsmanship, modern pipelines, and DORA improvement.",
            "observed",
            "leadership",
            "organization",
            "Former direct manager",
            [
                _support(
                    "source-manager-recommendation-2025",
                    "Recommendation · boundaries, communication, coaching, craftsmanship, and DORA",
                    "direct",
                    "corroborated",
                    "The direct-manager relationship and specific behavioral observations strengthen attribution.",
                )
            ],
            period="2025",
            caveat_ids=["caveat-selected-evidence", "caveat-team-attribution"],
            confidence_level="supported",
            confidence_rationale="The source is an informed manager perspective; it does not expose underlying DORA measurements.",
        ),
        _claim(
            "claim-2019-practical-feedback-request",
            "Participants asked for more relevant examples and hands-on depth",
            "A 2019 clean-code feedback record asks for examples closer to the participant's technology; another improvement field asks for an interactive hands-on format and explicit pitfalls.",
            "observed",
            "requested_improvement",
            "participant_feedback",
            "Anonymous participant feedback",
            [
                _support(
                    "source-participant-improvement-relevant-examples-2019",
                    "Facilitator-improvement response field",
                    "direct",
                    "documented",
                    "The documented improvement-question field directly establishes this classification.",
                )
            ],
            period="2019",
            caveat_ids=[
                "caveat-response-unit",
                "caveat-selected-evidence",
                "caveat-session-tracker-boundary",
            ],
            confidence_level="high",
            confidence_rationale="The requested improvements are explicit in documented improvement fields.",
        ),
        _claim(
            "claim-2024-practical-ai-takeaway",
            "A participant took away practical prompting and guardrails",
            "A 2024 participant identifies IDE-based Copilot use, better prompting, and repository instructions as quality guardrails among the session's key takeaways.",
            "observed",
            "participant_takeaway",
            "participant_feedback",
            "Anonymous participant feedback",
            [
                _support(
                    "source-participant-takeaway-ai-guardrails-2024",
                    "Three key takeaways response field",
                    "direct",
                    "documented",
                    "The classification follows the documented key-takeaways question field.",
                )
            ],
            period="2024",
            caveat_ids=[
                "caveat-response-unit",
                "caveat-selected-evidence",
                "caveat-session-tracker-boundary",
            ],
            confidence_level="high",
            confidence_rationale="The takeaway is explicit in the documented key-takeaways field.",
        ),
        _claim(
            "claim-2026-hands-on-depth-request",
            "Recent learners still request deeper hands-on AI practice",
            "A 2026 community-call improvement response requests multiple hands-on sessions on building agents and using them effectively.",
            "observed",
            "requested_improvement",
            "participant_feedback",
            "Anonymous participant feedback",
            [
                _support(
                    "source-participant-improvement-hands-on-agents-2026",
                    "Facilitator-improvement response field",
                    "direct",
                    "documented",
                    "The classification follows the documented improvement-question field.",
                )
            ],
            period="2026",
            caveat_ids=[
                "caveat-response-unit",
                "caveat-selected-evidence",
                "caveat-session-tracker-boundary",
            ],
            confidence_level="high",
            confidence_rationale="The requested improvement is explicit in the documented facilitator-improvement field.",
        ),
        _claim(
            "claim-evidence-corpus-coverage",
            "The public argument sits on a much larger held corpus",
            f"The held evidence inventory contains {inventory['evidence_markdown']:,} Markdown files, including {inventory['individual_evidence_records']:,} individual records and {inventory['informal_feedback_records']:,} informal-feedback records, plus {inventory['documentary_images']:,} documentary images.",
            "calculated",
            "data_quality",
            "corpus",
            "Knowledge-context repository",
            [
                _support(
                    "source-evidence-inventory-2026",
                    "Build-time repository inventory",
                    "aggregate",
                    "documented",
                    "The builder counts files without exposing private filenames.",
                ),
                _support(
                    "source-relationship-export-quality-2026",
                    "DuckDB tables · evidence_index",
                    "aggregate",
                    "documented",
                    "The quality report supplies the current indexed subset for comparison.",
                    relationship="qualifies",
                ),
            ],
            period="as of 2026-08-07",
            metric={
                "value": inventory["evidence_markdown"],
                "display": f"{inventory['evidence_markdown']:,} evidence Markdown files",
                "unit": "files",
            },
            method_id="method-corpus-coverage-v1",
            caveat_ids=["caveat-export-gap", "caveat-private-held-source"],
            confidence_level="high",
            confidence_rationale="Filesystem and export counts are deterministic; corpus size is not presented as claim quality.",
        ),
        _claim(
            "claim-export-embedding-gap",
            "4,411 chunks are absent from the retrieval index",
            f"The export quality report records {inventory['missing_in_chroma']:,} DuckDB chunk IDs that are not present in Chroma, with no extra Chroma IDs or document/metadata mismatches.",
            "calculated",
            "data_quality",
            "retrieval_export",
            "Knowledge-context export pipeline",
            [
                _support(
                    "source-relationship-export-quality-2026",
                    "ChromaDB alignment",
                    "direct",
                    "documented",
                    "The generated report exposes both the gap and the mismatch checks.",
                )
            ],
            period="as of 2026-08-07",
            metric={
                "value": inventory["missing_in_chroma"],
                "display": f"{inventory['missing_in_chroma']:,} missing embeddings",
                "unit": "chunks",
            },
            method_id="method-corpus-coverage-v1",
            caveat_ids=["caveat-export-gap"],
            confidence_level="high",
            confidence_rationale="The count is directly generated by the export consistency check.",
        ),
        _claim(
            "claim-export-provenance-gap",
            "Thirteen edge-provenance links remain unresolved",
            f"The export quality report records {inventory['orphan_edge_artifact_provenance']} soft orphan edge-to-artifact provenance links; source and target node checks report no orphans.",
            "calculated",
            "data_quality",
            "graph_export",
            "Knowledge-context export pipeline",
            [
                _support(
                    "source-relationship-export-quality-2026",
                    "Referential and graph checks",
                    "direct",
                    "documented",
                    "The report distinguishes soft provenance gaps from node-reference integrity.",
                )
            ],
            period="as of 2026-08-07",
            metric={
                "value": inventory["orphan_edge_artifact_provenance"],
                "display": f"{inventory['orphan_edge_artifact_provenance']} provenance gaps",
                "unit": "edges",
            },
            method_id="method-corpus-coverage-v1",
            caveat_ids=["caveat-export-gap"],
            confidence_level="high",
            confidence_rationale="The count is directly generated by the export consistency check.",
        ),
        _claim(
            "claim-feedback-to-executive-observation",
            "A 2020 development edge reappears as 2025 observed behavior",
            "The 2020 request to broaden senior-executive influence is concordant with independent 2025 descriptions of executive-to-developer communication, relationship-led influence, roadmap execution, data use, and leadership across reporting boundaries. This is non-causal and not a before/after score.",
            "interpreted",
            "relationship",
            "career_development",
            "Cross-source synthesis",
            [
                _support(
                    "source-360-feedback-2020",
                    "Greatest Development Area",
                    "interpretive",
                    "corroborated",
                    "Supplies the dated development edge.",
                ),
                _support(
                    "source-influence-recommendation-2025",
                    "Recommendation · influence, communication, execution, and data",
                    "interpretive",
                    "corroborated",
                    "Supplies a later independent observation aligned with the development edge.",
                ),
                _support(
                    "source-manager-recommendation-2025",
                    "Recommendation · leadership across formal boundaries",
                    "interpretive",
                    "corroborated",
                    "Supplies a second later independent observation.",
                ),
            ],
            period="2020→2025",
            method_id="method-feedback-executive-observation-v1",
            caveat_ids=[
                "caveat-non-causal-synthesis",
                "caveat-selected-evidence",
                "caveat-private-held-source",
            ],
            confidence_level="supported",
            confidence_rationale="The semantic correspondence is strong and independently observed twice, but no repeated measurement establishes change or causality.",
        ),
        _claim(
            "claim-strengths-later-observation-concordance",
            "Assessment themes recur in later independent observations",
            "Five 2020 assessment themes—Articulate, Meticulous, Evaluative, Networker, and Genuine—have close behavioral counterparts in two independently attributed 2025 recommendations. This is concordance, not psychometric validation.",
            "interpreted",
            "relationship",
            "leadership_behavior",
            "Cross-source synthesis",
            [
                _support(
                    "source-strengths-assessment-2020",
                    "Top 7 Strengths",
                    "interpretive",
                    "documented",
                    "Supplies the assessment labels.",
                ),
                _support(
                    "source-influence-recommendation-2025",
                    "Recommendation · relationships, communication, and data",
                    "interpretive",
                    "corroborated",
                    "Supplies independent behavioral counterparts.",
                ),
                _support(
                    "source-manager-recommendation-2025",
                    "Recommendation · meticulous and empathetic collaboration",
                    "interpretive",
                    "corroborated",
                    "Supplies a second set of independent behavioral counterparts.",
                ),
            ],
            period="2020→2025",
            method_id="method-strengths-observation-concordance-v1",
            caveat_ids=[
                "caveat-assessment-not-performance",
                "caveat-non-causal-synthesis",
                "caveat-selected-evidence",
            ],
            confidence_level="supported",
            confidence_rationale="Multiple explicit semantic mappings are present, but an assessment cannot be validated by testimonial language alone.",
        ),
        _claim(
            "claim-quality-before-ai-lineage",
            "AI adoption rests on a quality-control lineage",
            "Evidence from 2015, 2017, 2020, and 2025 precedes the 2026 Sutra claim of AI-native speed with commit-level gates. The sequence supports 'AI built on an engineering control system, not novelty alone' without proving causality or individual ownership of team outcomes.",
            "interpreted",
            "relationship",
            "engineering_system",
            "Cross-employer synthesis",
            [
                _support(
                    "source-exeter-performance-review-2015",
                    "Quality due diligence under high complexity",
                    "interpretive",
                    "corroborated",
                    "Establishes an early quality-discipline observation.",
                ),
                _support(
                    "source-amazon-process-recognition-2017",
                    "Team process-improvement award",
                    "interpretive",
                    "documented",
                    "Adds documented process-system recognition.",
                ),
                _support(
                    "source-amazon-delivery-recognition-2017",
                    "Exceptional delivery award",
                    "interpretive",
                    "documented",
                    "Places delivery recognition beside the process evidence.",
                ),
                _support(
                    "source-360-feedback-2020",
                    "Manager comment · quality as speed, defects, predictability",
                    "interpretive",
                    "corroborated",
                    "Makes the quality-speed theory explicit.",
                ),
                _support(
                    "source-manager-recommendation-2025",
                    "Craftsmanship, pipelines, and DORA observation",
                    "interpretive",
                    "corroborated",
                    "Adds later independent observation of engineering mechanisms.",
                ),
                _support(
                    "source-sutra-initiative-outcomes-2026",
                    "AI development and commit-gate team comment",
                    "interpretive",
                    "self_reported",
                    "Supplies the 2026 AI-native endpoint and its controls.",
                ),
            ],
            period="2015→2026",
            method_id="method-quality-before-ai-lineage-v1",
            caveat_ids=[
                "caveat-non-causal-synthesis",
                "caveat-team-attribution",
                "caveat-self-authored-source",
                "caveat-selected-evidence",
                "caveat-initiative-scope",
            ],
            confidence_level="supported",
            confidence_rationale="The control-system theme recurs across five dates and multiple source relationships; the 2026 speed endpoint remains team-reported.",
        ),
        _claim(
            "claim-title-independent-leadership-continuity",
            "Leadership behavior is documented beyond title and reporting line",
            "A 2008 early-career award, a 2015 cross-team observation, a 2023 informal-mentoring recommendation, and a 2025 manager description of leadership across formal boundaries support a title-independent leadership pattern.",
            "interpreted",
            "relationship",
            "leadership_behavior",
            "Cross-source synthesis",
            [
                _support(
                    "source-leadership-award-2008",
                    "Early-career leadership award",
                    "interpretive",
                    "documented",
                    "Supplies evidence before senior titles.",
                ),
                _support(
                    "source-cross-team-recommendation-2015",
                    "Cross-team and cross-location recommendation",
                    "interpretive",
                    "corroborated",
                    "Supplies leadership outside one team.",
                ),
                _support(
                    "source-purpose-first-mentoring-recommendation-2023",
                    "Informal mentoring without direct management",
                    "interpretive",
                    "corroborated",
                    "Supplies a no-reporting-line relationship.",
                ),
                _support(
                    "source-manager-recommendation-2025",
                    "Leadership across reporting lines, seniority, and teams",
                    "interpretive",
                    "corroborated",
                    "Makes the formal-boundary proposition explicit.",
                ),
                _support(
                    "source-technical-community-recognition-2010",
                    "Technical community contribution",
                    "indirect",
                    "documented",
                    "Adds a dated technical-community context.",
                    relationship="context",
                ),
                _support(
                    "source-philips-cto-recognition-2021",
                    "Company-wide outstanding achievement artifact",
                    "indirect",
                    "documented",
                    "Adds later company-wide recognition context.",
                    relationship="context",
                ),
            ],
            period="2008→2025",
            method_id="method-title-independent-leadership-v1",
            caveat_ids=["caveat-non-causal-synthesis", "caveat-selected-evidence"],
            confidence_level="supported",
            confidence_rationale="The pattern appears across employers and relationship types; it does not imply formal management scope at every point.",
        ),
        _claim(
            "claim-learn-build-teach-systemize-pattern",
            "A recurring learn → build → teach → systemize pattern",
            "Across IBM, Exeter, Amazon, and Philips records, technical learning or building repeatedly becomes reusable teaching, tools, guides, communities, or delivery systems. Evidence strength varies by employer, so this is an operating-pattern interpretation rather than a universal rule.",
            "interpreted",
            "relationship",
            "operating_pattern",
            "Cross-employer synthesis",
            [
                _support(
                    "source-us-patent-8560487",
                    "Public invention record",
                    "interpretive",
                    "corroborated",
                    "Represents build and codified invention at IBM.",
                ),
                _support(
                    "source-technical-community-recognition-2010",
                    "Technical-community contribution",
                    "interpretive",
                    "documented",
                    "Represents community transfer at IBM.",
                ),
                _support(
                    "source-cross-team-recommendation-2015",
                    "Technology sessions and organization-wide initiatives",
                    "interpretive",
                    "corroborated",
                    "Represents teaching and systemization at Exeter.",
                ),
                _support(
                    "source-amazon-work-examples-2018",
                    "Self-service tools, guides, workshops, and reflective examples",
                    "interpretive",
                    "self_reported",
                    "Represents reusable mechanisms at Amazon.",
                ),
                _support(
                    "source-session-response-corpus-2018-2026",
                    "Structured feedback-file corpus",
                    "interpretive",
                    "documented",
                    "Represents measured teaching and adaptation at Philips.",
                ),
                _support(
                    "source-sutra-recognition-2026",
                    "AI delivery and learning recognition",
                    "interpretive",
                    "documented",
                    "Represents a recent build-and-learning system endpoint.",
                ),
            ],
            period="2010→2026",
            method_id="method-learn-build-teach-systemize-v1",
            caveat_ids=[
                "caveat-non-causal-synthesis",
                "caveat-selected-evidence",
                "caveat-self-authored-source",
            ],
            confidence_level="supported",
            confidence_rationale="The pattern recurs across four employer contexts, but the selected sources do not prove that every initiative followed all four stages.",
        ),
        _claim(
            "claim-topic-frontier-teaching-continuity",
            "The topic frontier shifts while practical teaching persists",
            f"The talks ledger moves from wellness and foundational software topics toward observability; later feedback includes {sessions['category_datasets']['ai-genai']} AI-category files and {sessions['category_responses']['ai-genai']} response rows. Across the shift, practical examples, guardrails, and hands-on depth remain visible in participant feedback.",
            "interpreted",
            "relationship",
            "learning_evolution",
            "Cross-tracker synthesis",
            [
                _support(
                    "source-community-talks-ledger-2010-2021",
                    "Dated Complete Talks List",
                    "interpretive",
                    "self_reported",
                    "Supplies the earlier subject sequence.",
                ),
                _support(
                    "source-session-response-corpus-2018-2026",
                    "AI category counts and selected practical-feedback fields",
                    "interpretive",
                    "documented",
                    "Supplies the later measured topic composition and participant perspective.",
                ),
            ],
            period="2010→2026",
            metric={
                "value": sessions["category_datasets"]["ai-genai"],
                "display": f"{sessions['category_datasets']['ai-genai']} AI-category feedback files",
                "unit": "files",
            },
            method_id="method-topic-frontier-teaching-continuity-v1",
            caveat_ids=[
                "caveat-category-labels",
                "caveat-touchpoints-not-people",
                "caveat-session-tracker-boundary",
                "caveat-feedback-not-longitudinal",
                "caveat-non-causal-synthesis",
            ],
            confidence_level="supported",
            confidence_rationale="The dated topic shift and practical-feedback fields are explicit, but the two trackers have different scopes and incomplete coverage.",
        ),
        _claim(
            "claim-service-continuity-and-growth",
            "A recurring service record remains explicitly non-contiguous",
            f"Documentary service evidence begins before the 2014 financial ledger. The ledger records ten active years and a {books['growth_factor']}× 2014-to-2026 endpoint ratio, but not uninterrupted activity: no program is recorded for 2020–2021, no reviewed 2024 program record is present, and the next recorded years are 2025 and 2026.",
            "interpreted",
            "relationship",
            "community_service",
            "Cross-source synthesis",
            [
                _support(
                    "source-community-service-photo-record-2007-2015",
                    "Dated direct-service timeline",
                    "interpretive",
                    "documented",
                    "Supplies evidence of direct service before and during the ledger's early years.",
                ),
                _support(
                    "source-book-program-ledger-2014-2026",
                    "Annual aggregate rows and explicit unrecorded-year disclosures",
                    "interpretive",
                    "documented",
                    "Supplies the active-year, 2020–2021 no-program, 2024 no-record, resumption, total, and endpoint data.",
                ),
            ],
            period="2007→2026",
            metric={
                "value": books["growth_factor"],
                "display": f"{books['growth_factor']}× endpoint ratio",
                "unit": "times",
            },
            method_id="method-service-continuity-growth-v1",
            caveat_ids=[
                "caveat-active-years-with-gaps",
                "caveat-currency-not-normalized",
                "caveat-private-held-source",
                "caveat-non-causal-synthesis",
            ],
            confidence_level="supported",
            confidence_rationale="The dates and aggregates are explicit; recurrence is not relabeled as uninterrupted continuity, and every unrecorded year is disclosed.",
        ),
        _claim(
            "claim-professional-community-trust-bridge",
            "One privacy-safe identity match bridges professional and community trust",
            "One identity-redacted person appears in both a 2015 professional recommendation and multi-year book-program contribution records. This is a cross-context continuity signal; identity, amounts, and motive are not published.",
            "interpreted",
            "relationship",
            "trust",
            "Identity-redacted record linkage",
            [
                _support(
                    "source-cross-team-recommendation-2015",
                    "Identity-held professional recommendation",
                    "interpretive",
                    "corroborated",
                    "Supplies the professional-trust context without publishing identity.",
                ),
                _support(
                    "source-book-program-ledger-2014-2026",
                    "Identity-held multi-year contributor records",
                    "interpretive",
                    "documented",
                    "Supplies the community-trust continuity without publishing identity or amounts.",
                ),
            ],
            period="2015→2026",
            method_id="method-professional-community-trust-bridge-v1",
            caveat_ids=[
                "caveat-identity-withheld",
                "caveat-inference-not-motive",
                "caveat-private-held-source",
                "caveat-non-causal-synthesis",
            ],
            confidence_level="limited",
            confidence_rationale="The exact identity linkage was reviewed, but privacy prevents public independent verification and the records do not establish motive.",
        ),
        _claim(
            "claim-feedback-adaptation-tension",
            "Feedback shows adaptation and continuing demand for depth",
            "A 2019 request for more relevant, hands-on examples later coexists with a 2024 takeaway praising practical prompting and guardrails, while a 2026 participant still requests more hands-on agent-building depth. This is an ongoing adaptation signal, not a solved or causal trajectory.",
            "interpreted",
            "relationship",
            "learning_adaptation",
            "Cross-cohort feedback synthesis",
            [
                _support(
                    "source-participant-improvement-relevant-examples-2019",
                    "Facilitator-improvement response field",
                    "interpretive",
                    "documented",
                    "Supplies the earlier request for relevance and hands-on depth.",
                ),
                _support(
                    "source-participant-takeaway-ai-guardrails-2024",
                    "Key-takeaways response field",
                    "interpretive",
                    "documented",
                    "Supplies a later practical AI and guardrails takeaway.",
                ),
                _support(
                    "source-participant-improvement-hands-on-agents-2026",
                    "Facilitator-improvement response field",
                    "interpretive",
                    "documented",
                    "Supplies continuing demand for hands-on depth.",
                ),
            ],
            period="2019→2026",
            method_id="method-feedback-adaptation-tension-v1",
            caveat_ids=[
                "caveat-feedback-not-longitudinal",
                "caveat-non-causal-synthesis",
                "caveat-selected-evidence",
                "caveat-session-tracker-boundary",
            ],
            confidence_level="supported",
            confidence_rationale="The three documented fields support the tension; different cohorts and contexts prevent a claim of individual change or resolution.",
        ),
    ]


def _materialize_claims(
    raw_claims: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    claims: list[dict[str, Any]] = []
    supports: list[dict[str, Any]] = []
    for raw_claim in raw_claims:
        claim = dict(raw_claim)
        support_specs = claim.pop("support_specs")
        claim_slug = claim["id"].removeprefix("claim-")
        support_ids = []
        for index, spec in enumerate(support_specs, 1):
            support_id = f"support-{claim_slug}-{index:02d}"
            support_ids.append(support_id)
            supports.append(
                {
                    "id": support_id,
                    "claim_id": claim["id"],
                    **spec,
                }
            )
        claim["support_ids"] = support_ids
        claims.append(claim)
    return claims, supports


def _relationships(claims: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_id = {claim["id"]: claim for claim in claims}

    def relationship(
        relationship_id: str,
        title: str,
        claim_id: str,
        from_claim_id: str,
        to_claim_id: str,
        relation_type: str,
        state: str,
        statement: str,
        reasoning: str,
        method_id: str,
        caveat_ids: list[str],
        limitation: str,
        confidence_level: str,
        confidence_rationale: str,
    ) -> dict[str, Any]:
        return {
            "id": relationship_id,
            "title": title,
            "claim_id": claim_id,
            "from_claim_id": from_claim_id,
            "to_claim_id": to_claim_id,
            "relation_type": relation_type,
            "state": state,
            "statement": statement,
            "reasoning": reasoning,
            "method_id": method_id,
            "support_ids": by_id[claim_id]["support_ids"],
            "confidence": {
                "level": confidence_level,
                "rationale": confidence_rationale,
            },
            "caveat_ids": caveat_ids,
            "limitation": limitation,
        }

    return [
        relationship(
            "relationship-patent-application-to-grant",
            "First-patent application award → public patent grant",
            "claim-public-patent-record",
            "claim-2010-first-patent-achievement",
            "claim-public-patent-record",
            "award_artifact_to_public_registry",
            "observed",
            "The invention title and Datta's identity match between IBM's dated 2010 first-patent application award and the 2013 public grant record for US8560487B2.",
            "The method requires an exact normalized full-title match and the same named person as certificate recipient and registry co-inventor; the dates preserve application recognition before grant.",
            "method-patent-award-registry-match-v1",
            ["caveat-patent-scope", "caveat-selected-evidence"],
            "The 2010 artifact recognizes an application and the later record is a grant; the link does not establish sole inventorship, commercialization, adoption, revenue, citation impact, or current legal status.",
            "high",
            "Two direct records agree on the full invention title and named person, and the public grant identifier is uniquely specified.",
        ),
        relationship(
            "relationship-feedback-to-executive-observation",
            "Development edge → later independent observation",
            "claim-feedback-to-executive-observation",
            "claim-2020-executive-influence-development-signal",
            "claim-2025-executive-influence-observation",
            "development_signal_to_later_observation",
            "interpretive_non_causal",
            "A specific 2020 executive-influence development request is concordant with independent 2025 observations of the requested behavior.",
            "The method compares a dated manager development statement with two later, attributed observations and preserves their different source relationships.",
            "method-feedback-executive-observation-v1",
            [
                "caveat-non-causal-synthesis",
                "caveat-selected-evidence",
                "caveat-private-held-source",
            ],
            "No repeated score or controlled before/after measure establishes that the development request caused or completed the later behavior.",
            "supported",
            "The correspondence is explicit and independently observed twice; causal change is not measured.",
        ),
        relationship(
            "relationship-strengths-to-observed-behavior",
            "Assessment strengths → later observed behavior",
            "claim-strengths-later-observation-concordance",
            "claim-2020-strengths-profile",
            "claim-2025-cross-boundary-leadership",
            "assessment_to_later_observation_concordance",
            "interpretive_non_causal",
            "Five assessment labels have close counterparts in two later independent recommendations.",
            "The method maps only explicit 2020 labels to explicit 2025 behavioral descriptions from a colleague and a former manager.",
            "method-strengths-observation-concordance-v1",
            [
                "caveat-assessment-not-performance",
                "caveat-non-causal-synthesis",
                "caveat-selected-evidence",
            ],
            "Testimonial concordance cannot validate a psychometric profile or prove performance.",
            "supported",
            "Several mappings recur across two observers, but the evidence types remain fundamentally different.",
        ),
        relationship(
            "relationship-quality-before-ai",
            "Quality discipline → AI-native controlled delivery",
            "claim-quality-before-ai-lineage",
            "claim-2015-quality-discipline",
            "claim-sutra-ai-delivery",
            "engineering_control_lineage",
            "interpretive_non_causal",
            "A quality-and-delivery mechanism lineage from 2015–2025 precedes 2026 AI-native speed with commit-level controls.",
            "The path requires evidence at 2015, 2017, 2020, 2025, and 2026 and keeps independent observations separate from team-reported metrics.",
            "method-quality-before-ai-lineage-v1",
            [
                "caveat-non-causal-synthesis",
                "caveat-team-attribution",
                "caveat-self-authored-source",
                "caveat-selected-evidence",
                "caveat-initiative-scope",
            ],
            "Chronology supports lineage, not causality; Sutra speed and AI-code shares are team-reported.",
            "supported",
            "The control-system pattern recurs across employers and source types, with a weaker self-reported endpoint.",
        ),
        relationship(
            "relationship-title-independent-leadership",
            "Early leadership → cross-boundary leadership",
            "claim-title-independent-leadership-continuity",
            "claim-2008-early-leadership",
            "claim-2025-cross-boundary-leadership",
            "behavioral_continuity_across_roles",
            "interpretive_non_causal",
            "Leadership behavior appears before senior titles and later explicitly across reporting lines, seniority, and teams.",
            "The path combines an early employer award with cross-team, informal-mentoring, and direct-manager observations.",
            "method-title-independent-leadership-v1",
            ["caveat-non-causal-synthesis", "caveat-selected-evidence"],
            "The path does not imply formal people-management responsibility at every point.",
            "supported",
            "The pattern crosses employers and relationship types while remaining behaviorally bounded.",
        ),
        relationship(
            "relationship-learn-build-teach-systemize",
            "Build knowledge → multiply it through systems",
            "claim-learn-build-teach-systemize-pattern",
            "claim-public-patent-record",
            "claim-sutra-delivery-recognition",
            "recurring_operating_pattern",
            "interpretive_non_causal",
            "Across employers, technical learning and building repeatedly become teaching, reusable artifacts, communities, or delivery systems.",
            "The method selects representative IBM, Exeter, Amazon, and Philips sources and preserves their varying evidence grades.",
            "method-learn-build-teach-systemize-v1",
            [
                "caveat-non-causal-synthesis",
                "caveat-selected-evidence",
                "caveat-self-authored-source",
            ],
            "The selected sources do not establish that every project followed all four stages.",
            "supported",
            "The pattern recurs in four employer contexts but includes first-party evidence.",
        ),
        relationship(
            "relationship-topic-frontier-continuity",
            "Foundational teaching → AI learning frontier",
            "claim-topic-frontier-teaching-continuity",
            "claim-community-talks-reach",
            "claim-session-ai-feedback",
            "topic_shift_with_method_continuity",
            "mixed_method_interpretation",
            "Topics shift from wellness and foundational software through observability toward AI, while practical teaching concerns persist.",
            "The method keeps two trackers separate, uses their dated scopes, and relies only on explicit category fields and documented feedback questions.",
            "method-topic-frontier-teaching-continuity-v1",
            [
                "caveat-category-labels",
                "caveat-touchpoints-not-people",
                "caveat-session-tracker-boundary",
                "caveat-feedback-not-longitudinal",
                "caveat-non-causal-synthesis",
            ],
            "Tracker coverage differs, filename-derived categories are not hand-coded, and topic counts are not unique session counts.",
            "supported",
            "The direction of topic change is clear; corpus boundaries constrain completeness.",
        ),
        relationship(
            "relationship-connect-demand-composition",
            "Conversation volume → demand-driven share",
            "claim-connect-demand-share",
            "claim-connect-volume-2021",
            "claim-connect-demand-share",
            "part_to_whole_composition",
            "calculated_composition",
            "454 of 575 recorded connects were set up by others, yielding a 79% displayed share.",
            "The method sums twelve monthly numerator and denominator rows and retains both values beside the rounded percentage.",
            "method-connect-demand-v1",
            [
                "caveat-touchpoints-not-people",
                "caveat-inference-not-motive",
                "caveat-private-held-source",
            ],
            "A request demonstrates demand for a conversation, not motive, satisfaction, unique reach, or business outcome.",
            "high",
            "The arithmetic is deterministic and the interpretation is narrowly bounded.",
        ),
        relationship(
            "relationship-service-continuity-growth",
            "Direct service record → resumed, growing program",
            "claim-service-continuity-and-growth",
            "claim-community-service-photo-record",
            "claim-book-program-growth",
            "documented_continuity_with_gap",
            "mixed_method_interpretation",
            "Documented direct service precedes the financial ledger; the ledger resumes in 2022 after no program recorded for 2020–2021, has no reviewed 2024 program record, and later records 2025 and its highest endpoint in 2026.",
            "The method combines dated images with privacy-safe annual aggregates and refuses to interpolate 2020, 2021, or 2024 or imply uninterrupted post-2022 activity.",
            "method-service-continuity-growth-v1",
            [
                "caveat-active-years-with-gaps",
                "caveat-currency-not-normalized",
                "caveat-private-held-source",
                "caveat-non-causal-synthesis",
            ],
            "The records do not establish uninterrupted annual activity, any activity or amount for 2024, inflation-adjusted impact, or beneficiary counts; absence of a reviewed 2024 record is not treated as a verified zero.",
            "supported",
            "The timeline and endpoints are documented; the statement explicitly preserves all three unrecorded calendar years and the non-contiguous post-2022 sequence.",
        ),
        relationship(
            "relationship-professional-community-trust-bridge",
            "Professional trust ↔ community trust",
            "claim-professional-community-trust-bridge",
            "claim-2015-cross-team-leadership",
            "claim-book-program-total",
            "identity_redacted_cross_context_continuity",
            "privacy_limited",
            "One reviewed identity appears in both a professional recommendation and multi-year community contribution records.",
            "An exact held-record match is used, while the public output suppresses identity, amounts, and frequency.",
            "method-professional-community-trust-bridge-v1",
            [
                "caveat-identity-withheld",
                "caveat-inference-not-motive",
                "caveat-private-held-source",
                "caveat-non-causal-synthesis",
            ],
            "Privacy prevents public independent verification, and cross-context participation does not establish motive.",
            "limited",
            "The linkage is exact in held records, but its public proof is intentionally constrained.",
        ),
        relationship(
            "relationship-feedback-adaptation-tension",
            "Improvement request → adaptation with persistent demand",
            "claim-feedback-adaptation-tension",
            "claim-2019-practical-feedback-request",
            "claim-2026-hands-on-depth-request",
            "adaptation_with_persistent_demand",
            "interpretive_non_causal",
            "Later praise for practical AI prompting and guardrails sits between earlier and later requests for hands-on depth.",
            "The method uses documented question types—requested improvement and participant takeaway—not regex-derived sentiment or theme classification.",
            "method-feedback-adaptation-tension-v1",
            [
                "caveat-feedback-not-longitudinal",
                "caveat-non-causal-synthesis",
                "caveat-selected-evidence",
                "caveat-session-tracker-boundary",
            ],
            "Different cohorts and contexts prevent claims of individual longitudinal change, resolution, or causality.",
            "supported",
            "The three fields support the tension, but not a completed improvement trajectory.",
        ),
    ]


EXECUTIVE_SEMANTICS: dict[str, Any] = {
    "portfolio_thesis": "Datta turns complex change into capability that lasts — through trust, engineering discipline, learning, and service.",
    "levels": {
        "summary": "Executive signal",
        "narrative": "Why this matters",
        "proof": "Evidence",
        "method": "How this was derived",
        "context": "Evidence context",
    },
    "actions": {
        "inspect_claim": "Inspect claim",
        "open_source": "Open source",
        "open_public_source": "Open public source",
        "view_method": "See calculation",
        "search_data_room": "Search the evidence",
    },
    "evidence_basis": {
        "corroborated": "Publicly corroborated",
        "documented": "Documented record",
        "self_reported": "First-party initiative record",
    },
    "source_access": {
        "public_external": "Public source",
        "public_excerpt": "Published excerpt",
        "private_held": "Archived source",
        "aggregate_only": "Published aggregate",
    },
    "page_copy": {
        "brief": {
            "question": "What makes Datta ready to lead at executive scale?",
            "summary": "A concise view of leadership reach, disciplined innovation, capability building, and service.",
        },
        "leadership": {
            "question": "How does Datta lead across levels, functions, and formal boundaries?",
            "summary": "Observed behaviors show influence beyond title, strength across leadership levels, and deliberate growth in executive reach.",
        },
        "journey": {
            "question": "How has Datta turned technical depth into organizational leverage?",
            "summary": "A career progression from early leadership and technical contribution to delivery discipline and enterprise recognition.",
        },
        "trust": {
            "question": "Why do colleagues seek Datta out and trust his leadership?",
            "summary": "People repeatedly choose his counsel because he creates clarity, builds independent thinkers, and connects purpose to action.",
        },
        "innovation": {
            "question": "How does Datta turn emerging technology into governed execution?",
            "summary": "A record of carrying ideas from invention through engineered delivery while framing opportunity at portfolio scale.",
        },
        "learning": {
            "question": "What do people value and carry forward after learning with Datta?",
            "summary": "Participant evidence shows useful experiences, practical takeaways, and a curriculum that advances with the technology frontier.",
        },
        "community": {
            "question": "How does Datta create value beyond formal responsibility?",
            "summary": "Service, teaching, and giving compound over time as capability and reach grow.",
        },
        "data-room": {
            "question": "How can every featured conclusion be traced?",
            "summary": "Search the evidence record, inspect derivations, and follow every featured conclusion to its supporting sources.",
        },
    },
}


AUDIT_ONLY_CLAIM_IDS: tuple[str, ...] = (
    "claim-evidence-corpus-coverage",
    "claim-export-embedding-gap",
    "claim-export-provenance-gap",
    "claim-professional-community-trust-bridge",
)


STORY_BLOCKS: tuple[dict[str, Any], ...] = (
    {
        "id": "brief-influence-beyond-hierarchy",
        "page_id": "brief",
        "title": "Influence beyond hierarchy",
        "meaning": "Leadership is documented before senior titles and later across reporting lines, seniority, and teams.",
        "proof": "Early-career recognition and a later manager observation, seventeen years apart.",
        "primary_claim_id": "claim-title-independent-leadership-continuity",
        "folded_claim_ids": [],
    },
    {
        "id": "brief-speed-built-on-discipline",
        "page_id": "brief",
        "title": "Speed built on discipline",
        "meaning": "A decade of quality and delivery controls anchors the current AI story.",
        "proof": "Quality-control signals recur from 2015 through 2026.",
        "primary_claim_id": "claim-quality-before-ai-lineage",
        "folded_claim_ids": [],
    },
    {
        "id": "brief-capability-that-multiplies",
        "page_id": "brief",
        "title": "Capability that multiplies",
        "meaning": "What Datta learns and builds repeatedly becomes tools, teaching, communities, and reusable systems.",
        "proof": "The pattern appears across IBM, Exeter, Amazon, and Philips records.",
        "primary_claim_id": "claim-learn-build-teach-systemize-pattern",
        "folded_claim_ids": [],
    },
    {
        "id": "brief-service-that-compounds",
        "page_id": "brief",
        "title": "Service that compounds",
        "meaning": "Hands-on service matured into a recurring education-material program with growing recorded support.",
        "proof": "Direct-service records precede ten recorded program years.",
        "primary_claim_id": "claim-service-continuity-and-growth",
        "folded_claim_ids": [],
    },
    {
        "id": "leadership-boundaries",
        "page_id": "leadership",
        "title": "Leads across formal boundaries",
        "meaning": "Leadership reaches beyond the org chart through technical credibility, empathy, coaching, and shared standards.",
        "proof": "A direct manager describes leadership across reporting lines, seniority, and teams.",
        "primary_claim_id": "claim-2025-cross-boundary-leadership",
        "folded_claim_ids": ["claim-2015-cross-team-leadership"],
    },
    {
        "id": "leadership-benchmark",
        "page_id": "leadership",
        "title": "Leadership behaviors exceed the benchmark",
        "meaning": "Multi-rater evidence and later independent observations align around communication, rigor, evaluation, relationships, and authenticity.",
        "proof": "All five measured behaviors were above the company comparison; mean delta +0.31.",
        "primary_claim_id": "claim-2020-360-company-deltas",
        "folded_claim_ids": [
            "claim-2020-strengths-profile",
            "claim-strengths-later-observation-concordance",
        ],
    },
    {
        "id": "leadership-growth",
        "page_id": "leadership",
        "title": "Deliberate growth expanded executive reach",
        "meaning": "A clearly named growth goal became a testable leadership direction and later appears in independently attributed behavior.",
        "proof": "A 2020 growth goal aligns with independent 2025 descriptions of executive-to-developer influence.",
        "primary_claim_id": "claim-feedback-to-executive-observation",
        "folded_claim_ids": [
            "claim-2020-executive-influence-development-signal",
            "claim-2025-executive-influence-observation",
        ],
    },
    {
        "id": "journey-span",
        "page_id": "journey",
        "title": "Leadership showed up early",
        "meaning": "The record begins with end-to-end ownership and widens across two decades of technical and organizational scope.",
        "proof": "A 2008 award begins a career record spanning 2007–2026.",
        "primary_claim_id": "claim-career-calendar-span",
        "folded_claim_ids": ["claim-2008-early-leadership"],
    },
    {
        "id": "journey-community",
        "page_id": "journey",
        "title": "Technical depth became community contribution",
        "meaning": "Building expertise and sharing it with a wider technical community became an early recurring pattern.",
        "proof": "IBM recognized contribution to its India technical exchange in 2010.",
        "primary_claim_id": "claim-2010-technical-community-recognition",
        "folded_claim_ids": [],
    },
    {
        "id": "journey-delivery",
        "page_id": "journey",
        "title": "Process discipline became delivery strength",
        "meaning": "Engineering improvement and dependable execution were recognized as mutually reinforcing capabilities.",
        "proof": "Adjacent awards recognized process improvement and exceptional project delivery.",
        "primary_claim_id": "claim-2017-process-delivery-recognition",
        "folded_claim_ids": [],
    },
    {
        "id": "journey-enterprise",
        "page_id": "journey",
        "title": "Impact earned enterprise recognition",
        "meaning": "The career arc progressed from local ownership to visible contribution at company-wide technical leadership level.",
        "proof": "Named among outstanding-achievement recipients in the CTO Annual Address.",
        "primary_claim_id": "claim-2021-cto-recognition",
        "folded_claim_ids": [],
    },
    {
        "id": "trust-sought-out",
        "page_id": "trust",
        "title": "People chose to seek him out",
        "meaning": "A high share of conversations began through others’ initiative, signaling accessibility and continued demand for dialogue.",
        "proof": "454 of 575 recorded conversations were requested by others — 79%.",
        "primary_claim_id": "claim-connect-demand-share",
        "folded_claim_ids": ["claim-connect-volume-2021"],
    },
    {
        "id": "trust-independent-thinkers",
        "page_id": "trust",
        "title": "Builds independent thinkers",
        "meaning": "Mentoring emphasizes reasoning, capability, and values so people leave stronger rather than more dependent.",
        "proof": "A former mentee describes guidance that develops thinking, skills, and values.",
        "primary_claim_id": "claim-2020-mentoring-method",
        "folded_claim_ids": [],
    },
    {
        "id": "trust-purpose",
        "page_id": "trust",
        "title": "Creates clarity and purpose",
        "meaning": "Calm presence, explicit outcomes, openness to input, and availability make trust practical across formal boundaries.",
        "proof": "A colleague outside his reporting line describes calmness, clarity, openness, and availability.",
        "primary_claim_id": "claim-2023-purpose-first-mentoring",
        "folded_claim_ids": [],
    },
    {
        "id": "innovation-patent",
        "page_id": "innovation",
        "title": "Ideas carried from invention to public patent",
        "meaning": "Innovation progressed from an employer-recognized application to a traceable public grant record.",
        "proof": "IBM’s 2010 application award matches the 2013 public grant title and inventor identity.",
        "primary_claim_id": "claim-public-patent-record",
        "folded_claim_ids": ["claim-2010-first-patent-achievement"],
    },
    {
        "id": "innovation-controlled-ai",
        "page_id": "innovation",
        "title": "AI delivery accelerated with engineered control",
        "meaning": "Current AI execution combines development speed, traceability, automated quality gates, and organizational delivery recognition.",
        "proof": "3× team-reported development speed, commit-level quality gates, and 90%+ traceability improvement.",
        "primary_claim_id": "claim-sutra-ai-delivery",
        "folded_claim_ids": [
            "claim-sutra-traceability",
            "claim-sutra-delivery-recognition",
            "claim-2015-quality-discipline",
            "claim-2020-quality-speed-framing",
        ],
    },
    {
        "id": "innovation-portfolio-value",
        "page_id": "innovation",
        "title": "AI opportunity framed at portfolio scale",
        "meaning": "Innovation is translated into an explicit portfolio-level capacity and efficiency opportunity across multiple initiatives.",
        "proof": "Eight initiatives identified an estimated potential €3.5M annual efficiency opportunity and ~18,000 productivity hours.",
        "primary_claim_id": "claim-xite-potential-efficiency",
        "folded_claim_ids": ["claim-xite-potential-hours"],
    },
    {
        "id": "learning-listening-system",
        "page_id": "learning",
        "title": "Feedback shapes every iteration",
        "meaning": "Learning is managed as a listening system that combines scale, scored questions, and written participant input.",
        "proof": "1,050 submitted responses, including 1,811 written inputs and 2,149 question ratings.",
        "primary_claim_id": "claim-session-post-responses",
        "folded_claim_ids": [
            "claim-session-post-datasets",
            "claim-session-rating-observations",
            "claim-session-qualitative-entries",
            "claim-session-audience-surveys",
        ],
    },
    {
        "id": "learning-reach",
        "page_id": "learning",
        "title": "Knowledge shared at scale",
        "meaning": "A sustained teaching record turns professional experience into reusable learning for broader communities.",
        "proof": "50 recorded sessions and 3,732 participant attendances across 2010–2021.",
        "primary_claim_id": "claim-community-talks-reach",
        "folded_claim_ids": [],
    },
    {
        "id": "learning-valued",
        "page_id": "learning",
        "title": "Learners valued the experience",
        "meaning": "Ratings and participant words show that learners valued both the experience and practical lessons they could carry forward.",
        "proof": "Presenter means of 4.58/5 and 9.12/10 on their original scales; recommendation likelihood 8.87/10.",
        "primary_claim_id": "claim-student-presenter-ratings",
        "folded_claim_ids": [
            "claim-student-feedback-coverage",
            "claim-student-recommendation-likelihood",
            "claim-student-takeaway-interview-resilience-2017",
            "claim-student-takeaway-uncertainty-2020",
        ],
    },
    {
        "id": "learning-frontier",
        "page_id": "learning",
        "title": "The curriculum advances with the frontier",
        "meaning": "Topics progress from foundational engineering through delivery performance to applied AI, guided by continuing participant feedback.",
        "proof": "Foundational engineering expanded through DORA into 23 AI feedback sets, while participant feedback keeps sharpening practical depth.",
        "primary_claim_id": "claim-topic-frontier-teaching-continuity",
        "folded_claim_ids": [
            "claim-feedback-adaptation-tension",
            "claim-session-ai-feedback",
            "claim-session-dora-feedback",
            "claim-2019-practical-feedback-request",
            "claim-2024-practical-ai-takeaway",
            "claim-2026-hands-on-depth-request",
        ],
    },
    {
        "id": "community-presence",
        "page_id": "community",
        "title": "Service began with presence",
        "meaning": "Contribution began through direct teaching, wellbeing work, rural-school engagement, and material distribution.",
        "proof": "Dated images document teaching, yoga, rural-school engagement, and material distribution from 2007–2015.",
        "primary_claim_id": "claim-community-service-photo-record",
        "folded_claim_ids": [],
        "image_source_id": "source-community-service-photo-record-2007-2015",
    },
    {
        "id": "community-scaled-giving",
        "page_id": "community",
        "title": "Giving grew with capacity",
        "meaning": "A recurring education-material program converted personal capacity into sustained, increasing support.",
        "proof": "₹1.97M directed to education materials across ten recorded years; recorded 2014→2026 totals grew 13.3×.",
        "primary_claim_id": "claim-book-program-total",
        "folded_claim_ids": ["claim-book-program-growth"],
    },
)


PAGE_LABELS = {
    "brief": "Executive brief",
    "leadership": "Leadership",
    "journey": "Career journey",
    "trust": "Trust",
    "innovation": "Innovation & value",
    "learning": "Learning",
    "community": "Community & service",
    "data-room": "Data room",
}


def _pages() -> list[dict[str, Any]]:
    claims_by_page: dict[str, list[str]] = {page_id: [] for page_id in PAGE_LABELS}
    for block in STORY_BLOCKS:
        claims_by_page[block["page_id"]].append(block["primary_claim_id"])
        claims_by_page[block["page_id"]].extend(block["folded_claim_ids"])
    claims_by_page["data-room"] = list(AUDIT_ONLY_CLAIM_IDS)

    return [
        {
            "id": page_id,
            "route": page_id,
            "label": label,
            **EXECUTIVE_SEMANTICS["page_copy"][page_id],
            "claim_ids": claims_by_page[page_id],
        }
        for page_id, label in PAGE_LABELS.items()
    ]


def _conflicts() -> list[dict[str, Any]]:
    return [
        {
            "id": "conflict-session-population-accounting",
            "title": "Historical combined population vs corrected analysis population",
            "status": "resolved_by_versioned_recalculation",
            "severity": "material",
            "description": "A historical portfolio assertion used 90 unique files and 1,183 response rows as a session-feedback headline, which included two pre-session audience surveys. The corrected narrative now records that prior error explicitly.",
            "source_ids": [
                "source-session-corrected-narrative-2026",
                "source-session-response-corpus-2018-2026",
                "source-session-corrected-summary-2026",
            ],
            "affected_claim_ids": [
                "claim-session-post-datasets",
                "claim-session-post-responses",
                "claim-session-qualitative-entries",
                "claim-session-audience-surveys",
            ],
            "resolution": "Version 1 of the public method excludes two duplicate files, reports two pre-session surveys separately, and labels the remaining 88 records as post-event/interaction analysis files rather than facilitated sessions.",
        },
        {
            "id": "conflict-session-rating-units",
            "title": "Rating counts used incompatible populations and units",
            "status": "resolved_by_unit_definition",
            "severity": "material",
            "description": "The historical 2,296 figure counts question-level rating observations across all 92 extracted source files. The post-event/interaction analysis population contains 2,149 rating observations; 221 is the number of question-level aggregates, not observations.",
            "source_ids": [
                "source-session-corrected-narrative-2026",
                "source-session-corrected-summary-2026",
                "source-session-response-corpus-2018-2026",
            ],
            "affected_claim_ids": ["claim-session-rating-observations"],
            "resolution": "The public claim names the population and unit together and publishes the formula: sum ratings[*].count over the 88-file analysis population.",
        },
        {
            "id": "conflict-session-year-count",
            "title": "Historical 'eight years' label vs nine recorded calendar years",
            "status": "resolved_by_label_correction",
            "severity": "moderate",
            "description": "The inclusive recorded-year range 2018–2026 contains nine calendar years, while a historical narrative labeled it eight years.",
            "source_ids": [
                "source-session-corrected-narrative-2026",
                "source-session-response-corpus-2018-2026",
            ],
            "affected_claim_ids": ["claim-session-post-datasets"],
            "resolution": "The portfolio uses the date range 2018–2026 and does not publish the historical eight-year label.",
        },
        {
            "id": "conflict-session-category-counts",
            "title": "Historical category counts included pre-session surveys",
            "status": "resolved_by_population_separation",
            "severity": "moderate",
            "description": "Historical category headlines reported 24 AI/GenAI files and 12 DORA files. After pre-session surveys are separated, the post-event/interaction population contains 23 AI/GenAI files and 11 DORA files.",
            "source_ids": [
                "source-session-corrected-narrative-2026",
                "source-session-corrected-summary-2026",
                "source-session-response-corpus-2018-2026",
            ],
            "affected_claim_ids": ["claim-session-ai-feedback", "claim-session-dora-feedback"],
            "resolution": "Category counts now use only the 88-file analysis population and are labeled filename-pattern-derived file counts, not distinct session counts.",
        },
        {
            "id": "conflict-career-duration-labels",
            "title": "Resume duration labels are not mutually consistent",
            "status": "resolved_by_concept_separation",
            "severity": "moderate",
            "description": "The held 2026 record contains a 19-year title, a 15-years-of-experience summary inherited from an earlier format, and dates spanning 2007–2026.",
            "source_ids": ["source-career-resume-2026"],
            "affected_claim_ids": ["claim-career-calendar-span"],
            "resolution": "The portfolio makes only the reproducible inclusive calendar-span claim—20 calendar years touched—and explicitly does not relabel it as completed experience or tenure.",
        },
        {
            "id": "conflict-jscpd-causality",
            "title": "Historical before/after language exceeded the available design",
            "status": "claim_withheld",
            "severity": "material",
            "description": "A historical narrative described the JSCPD pair as proof of measurable code improvement, but the committed extract has unmatched before and after populations and no shared outcome measure.",
            "source_ids": [
                "source-session-corrected-narrative-2026",
                "source-session-response-corpus-2018-2026",
            ],
            "affected_claim_ids": [],
            "resolution": "The corrected narrative states the limitation, and this portfolio publishes no causal JSCPD improvement claim.",
        },
        {
            "id": "conflict-sutra-onboarding-arithmetic",
            "title": "Sutra onboarding percentage and endpoint imply different reductions",
            "status": "metric_withheld",
            "severity": "material",
            "description": "The initiative announcement pairs '30–40% faster' with '3 weeks to 3 days'; a simple elapsed-time calculation for the latter is about an 86% reduction, so the statements do not describe the same metric.",
            "source_ids": ["source-sutra-initiative-outcomes-2026"],
            "affected_claim_ids": ["claim-sutra-ai-delivery"],
            "resolution": "The portfolio withholds the onboarding percentage and endpoint claim pending a definition of the baseline and metric. Unrelated traceability and attributed AI-delivery statements remain separately scoped.",
        },
        {
            "id": "conflict-sutra-zero-quality-boundary",
            "title": "Quality gates do not prove zero quality compromise",
            "status": "claim_bounded_to_observed_controls",
            "severity": "material",
            "description": "The attributed Sutra commentary uses zero-compromise language. The available evidence summary documents commit-blocking rules and external quality tools, but it does not provide an independent defect or technical-debt audit proving zero compromise.",
            "source_ids": ["source-sutra-initiative-outcomes-2026"],
            "affected_claim_ids": ["claim-sutra-ai-delivery"],
            "resolution": "The public claim reports the observed control system—commit gates and external tooling—and does not publish a zero-defect, zero-debt, or zero-compromise conclusion.",
        },
    ]


def build_portfolio_data(root: Path = REPO_ROOT) -> dict[str, Any]:
    """Build a deterministic, public-safe portfolio dataset from held evidence."""
    sessions = _session_metrics(root)
    student = _student_feedback_metrics(root)
    connect = _connect_metrics(root)
    books = _book_metrics(root)
    career = _career_metrics(root)
    assessment = _assessment_metrics(root)
    inventory = _inventory_metrics(root)
    claims, supports = _materialize_claims(
        _claims(sessions, student, connect, books, career, assessment, inventory)
    )
    methods = _methods(sessions, student, connect, books, career, assessment, inventory)
    conflicts = _conflicts()
    relationships = _relationships(claims)
    data: dict[str, Any] = {
        "meta": {
            "schema_version": 3,
            "title": "Datta — leadership, with receipts",
            "subtitle": "An interactive executive portfolio in three depths: summary, explanation, and auditable detail.",
            "generated_at": AS_OF,
            "as_of": AS_OF,
            "publication_contract": "Every claim has claim-specific support. Every calculated or interpreted claim has a versioned method. Private sources expose only a stable ID, access state, approved excerpt, hash, and safe locator.",
            "depth_model": [
                {"level": 1, "label": "Summary", "description": "Decision-ready claim and metric."},
                {
                    "level": 2,
                    "label": "Explanation",
                    "description": "Leadership meaning and the bounded evidence signal.",
                },
                {
                    "level": 3,
                    "label": "Detail",
                    "description": "Source records, locators, method inputs, scope definitions, reconciliation context, and public links.",
                },
            ],
        },
        "executive_semantics": json.loads(json.dumps(EXECUTIVE_SEMANTICS, ensure_ascii=False)),
        "pages": _pages(),
        "story_blocks": [
            {
                **block,
                "folded_claim_ids": list(block["folded_claim_ids"]),
            }
            for block in STORY_BLOCKS
        ],
        "audit_only_claim_ids": list(AUDIT_ONLY_CLAIM_IDS),
        "claims": claims,
        "supports": supports,
        "sources": _sources(root),
        "methods": methods,
        "relationships": relationships,
        "caveats": list(CAVEATS),
        "conflicts": conflicts,
        "data_quality": {
            "summary": "The portfolio is a curated publication layer over a larger private corpus. It exposes corrected units, source conflicts, selection limits, privacy boundaries, and current export gaps rather than hiding them.",
            "coverage": {
                "evidence_markdown_files": inventory["evidence_markdown"],
                "individual_evidence_records_excluding_indexes": inventory[
                    "individual_evidence_records"
                ],
                "informal_feedback_records_excluding_index": inventory["informal_feedback_records"],
                "documentary_images": inventory["documentary_images"],
                "records_with_yaml_frontmatter": inventory["frontmatter_records"],
                "evidence_index_rows": inventory["evidence_index_rows"],
                "relationship_graph_nodes": inventory["nodes"],
                "relationship_graph_edges": inventory["edges"],
                "note": "Filesystem classes and evidence-index rows have different scopes; no misleading coverage percentage is calculated.",
            },
            "export_gaps": [
                {
                    "id": "gap-retrieval-index",
                    "count": inventory["missing_in_chroma"],
                    "unit": "chunks",
                    "description": "DuckDB chunks absent from the Chroma retrieval index.",
                    "impact": "Some held text may not be retrievable through semantic search even though direct source-linked portfolio claims remain auditable.",
                    "source_id": "source-relationship-export-quality-2026",
                },
                {
                    "id": "gap-edge-artifact-provenance",
                    "count": inventory["orphan_edge_artifact_provenance"],
                    "unit": "edges",
                    "description": "Soft edge-to-artifact provenance links that do not resolve.",
                    "impact": "Those graph edges require provenance repair before they should support new public claims.",
                    "source_id": "source-relationship-export-quality-2026",
                },
                {
                    "id": "gap-evidence-index-scope",
                    "count": inventory["evidence_index_rows"],
                    "unit": "indexed evidence rows",
                    "description": f"The generated evidence index contains {inventory['evidence_index_rows']} rows, while the filesystem contains {inventory['individual_evidence_records']} individual evidence records plus other evidence classes.",
                    "impact": "The scopes are not directly comparable; the site avoids claiming full-corpus indexing coverage.",
                    "source_id": "source-relationship-export-quality-2026",
                },
            ],
            "unit_dictionary": [
                {
                    "unit": "analysis file",
                    "definition": "One non-duplicate, non-pre-survey workbook extract in the operational post-event/interaction population; not necessarily one facilitated session.",
                },
                {
                    "unit": "response row",
                    "definition": "One submitted spreadsheet row; not necessarily a unique person or attendee.",
                },
                {
                    "unit": "rating observation",
                    "definition": "One response to one rating question; one response row may contribute multiple observations.",
                },
                {
                    "unit": "qualitative entry",
                    "definition": "One populated qualitative field value; one response row may contribute multiple entries.",
                },
                {
                    "unit": "participant instance",
                    "definition": "An approximate attendance touchpoint in a first-party activity ledger; not a unique person.",
                },
            ],
            "conflict_ids": [conflict["id"] for conflict in conflicts],
            "privacy_boundary": "Raw participant rows, internal URLs, emails, local paths, identities in financial records, individual contribution amounts, account data, and private corporate payloads are not published.",
        },
    }
    validate_portfolio_data(data)
    return data


def _unique_ids(records: list[dict[str, Any]], label: str) -> set[str]:
    ids = [record["id"] for record in records]
    if len(ids) != len(set(ids)):
        duplicates = sorted(item for item, count in Counter(ids).items() if count > 1)
        raise ValueError(f"Duplicate {label} IDs: {duplicates}")
    return set(ids)


def validate_portfolio_data(data: dict[str, Any]) -> None:
    """Fail closed if the browser bundle loses traceability or leaks private detail."""
    required = {
        "meta",
        "executive_semantics",
        "pages",
        "story_blocks",
        "audit_only_claim_ids",
        "claims",
        "supports",
        "sources",
        "methods",
        "relationships",
        "caveats",
        "conflicts",
        "data_quality",
    }
    missing = required - data.keys()
    if missing:
        raise ValueError(f"Missing top-level portfolio collections: {sorted(missing)}")

    page_ids = _unique_ids(data["pages"], "page")
    story_block_ids = _unique_ids(data["story_blocks"], "story block")
    claim_ids = _unique_ids(data["claims"], "claim")
    support_ids = _unique_ids(data["supports"], "support")
    source_ids = _unique_ids(data["sources"], "source")
    method_ids = _unique_ids(data["methods"], "method")
    relationship_ids = _unique_ids(data["relationships"], "relationship")
    caveat_ids = _unique_ids(data["caveats"], "caveat")
    conflict_ids = _unique_ids(data["conflicts"], "conflict")

    all_primary_ids = (
        page_ids
        | story_block_ids
        | claim_ids
        | support_ids
        | source_ids
        | method_ids
        | relationship_ids
        | caveat_ids
        | conflict_ids
    )
    expected_count = sum(
        len(collection)
        for collection in (
            data["pages"],
            data["story_blocks"],
            data["claims"],
            data["supports"],
            data["sources"],
            data["methods"],
            data["relationships"],
            data["caveats"],
            data["conflicts"],
        )
    )
    if len(all_primary_ids) != expected_count:
        raise ValueError("IDs must be globally unique across primary portfolio collections")

    claim_by_id = {claim["id"]: claim for claim in data["claims"]}
    support_by_id = {support["id"]: support for support in data["supports"]}
    method_by_id = {method["id"]: method for method in data["methods"]}

    expected_page_ids = set(PAGE_LABELS)
    if page_ids != expected_page_ids:
        raise ValueError(
            f"Portfolio pages must match the executive IA: {sorted(expected_page_ids)}"
        )
    if set(data["executive_semantics"].get("page_copy", {})) != page_ids:
        raise ValueError("Executive page copy must resolve exactly to the portfolio pages")

    page_routes = [page["route"] for page in data["pages"]]
    if len(page_routes) != len(set(page_routes)):
        raise ValueError("Page routes must be unique")
    for page in data["pages"]:
        if not page["claim_ids"]:
            raise ValueError(f"Page has no claims: {page['id']}")
        unknown = set(page["claim_ids"]) - claim_ids
        if unknown:
            raise ValueError(f"Page {page['id']} references unknown claims: {sorted(unknown)}")
    mapped_claims = {claim_id for page in data["pages"] for claim_id in page["claim_ids"]}
    if mapped_claims != claim_ids:
        raise ValueError(
            f"Every claim must appear on a page; unmapped: {sorted(claim_ids - mapped_claims)}"
        )

    audit_only_claim_ids = data["audit_only_claim_ids"]
    if len(audit_only_claim_ids) != len(set(audit_only_claim_ids)):
        raise ValueError("Audit-only claim IDs must not repeat")
    if tuple(audit_only_claim_ids) != AUDIT_ONLY_CLAIM_IDS:
        raise ValueError("Audit-only claims must match the four approved audit records")
    if set(audit_only_claim_ids) - claim_ids:
        raise ValueError("Audit-only claims reference an unknown claim")

    blocks_by_page: dict[str, list[dict[str, Any]]] = {page_id: [] for page_id in page_ids}
    story_claim_owners: list[str] = []
    banned_title_pattern = re.compile(
        r"\b(?:not|gaps?|confidence|rows?|files?|ledger)\b", re.IGNORECASE
    )
    for block in data["story_blocks"]:
        page_id = block.get("page_id")
        if page_id not in page_ids:
            raise ValueError(f"Story block references an unknown page: {block['id']}")
        if page_id == "data-room":
            raise ValueError("Data room must not contain story blocks")
        if banned_title_pattern.search(block.get("title", "")):
            raise ValueError(f"Story block title contains banned language: {block['id']}")
        if not all(block.get(field, "").strip() for field in ("title", "meaning", "proof")):
            raise ValueError(f"Story block lacks executive copy: {block['id']}")

        primary_claim_id = block.get("primary_claim_id")
        folded_claim_ids = block.get("folded_claim_ids")
        if primary_claim_id not in claim_ids:
            raise ValueError(f"Story block references an unknown primary claim: {block['id']}")
        if not isinstance(folded_claim_ids, list):
            raise ValueError(f"Story block folded claims must be a list: {block['id']}")
        if set(folded_claim_ids) - claim_ids:
            raise ValueError(f"Story block references an unknown folded claim: {block['id']}")
        if primary_claim_id in folded_claim_ids or len(folded_claim_ids) != len(
            set(folded_claim_ids)
        ):
            raise ValueError(f"Story block repeats a claim: {block['id']}")
        if not claim_by_id[primary_claim_id]["support_ids"]:
            raise ValueError(f"Story block primary claim has no support: {block['id']}")
        image_source_id = block.get("image_source_id")
        if image_source_id and image_source_id not in source_ids:
            raise ValueError(f"Story block references an unknown image source: {block['id']}")

        blocks_by_page[page_id].append(block)
        story_claim_owners.extend([primary_claim_id, *folded_claim_ids])

    for page_id in page_ids - {"data-room"}:
        block_count = len(blocks_by_page[page_id])
        if not 2 <= block_count <= 4:
            raise ValueError(
                f"Page {page_id} must contain two to four story blocks, found {block_count}"
            )
    if blocks_by_page["data-room"]:
        raise ValueError("Data room must not contain story blocks")

    duplicate_story_claims = sorted(
        claim_id for claim_id, count in Counter(story_claim_owners).items() if count > 1
    )
    if duplicate_story_claims:
        raise ValueError(
            f"Claims cannot be owned by multiple story blocks: {duplicate_story_claims}"
        )
    audit_only_set = set(audit_only_claim_ids)
    if set(story_claim_owners) & audit_only_set:
        raise ValueError("Audit-only claims cannot be assigned to story blocks")
    expected_story_claims = claim_ids - audit_only_set
    if set(story_claim_owners) != expected_story_claims:
        raise ValueError(
            "Every non-audit claim must be assigned exactly once across story blocks; "
            f"unassigned: {sorted(expected_story_claims - set(story_claim_owners))}"
        )

    page_claims = {page["id"]: page["claim_ids"] for page in data["pages"]}
    for page_id, blocks in blocks_by_page.items():
        expected_claims = (
            list(audit_only_claim_ids)
            if page_id == "data-room"
            else [
                claim_id
                for block in blocks
                for claim_id in [
                    block["primary_claim_id"],
                    *block["folded_claim_ids"],
                ]
            ]
        )
        if page_claims[page_id] != expected_claims:
            raise ValueError(f"Page claim ownership diverges from story blocks: {page_id}")

    valid_kinds = {"observed", "calculated", "interpreted"}
    valid_confidence = {"high", "supported", "limited", "contested"}
    for claim in data["claims"]:
        if claim["kind"] not in valid_kinds:
            raise ValueError(f"Invalid claim kind: {claim['id']}")
        if not claim["support_ids"]:
            raise ValueError(f"Claim has no support: {claim['id']}")
        unknown_supports = set(claim["support_ids"]) - support_ids
        if unknown_supports:
            raise ValueError(
                f"Claim {claim['id']} references unknown supports: {sorted(unknown_supports)}"
            )
        for support_id in claim["support_ids"]:
            if support_by_id[support_id]["claim_id"] != claim["id"]:
                raise ValueError(f"Support {support_id} is attached to the wrong claim")
        if not any(
            support_by_id[support_id]["relationship"] == "supports"
            for support_id in claim["support_ids"]
        ):
            raise ValueError(f"Claim has no positive support edge: {claim['id']}")
        if claim["kind"] in {"calculated", "interpreted"}:
            if claim.get("method_id") not in method_ids:
                raise ValueError(f"Derived claim lacks a valid method: {claim['id']}")
            if not method_by_id[claim["method_id"]]["inputs"]:
                raise ValueError(f"Derived claim method has no inputs: {claim['id']}")
        if set(claim["caveat_ids"]) - caveat_ids:
            raise ValueError(f"Claim references unknown caveat: {claim['id']}")
        if set(claim["conflict_ids"]) - conflict_ids:
            raise ValueError(f"Claim references unknown conflict: {claim['id']}")
        if claim["confidence"]["level"] not in valid_confidence:
            raise ValueError(f"Invalid confidence level: {claim['id']}")
        if not claim["confidence"]["rationale"]:
            raise ValueError(f"Claim confidence lacks rationale: {claim['id']}")

    valid_relationships = {"supports", "qualifies", "contradicts", "context"}
    valid_directness = {"direct", "aggregate", "indirect", "interpretive"}
    valid_grades = {"corroborated", "documented", "self_reported"}
    for support in data["supports"]:
        if support["claim_id"] not in claim_ids or support["source_id"] not in source_ids:
            raise ValueError(f"Support edge has an unknown endpoint: {support['id']}")
        if support["relationship"] not in valid_relationships:
            raise ValueError(f"Invalid support relationship: {support['id']}")
        if support["directness"] not in valid_directness:
            raise ValueError(f"Invalid support directness: {support['id']}")
        if support["grade"] not in valid_grades:
            raise ValueError(f"Invalid support grade: {support['id']}")
        if not support["locator"] or not support["rationale"]:
            raise ValueError(f"Support edge lacks locator or rationale: {support['id']}")

    for source in data["sources"]:
        if not re.fullmatch(r"source-[a-z0-9-]+", source["id"]):
            raise ValueError(f"Source ID is not stable and human-readable: {source['id']}")
        if not re.fullmatch(r"[0-9a-f]{64}", source["sha256"]):
            raise ValueError(f"Source lacks a SHA-256 digest: {source['id']}")
        if source.get("checksum_scope") != "held_canonical_artifact":
            raise ValueError(f"Source checksum scope is missing or invalid: {source['id']}")
        if not isinstance(source.get("checksum_note"), str) or not source["checksum_note"].strip():
            raise ValueError(f"Source checksum note is missing: {source['id']}")
        if source["access_state"] not in {
            "public_external",
            "public_excerpt",
            "private_held",
            "aggregate_only",
        }:
            raise ValueError(f"Invalid source access state: {source['id']}")
        if not source["approved_excerpt"]:
            raise ValueError(f"Source lacks an approved excerpt: {source['id']}")
        if source.get("excerpt_kind") not in {"verbatim", "editorial_summary"}:
            raise ValueError(f"Source has an invalid excerpt kind: {source['id']}")
        url = source.get("external_url")
        if source["access_state"] == "public_external" and not url:
            raise ValueError(f"Public external source lacks a URL: {source['id']}")
        if (
            source["access_state"] == "public_external"
            and "not live external page content" not in source["checksum_note"]
        ):
            raise ValueError(f"Public external source checksum note is ambiguous: {source['id']}")
        if url:
            parsed = urlparse(url)
            if (
                parsed.scheme != "https"
                or parsed.hostname not in ALLOWED_EXTERNAL_HOSTS
                or parsed.username
                or parsed.password
            ):
                raise ValueError(f"External URL is not allow-listed: {source['id']}")

    input_ids: list[str] = []
    for method in data["methods"]:
        if not method["inputs"]:
            raise ValueError(f"Method has no inputs: {method['id']}")
        if not method["inclusion_rules"] or not method["exclusion_rules"]:
            raise ValueError(f"Method lacks inclusion or exclusion rules: {method['id']}")
        if not method["deduplication"] or not method["rounding"] or not method["result"]:
            raise ValueError(f"Method lacks audit fields: {method['id']}")
        if set(method["caveat_ids"]) - caveat_ids:
            raise ValueError(f"Method references unknown caveat: {method['id']}")
        for item in method["inputs"]:
            input_ids.append(item["id"])
            if not item.get("source_id") and not item.get("claim_id"):
                raise ValueError(f"Method input lacks a source or claim: {item['id']}")
            if item.get("source_id") and item["source_id"] not in source_ids:
                raise ValueError(f"Method input references unknown source: {item['id']}")
            if item.get("claim_id") and item["claim_id"] not in claim_ids:
                raise ValueError(f"Method input references unknown claim: {item['id']}")
    if len(input_ids) != len(set(input_ids)):
        raise ValueError("Method input IDs must be globally unique")

    for relationship in data["relationships"]:
        if relationship["claim_id"] not in claim_ids:
            raise ValueError(f"Relationship has unknown relationship claim: {relationship['id']}")
        if relationship["from_claim_id"] not in claim_ids:
            raise ValueError(f"Relationship has unknown source endpoint: {relationship['id']}")
        if relationship["to_claim_id"] not in claim_ids:
            raise ValueError(f"Relationship has unknown target endpoint: {relationship['id']}")
        if relationship["method_id"] not in method_ids:
            raise ValueError(f"Relationship has unknown method: {relationship['id']}")
        if not relationship["support_ids"]:
            raise ValueError(f"Relationship has no source-linked supports: {relationship['id']}")
        if set(relationship["support_ids"]) != set(
            claim_by_id[relationship["claim_id"]]["support_ids"]
        ):
            raise ValueError(f"Relationship supports diverge from its claim: {relationship['id']}")
        if set(relationship["caveat_ids"]) - caveat_ids:
            raise ValueError(f"Relationship references unknown caveat: {relationship['id']}")
        if relationship["confidence"]["level"] not in valid_confidence:
            raise ValueError(f"Relationship confidence is invalid: {relationship['id']}")
        if not relationship["reasoning"] or not relationship["limitation"]:
            raise ValueError(f"Relationship lacks reasoning or limitation: {relationship['id']}")

    for conflict in data["conflicts"]:
        if set(conflict["source_ids"]) - source_ids:
            raise ValueError(f"Conflict references unknown source: {conflict['id']}")
        if set(conflict["affected_claim_ids"]) - claim_ids:
            raise ValueError(f"Conflict references unknown claim: {conflict['id']}")
        if not conflict["resolution"]:
            raise ValueError(f"Conflict lacks a resolution: {conflict['id']}")

    referenced_sources = (
        {support["source_id"] for support in data["supports"]}
        | {
            item["source_id"]
            for method in data["methods"]
            for item in method["inputs"]
            if item.get("source_id")
        }
        | {source_id for conflict in data["conflicts"] for source_id in conflict["source_ids"]}
        | {gap["source_id"] for gap in data["data_quality"]["export_gaps"]}
    )
    if referenced_sources != source_ids:
        raise ValueError(
            f"Every public source must be used; unused: {sorted(source_ids - referenced_sources)}"
        )

    used_methods = {claim["method_id"] for claim in data["claims"] if claim.get("method_id")} | {
        relationship["method_id"] for relationship in data["relationships"]
    }
    if used_methods != method_ids:
        raise ValueError(f"Every method must be used; unused: {sorted(method_ids - used_methods)}")

    serialized_original = json.dumps(data, ensure_ascii=False)
    serialized = serialized_original.lower()
    for token in FORBIDDEN_PUBLIC_TOKENS:
        if token in serialized:
            raise ValueError(f"Public dataset contains forbidden token: {token}")
    for domain in FORBIDDEN_INTERNAL_DOMAINS:
        if domain in serialized:
            raise ValueError(f"Public dataset contains an internal domain: {domain}")
    if EMAIL_PATTERN.search(serialized_original):
        raise ValueError("Public dataset contains an email address")
    if (
        INTERNATIONAL_PHONE_PATTERN.search(serialized_original)
        or SEPARATED_PHONE_PATTERN.search(serialized_original)
        or CONTIGUOUS_PHONE_PATTERN.search(serialized_original)
    ):
        raise ValueError("Public dataset contains a phone number")
    embedded_urls = set(URL_PATTERN.findall(serialized_original))
    catalog_urls = {
        source["external_url"] for source in data["sources"] if source.get("external_url")
    }
    if embedded_urls != catalog_urls:
        raise ValueError(
            "Every payload URL must be an allow-listed source external_url; "
            f"unexpected={sorted(embedded_urls - catalog_urls)}"
        )
    if '"path"' in serialized or "evidence_file" in serialized:
        raise ValueError("Public dataset exposes a private path field")


def portfolio_json(data: dict[str, Any]) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def write_portfolio_data(data: dict[str, Any], output: Path = DEFAULT_OUTPUT) -> None:
    """Write the validated browser bundle in a deterministic format."""
    validate_portfolio_data(data)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(portfolio_json(data), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if the committed output differs from a fresh deterministic build.",
    )
    args = parser.parse_args()
    data = build_portfolio_data()
    rendered = portfolio_json(data)
    if args.check:
        if not args.output.is_file() or args.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"Portfolio data is stale: {args.output}")
        print(f"Portfolio data is current: {args.output}")
        return
    write_portfolio_data(data, args.output)
    print(
        f"Wrote {args.output} with {len(data['claims'])} claims, "
        f"{len(data['supports'])} support edges, and "
        f"{len(data['relationships'])} explicit relationships."
    )


if __name__ == "__main__":
    main()
