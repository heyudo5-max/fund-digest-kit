# Step 3 — Draft the Video Script

Turn the metrics and insights into a script someone can actually record. Friendly, relaxed, helpful — a sharp friend who watches venture, not a news anchor and not a hype account.

## Default structure

Build the script around the **strongest 2–3 insights**, not a recitation of every number. Numbers are evidence; insights are the story.

```
HOOK (0–3s)        One line that earns the next 5 seconds. A surprising number or a sharp question.  [visual: 01_headline.png]
THE SETUP (3–10s)  What period this covers + the one-sentence headline takeaway.
THE BODY (10–45s)  The 2–3 insights, each: claim → quick proof (a number or named deal) → why it matters to you.  [visual: 02_stage_split.png / 03_regions.png where they support a point]
WHO'S HIRING GTM   The Series A–C companies staffing up Sales & Marketing — name 2–4, say what it signals.  [visual: 04_hiring_gtm.png]
THE TAKEAWAY (~10s) The practical "so if you're building/raising right now..." line.
OUTRO/CTA          Light, relaxed call to follow / come back next [week/month].
```

**Every beat should name the on-screen visual** (in square brackets, as above) so the editor knows what to cut to. The four cards come from `scripts/make_visuals.py`; reference them by filename. If a beat needs a visual that doesn't exist yet, describe it in the cue (e.g. `[visual: text card — "median round: $3M"]`) so it can be made.

**The "who's hiring GTM" beat** is a fixed part of the script now. Pull the named companies from the Series A–C hiring data (workbook Metrics section or `make_visuals` output). Frame it usefully for the audience: for founders it signals which peers are scaling revenue and who's setting the pace; for job-seekers and agencies/vendors it's a live list of where GTM budget is landing. Keep it concrete — "ExampleAI (Series A) and HealthGrid (Series C) are both hiring across sales and marketing" — not "some companies are hiring." If no A–C company shows GTM hiring this period, say so briefly and skip the card; don't manufacture the segment.

Adjust length to platform (below). Always include both **spoken VO lines** and light **[on-screen text / b-roll]** cues so it's production-ready.

## Platform variants

Produce a primary script, then note how to trim/extend for each platform. Same insights, different pacing.

- **TikTok / Instagram Reels** — 30–60s. Fast hook in the first 1–2 seconds (people scroll instantly). Punchy, one idea every few seconds, casual spoken cadence. On-screen text reinforces the spoken numbers. End with a loose, non-corporate CTA.
- **YouTube (Shorts)** — same as above, ~60s.
- **YouTube (standard / long-form)** — 2–5 min. Room to breathe: expand each insight with an example, add a "what this means if you're raising" segment, maybe a quick chart callout. Still relaxed, just less compressed.

## Writing the lines

- **Hook ideas**: lead with the single most surprising thing the data showed. A number ("Seed deals were up but seed dollars dropped — here's what that means"), a contrast, or a myth-bust. Never open with "Hey guys, welcome back."
- **Plain language**: say "early-stage" not "pre-Series-A capital formation." Translate jargon.
- **Show, don't inflate**: cite a real round or number rather than adjectives. "MEGA HUGE WEEK" is weaker than "$4.2B across 38 rounds — up 18% on last week."
- **Talk to one founder**: "you," not "founders should." It reads warmer.
- **Hedge honestly on one week**: "one week isn't a trend, but it's worth watching."
- **Keep the CTA light**: "I do this every [week] — come hang out next time" beats "SMASH that subscribe button."

## Format the output like this

```markdown
# [Cadence] Funding Digest — [date window]
**Platform:** [primary target] · **Est. runtime:** [Xs]

## Script

**[HOOK]**
VO: "..."
[visual: 01_headline.png]

**[SETUP]**
VO: "..."
[on-screen: ...]

... (continue through BODY sections, each with its visual cue) ...

**[WHO'S HIRING GTM]**
VO: "..."
[visual: 04_hiring_gtm.png]

**[TAKEAWAY]**
VO: "..."

**[CTA]**
VO: "..."

---
## Platform notes
- TikTok/Reels: [trim notes]
- YouTube long-form: [expansion notes]

## Sources
- [deal/insight → source]
```

Always end with the **sources list** so claims are traceable. Save the finished script to `script-<cadence>-<date>.md` and present it to the user.

## Worked mini-example (tone reference only)

> **[HOOK]** VO: "Founders raised more money this week — but at way fewer companies. That's the whole story." [on-screen: $4.2B ▲ · deals ▼]
> **[SETUP]** VO: "Quick look at the week of June 22nd in startup land, and one thing jumped out."
> **[BODY]** VO: "Total funding was up about 18%, but almost half of it went into just two mega-rounds. So the headline number looks hot — the median deal? Basically flat. If you're raising a seed right now, the big-number headlines aren't really your market." [visual: 02_stage_split.png]
> **[WHO'S HIRING GTM]** VO: "And here's a useful one to bookmark: two of this week's freshly-funded companies are already loading up on go-to-market. ExampleAI, just off a Series A, is hiring across sales *and* marketing, and HealthGrid at Series C is doing the same. When a company staffs GTM right after a raise, that's them betting the product's ready to sell — worth watching if you're a founder, a candidate, or selling into them." [visual: 04_hiring_gtm.png]

Match that register: specific, calm, genuinely useful.
