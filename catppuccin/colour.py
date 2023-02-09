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

    @property
    def rgb(self) -> Tuple[int, int, int]:
        """Get the colour as a 3-tuple of red, green, and blue."""
        return self.red, self.green, self.blue

    @property
    def hex(self) -> str:
        """Get the colour as a lowercase hex string."""
        return f"{self.red:02x}{self.green:02x}{self.blue:02x}"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Colour):
            raise ValueError("Cannot check equality with non-colour types.")
        return self.hex == other.hex

    @classmethod
    def from_hex(cls, hex_string: str) -> Colour:
        """Create a color from hex string."""
        if len(hex_string) != 6:
            raise ValueError("Hex string must be 6 characters long.")
        match = re.match(r"([\da-fA-F]{2})" * 3, hex_string)
        if match is None:
            raise ValueError("Hex string have an invalid format.")
        hex_r, hex_g, hex_b = match.groups()
        return Colour(*(int(col, 16) for col in (hex_r, hex_g, hex_b)))
