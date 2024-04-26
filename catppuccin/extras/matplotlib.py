"""Soothing pastel theme for matplotlib"""

from __future__ import annotations

import json
from pathlib import Path
from typing import cast

import matplotlib as mpl
import matplotlib.colors
import matplotlib.style


def _load_palette_json() -> dict[str, dict[str, dict[str, str]]]:
    # TODO: kill this function and load from actual PALETTE objects.  # noqa: TD002, TD003, FIX002, E501
    with (CATPPUCCIN_STYLE_DIRECTORY / "palettes.json").open() as f:
        return cast(dict[str, dict[str, dict[str, str]]], json.load(f))


CATPPUCCIN_STYLE_DIRECTORY = Path(__file__).parent / "matplotlib_styles"
MPL_PALETTES = _load_palette_json()


def _register_styles() -> None:
    """Register the included stylesheets in the mpl style library."""
    catppuccin_stylesheets = mpl.style.core.read_style_directory(  # type: ignore [attr-defined]
        CATPPUCCIN_STYLE_DIRECTORY
    )
    mpl.style.core.update_nested_dict(mpl.style.library, catppuccin_stylesheets)  # type: ignore [attr-defined]


def _register_colormap_list() -> None:
    """Register the included color maps in the `matplotlib` colormap library."""
    for palette_name in ["latte", "frappe", "macchiato", "mocha"]:
        cmap = get_colormap_from_list(palette_name, ["base", "blue"])
        mpl.colormaps.register(cmap=cmap, name=palette_name)


def get_colormap_from_list(
    palette_name: str, color_names: list[str]
) -> matplotlib.colors.LinearSegmentedColormap:
    """# TODO: add proper description."""
    colors = [load_color(palette_name, color_name) for color_name in color_names]
    return matplotlib.colors.LinearSegmentedColormap.from_list(palette_name, colors)


def load_color(palette_name: str, color_name: str, *, color_format: str = "hex") -> str:
    """# TODO: add proper description."""
    return MPL_PALETTES[palette_name][color_name][color_format]
