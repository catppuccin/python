"""
Functionality relating to individual colours.
"""
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Colour:
    """A colour with three channels; red, green, and blue."""

    red: int
    green: int
    blue: int

    @property
    def rgb(self) -> Tuple[int, int, int]:
        """Get the colour as a 3-tuple of red, green, and blue."""
        return (self.red, self.green, self.blue)

    @property
    def hex(self) -> str:
        """Get the colour as a lowercase hex string."""
        return f"{self.red:02x}{self.green:02x}{self.blue:02x}"
