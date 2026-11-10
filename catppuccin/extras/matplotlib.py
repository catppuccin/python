"""Soothing pastel theme for `matplotlib`.

The following code was ported from [catppuccin/matplotlib](https://github.com/catppuccin/matplotlib).
Thanks to [Bram de Wilde](https://github.com/brambozz) for the original source code and
for allowing this port.

The library tries to register styles and colormaps if `matplotlib` is installed.
See the examples below for some use cases:

1. Load a style, using `plt.style.use`

    ```python
    import matplotlib.pyplot as plt

    plt.style.use("catppuccin.mocha")
    plt.plot([0,1,2,3], [1,2,3,4])
    plt.show()
    ```

1. Mix it with different stylesheets!

    ```python
    import matplotlib.pyplot as plt

    plt.style.use(["ggplot", "catppuccin.mocha"])
    plt.plot([0,1,2,3], [1,2,3,4])
    plt.show()
    ```

1. Pick the style from a flavor, using `style_name`

    ```python
    import catppuccin
    import matplotlib.pyplot as plt
    from catppuccin.extras.matplotlib import style_name

    flavor = catppuccin.PALETTE.latte
    plt.style.use(style_name(flavor))
    plt.plot([0,1,2,3], [1,2,3,4])
    plt.show()
    ```

1. Load individual colors

    ```python
    import matplotlib.pyplot as plt
    import catppuccin

    plt.plot([0,1,2,3], [1,2,3,4], color=catppuccin.PALETTE.latte.colors.peach.hex)
    plt.show()
    ```

1. Just use the colormaps in your plots

    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    rng = np.random.default_rng()
    data = rng.integers(10, size=(30, 30))

    plt.imshow(data, cmap="catppuccin.mocha")
    plt.show()
    ```

1. Define custom colormaps

    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    import catppuccin
    from matplotlib.colors import LinearSegmentedColormap

    cmap = LinearSegmentedColormap.from_list(
        "my_custom_palette",
        [
            color.hex for color in catppuccin.PALETTE.frappe.colors
            if color.identifier in ["red", "peach", "yellow", "green"]
        ],
    )
    rng = np.random.default_rng()
    data = rng.integers(10, size=(30, 30))

    plt.imshow(data, cmap=cmap)
    plt.show()
    ```
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import matplotlib as mpl
import matplotlib.colors

from catppuccin.palette import PALETTE

if TYPE_CHECKING:
    from catppuccin.models import Flavor

DEFAULT_COLORMAP_COLORS = ("blue", "teal", "yellow", "peach", "red")


def style_name(flavor: Flavor) -> str:
    """Name of the matplotlib style for a flavor, for use with `plt.style.use`.

    The flavor's colormap is registered under the same name.
    """
    return f"catppuccin.{flavor.identifier}"


# Register the included color maps in the `matplotlib` colormap library.
for _palette in PALETTE:
    _cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        style_name(_palette),
        [getattr(_palette.colors, name).hex for name in DEFAULT_COLORMAP_COLORS],
    )
    mpl.colormaps.register(cmap=_cmap, force=True)
