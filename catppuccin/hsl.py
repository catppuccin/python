from __future__ import annotations

from typing import Tuple


def rgb_to_hsl(r: int, g: int, b: int) -> Tuple[int, int, int]:
    r /= 255
    g /= 255
    b /= 255

    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    if delta == 0:
        h = 0
    elif cmax == r:
        h = ((g - b) / delta) % 6
    elif cmax == g:
        h = (b - r) / delta + 2
    else:
        h = (r - g) / delta + 4

    h = round(h * 60)
    if h < 0:
        h += 360

    l = (cmax + cmin) / 2

    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))

    return h, round(s, 2), round(l, 2)
