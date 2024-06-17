"""Soothing pastel theme for `matplotlib`.

The following code was ported from [catppuccin/matplotlib](https://github.com/catppuccin/matplotlib).
Thanks to [Bram de Wilde](https://github.com/brambozz) for the original source code and
for allowing this port.
"""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Iterable, cast

import matplotlib as mpl
import matplotlib.colors
import matplotlib.style

from catppuccin.palette import PALETTE

CATPPUCCIN_STYLE_DIRECTORY = Path(__file__).parent / "matplotlib_styles"
DEFAULT_COLORMAP_COLORS = ("base", "blue")


def _register_styles() -> None:
    """Register the included stylesheets in the mpl style library."""
    catppuccin_stylesheets = mpl.style.core.read_style_directory(  # type: ignore [attr-defined]
        CATPPUCCIN_STYLE_DIRECTORY
    )
    mpl.style.core.update_nested_dict(mpl.style.library, catppuccin_stylesheets)  # type: ignore [attr-defined]


def _register_colormap_list() -> None:
    """Register the included color maps in the `matplotlib` colormap library."""
    for palette_name in asdict(PALETTE):
        cmap = get_colormap_from_list(palette_name, DEFAULT_COLORMAP_COLORS)
        mpl.colormaps.register(cmap=cmap, name=palette_name)


def get_colormap_from_list(
    palette_name: str,
    color_names: Iterable[str],
) -> matplotlib.colors.LinearSegmentedColormap:
    """Get a `matplotlib` colormap from a list of colors for a specific palette."""
    colors = [load_color(palette_name, color_name) for color_name in color_names]
    return matplotlib.colors.LinearSegmentedColormap.from_list(palette_name, colors)


def load_color(palette_name: str, color_name: str) -> str:
    """Load the color for a given palette and color name."""
    return cast(
        str,
        PALETTE.__getattribute__(palette_name).colors.__getattribute__(color_name).hex,
    )
