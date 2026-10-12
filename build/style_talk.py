import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "paper/figures-src"))
import matplotlib as mpl
import style as _s
from style import *  # noqa
_s.OUT_DIR = ROOT / "assets/fig"

def apply_style():
    _s.apply_style()
    mpl.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "Times", "Nimbus Roman", "DejaVu Serif"],
        "font.size": 13, "axes.labelsize": 14,
        "xtick.labelsize": 13, "ytick.labelsize": 13, "legend.fontsize": 13,
        "mathtext.fontset": "stix",
    })
