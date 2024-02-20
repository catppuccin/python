"""Code generation script for creating the global palette constant."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

from catppuccin.models import HSL, RGB, Color, Flavor, FlavorColors, Palette

HEADER = '''"""Catppuccin palette definition."""
from catppuccin.models import HSL, RGB, Color, Flavor, FlavorColors, Palette'''


def load_palette_json() -> dict[str, Any]:
    """Load palette data from `./palette.json`."""
    with Path("palette.json").open() as f:
        return cast(dict[str, Any], json.load(f))


def make_color(identifier: str, fields: dict[str, Any]) -> Color:
    """Create a Color instance from a set of fields."""
    return Color(
        name=fields["name"],
        identifier=identifier,
        accent=fields["accent"],
        order=fields["order"],
        hex=fields["hex"],
        rgb=RGB(**fields["rgb"]),
        hsl=HSL(**fields["hsl"]),
    )


def make_flavor(identifier: str, fields: dict[str, Any]) -> Flavor:
    """Create a Flavor instance from a set of fields."""
    return Flavor(
        name=fields["name"],
        identifier=identifier,
        order=fields["order"],
        dark=fields["dark"],
        colors=FlavorColors(
            **{
                identifier: make_color(identifier, fields)
                for identifier, fields in fields["colors"].items()
            }
        ),
    )


def codegen() -> str:
    """Generate contents of `catppuccin/palette.py`."""
    palette_json = load_palette_json()
    palette = Palette(
        *[
            make_flavor(identifier, fields)
            for identifier, fields in palette_json.items()
        ]
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
