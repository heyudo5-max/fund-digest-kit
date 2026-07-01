# Step 1 — Capture Data

Goal: assemble a complete, de-duplicated list of the period's funding rounds and acquisitions, then aggregate them into the core metrics. Record each deal as you research — preferably in the **Deals tab of `assets/funding-digest-workbook.xlsx`**, which auto-calculates the metrics. (`assets/deals-template.csv` is the same schema in plain CSV form, for the Python backup path or bulk import.)

## The core metrics (all cadences)

Every cadence reports the same six things. The difference is framing: **weekly = snapshot**, **monthly/quarterly/annual = trend**, where you compare against prior periods and call out direction (up/down/flat) and momentum.

1. **How many startups / deals?** Count funding rounds and acquisitions separately. Note how many rounds had undisclosed amounts.

2. **Themes — what kind of companies?**
   - **Customer type**: B2B / B2C / B2G / B2B2C. Tag each deal.
   - **Industry & sub-segment**: e.g. fintech → payments infra; healthcare → clinical AI; climate → grid software. Be specific; "AI" alone is not a segment — pair it with the domain it's applied to (AI + legal, AI + bio, AI + devtools).
   - **Use case**: the actual job the product does (e.g. "automates SOC2 evidence collection," "AI scribe for clinicians"). This is what makes the digest feel concrete.

3. **Aggregate total funding** raised across all disclosed rounds in the window (USD). This is the money *into startups*.

4. **Stage / bracket split**: distribution across pre-seed, seed, Series A, B, C, growth/late, and "other" (debt, grants, undisclosed). Report both **count share** (how many deals at each stage) and **dollar share** (how much money at each stage) — they tell different stories. A week can be lots of seed deals but most dollars in one mega-round.

5. **Top countries by region**: group by region (North America, Europe, India/South Asia, MENA, LATAM, SEA, East Asia, Africa, ANZ) then name top countries within. The US will usually dominate dollars — acknowledge it briefly, then highlight notable non-US activity so the digest has range.

6. **Total VC capital deployed + period-over-period growth**: the same dollar pool as #3 viewed from the investor side, plus the trend vs. the previous comparable period (week-over-week for weekly, month-over-month for monthly, etc.). Report the % change and whether it's rising or cooling. *(Note: items 3 and 6 measure the same underlying dollars; #3 is the static total, #6 adds the growth comparison. Don't double-count them as separate findings.)*

## Cadence-specific emphasis

- **Weekly** — Snapshot. Lead with the standout rounds and the week's flavor. Growth = week-over-week. Keep it punchy; one week rarely establishes a trend, so frame surprises as "this week" not "the new normal."
- **Monthly** — First real trend signal. Compare to the prior 1–2 months. Call out stages or sectors that are heating up or cooling.
- **Quarterly** — Strong trend view. Compare to prior quarter and the year-ago quarter. Good place for "the quarter in three storylines."
- **Annual** — Big-picture. Year-over-year shifts, what rose and fell, and a forward-looking "what to watch." Reference quarterly arcs within the year.

## Search strategy

Work the sources systematically rather than one big query:

1. **Breadth pass** — FinSMEs and Crunchbase News for the window to capture as many rounds as possible. Search by date range; page through.
2. **Depth pass** — TechCrunch / Axios / Tech.eu for the larger or more notable rounds to get context and investor names.
3. **Regional pass** — at least one region-specific source (EU-Startups, Inc42, regional outlets) so non-US activity isn't undercounted.
4. **Primary verification** — for any deal that will anchor a headline claim, open the company's or lead investor's own announcement and confirm amount + stage.
5. **Acquisitions pass** — search M&A / acquisition news for the window separately.

For each deal, capture a row in the workbook's Deals tab (or the CSV). Aim for completeness on the big rounds and a representative sample of the long tail — you don't need every $200K pre-seed, but you do need enough to characterize stage and sector mix honestly.

## Honesty about coverage

Public sources don't capture every round, and many seed deals are announced weeks late. State this briefly when relevant ("based on publicly announced rounds this week"). It keeps the digest credible and stops you from over-claiming precision.
