# Evidence: Professional Session and Interaction Feedback (2018–2026)

## Source

- **Extracted source records:** 92 Excel workbook records
- **Committed extract:** [all_sessions_data.json](all_sessions_data.json)
- **Reproducible aggregate:** [summary_stats.json](summary_stats.json)
- **Processor:** [process_feedback.py](process_feedback.py)
- **Recorded years:** 2018–2026
- **Ingested:** 2026-08-05
- **Channel:** `manual_batch`
- **Raw workbook location at ingestion:**
  `/Users/dsvellal/Downloads/Website/Philips-Sessions-Feedback/`
- **Raw workbooks committed here:** No

The committed extract contains per-file metadata, response-row counts, extracted
question-level rating summaries, extracted text entries, and up to three sample
rows. The summary is reproducible from that extract. The original participant-level
rating rows are not committed, so they cannot be fully recalculated from this
repository alone.

## Corrected Population Accounting

The prior aggregate included two pre-session audience surveys in the claimed
post-event population. Duplicates and pre-surveys are now separate, mutually
exclusive exclusions.

| Population | Files | Response rows | Extracted qualitative entries | Rating-question aggregates | Rating observations |
|---|---:|---:|---:|---:|---:|
| All extracted source records | 92 | 1,193 | 2,023 | 228 | 2,296 |
| Duplicate files excluded | 2 | 10 | 20 | 5 | 16 |
| Unique files, including pre-surveys | 90 | 1,183 | 2,003 | 223 | 2,280 |
| Pre-session audience surveys, reported separately | 2 | 133 | 192 | 2 | 131 |
| **Post-event/interaction feedback analysis population** | **88** | **1,050** | **1,811** | **221** | **2,149** |

The file and row calculations are:

- `92 source files − 2 duplicates − 2 pre-surveys = 88 analysis files`
- `1,193 source rows − 10 duplicate rows − 133 pre-survey rows = 1,050 analysis rows`

“Response rows” are spreadsheet rows, not verified unique participants or total
attendance. “Qualitative entries” count records in each file's extracted
`text_feedback` list. One response row can contribute multiple entries.

The 88-file population is an operational evidence population, not a literal count
of 88 facilitated sessions. It also contains interaction feedback, `.connect`
records, feedback about Datta, and the JSCPD before/after pair. Establishing a
delivery count would require an additional reviewed `record_kind` classification
and event-level deduplication.

## Excluded Pre-session Surveys

| Survey | Response rows | Qualitative entries | Rating-question aggregates | Rating observations |
|---|---:|---:|---:|---:|
| DORA for Software Leaders — Understanding the audience, 2025-08-21 | 1 | 2 | 1 | 1 |
| GROW 3.0 — Understanding our audience, 2025-08-28 | 132 | 190 | 1 | 130 |
| **Total** | **133** | **192** | **2** | **131** |

These records are useful audience research, but they are not feedback about a
completed event and are not included in post-event category, year, quote, or rating
aggregates.

## Analysis Population by Recorded Year

| Year | Files | Response rows | Qualitative entries | Rating-question aggregates | Rating observations |
|---|---:|---:|---:|---:|---:|
| 2018 | 1 | 9 | 12 | 1 | 9 |
| 2019 | 20 | 291 | 978 | 78 | 898 |
| 2020 | 16 | 289 | 366 | 44 | 361 |
| 2021 | 6 | 29 | 60 | 16 | 69 |
| 2022 | 1 | 7 | 6 | 0 | 0 |
| 2023 | 3 | 14 | 6 | 3 | 5 |
| 2024 | 3 | 34 | 48 | 7 | 74 |
| 2025 | 26 | 268 | 207 | 33 | 323 |
| 2026 | 12 | 109 | 128 | 39 | 410 |
| **Total** | **88** | **1,050** | **1,811** | **221** | **2,149** |

Year is derived from the extracted `date` field. A year count is a count of files
in the analysis population, not unique sessions or people.

## Analysis Population by Filename-derived Category

| Category | Files | Response rows | Qualitative entries | Rating-question aggregates | Rating observations |
|---|---:|---:|---:|---:|---:|
| AI / GenAI | 23 | 288 | 256 | 45 | 560 |
| Before / after | 2 | 22 | 42 | 2 | 12 |
| Code quality | 18 | 319 | 388 | 57 | 615 |
| `.connect` records | 2 | 76 | 424 | 1 | 9 |
| DORA / Continuous Value Delivery | 11 | 79 | 64 | 18 | 116 |
| Feedback about Datta | 9 | 57 | 106 | 23 | 113 |
| Interview / hiring | 9 | 72 | 165 | 33 | 220 |
| Other | 9 | 109 | 334 | 31 | 452 |
| Technical debt | 5 | 28 | 32 | 11 | 52 |
| **Total** | **88** | **1,050** | **1,811** | **221** | **2,149** |

