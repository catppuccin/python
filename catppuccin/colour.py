"""
Functionality relating to individual colours.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Tuple


@dataclass(frozen=True)
class Colour:
    """A colour with three channels; red, green, and blue."""

    red: int
    green: int
    blue: int
    alpha: int = 255

    @property
    def rgb(self) -> Tuple[int, int, int]:
        """Get the colour as a 3-tuple of red, green, and blue."""
        return self.red, self.green, self.blue

    @property
    def rgba(self) -> Tuple[int, int, int, int]:
        """Get the colour as a 4-tuple of red, green, blue, and alpha."""
        return self.red, self.green, self.blue, self.alpha

    @property
    def hex(self) -> str:
        """Get the colour as a lowercase hex string."""
        if self.alpha < 255:
            return f"{self.red:02x}{self.green:02x}{self.blue:02x}{self.alpha:02x}"
        return f"{self.red:02x}{self.green:02x}{self.blue:02x}"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Colour):
            raise ValueError("Cannot check equality with non-colour types.")

        return self.hex == other.hex

    @classmethod
    def from_hex(cls, hex_string: str) -> Colour:
        """Create a colour from hex string."""
        if len(hex_string) not in (6, 8):
            raise ValueError("Hex string must be 6 or 8 characters long.")

        num_groups = 3 if len(hex_string) == 6 else 4
        match = re.match(r"([\da-fA-F]{2})" * num_groups, hex_string)
        if match is None:
            raise ValueError("Hex string has an invalid format.")

        components = (int(col, 16) for col in match.groups())
        return Colour(*components)

    def opacity(self, opacity: float) -> Colour:
        """Return a new colour with the given opacity."""
        if not 0 <= opacity <= 1:
            raise ValueError("Opacity must be between 0 and 1.")

        return Colour(self.red, self.green, self.blue, int(opacity * 255))
