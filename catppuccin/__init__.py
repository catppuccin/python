"""🐍 Soothing pastel theme for Python."""

import importlib.util

from catppuccin.palette import PALETTE, ColorName, FlavorName

__all__ = ["PALETTE", "ColorName", "FlavorName"]

# Attempt to register styles and colormaps if matplotlib is available
if importlib.util.find_spec("matplotlib") is not None:
    from catppuccin.extras.matplotlib import _register_colormap_list, _register_styles

    _register_styles()
    _register_colormap_list()
