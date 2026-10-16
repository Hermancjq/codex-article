"""Reproducible manuscript figures from verified accounting and exact thresholds.

Figure 3 is an explicitly hypothetical conditional stress test. Its numerical
curves are not observations, calibrated forecasts, probabilities or policy targets.
Figures 1 and 2 preserve all annual observations and the specified stages.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parents[1]
WORK = BASE / "figure_work"
OUT = BASE / "output" / "figures"
os.environ.setdefault("MPLCONFIGDIR", str(WORK / "matplotlib_cache"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np
import pandas as pd

sys.path.insert(0, str(WORK / "skill_assets"))
sys.path.insert(0, str(BASE / "models"))
from audit_panel_alignment import require_matplotlib_panel_alignment
from transition_models import required_deployment_rate

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Arial", "Liberation Sans"],
    "font.size": 8,
    "axes.labelsize": 8,
    "axes.titlesize": 9,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    "axes.linewidth": 0.65,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "xtick.major.size": 3,
    "ytick.major.size": 3,
    "pdf.fonttype": 42,
    "svg.fonttype": "none",
    "savefig.facecolor": "white",
})

WIDTH = 183 / 25.4
BLUE = "#27719B"
GREEN = "#287B65"
OCHRE = "#B37724"
INK = "#282D32"
GRAY = "#6E7378"
PALE = "#EEEEEE"


def clean_axes(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_axisbelow(True)
    ax.grid(axis="y", color="#E7E7E7", linewidth=0.45)
    ax.tick_params(colors=INK)


def export(fig, stem):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.canvas.draw()
    fig.savefig(OUT / f"{stem}.pdf")
    fig.savefig(OUT / f"{stem}.svg")
    fig.savefig(OUT / f"{stem}.png", dpi=300)
    plt.close(fig)


def historical_figure():
    data = pd.read_csv(BASE / "output" / "analysis" / "annual.csv")
    assert data.year.tolist() == list(range(2015, 2026))
    assert np.all(np.isfinite(data.select_dtypes("number")))
    assert np.allclose(data.implied_fuel_mt,
                       data.turnover_100m_tkm * data.fuel_intensity_kg_tkm / 10)
    columns = ["year", "turnover_100m_tkm", "fuel_intensity_kg_tkm",
               "implied_fuel_mt", "activity_index", "intensity_index", "fuel_index"]
    data[columns].to_csv(OUT / "figure1_source_data.csv", index=False)
    fig, ax = plt.subplots(figsize=(WIDTH, 3.6))
    fig.subplots_adjust(left=0.11, right=0.97, bottom=0.28, top=0.78)
    clean_axes(ax)
    ax.axvspan(2019.5, 2022.5, facecolor=PALE, zorder=0)
    ax.axvline(2017, color=GRAY, linewidth=0.8, linestyle=(0, (2, 2)), zorder=1)
    for column, label, color, style, marker in [
        ("activity_index", "Transport activity Q (official)", BLUE, "-", "o"),
        ("intensity_index", "Fuel intensity I (official)", GREEN, "--", "s"),
        ("fuel_index", "Fuel quantity Q × I (reconstructed)", OCHRE, "-.", "^"),
    ]:
        ax.plot(data.year, data[column], color=color, linestyle=style,
                marker=marker, markersize=3.1, linewidth=1.6, label=label)
    ax.set(xlim=(2014.8, 2025.2), ylim=(50, 210),
           xlabel="Year", ylabel="Index (2015 = 100)")
    ax.set_xticks(list(range(2015, 2026)))
    ax.set_yticks([60, 80, 100, 120, 140, 160, 180, 200])
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.025), ncol=1,
              frameon=False, borderaxespad=0, handlelength=3,
              labelspacing=0.65)
    fig.text(0.11, 0.045,
             "CAAC annual bulletins; fuel is reconstructed from rounded Q and I.\n"
             "Grey: 2020–2022; vertical dashed line: 2017 reporting-programme change.",
             fontsize=7, ha="left", va="bottom", color=GRAY, linespacing=1.6)
    export(fig, "figure1_historical_indices")


def decomposition_figure():
    data = pd.read_csv(BASE / "output" / "analysis" / "periods.csv")
    stages = [(2017, 2019), (2019, 2022), (2022, 2025)]
    selected = []
    for start, end in stages:
        row = data[(data.start == start) & (data.end == end)]
        if len(row) != 1:
            raise ValueError(f"Expected one frozen decomposition for {start}–{end}")
        row = row.iloc[0]
        selected.append({
            "start": start, "end": end,
            "chain_activity_effect_mt": row.chain_activity_effect_10kt / 100,
            "chain_intensity_effect_mt": row.chain_intensity_effect_10kt / 100,
            "net_reconstructed_fuel_change_mt": row.change_10kt / 100,
        })
    source = pd.DataFrame(selected)
    assert np.allclose(source.chain_activity_effect_mt + source.chain_intensity_effect_mt,
                       source.net_reconstructed_fuel_change_mt, atol=1e-8)
    source.to_csv(OUT / "figure2_source_data.csv", index=False)
    fig, ax = plt.subplots(figsize=(WIDTH, 3.25))
    fig.subplots_adjust(left=0.11, right=0.97, bottom=0.24, top=0.82)
    clean_axes(ax)
    x = np.arange(3)
    ax.axhline(0, color=GRAY, linewidth=0.65, zorder=2)
    ax.bar(x - 0.17, source.chain_activity_effect_mt, width=0.30,
           color=BLUE, label="Activity effect", zorder=3)
    ax.bar(x + 0.17, source.chain_intensity_effect_mt, width=0.30,
           color=GREEN, label="Intensity effect", zorder=3)
    ax.plot(x, source.net_reconstructed_fuel_change_mt, linestyle="none", marker="D",
            markersize=5, color=INK, label="Net fuel change", zorder=4)
    ax.set(xlim=(-0.6, 2.6), ylabel="Reconstructed fuel change (Mt)")
    ax.set_xticks(x, [f"{a}–{b}" for a, b in stages])
    vals = source.iloc[:, 2:].to_numpy().ravel()
    pad = (vals.max() - vals.min()) * 0.15
    ax.set_ylim(min(0, vals.min()) - pad, max(0, vals.max()) + pad)
    handles, labels = ax.get_legend_handles_labels()
    order = [labels.index(name) for name in ["Activity effect", "Intensity effect", "Net fuel change"]]
    ax.legend([handles[i] for i in order], [labels[i] for i in order],
              loc="lower left", bbox_to_anchor=(0, 1.04), ncol=3,
              frameon=False, borderaxespad=0, handlelength=2.3, columnspacing=2)
    fig.text(0.11, 0.07,
             "Chain-linked annual LMDI contributions; net change = activity effect + intensity effect.\n"
             "2017–2025 is the primary window; 1 Mt = 100 units of 10,000 tonnes.",
             fontsize=7, ha="left", va="bottom", color=GRAY, linespacing=1.6)
    export(fig, "figure2_chain_lmdi")


def conditional_figure():
    horizon = 15
    growth = np.linspace(0.02, 0.06, 161)
    improvement = [0.0, 0.01, 0.02]
    full_adoption = []
    curves = []
    for efficiency in improvement:
        g = np.log1p(growth)
        b = -np.log1p(-efficiency)
        required = np.maximum(0.0, 1.0 - np.exp(-(g - b) * horizon))
        curves.append(required)
        for a, theta in zip(growth, required):
            full_adoption.append({"panel": "a", "horizon_years": horizon,
                                  "annual_activity_growth": a,
                                  "annual_baseline_intensity_improvement": efficiency,
                                  "minimum_full_adoption_benefit": theta,
                                  "evidence_type": "conditional_analytic_stress_test"})
    pd.DataFrame(full_adoption).to_csv(OUT / "figure3a_source_data.csv", index=False)
    delay = np.linspace(0, 10, 101)
    thresholds = []
    for tau in delay:
        r = required_deployment_rate(horizon, float(np.log1p(0.02)),
                                     float(-np.log1p(-0.01)), 0.20, float(tau))
        assert r["status"] == "deployment_threshold_exists"
        thresholds.append({"delay_years": tau, "horizon_years": horizon,
                           "annual_activity_growth": 0.02,
                           "annual_baseline_intensity_improvement": 0.01,
                           "technical_benefit": 0.20,
                           "required_annual_deployment_rate": r["required_r"],
                           "required_fuel_weighted_adoption_share": r["required_share"],
                           "exploratory_deployment_rate_ceiling": 0.12,
                           "evidence_type": "conditional_analytic_stress_test"})
    panelb = pd.DataFrame(thresholds)
    panelb.to_csv(OUT / "figure3b_source_data.csv", index=False)
    assert np.all(np.diff(panelb.required_annual_deployment_rate) > 0)
    fig, axes = plt.subplots(1, 2, figsize=(WIDTH, 4.0))
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.32, top=0.80, wspace=0.34)
    for ax in axes:
        clean_axes(ax)
    a, b = axes
    a.axhspan(10, 30, facecolor=PALE, zorder=0)
    for y, efficiency, color, style in zip(curves, improvement,
                                          [BLUE, OCHRE, GREEN], ["-", "--", "-."]):
        a.plot(100 * growth, 100 * y, color=color, linewidth=1.7, linestyle=style,
               label=f"Baseline improvement {efficiency:.0%}/year")
    a.set(xlim=(2, 6), ylim=(0, 65), xlabel="Annual activity growth (%)",
          ylabel="Minimum full-adoption benefit (%)")
    a.set_xticks([2, 3, 4, 5, 6])
    a.set_yticks([0, 10, 20, 30, 40, 50, 60])
    a.legend(loc="lower left", bbox_to_anchor=(0, 1.07), frameon=False,
             borderaxespad=0, handlelength=2.6, labelspacing=0.65)
    b.plot(delay, 100 * panelb.required_annual_deployment_rate, color=BLUE,
           linewidth=1.9, label="Required deployment rate")
    b.axhline(12, color=OCHRE, linestyle="--", linewidth=1.3,
              label="Exploratory ceiling: 12%/year")
    b.set(xlim=(0, 10), ylim=(0, 25), xlabel="Deployment delay (years)",
          ylabel="Required annual deployment rate (%)")
    b.set_xticks([0, 2, 4, 6, 8, 10])
    b.set_yticks([0, 5, 10, 15, 20, 25])
    b.legend(loc="lower left", bbox_to_anchor=(0, 1.07), frameon=False,
             borderaxespad=0, handlelength=2.6, labelspacing=0.65)
    for ax, letter in zip(axes, ["a", "b"]):
        ax.annotate(letter, xy=(0, 1), xycoords="axes fraction",
                    xytext=(-25, 34), textcoords="offset points", fontsize=9,
                    fontweight="bold", ha="left", va="bottom")
    fig.text(0.085, 0.04,
             "Conditional stress test, H = 15 years (2025–2040); no China calibration or official forecast.\n"
             "a  Grey band: assumed 10–30% technical benefit. b  Fixed growth 2%/year, baseline improvement 1%/year, benefit 20%.\n"
             "Activity growth and baseline improvement are ordinary annual rates, converted to continuous log rates in the model.",
             fontsize=7, ha="left", va="bottom", color=GRAY, linespacing=1.7)
    fig.canvas.draw()
    alignment = require_matplotlib_panel_alignment(
        fig, json_out=OUT / "figure3_deployment_thresholds.alignment.json",
        overlay_svg=OUT / "figure3_deployment_thresholds.alignment.svg",
        tolerance_pt=1.5, gutter_tolerance_pt=1.5,
        require_panel_labels=True, strict=True,
    )
    assert alignment["verdict"] == "PASS"
    export(fig, "figure3_deployment_thresholds")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", choices=["all", "conditional", "historical"], default="all")
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    if args.only in {"all", "conditional"}:
        conditional_figure()
    if args.only in {"all", "historical"}:
        historical_figure()
        decomposition_figure()


if __name__ == "__main__":
    main()
