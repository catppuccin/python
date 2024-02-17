"""Code generation script for creating the global palette constant."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from catppuccin.models import HSL, RGB, Color, Flavor, FlavorColors, Palette

HEADER = '''"""Catppuccin palette definition."""
from catppuccin.models import HSL, RGB, Color, Flavor, FlavorColors, Palette'''


def load_palette_json() -> dict[str, Any]:
    """Load palette data from `./palette.json`."""
    with Path("palette.json").open() as f:
        return json.load(f)


def make_color(fields: dict[str, Any]) -> Color:
    """Create a Color instance from a set of fields."""
    return Color(
        name=fields["name"],
        order=fields["order"],
        hex=fields["hex"],
        rgb=RGB(**fields["rgb"]),
        hsl=HSL(**fields["hsl"]),
        accent=fields["accent"],
    )


def make_flavor(fields: dict[str, Any]) -> Flavor:
    """Create a Flavor instance from a set of fields."""
    return Flavor(
        name=fields["name"],
        order=fields["order"],
        dark=fields["dark"],
        colors=FlavorColors(
            **{
                color_name: make_color(color_data)
                for color_name, color_data in fields["colors"].items()
            }
        ),
    )


def codegen() -> str:
    """Generate contents of `catppuccin/palette.py`."""
    palette_json = load_palette_json()
    palette = Palette(
        *[make_flavor(flavor_data) for flavor_data in palette_json.values()]
    )

    lines = [
        HEADER,
        f"PALETTE = {palette!r}",
    ]

    return "\n".join(lines)


if __name__ == "__main__":
    with Path("catppuccin/palette.py").open("w") as f:
        source = codegen()
        print(source, file=f)
