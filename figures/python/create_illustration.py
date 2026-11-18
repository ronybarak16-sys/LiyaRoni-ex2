"""Original programmatic illustration for Chapter 2: a *conceptual* neighborhood map.

Everything is built from matplotlib artists (Rectangle, Circle, Ellipse, Polygon,
FancyBboxPatch, Line2D) — no external images. The neighborhood is fictional; it shows
the planning factors discussed in the chapter (shade, water, traffic, quiet streets,
dog park, hot open plaza) and a suggested shaded route.

Output: figures/generated/original_neighborhood_map.png (300 dpi) + .pdf (vector)
Run:    python figures/python/create_illustration.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.lines import Line2D
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon, Rectangle

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "figures" / "generated"

NAVY, CREAM, SAGE, SAGE_DARK = "#183153", "#FFF8ED", "#87A98C", "#4F7656"
CORAL, CORAL_DARK, GOLD, CHARCOAL = "#E98B73", "#B5533B", "#D8B56A", "#333333"
ROAD, ROAD_BUSY, BLOCK, WATER, PAPER = "#E6E1D6", "#C9C3B6", "#EFE6D4", "#5B9BD5", "#FFFCF6"

# Map layout in abstract units (0..100 x 0..60). All positions are explicit.
BLOCKS = [(4, 34, 22, 20), (30, 34, 18, 20), (52, 34, 20, 20), (76, 34, 20, 20),
          (4, 4, 22, 22), (76, 4, 20, 22)]
PARK = (30, 4, 42, 22)            # x, y, w, h — urban park in the lower middle
DOG_PARK = (56, 8, 13, 13)        # fenced dog run inside the park
PLAZA = (52, 34, 20, 20)          # commercial plaza: hot, crowded, little shade
TREE_ROW = [(28, y) for y in range(8, 58, 6)] + [(x, 30) for x in range(8, 74, 6)]
PARK_TREES = [(35, 9), (40, 20), (46, 12), (51, 21), (36, 16)]
FOUNTAINS = [(43, 7.5), (62.5, 23.2)]
ROUTE = [(15, 33.2), (15, 30.2), (27.6, 30.2), (27.6, 24), (34, 24), (34, 14), (55, 14)]


def font(size: float, bold: bool = False) -> font_manager.FontProperties:
    for name in ("Gisha", "Arial", "DejaVu Sans"):
        try:
            path = font_manager.findfont(font_manager.FontProperties(
                family=name, weight="bold" if bold else "normal"), fallback_to_default=False)
            return font_manager.FontProperties(fname=path, size=size)
        except ValueError:
            continue
    return font_manager.FontProperties(size=size)


def draw_tree(ax, x, y, r=1.6):
    ax.add_patch(Circle((x + 0.35, y - 0.35), r, color="#000000", alpha=0.08, lw=0))  # shade
    ax.add_patch(Circle((x, y), r, color=SAGE, lw=0, zorder=4))
    ax.add_patch(Circle((x - 0.45, y + 0.45), r * 0.55, color="#A3C0A7", lw=0, zorder=5))


def draw_dog_marker(ax, x, y, s=1.0):
    """A tiny dog built from ellipses/circles/polygons (same character as the TikZ dog)."""
    z = 9
    ax.add_patch(Ellipse((x, y), 4.0 * s, 1.9 * s, color=GOLD, zorder=z))
    for lx in (-1.3, -0.8, 0.9, 1.4):
        ax.add_patch(Rectangle((x + lx * s - 0.22 * s, y - 2.1 * s), 0.45 * s, 1.5 * s,
                               color="#A9813A" if lx in (-0.8, 1.4) else GOLD, zorder=z - 1))
    ax.add_patch(Circle((x - 2.1 * s, y + 1.3 * s), 0.95 * s, color=GOLD, zorder=z))
    ax.add_patch(Ellipse((x - 3.0 * s, y + 1.0 * s), 1.2 * s, 0.7 * s, color="#F3DFB2", zorder=z))
    ax.add_patch(Circle((x - 3.55 * s, y + 1.15 * s), 0.2 * s, color=CHARCOAL, zorder=z + 1))
    ax.add_patch(Polygon([(x - 1.9 * s, y + 2.1 * s), (x - 1.2 * s, y + 1.9 * s),
                          (x - 1.5 * s, y + 0.6 * s)], color="#A9813A", zorder=z + 1))
    ax.add_line(Line2D([x + 2.0 * s, x + 2.7 * s], [y + 0.3 * s, y + 1.4 * s],
                       color="#A9813A", lw=3, solid_capstyle="round", zorder=z))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"pdf.fonttype": 42})
    fig, ax = plt.subplots(figsize=(7.2, 4.6), dpi=150)
    fig.patch.set_facecolor(PAPER)
    ax.set_xlim(0, 100)
    ax.set_ylim(-9, 60)
    ax.set_aspect("equal")
    ax.axis("off")

    # streets
    ax.add_patch(Rectangle((0, 0), 100, 60, color=ROAD, zorder=0))
    ax.add_patch(Rectangle((72.5, 0), 3.0, 60, color=ROAD_BUSY, zorder=1))   # main road
    for y in range(2, 60, 6):
        ax.add_patch(Rectangle((73.85, y), 0.3, 3, color="white", zorder=2))
    # city blocks
    for x, y, w, h in BLOCKS:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=1.5",
                                    color=BLOCK, zorder=2))
    # hot commercial plaza
    px, py, pw, ph = PLAZA
    ax.add_patch(FancyBboxPatch((px, py), pw, ph, boxstyle="round,pad=0,rounding_size=1.5",
                                color="#F6D9C9", zorder=3))
    # park + dog park fence
    x, y, w, h = PARK
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=2",
                                color="#DCE8D6", zorder=2))
    dx, dy, dw, dh = DOG_PARK
    ax.add_patch(Rectangle((dx, dy), dw, dh, fill=False, ec=SAGE_DARK, lw=1.6, ls=(0, (3, 2)), zorder=6))
    # trees (shade)
    for tx, ty in TREE_ROW + PARK_TREES:
        draw_tree(ax, tx, ty)
    # water fountains
    for fx, fy in FOUNTAINS:
        ax.add_patch(Circle((fx, fy), 1.3, color=WATER, zorder=7))
        ax.add_patch(Circle((fx, fy), 0.5, color="white", zorder=8))
    # cars on the busy road
    for cy in (8, 27, 47):
        ax.add_patch(FancyBboxPatch((73.0, cy), 2.0, 3.6, boxstyle="round,pad=0,rounding_size=0.6",
                                    color=CORAL_DARK, zorder=4))
    # suggested shaded route
    rx, ry = zip(*ROUTE)
    ax.add_line(Line2D(rx, ry, color=NAVY, lw=2.6, ls=(0, (4, 2)), zorder=8,
                       solid_capstyle="round"))
    ax.add_patch(Circle(ROUTE[0], 1.2, color=NAVY, zorder=9))
    draw_dog_marker(ax, 51, 16.6, s=0.75)

    # labels (Hebrew renders natively with matplotlib >= 3.11)
    lab = dict(ha="center", va="center", zorder=10, color=CHARCOAL)
    ax.text(15, 44, "בית", fontproperties=font(10, True), **lab)
    ax.text(62, 44, "כיכר מסחרית:\nחשופה לשמש", fontproperties=font(8.5), **lab)
    ax.text(43, 3.6 - 1.4, "פארק עירוני", fontproperties=font(9, True), color=SAGE_DARK,
            ha="center", va="center", zorder=10)
    ax.text(dx + dw / 2, dy + dh / 2, "גינת\nכלבים", fontproperties=font(8.5, True),
            color=SAGE_DARK, ha="center", va="center", zorder=10)
    ax.text(86, 57.5, "כביש ראשי סואן", fontproperties=font(8.5, True), color=CORAL_DARK,
            ha="center", va="center", zorder=10)
    ax.text(39, 32.4, "רחוב שקט עם עצים", fontproperties=font(8), **lab)

    # legend row (drawn manually, RTL order from right)
    items = [("מסלול מוצל מומלץ", NAVY, "line"), ("ברזייה", WATER, "dot"),
             ("עץ וצל", SAGE, "dot"), ("תנועה כבדה", CORAL_DARK, "box")]
    lx = 97
    for text, color, kind in items:
        if kind == "line":
            ax.add_line(Line2D([lx - 4, lx], [-5.5, -5.5], color=color, lw=2.4, ls=(0, (4, 2))))
        elif kind == "dot":
            ax.add_patch(Circle((lx - 1.5, -5.5), 1.3, color=color))
        else:
            ax.add_patch(Rectangle((lx - 2.6, -6.8), 2.4, 2.6, color=color))
        ax.text(lx - 5.2, -5.5, text, fontproperties=font(8.5), ha="right", va="center", color=CHARCOAL)
        lx -= 25

    fig.tight_layout(pad=0.3)
    fig.savefig(OUT_DIR / "original_neighborhood_map.png", dpi=300, facecolor=PAPER)
    fig.savefig(OUT_DIR / "original_neighborhood_map.pdf", facecolor=PAPER,
                metadata={"CreationDate": None, "ModDate": None})
    print("original_neighborhood_map written")


if __name__ == "__main__":
    main()
