# Funding Digest 

Claude Code reads this file automatically at the start of every session, so the context below is always available without re-explaining it.

## What this repo is for

Producing a recurring funding & acquisitions digest and turning it into a short-form video script for TikTok, Instagram, and YouTube. The audience is startup founders (building, raising, or eyeing an exit) and people who follow the VC space.

## How to run it

Skills live under `skills/<name>/`. Invoke one by pointing at its file, e.g.:

```
Read skills/funding-digest/SKILL.md and produce the weekly digest for the week of [dates].
```

`skills/funding-digest/SKILL.md` is the main workflow: capture data → gather insights → draft script. It pulls in its own reference files and uses the shared tooling below.

## Shared resources 

- `assets/funding-digest-workbook.xlsx` — **primary** metrics calculator. Enter deals on the Deals tab; the Metrics tab auto-totals everything. Only the yellow *prior-period total* cell is typed by hand.
- `assets/deals-template.csv` — same schema in CSV form (for the Python backup path).
- `scripts/aggregate.py` — **backup** calculator; computes the same metrics from a CSV.
- `outputs/` — where finished digests and scripts are saved (`outputs/script-<cadence>-<date>.md`).

## House style (applies to every script)

Friendly, relaxed, helpful — a knowledgeable friend who watches venture, not a news anchor and not a hype account. Confident, not breathless. No fake urgency, no jargon dumps; always explain the "so what" for a founder in plain language. Favor specific, sourced claims ("three of the five biggest rounds were applied-AI in regulated industries") over broad ones ("AI is hot").

## Data integrity rules

- Reputable sources only (FinSMEs, TechCrunch, company/investor announcements, LinkedIn, Crunchbase News, regional outlets). Keep a source against every deal.
- De-duplicate rounds across outlets; count each once. Keep funding rounds and acquisitions in separate buckets.
- Never fabricate numbers. Undisclosed rounds count toward deal volume, not dollar totals.
- The US usually dominates dollars — acknowledge briefly, then surface notable non-US activity.

## What not to commit

Dated working files (`deals-*.xlsx`, `deals-*.csv`), generated `metrics.json`, and finished scripts are ignored by git — see `.gitignore`. The templates in `assets/` are committed; your weekly working copies are not.