Category is assigned by filename-pattern rules in `categorize_session()`. It has
not been independently hand-coded. In particular, “other” is heterogeneous, and
the file count in any category should not be treated as a count of distinct talks.

## Rating Coverage, Not a Global Score

The analysis population contains:

- 95 question-level aggregates on an inferred 5-point scale, representing 824
  rating observations;
- 126 question-level aggregates on an inferred 10-point scale, representing 1,325
  rating observations;
- 221 question-level aggregates and 2,149 rating observations in total.

No global average rating is reported. The questions cover different constructs,
including effectiveness, recommendation likelihood, familiarity, facilitation,
and other context-specific measures. Dividing 10-point averages by two and then
averaging every question equally produced the prior 4.3/5 figure, but that result
is not a defensible satisfaction measure.

The scale is inferred during extraction from the observed numeric values. A
nominal 10-point question whose observed answers never exceed five could therefore
be misclassified. Question-specific claims should be checked against their wording
and source workbook before publication.

## JSCPD Before/After Pair

The committed extract contains two files grouped by their filenames:

| File | Response rows | Rating-question aggregates | Rating observations |
|---|---:|---:|---:|
| JSCPD Before Elimination | 16 | 0 | 0 |
| JSCPD After Elimination | 6 | 2 | 12 |

The six post-exercise respondents rated:

- session effectiveness at 8.33/10, range 6–10, `n=6`;
- likelihood to recommend Datta for a similar exercise at 8.50/10, range 7–10,
  `n=6`.

The committed extract does not contain matched before/after outcome measures.
These values support reporting post-exercise perceptions; they do **not** establish
that the workshop caused a measurable reduction in code duplication.

## Illustrative Feedback

These excerpts demonstrate both reported value and requests for improvement. They
are examples, not a representative sample or sentiment analysis.

> “I was given the room to think in my own space.”

Source record: New Hire Mentoring feedback, 2019-07-26.

> “More hands-on demos, real project examples, and additional guidance on effective prompting would make it even better.”

Source record: Coding with GitHub CoPilot feedback, 2026-01-28.

> “Expectations check before the meeting.”

Source record: IEC 62304 session feedback, 2025-05-21.

## What This Corpus Supports

With the population boundary and caveats above, the corpus supports these factual
statements:

- professional feedback records span the recorded years 2018–2026;
- the post-event/interaction analysis population contains 88 datasets and 1,050
  response rows;
- AI/GenAI is represented by 23 datasets and 288 post-event response rows;
- code-quality material is represented by 18 datasets and 319 response rows;
- the evidence includes positive feedback and actionable requests concerning
  hands-on practice, audience relevance, depth, pacing, and facilitation.

The corpus alone does not support claims that Datta personally presented every
file represented, that every file is a distinct session, that response rows equal
attendance, or that one aggregate score measures satisfaction across the archive.

## Reproduction

Regenerate the committed summary without the unavailable source-workbook directory:

```bash
.venv/bin/python data/evidence/sessions/process_feedback.py \
  --from-json data/evidence/sessions/all_sessions_data.json \
  --summary-output data/evidence/sessions/summary_stats.json
```

The generated JSON is deterministic for a given committed extract. Focused
regression coverage is in `tests/test_process_feedback.py`.

## Methodology and Limitations

1. Duplicate files are identified during extraction by the duplicate filename
   suffix and excluded first.
2. Among unique files, records flagged `is_pre_session_survey=true` are reported
   separately and excluded from the post-event analysis population.
3. Year and category tables are calculated only from the remaining population.
4. A rating-question aggregate is one entry in a file's `ratings` mapping. Rating
   observations are the sum of each entry's `count` value.
5. A qualitative entry is one item in a file's `text_feedback` list; it is not a
   unique respondent and has not been manually coded or deduplicated.
6. The extractor keeps only a three-row raw-data sample. Aggregate averages cannot
   be independently recalculated at participant level from the committed JSON.
7. Some legacy text extraction includes fields that may be metadata rather than
   qualitative feedback. Publication should use reviewed excerpts, not the raw
   qualitative-entry count as a measure of sentiment.
8. Ratings and quotations reflect voluntary, context-specific feedback and should
   not be described as an unbiased sample of all participants.

## Cross-references

- [Student feedback evidence](student-feedback/STUDENT-FEEDBACK-EVIDENCE.md)
- [Giveback and talks delivery ledger](givebacks-talks-spreadsheet.md)
- `data/evidence/2025/ai-genai-leadership.md`
- `data/evidence/2025/skill-building-philips-university.md`
