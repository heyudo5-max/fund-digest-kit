#!/usr/bin/env python3
"""Aggregate a deals CSV into the core funding-digest metrics.

Usage:
    python scripts/aggregate.py path/to/deals.csv [--prior-total USD] [--json metrics.json]

Reads the schema defined in assets/deals-template.csv. Amounts may be blank
(undisclosed); those rows count toward deal volume but not dollar totals.
Prints a human-readable summary and writes metrics.json.
"""
import argparse
import csv
import json
from collections import Counter, defaultdict


def to_float(value):
    value = (value or "").strip().replace(",", "").replace("$", "")
    try:
        return float(value)
    except ValueError:
        return None


def fmt_usd(n):
    if n is None:
        return "n/a"
    for unit, div in (("B", 1e9), ("M", 1e6), ("K", 1e3)):
        if abs(n) >= div:
            return f"${n/div:.2f}{unit}"
    return f"${n:.0f}"


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def aggregate(rows, prior_total=None):
    funding = [r for r in rows if (r.get("deal_type") or "").strip().lower() == "funding"]
    acquisitions = [r for r in rows if (r.get("deal_type") or "").strip().lower() == "acquisition"]

    amounts = [(r, to_float(r.get("amount_usd"))) for r in funding]
    disclosed = [(r, a) for r, a in amounts if a is not None]
    total = sum(a for _, a in disclosed)
    undisclosed_count = len(funding) - len(disclosed)

    # dollar + count share by stage
    stage_dollars = defaultdict(float)
    stage_counts = Counter()
    for r, a in amounts:
        stage = (r.get("stage") or "Unknown").strip() or "Unknown"
        stage_counts[stage] += 1
        if a is not None:
            stage_dollars[stage] += a

    customer_split = Counter((r.get("customer_type") or "Unknown").strip() or "Unknown" for r in funding)
    sectors = Counter((r.get("sector") or "Unknown").strip() or "Unknown" for r in funding)
    regions_count = Counter((r.get("region") or "Unknown").strip() or "Unknown" for r in funding)
    region_dollars = defaultdict(float)
    country_dollars = defaultdict(float)
    for r, a in disclosed:
        region_dollars[(r.get("region") or "Unknown").strip() or "Unknown"] += a
        country_dollars[(r.get("country") or "Unknown").strip() or "Unknown"] += a

    # Series A-C companies hiring sales / marketing
    def truthy(v):
        return (v or "").strip().lower() in ("y", "yes", "true", "1", "x")
    abc = {"series a", "series b", "series c"}
    hiring = []
    for r in funding:
        if (r.get("stage") or "").strip().lower() in abc:
            s, mk = truthy(r.get("hiring_sales")), truthy(r.get("hiring_marketing"))
            if s or mk:
                roles = ", ".join([x for x in (["Sales"] if s else []) + (["Marketing"] if mk else [])])
                hiring.append({"company": (r.get("company") or "").strip(),
                               "stage": (r.get("stage") or "").strip(), "roles": roles,
                               "careers_url": (r.get("careers_url") or "").strip()})

    growth = None
    if prior_total not in (None, 0):
        growth = (total - prior_total) / prior_total * 100.0

    return {
        "funding_deal_count": len(funding),
        "acquisition_count": len(acquisitions),
        "undisclosed_funding_count": undisclosed_count,
        "total_raised_usd": total,
        "total_raised_human": fmt_usd(total),
        "median_disclosed_usd": sorted(a for _, a in disclosed)[len(disclosed)//2] if disclosed else None,
        "prior_total_usd": prior_total,
        "growth_pct_vs_prior": round(growth, 1) if growth is not None else None,
        "stage_counts": dict(stage_counts.most_common()),
        "stage_dollars": {k: round(v) for k, v in sorted(stage_dollars.items(), key=lambda x: -x[1])},
        "customer_type_split": dict(customer_split.most_common()),
        "top_sectors": dict(sectors.most_common(10)),
        "deals_by_region": dict(regions_count.most_common()),
        "dollars_by_region": {k: round(v) for k, v in sorted(region_dollars.items(), key=lambda x: -x[1])},
        "top_countries_by_dollars": {k: round(v) for k, v in sorted(country_dollars.items(), key=lambda x: -x[1])[:8]},
        "series_abc_hiring_gtm": hiring,
        "series_abc_hiring_count": len(hiring),
    }


def print_summary(m):
    print("\n=== Funding Digest — Metrics Summary ===\n")
    print(f"Funding rounds: {m['funding_deal_count']}  (undisclosed amount: {m['undisclosed_funding_count']})")
    print(f"Acquisitions:   {m['acquisition_count']}")
    print(f"Total raised:   {m['total_raised_human']}", end="")
    if m["growth_pct_vs_prior"] is not None:
        arrow = "up" if m["growth_pct_vs_prior"] >= 0 else "down"
        print(f"  ({arrow} {abs(m['growth_pct_vs_prior'])}% vs prior {fmt_usd(m['prior_total_usd'])})")
    else:
        print()
    if m["median_disclosed_usd"] is not None:
        print(f"Median round:   {fmt_usd(m['median_disclosed_usd'])}")

    print("\nStage — by deal count:")
    for k, v in m["stage_counts"].items():
        print(f"  {k:<14} {v}")
    print("Stage — by dollars:")
    for k, v in m["stage_dollars"].items():
        print(f"  {k:<14} {fmt_usd(v)}")

    print("\nCustomer type:", ", ".join(f"{k} {v}" for k, v in m["customer_type_split"].items()))
    print("Top sectors:  ", ", ".join(f"{k} ({v})" for k, v in m["top_sectors"].items()))
    print("\nDeals by region:", ", ".join(f"{k} {v}" for k, v in m["deals_by_region"].items()))
    print("Top countries by $:")
    for k, v in m["top_countries_by_dollars"].items():
        print(f"  {k:<16} {fmt_usd(v)}")

    print("\nSeries A-C hiring Sales/Marketing:")
    if m["series_abc_hiring_gtm"]:
        for h in m["series_abc_hiring_gtm"]:
            print(f"  {h['company']:<16} {h['stage']:<10} hiring: {h['roles']}")
    else:
        print("  (none captured)")
    print()


def main():
    p = argparse.ArgumentParser(description="Aggregate a deals CSV into funding-digest metrics.")
    p.add_argument("csv_path")
    p.add_argument("--prior-total", type=float, default=None,
                   help="Previous comparable period's total raised (USD) for growth calc.")
    p.add_argument("--json", default="metrics.json", help="Where to write metrics JSON.")
    args = p.parse_args()

    rows = load(args.csv_path)
    metrics = aggregate(rows, prior_total=args.prior_total)
    print_summary(metrics)
    with open(args.json, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    print(f"Wrote {args.json}")


if __name__ == "__main__":
    main()
