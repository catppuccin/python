"""Dataclass definitions for the Catppuccin palette data structure."""

from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class RGB:
    """Color represented as red, green, and blue (all 0-255)."""

    r: int
    g: int
    b: int


@dataclass(frozen=True)
class HSL:
    """Color represented as hue (0-359), saturation (0-1), and lightness (0-1)."""

    h: float
    s: float
    l: float  # noqa: E741


@dataclass(frozen=True)
class Color:
    """A single color in the Catppuccin palette."""

    name: str
    identifier: str
    accent: bool
    order: int
    hex: str
    rgb: RGB
    hsl: HSL


@dataclass(frozen=True)
class FlavorColors:
    """All of the colors for a particular flavor of Catppuccin.

    Can be iterated over, in which case the colors are yielded in order.
    """

    rosewater: Color
    flamingo: Color
    pink: Color
    mauve: Color
    red: Color
    maroon: Color
    peach: Color
    yellow: Color
    green: Color
    teal: Color
    sky: Color
    sapphire: Color
    blue: Color
    lavender: Color
    text: Color
    subtext1: Color
    subtext0: Color
    overlay2: Color
    overlay1: Color
    overlay0: Color
    surface2: Color
    surface1: Color
    surface0: Color
    base: Color
    mantle: Color
    crust: Color

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
    identifier: str
    order: int
    dark: bool
    colors: FlavorColors


@dataclass(frozen=True)
class Palette:
    """The top-level type that encompasses the Catppuccin palette data structure.

    Primarily used via the PALETTE constant.
    Can be iterated over, in which case the flavors are yielded in the canonical
    order: Latte, Frappé, Macchiato, Mocha.
    """

    latte: Flavor
    frappe: Flavor
    macchiato: Flavor
    mocha: Flavor

    def __iter__(self) -> Iterator[Flavor]:
        """Iterate over flavors in the palette."""
        yield from [self.latte, self.frappe, self.macchiato, self.mocha]
