"""Dataclass definitions for the Catppuccin palette data structure."""
from dataclasses import dataclass


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
    order: int
    hex: str
    rgb: RGB
    hsl: HSL
    accent: bool


@dataclass(frozen=True)
class FlavorColors:
    """All of the colors for a particular flavor of Catppuccin."""

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


@dataclass(frozen=True)
class Flavor:
    """A flavor is a collection of colors.

    Catppuccin has four flavors; Latte, Frappé, Macchiato, and Mocha.
    Can be iterated over, in which case the colors are yielded in order.
    """

    name: str
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