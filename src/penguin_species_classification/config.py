from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

ROOT = (
    Path(__file__).resolve().parents[2]
)  # The project root folder [2] is the grandparent folder.
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"

RANDOM_STATE = 42
TEST_SIZE = 0.2

SPECIES_PALETTE = {
    "Adelie": "#E8833A",
    "Chinstrap": "#9B5DE5",
    "Gentoo": "#2A9D8F",
}


def set_style() -> None:
    sns.set_theme(style="whitegrid", context="notebook")
    plt.rcParams["figure.dpi"] = (
        110  # Controls the graph's dots per inch (sharper and larger)
    )
    plt.rcParams["savefig.dpi"] = 200  # High resolution when exporting the image
    plt.rcParams["savefig.bbox"] = (
        "tight"  # Cropping excess white margins when exporting graphics
    )
