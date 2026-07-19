# Funding Digest Kit

This repo generates a startup funding & acquisitions digest and video script for TikTok, Instagram, and YouTube with one-line prompts, no context re-explaining each session.

## How it works

Claude Code reads `CLAUDE.md` automatically at the start of every session — it holds the audience, tone, sources, and where things live. 

```
Read skills/funding-digest/SKILL.md and produce the weekly digest for the week of June 22–28.
```

Claude captures the week's rounds and acquisitions, aggregates the metrics, derives insights, and writes the script — the context it needs is already in the repo.

## What's inside

```
funding-digest/
│
├── CLAUDE.md                       ← Read every session. Audience, tone, sources, paths.
├── README.md
├── .gitignore
│
├── skills/                         ← Claude executes these. One-line prompts.
│   └── funding-digest/
│       ├── SKILL.md                ← Main workflow: capture data → insights → script
│       └── references/
│           ├── data-capture.md     ← Metrics + search strategy per cadence
│           ├── insights-playbook.md← Insight questions + quality bar
│           └── script-templates.md ← Script structure, platform variants, tone
│
├── assets/
│   ├── funding-digest-workbook.xlsx← PRIMARY: enter deals, metrics auto-calculate
│   └── deals-template.csv          ← Same schema in CSV form (for the Python backup)
│
├── scripts/
│   ├── aggregate.py                ← BACKUP calculator: metrics from a CSV
│   └── make_visuals.py             ← Generates video-ready PNG cards from the deals data
│
└── outputs/                        ← Finished digests, scripts, and visuals/ land here
    └── .gitkeep
```

## Getting started

### 1. Clone and open

```
git clone https://github.com/heyudo5-max/funding-digest
cd funding-digest
claude
```

### 2. Run the digest

```
Read skills/funding-digest/SKILL.md and produce the weekly digest for the previous week.
```

Or monthly / quarterly / annual:

```
Read skills/funding-digest/SKILL.md and do the monthly digest for June 2026.
```

Claude will confirm the exact date window, gather the deals, total them in the workbook, pull out the insights, and save a script to `outputs/`.

## How the math gets done

The **spreadsheet is the primary calculator**. Enter one row per deal on the workbook's Deals tab and the Metrics tab totals everything with live formulas — counts, total and median raised, stage split by deals and dollars, customer-type / sector / region tallies, and growth vs. the prior period. The only cell you type by hand is the yellow *prior-period total*.

The **Python script is a backup** for automated runs or when your data is already a CSV. Same columns as the workbook:

```bash
python scripts/aggregate.py assets/deals-template.csv --prior-total 12000000
```

## Visuals for the video

`scripts/make_visuals.py` turns the same deals data into four PNG cards you can drop straight into an edit — a headline stat card, a funding-by-stage bar, a top-regions bar, and a "who's hiring GTM" card listing the Series A–C companies staffing up Sales & Marketing:

```bash
python scripts/make_visuals.py assets/deals-template.csv \
    --prior-total 12000000 --format vertical --tag "Week of Jun 22-28"
```

`--format` is `vertical` (1080×1920, TikTok/Reels/Shorts), `landscape` (1920×1080, YouTube), or `square`. Cards land in `outputs/visuals/`. Requires `matplotlib` (`pip install matplotlib`).

## What each video includes

Metrics summary → 3–6 sourced insights → a **"who's hiring GTM"** beat naming the Series A–C companies hiring Sales & Marketing → the visual cards, referenced beat-by-beat in the script.

## Requirements

- Python 3.8+ only if you use the backup script (standard library, no installs).

## License

MIT
