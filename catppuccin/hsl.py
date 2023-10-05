"""
Utilities for working with HSL colours.
"""
from __future__ import annotations

from typing import Tuple


# pylint: disable=invalid-name
def rgb_to_hsl(r: int, g: int, b: int) -> Tuple[int, float, float]:
    """Convert RGB to HSL."""
    r1 = r / 255
    g1 = g / 255
    b1 = b / 255

    cmax = max(r1, g1, b1)
    cmin = min(r1, g1, b1)
    delta = cmax - cmin

    if delta == 0:
        h = 0.0
    elif cmax == r1:
        h = ((g1 - b1) / delta) % 6
    elif cmax == g1:
        h = (b1 - r1) / delta + 2
    else:
        h = (r1 - g1) / delta + 4

    h = round(h * 60)
    if h < 0:
        h += 360

    l = (cmax + cmin) / 2

    if delta == 0:
        s = 0.0
    else:
        s = delta / (1 - abs(2 * l - 1))

    return h, round(s, 2), round(l, 2)
