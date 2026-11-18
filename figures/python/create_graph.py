"""Generate the Chapter 3 graph: walk-time distribution across an example urban day.

DATA ARE ILLUSTRATIVE (a fictional schedule) — not a veterinary recommendation.
Output: figures/generated/activity_graph.pdf (vector) + .png preview.
Hebrew labels rely on matplotlib>=3.11 native bidi layout (verified; a manual
string-reversal helper was tried first and produced double-reversed text).
Run:    python figures/python/create_graph.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless, deterministic backend
import matplotlib.pyplot as plt
from matplotlib import font_manager



ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "figures" / "generated"

# ---- Explicit illustrative dataset (minutes per walk) -------------------------------
WALKS = [
    # (Hebrew label,   start time, minutes)
    ("טיול בוקר", "07:00", 20),
    ("טיול צהריים", "13:00", 15),
    ("טיול ערב", "18:30", 35),
    ("טיול לילה", "22:30", 10),
]
TOTAL_MINUTES = sum(m for _, _, m in WALKS)  # = 80, used in the Chapter 3 formula example

# ---- Book palette (matches book/preamble.tex) ---------------------------------------
NAVY, CORAL, CHARCOAL, MUTED, PAPER = "#183153", "#E98B73", "#333333", "#8A8F98", "#FFFCF6"
HIGHLIGHT_INDEX = 2  # the longest walk (evening) is emphasised in coral


def hebrew_font() -> font_manager.FontProperties:
    """Prefer Gisha (Hebrew sans used in the book); fall back to Arial / DejaVu."""
    for name in ("Gisha", "Arial", "DejaVu Sans"):
        try:
            path = font_manager.findfont(name, fallback_to_default=False)
            return font_manager.FontProperties(fname=path)
        except ValueError:
            continue
    return font_manager.FontProperties()


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    font = hebrew_font()
    plt.rcParams.update({"pdf.fonttype": 42, "svg.hashsalt": "dogbook",
                         "font.family": font.get_name()})

    labels = [f"{name}\n{start}" for name, start, _ in WALKS]
    minutes = [m for _, _, m in WALKS]
    colors = [CORAL if i == HIGHLIGHT_INDEX else NAVY for i in range(len(WALKS))]

    fig, ax = plt.subplots(figsize=(6.4, 3.3), dpi=150)
    fig.patch.set_facecolor(PAPER)
    ax.set_facecolor(PAPER)

    # x positions are reversed so the day reads right-to-left, like the Hebrew text
    x = list(range(len(WALKS)))[::-1]
    bars = ax.bar(x, minutes, width=0.56, color=colors, edgecolor=PAPER, linewidth=2, zorder=3)

    for bar, value in zip(bars, minutes):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 0.8, f"{value} דק׳",
                ha="center", va="bottom", fontproperties=font, fontsize=11,
                color=CHARCOAL, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontproperties=font, fontsize=10, color=CHARCOAL)
    ax.set_ylabel("משך הטיול (דקות)", fontproperties=font, fontsize=10, color=MUTED)
    ax.set_ylim(0, max(minutes) * 1.25)
    ax.yaxis.grid(True, color="#E4E0D8", linewidth=0.8, zorder=0)
    ax.tick_params(axis="y", colors=MUTED, labelsize=9)
    ax.tick_params(axis="x", length=0)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color("#BDB8AE")

    ax.text(0.99, 0.97, f"סה״כ ביום: {TOTAL_MINUTES} דקות", transform=ax.transAxes,
            ha="right", va="top", fontproperties=font, fontsize=11, color=NAVY,
            fontweight="bold")
    ax.text(0.01, 0.97, "נתונים להמחשה בלבד", transform=ax.transAxes,
            ha="left", va="top", fontproperties=font, fontsize=9, color=MUTED)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "activity_graph.pdf", facecolor=PAPER,
                metadata={"CreationDate": None, "ModDate": None})
    fig.savefig(OUT_DIR / "activity_graph.png", facecolor=PAPER, dpi=200)
    print(f"activity_graph written; total = {TOTAL_MINUTES} min; data = {minutes}")


if __name__ == "__main__":
    main()
