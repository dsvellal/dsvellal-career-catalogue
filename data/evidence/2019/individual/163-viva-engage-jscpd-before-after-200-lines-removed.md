# Evidence: Viva Engage — Single JSCPD Pairing Report: ~200 Lines Removed (Oct 2019)

## Source
- **Platform:** Viva Engage (IEN Software Engineering Excellence community)
- **Date:** 2019-10-03 (post) / 2019-10-04 (Datta's reply)
- **Ingested:** 2026-08-05
- **Channel:** internal_snapshot
- **Category:** JSCPD Impact / Before-After Evidence / Technical Debt Reduction
- **Image:** [viva-engage-jscpd-before-after-raja-2019.jpg](../../images/2019/viva-engage-jscpd-before-after-raja-2019.jpg)

## References
- **Type:** Internal (Philips Viva Engage — requires SSO)
- **Captured:** 2026-08-05 (from authenticated screenshot)
- **Status:** Captured (screenshot preserved)
- **Seen by:** 169
- **Internal links (preserved for reference, will die):**
  - Installation guide: https://docs.philips.com/p/r/personal/dsvellal_philips_com/_layouts/15/guestaccess.aspx?...
  - Source archive: https://gitlab.ta.philips.com/Rajeshwar.Raja/simulator
  - Commit ID: ad22ced7

## Post Details

### Original Post
- **Author:** Raja, Rajeshwar
- **Date:** Oct 3, 2019 · @2
- **Seen by:** 169
- **Reactions:** "You and 3 others" (4 total, Datta liked it)
- **Title:** "JavaScript Copy Paste Detector Tool & My Experience"

### Post Content (verbatim)
> I was working on setting up quality gates for a project and I approached Datta for help, he supported me in setting up CodeScene and suggested jscpd tool for reducing technical debt (code duplication).
>
> Datta and I sat together and analyzed the code base with jscpd tool. It took surprisingly less time to setup the tool, for first time use (~15min) and analysis took 10 seconds for 15kloc code base. The report is easy to ready and for the next one hour we removed code duplications.
>
> The installation guide for the tool is available at https://docs.philips.com/p/r/personal/dsvellal_philips_com/_layouts/15/guestaccess.aspx?...
>
> I was a rewarding experience, I was able to **remove ~200 lines of duplicate code in a short time**. Thanks to @SW_COE and Subramanya Vellal, Dattatreya.
>
> Source Archive: https://gitlab.ta.philips.com/Rajeshwar.Raja/simulator
> Commit ID: ad22ced7

### Attachments
1. **jscpd-report-after.html** — duplication report after cleanup
2. **jscpd-report-before.html** — duplication report before cleanup

(Both visible as embedded previews in the post showing graph/chart comparisons)

### Datta's Reply — **Community expert** badge
- **Date:** Oct 4, 2019
- **Content:**
> "Thank you **Raja, Rajeshwar** for piloting this. Very rewarding to see you commit the changes so fast! Very commendable!"

## Datta's Involvement
- **Role at time:** Competency Specialist – Software Excellence, Software Center of Excellence
- **Badge:** **Community expert**
- **Involvement type:** Hands-on pairing + tool recommendation + installation guide author

## Key Quantified Data

| Metric | Value |
|--------|-------|
| **Setup time** | ~15 minutes (first time use) |
| **Analysis time** | 10 seconds for 15,000 LOC |
| **Code removed** | ~200 lines of duplicate code |
| **Time to remove** | ~1 hour (Datta + Rajeshwar pair session) |
| **Codebase** | 15,000 lines of code (simulator project) |
| **Evidence** | Before/after HTML reports + Git commit (ad22ced7) |

## Key Quotes

> "I approached Datta for help, he supported me in setting up CodeScene and suggested jscpd tool"

> "Datta and I **sat together** and analyzed the code base with jscpd tool"

> "I was able to **remove ~200 lines of duplicate code in a short time**. Thanks to @SW_COE and Subramanya Vellal, Dattatreya."

> (Datta) "Very rewarding to see you commit the changes so fast! Very commendable!"

## Key Context
- **Before/After HTML reports attached** — preserved artifacts for this one reported instance
- **Git commit ID provided** — a traceable locator for the reported code changes; the internal repository is not publicly openable
- **Installation guide hosted on Datta's SharePoint** — he created the enablement material
- **15-minute setup** — demonstrates tool accessibility
- **Same Rajeshwar Raja** who later thanked Datta for SonarQube support in 2024
- **"Community expert" badge** on Datta's reply — recognized authority
- **Pattern:** Developer seeks help → Datta pairs with them → Problem solved → Developer publishes publicly → Community benefits

## Leadership Indicators
- Hands-on pairing ("sat together and analyzed")
- Created installation guide hosted on his SharePoint
- Recommended the right tool for the problem (JSCPD for duplication)
- Results shared publicly with before/after proof
- Recognized as "Community expert"
- Developer publicly credits him and SWCoE

## Skills Demonstrated
- JSCPD tool expertise
- Code duplication detection and elimination
- Pair programming / hands-on support
- Technical enablement (installation guides)
- JavaScript/code analysis
- CodeScene recommendation

## Bounded Impact Statement
This is a well-documented single-instance report of JSCPD use:
- **Problem:** Developer needs quality gates for duplication
- **Action:** The author says Datta paired with him and helped set up JSCPD in about 15 minutes
- **Result:** The author reports removing about 200 duplicate lines during roughly one hour of work
- **Evidence:** Preserved before/after HTML reports and an internal Git commit locator
- **Internal visibility:** The captured post records 169 view events, not verified unique people

The other JSCPD records demonstrate additional activity and follow-through, but
this result cannot be multiplied by their count. This instance does not estimate
enterprise-wide code reduction, a typical workshop outcome, or causal impact for
unmatched before/after populations.

## Cross-References
- [[jscpd-code-duplication-initiative]] — Cross-BU JSCPD enablement and reporting (this is one instance)
- [[enterprise-tooling-pi-gate]] — Same Rajeshwar Raja thanked Datta for SonarQube in 2024
- Email: Multiple JSCPD report submissions from developers (2019)
- Session feedback: "JSCPD Before Elimination" and "JSCPD After Elimination" spreadsheets
