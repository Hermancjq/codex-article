"""Official-data accounting; no observations are bundled or invented.

Run: python analyze_official_data.py verified_data.csv --output output/analysis
Input units: turnover in 100 million tonne-km; intensity in kg/tonne-km.
"""
import argparse
import csv
import json
import math
from pathlib import Path
from urllib.parse import urlparse


def logarithmic_mean(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("LMDI requires strictly positive quantities")
    if math.isclose(a, b, rel_tol=1e-12):
        return (a + b) / 2
    return (a - b) / math.log(a / b)


def decompose(q0, q1, i0, i1):
    """Exact additive fuel decomposition in 10,000 tonnes."""
    f0, f1 = 10 * q0 * i0, 10 * q1 * i1
    weight = logarithmic_mean(f1, f0)
    activity = weight * math.log(q1 / q0)
    intensity = weight * math.log(i1 / i0)
    residual = f1 - f0 - activity - intensity
    if not math.isclose(residual, 0.0, abs_tol=1e-8 * max(f0, f1)):
        raise ArithmeticError("Decomposition identity failed")
    return dict(fuel_start_10kt=f0, fuel_end_10kt=f1,
                change_10kt=f1-f0, activity_effect_10kt=activity,
                intensity_effect_10kt=intensity, residual_10kt=residual)


def break_even_intensity_reduction(activity_growth):
    if activity_growth <= -1:
        raise ValueError("Growth must exceed -100%")
    return 1 - 1 / (1 + activity_growth)


def required_intensity_ratio(activity_ratio, fuel_target_ratio=1):
    if activity_ratio <= 0 or fuel_target_ratio <= 0:
        raise ValueError("Ratios must be positive")
    return fuel_target_ratio / activity_ratio


def read_verified(path):
    rows = list(csv.DictReader(Path(path).open(encoding="utf-8-sig")))
    if not rows:
        raise ValueError("No official observations supplied; empirical analysis was NOT run")
    output = []
    for row in rows:
        if row.get("verification_status") != "verified":
            raise ValueError("Every observation requires source verification")
        if row.get("scope_match") != "true":
            raise ValueError("Turnover and intensity must have explicitly matched coverage")
        for key in ("turnover_source_url", "intensity_source_url"):
            host = urlparse(row.get(key, "")).hostname or ""
            if not any(host == h or host.endswith("." + h)
                       for h in ("caac.gov.cn", "stats.gov.cn")):
                raise ValueError("Expected an official CAAC/NBS source URL")
        for key in ("turnover_source_sha256", "intensity_source_sha256"):
            digest = row.get(key, "")
            if len(digest) != 64 or any(x not in "0123456789abcdef" for x in digest):
                raise ValueError("Source-file SHA-256 required")
        for key in ("turnover_locator", "intensity_locator", "coverage_definition"):
            if not row.get(key, "").strip():
                raise ValueError("Source locator and statistical coverage are required")
        year = int(row["year"])
        q, intensity = float(row["turnover_100m_tkm"]), float(row["fuel_intensity_kg_tkm"])
        if not (math.isfinite(q) and math.isfinite(intensity) and q > 0 and intensity > 0):
            raise ValueError("Nonpositive or nonfinite official input")
        output.append(dict(year=year, q=q, i=intensity))
    output.sort(key=lambda r: r["year"])
    if len({r["year"] for r in output}) != len(output):
        raise ValueError("Duplicate years require reconciliation")
    return output


def analyze(rows):
    intervals = []
    for a, b in zip(rows, rows[1:]):
        if b["year"] - a["year"] != 1:
            continue  # Never label a multi-year gap as a one-year observation.
        d = decompose(a["q"], b["q"], a["i"], b["i"])
        gq = b["q"] / a["q"] - 1
        gi = b["i"] / a["i"] - 1
        gf = d["fuel_end_10kt"] / d["fuel_start_10kt"] - 1
        elasticity = math.log1p(gf) / math.log1p(gq) if abs(gq) > 1e-10 else None
        intervals.append(dict(start=a["year"], end=b["year"], **d,
                              activity_growth=gq, intensity_growth=gi,
                              fuel_growth=gf, fuel_activity_log_elasticity=elasticity,
                              break_even_intensity_reduction=break_even_intensity_reduction(gq),
                              pandemic_transition=bool({a["year"], b["year"]} & {2020, 2021, 2022})))
    if not intervals:
        raise ValueError("No consecutive-year interval available")
    return dict(status="official-input accounting completed", observations=len(rows),
                period=[rows[0]["year"], rows[-1]["year"]], intervals=intervals,
                boundaries=["Fuel is reconstructed from matched-scope turnover and intensity; it is not an independent observation.",
                            "No causal engine-technology effect is identified.",
                            "No CO2 emission factor or lifecycle claim is assumed.",
                            "Source verification is human/analyst work; schema validation alone cannot verify authenticity."])


def self_check():
    # Deliberately synthetic arithmetic examples, never empirical observations.
    assert logarithmic_mean(5, 5) == 5
    d = decompose(10, 12, .3, .25)
    assert abs(d["change_10kt"]) < 1e-10
    assert abs(d["activity_effect_10kt"] + d["intensity_effect_10kt"]) < 1e-10
    d = decompose(10, 10, .3, .27)
    assert abs(d["activity_effect_10kt"]) < 1e-10
    assert math.isclose(d["change_10kt"], -3)
    assert math.isclose(break_even_intensity_reduction(.1), 1 / 11)
    assert math.isclose(required_intensity_ratio(2, .8), .4)
    print("Seven synthetic arithmetic checks passed; no empirical analysis was performed.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?")
    parser.add_argument("--output", default="output/analysis")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return
    if not args.input:
        parser.error("Supply verified official data, or --self-check")
    result = analyze(read_verified(args.input))
    target = Path(args.output)
    target.mkdir(parents=True, exist_ok=True)
    (target / "accounting_results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    with (target / "decomposition.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=result["intervals"][0].keys())
        writer.writeheader()
        writer.writerows(result["intervals"])
    print(f"Accounted for {result['observations']} source-verified annual observations.")


if __name__ == "__main__":
    main()
