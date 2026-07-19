
# Skill: Funding Digest

Turn a period's startup funding rounds and acquisitions into (1) clean aggregated metrics, (2) a short list of genuinely useful insights, and (3) a ready-to-record video script in a friendly, relaxed, helpful tone.

The audience is **startup founders** (building, raising, or eyeing an exit) and **people who follow the VC space**. Everything you produce should pass the test: *would a founder find this specific and useful, or is it filler?*

---

## Quick Start

```
Read skills/funding-digest/SKILL.md and produce the weekly digest for last week or for monthly/quarterly/annual 

Read skills/funding-digest/SKILL.md and do the monthly digest for June 2026.
```

That's it. Claude will research and aggregate insights on funding activity and create a video script.

---

## When to run this skill
- Sharing a period round-up of recent VC activity

---
## Workflow and inputs 

Run three steps in order. Don't skip the data step and jump to a script — the script is only as good as the aggregation behind it.

1. **Capture data** → see `skills/funding-digest/references/data-capture.md`
2. **Gather insights** → see `skills/funding-digest/references/insights-playbook.md`
3. **Draft the script** → see `skills/funding-digest/references/script-templates.md`

Read each reference file when you reach that step rather than all upfront. 

---


## Step 0: Confirm the cadence and window

Before researching, lock down:

- **Cadence**: weekly, monthly, quarterly, or annual. Each captures the same core metrics; monthly/quarterly/annual additionally emphasize *trends over time* rather than a single snapshot.
- **Exact date window**: e.g. "the week of June 22–28, 2026." Always resolve relative phrases ("last week," "this month") to concrete dates using today's date, and state the window back to the user.
- **Geographic scope**: global by default. The US will almost always dominate by dollars — note it, but actively surface what's happening elsewhere (Europe, India, MENA, LATAM, SEA, Africa) so the digest isn't just "US raised a lot again."
- **Prior-period baseline**: to report period-over-period growth you need the previous period's totals. If you produced a digest last period, reuse those numbers; otherwise estimate the prior total from the same sources and label it an estimate.

If the user hasn't said which cadence, ask once — it changes the framing.

## Sourcing rules

Pull from reputable, primary-leaning sources and always keep a citation against each deal:

- **FinSMEs** (https://www.finsmes.com) — high-volume, structured round announcements; excellent for breadth.
- **TechCrunch** (https://techcrunch.com) — larger rounds, context, and narrative.
- **Company and investor announcements** — the primary source; a startup's or VC's own post is the ground truth for amount, stage, and investors.
- **LinkedIn** — founder/VC posts often surface rounds and hiring signals before press.
- Other acceptable aggregators: Crunchbase News, PitchBook coverage, Axios Pro Rata, EU-Startups, Tech.eu, Inc42 (India), regional outlets.

Guidelines:
- **Verify amount and stage against the primary announcement** when a deal anchors a major claim. Aggregators sometimes mislabel stage or round size.
- **De-duplicate**: the same round appears across multiple outlets. Count it once.
- **Distinguish funding rounds from acquisitions** — keep them in separate buckets; an exit is a different story than a raise.
- **Don't fabricate**. If you can't find a number, say "not disclosed" rather than guessing. Undisclosed rounds still count toward deal volume but not toward dollar totals.
- **For every Series A, B, and C round, check hiring.** Look at the company's careers page and LinkedIn jobs for open **sales** and **marketing** roles, and mark `hiring_sales` / `hiring_marketing` = `Y` in the row (with the `careers_url`). A just-funded A–C company staffing up GTM is a strong "scaling revenue" signal and feeds a dedicated segment of the video. Don't guess — only mark `Y` if you actually see relevant open roles.
- Record everything in the workbook's Deals tab (`assets/funding-digest-workbook.xlsx`) as you go, or the CSV (`assets/deals-template.csv`) if using the backup path.

## Quantifying the metrics

**Primary path — the spreadsheet.** Capture deals in `assets/funding-digest-workbook.xlsx` (the "Deals" tab), and the "Metrics" tab computes everything automatically with live formulas: deal and acquisition counts, total and median raised, stage split (deals *and* dollars), B2B/B2C/B2G split, sector and region tallies, and period-over-period growth. The only cell anyone types into by hand is the yellow **prior-period total** on the Metrics tab, which drives the growth number. Copy a fresh workbook for each period so history is preserved.

Do it like this:
1. Copy the template to a dated file (e.g. `deals-2026-06-28.xlsx`).
2. Enter one row per deal on the Deals tab, matching the column headers. Leave `amount_usd` blank for undisclosed rounds — they still count toward deal volume.
3. Type last period's total into the yellow cell so growth calculates.
4. Read the Metrics tab. Those are the numbers you carry into the insights and script.

If you're working in an environment where the formulas don't auto-recalculate after edits (some headless/automated setups), recalculate with the xlsx tooling — e.g. `python /path/to/xlsx/scripts/recalc.py deals-2026-06-28.xlsx` — or just open and save the file in Excel/Google Sheets/LibreOffice once, which forces a recalc.

**Backup path — the Python script.** If a spreadsheet isn't convenient (e.g. a fully automated run, or the data is already a CSV), `scripts/aggregate.py` computes the same metrics from a CSV:

```bash
python scripts/aggregate.py path/to/deals.csv --prior-total <previous_period_total_usd>
```

It prints a summary and writes `metrics.json`. The workbook and the script use the same column schema, so a CSV exported from the Deals tab works directly.

**Quick read.** For a handful of deals where the user just wants a fast take, it's fine to total them up directly in your reply — but state the numbers as approximate, and never invent precision the underlying data doesn't support. For anything that will be published on a regular cadence, use the spreadsheet so the numbers are consistent and checkable.

## Generating visuals for the video

Produce ready-to-drop graphics from the same data so the script isn't just talking-head. Run:

```bash
python scripts/make_visuals.py assets/deals-template.csv \
    --prior-total <previous_period_total_usd> \
    --format vertical --tag "Week of Jun 22-28, 2026" --out outputs/visuals
```

Point it at your dated deals file (`.csv` or `.xlsx` — it reads the Deals tab). It writes four PNG cards to `outputs/visuals/`:

- `01_headline.png` — total raised, deal count, growth arrow (the hook visual)
- `02_stage_split.png` — funding by stage bar
- `03_regions.png` — top regions by dollars bar
- `04_hiring_gtm.png` — the Series A–C companies hiring Sales & Marketing

`--format` accepts `vertical` (1080×1920, for TikTok/Reels/Shorts — the default), `landscape` (1920×1080, for YouTube), or `square`. Generate whichever the target platform needs; for a multi-platform post, run it twice (vertical + landscape). In the script, reference each card at the beat where it appears so the editor knows what goes on screen (the script template shows how). If the user wants a look not covered here — a different chart, a branded template, an animated build — offer to extend the script or hand off to a design tool; don't force everything into these four cards.

## Output

By default, deliver in this order in your reply:
1. A short **metrics summary** (the headline numbers, plus the Series A–C companies hiring Sales/Marketing).
2. **3–6 insights**, each with a one-line "why it matters" and its source(s).
3. The **video script**, formatted per `skills/funding-digest/references/script-templates.md` — including the "who's hiring GTM" beat and on-screen references to the generated visuals.
4. The **visuals** in `outputs/visuals/`.

Save the script to a dated file in `outputs/` (e.g. `outputs/script-<cadence>-<date>.md`) and present it alongside the visuals. Keep the chat summary tight; the script and visuals are the deliverables.

## Tone reminder

Friendly, relaxed, helpful — like a knowledgeable friend who watches this space, not a news anchor and not a hype account. Confident but not breathless. No "🚨 BREAKING," no fake urgency, no jargon dumps. Explain the "so what" for a founder in plain language.
