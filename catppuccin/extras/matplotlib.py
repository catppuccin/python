"""Soothing pastel theme for `matplotlib`.

The following code was ported from [catppuccin/matplotlib](https://github.com/catppuccin/matplotlib).
Thanks to [Bram de Wilde](https://github.com/brambozz) for the original source code and
for allowing this port.

The library tries to register styles and colormaps if `matplotlib` is installed.
See the examples below for some use cases:

1. Load a style, using `mpl.style.use`

   ```python
   import catppuccin
   import matplotlib as mpl
   import matplotlib.pyplot as plt

   mpl.style.use(catppuccin.PALETTE.mocha.identifier)
   plt.plot([0,1,2,3], [1,2,3,4])
   plt.show()
   ```

1. Mix it with different stylesheets!

   ```python
   import catppuccin
   import matplotlib as mpl
   import matplotlib.pyplot as plt

   mpl.style.use(["ggplot", catppuccin.PALETTE.mocha.identifier])
   plt.plot([0,1,2,3], [1,2,3,4])
   plt.show()
   ```

1. Load individual colors

   ```python
   import matplotlib.pyplot as plt
   import catppuccin
   from catppuccin.extras.matplotlib import load_color

   color = load_color(catppuccin.PALETTE.latte.identifier, "peach")
   plt.plot([0,1,2,3], [1,2,3,4], color=color)
   plt.show()
   ```

1. Define custom colormaps

   ```python
   import matplotlib.pyplot as plt
   import numpy as np
   import catppuccin
   from catppuccin.extras.matplotlib import get_colormap_from_list

   cmap = get_colormap_from_list(
       catppuccin.PALETTE.frappe.identifier,
       ["red", "peach", "yellow", "green"],
   )
   rng = np.random.default_rng()
   data = rng.integers(2, size=(30, 30))

   plt.imshow(data, cmap=cmap)
   plt.show()
   ```
"""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import TYPE_CHECKING, cast

import matplotlib as mpl
import matplotlib.colors
import matplotlib.style

from catppuccin.palette import PALETTE

if TYPE_CHECKING:
    from collections.abc import Iterable

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
        mpl.colormaps.register(cmap=cmap, name=palette_name, force=True)


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
