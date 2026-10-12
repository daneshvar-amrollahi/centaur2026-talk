"""fig:drift-bars — verification claim visualization.

Slope chart: each Full configuration has a UNSAT marker and a SAT marker
connected by a line. The line and arrow visually encode the drift increase
from UNSAT to SAT pool. The ratio is annotated above each pair.

Four configurations are shown (Full repair, one per domain x model cell):
  Traffic / Claude, Traffic / GPT, Wildlife / Claude, Wildlife / GPT.
"""

from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np

from style_talk import (
    apply_style, save_pdf, NLI_COUNTS, CELL_ORDER,
    VERDICT_COLOR,
)


def _drift_rate(counts):
    drift = counts[4] + counts[5]  # Un + Co
    total = sum(counts)
    return drift, total


def main() -> None:
    apply_style()

    cells = CELL_ORDER
    n = len(cells)

    unsat_rates = []
    sat_rates = []
    ratios = []
    for cell in cells:
        full = NLI_COUNTS[cell]["full"]
        ud, ut = _drift_rate(full["UNSAT"])
        sd, st = _drift_rate(full["SAT"])
        ur = 100.0 * ud / ut
        sr = 100.0 * sd / st
        unsat_rates.append(ur)
        sat_rates.append(sr)
        ratios.append(sr / ur)

    fig, ax = plt.subplots(figsize=(6.6, 3.0))

    x = np.arange(n)

    for i, (u, s) in enumerate(zip(unsat_rates, sat_rates)):
        ax.annotate(
            "", xy=(i, s), xytext=(i, u),
            arrowprops=dict(
                arrowstyle="-|>", color="0.45",
                lw=1.6, mutation_scale=14,
                shrinkA=4, shrinkB=4,
            ),
        )

    ax.scatter(x, unsat_rates,
               s=160, color=VERDICT_COLOR["UNSAT"], zorder=3,
               edgecolor="white", linewidth=1.4, label="UNSAT (formally equivalent)")
    ax.scatter(x, sat_rates,
               s=160, color=VERDICT_COLOR["SAT"], zorder=3,
               edgecolor="white", linewidth=1.4, label="SAT (not equivalent)")

    for i, val in enumerate(unsat_rates):
        ax.text(i - 0.07, val, f"{val:.1f}%",
                ha="right", va="center", fontsize=13,
                color=VERDICT_COLOR["UNSAT"], fontweight="bold")
    for i, val in enumerate(sat_rates):
        ax.text(i + 0.07, val, f"{val:.1f}%",
                ha="left", va="center", fontsize=13,
                color=VERDICT_COLOR["SAT"], fontweight="bold")

    ymax_per_cell = [max(u, s) for u, s in zip(unsat_rates, sat_rates)]
    overall_ymax = max(ymax_per_cell)
    for i, ratio in enumerate(ratios):
        ax.text(i, overall_ymax + 6, f"{ratio:.2f}$\\times$",
                ha="center", va="bottom",
                fontsize=15, color="0.20", fontweight="bold")

    ax.set_xticks(x)
    labels = [c.replace(" / ", "\n") for c in cells]
    ax.set_xticklabels(labels, fontsize=13)
    ax.set_ylabel("Drift rate (%)")
    ax.set_ylim(0, overall_ymax + 14)
    ax.set_xlim(-0.55, n - 0.45)

    ax.axhline(overall_ymax + 4, color="0.85", lw=0.6, ls="-")

    ax.legend(loc="lower right", frameon=False, ncol=1,
              handlelength=0.8, handletextpad=0.5, fontsize=13,
              bbox_to_anchor=(1.0, 0.02))

    ax.tick_params(axis="x", length=0, pad=4)
    ax.tick_params(axis="y", length=3, pad=2)

    plt.tight_layout()
    save_pdf(fig, "drift_bars")


if __name__ == "__main__":
    main()
