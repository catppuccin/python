"""Code generation script for creating the global palette constant."""

from __future__ import annotations

import json
import subprocess
from dataclasses import asdict
from importlib import reload
from pathlib import Path
from typing import Any, cast

import catppuccin
from catppuccin.models import HSL, RGB, Color, Flavor, FlavorColors, Palette

HEADER = '''"""Catppuccin palette definition."""
from catppuccin.models import HSL, RGB, Color, Flavor, FlavorColors, Palette'''

DPI = 200


def load_palette_json() -> dict[str, Any]:
    """Load palette data from `./palette.json`."""
    with Path("palette.json").open() as f:
        palette_json = cast(dict[str, Any], json.load(f))
    del palette_json["version"]
    return palette_json


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


def palette_codegen() -> str:
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


def generate_mpl_styles() -> None:
    """Generate the matplotlib .mplstyle files."""
    template_text = (Path.cwd() / "matplotlib_template.txt").read_text()

    for key, palette in asdict(catppuccin.PALETTE).items():
        print(f"- {key}")
        text = template_text
        text = text.replace("<palette>", key)
        for color in palette["colors"]:
            text = text.replace(
                f"<{color}>",
                palette["colors"][color]["hex"].replace("#", ""),
            )
        style_path = Path(catppuccin.__file__).parent / f"{key}.mplstyle"
        with style_path.open("w", newline="\n") as f:
            f.write(text)


def main() -> None:  # noqa: D103
    print("running palette codegen")
    palette_path = Path.cwd() / "catppuccin" / "palette.py"
    with palette_path.open("w", newline="\n") as f:
        f.write(palette_codegen())
    print("formatting with ruff")
    ruff_format = f"ruff format {palette_path}"
    subprocess.run(ruff_format.split(), check=True, stdout=subprocess.DEVNULL)
    print("palette.py generation complete")

    print("generating matplotlib styles")
    reload(catppuccin)  # Reload the palette
    generate_mpl_styles()
    print("matplotlib styles generation complete")


if __name__ == "__main__":
    main()
