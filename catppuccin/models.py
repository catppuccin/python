"""Dataclass definitions for the Catppuccin palette data structure."""

from collections.abc import Iterator
from dataclasses import dataclass

__all__ = ["Palette", "Flavor", "FlavorColors", "Color", "RGB", "HSL"]


@dataclass(frozen=True)
class RGB:
    """Color represented as red, green, and blue (all 0-255)."""

    r: int
    """@public"""
    g: int
    """@public"""
    b: int
    """@public"""


@dataclass(frozen=True)
class HSL:
    """Color represented as hue (0-359), saturation (0-1), and lightness (0-1)."""

    h: float
    """@public"""
    s: float
    """@public"""
    l: float  # noqa: E741
    """@public"""


@dataclass(frozen=True)
class Color:
    """A single color in the Catppuccin palette."""

    name: str
    """A human-readable name such as `Pink` or `Surface0`."""
    identifier: str
    """The lowercase key used to identify the color. This differs from `name` in
    that it's intended for machine usage rather than presentation."""
    accent: bool
    """Whether the color is considered an accent color. Accent colors are the
    first 14 colors in the palette, also called the analogous colours. The
    remaining 12 non-accent colors are also referred to as the monochromatic
    colors."""
    order: int
    """Order of the color in the palette spec."""
    hex: str
    """The color represented as a six-digit hex string with a leading hash (#)."""
    rgb: RGB
    """The color represented as individual red, green, and blue channels. (0-255)"""
    hsl: HSL
    """The color represented as individual hue (0-359), saturation (0-1), and
    lightness (0-1) channels."""


@dataclass(frozen=True)
class FlavorColors:
    """All of the colors for a particular flavor of Catppuccin.

    Can be iterated over, in which case the colors are yielded in order.
    """

    rosewater: Color
    """@public"""
    flamingo: Color
    """@public"""
    pink: Color
    """@public"""
    mauve: Color
    """@public"""
    red: Color
    """@public"""
    maroon: Color
    """@public"""
    peach: Color
    """@public"""
    yellow: Color
    """@public"""
    green: Color
    """@public"""
    teal: Color
    """@public"""
    sky: Color
    """@public"""
    sapphire: Color
    """@public"""
    blue: Color
    """@public"""
    lavender: Color
    """@public"""
    text: Color
    """@public"""
    subtext1: Color
    """@public"""
    subtext0: Color
    """@public"""
    overlay2: Color
    """@public"""
    overlay1: Color
    """@public"""
    overlay0: Color
    """@public"""
    surface2: Color
    """@public"""
    surface1: Color
    """@public"""
    surface0: Color
    """@public"""
    base: Color
    """@public"""
    mantle: Color
    """@public"""
    crust: Color
    """@public"""

    def __iter__(self) -> Iterator[Color]:
        """Iterate over colors in the flavor."""
        yield from [
            self.rosewater,
            self.flamingo,
            self.pink,
            self.mauve,
            self.red,
            self.maroon,
            self.peach,
            self.yellow,
            self.green,
            self.teal,
            self.sky,
            self.sapphire,
            self.blue,
            self.lavender,
            self.text,
            self.subtext1,
            self.subtext0,
            self.overlay2,
            self.overlay1,
            self.overlay0,
            self.surface2,
            self.surface1,
            self.surface0,
            self.base,
            self.mantle,
            self.crust,
        ]


@dataclass(frozen=True)
class Flavor:
    """A flavor is a collection of colors.

    Catppuccin has four flavors; Latte, Frappé, Macchiato, and Mocha.
    """

    name: str
    """A human-readable name such as `Latte` or `Mocha`."""
    identifier: str
    """The lowercase key used to identify the flavor. This differs from `name`
    in that it's intended for machine usage rather than presentation"""
    order: int
    """Order of the flavor in the palette spec."""
    dark: bool
    """Whether this flavor is dark or light oriented. Latte is light, the other
    three flavors are dark."""
    colors: FlavorColors
    """@public"""


@dataclass(frozen=True)
class Palette:
    """The top-level type that encompasses the Catppuccin palette data structure.

    Primarily used via the `PALETTE` constant.
    Can be iterated over, in which case the flavors are yielded in the canonical
    order: Latte, Frappé, Macchiato, Mocha.
    """

    latte: Flavor
    """The light flavor."""
    frappe: Flavor
    """The lightest dark flavor."""
    macchiato: Flavor
    """The medium dark flavor."""
    mocha: Flavor
    """The darkest dark flavor."""

    def __iter__(self) -> Iterator[Flavor]:
        """Iterate over flavors in the palette."""
        yield from [self.latte, self.frappe, self.macchiato, self.mocha]
