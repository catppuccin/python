"""Utilities for working with HSL colours."""
from __future__ import annotations


def rgb_to_hsl(r: int, g: int, b: int) -> tuple[int, float, float]:
    """Convert RGB to HSL."""
    r1 = r / 255
    g1 = g / 255
    b1 = b / 255

    cmax = max(r1, g1, b1)
    cmin = min(r1, g1, b1)
    delta = cmax - cmin

    if delta == 0:
        hue = 0.0
    elif cmax == r1:
        hue = ((g1 - b1) / delta) % 6
    elif cmax == g1:
        hue = (b1 - r1) / delta + 2
    else:
        hue = (r1 - g1) / delta + 4

    hue = round(hue * 60)
    if hue < 0:
        hue += 360

    lightness = (cmax + cmin) / 2
    saturation = 0 if delta == 0 else delta / (1 - abs(2 * lightness - 1))

    return hue, round(saturation, 2), round(lightness, 2)
