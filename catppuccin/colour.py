"""Functionality relating to individual colours."""
from __future__ import annotations

import re
from dataclasses import dataclass

from catppuccin.hsl import rgb_to_hsl

HEXLEN_NO_ALPHA = 6
HEXLEN_ALPHA = 8
MAX_ALPHA = 255


@dataclass(frozen=True)
class Colour:
    """A colour with three channels; red, green, and blue."""

    red: int
    green: int
    blue: int
    alpha: int = MAX_ALPHA

    @property
    def rgb(self) -> tuple[int, int, int]:
        """Get the colour as a 3-tuple of red, green, and blue."""
        return self.red, self.green, self.blue

    @property
    def rgba(self) -> tuple[int, int, int, int]:
        """Get the colour as a 4-tuple of red, green, blue, and alpha."""
        return self.red, self.green, self.blue, self.alpha

    @property
    def hsl(self) -> tuple[float, float, float]:
        """Get the colour as a 3-tuple of hue, saturation, and lightness."""
        return rgb_to_hsl(*self.rgb)

    @property
    def hsla(self) -> tuple[float, float, float, float]:
        """Get the colour as a 4-tuple of hue, saturation, lightness, and alpha."""
        return (*self.hsl, self.alpha)

    @property
    def hex(self) -> str:
        """Get the colour as a lowercase hex string."""
        if self.alpha < MAX_ALPHA:
            return f"{self.red:02x}{self.green:02x}{self.blue:02x}{self.alpha:02x}"
        return f"{self.red:02x}{self.green:02x}{self.blue:02x}"

    def __eq__(self, other: object) -> bool:
        """Check equality against another colour."""
        if not isinstance(other, Colour):
            e = "Cannot check equality with non-colour types."
            raise TypeError(e)

        return self.hex == other.hex

    @classmethod
    def from_hex(cls, hex_string: str) -> Colour:
        """Create a colour from hex string."""
        if len(hex_string) not in (HEXLEN_NO_ALPHA, HEXLEN_ALPHA):
            e = f"Hex string must be {HEXLEN_NO_ALPHA} or {
                HEXLEN_ALPHA} characters long."
            raise ValueError(e)

        num_groups = (
            HEXLEN_NO_ALPHA // 2
            if len(hex_string) == HEXLEN_NO_ALPHA
            else HEXLEN_ALPHA // 2
        )
        match = re.match(r"([\da-fA-F]{2})" * num_groups, hex_string)
        if match is None:
            e = "Hex string has an invalid format."
            raise ValueError(e)

        components = (int(col, 16) for col in match.groups())
        return Colour(*components)

    def opacity(self, opacity: float) -> Colour:
        """Return a new colour with the given opacity."""
        if not 0 <= opacity <= 1:
            e = "Opacity must be between 0 and 1."
            raise ValueError(e)

        return Colour(self.red, self.green, self.blue, int(opacity * MAX_ALPHA))
