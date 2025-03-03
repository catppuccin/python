"""Code generation script for creating the global palette constant."""

from __future__ import annotations

import json
import subprocess
from dataclasses import asdict
from pathlib import Path
from typing import Any, cast

from catppuccin.models import HSL, RGB, Color, Flavor, FlavorColors, Palette
from example_plots import example_plots, plot_palette

HEADER = '''"""Catppuccin palette definition."""
from catppuccin.models import HSL, RGB, Color, Flavor, FlavorColors, Palette'''

DPI = 200


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
    print("running codegen")
    palette_path = Path.cwd() / "catppuccin" / "palette.py"
    with palette_path.open("w", newline="\n") as f:
        f.write(codegen())
    print("formatting with ruff")
    ruff_format = f"ruff format {palette_path}"
    subprocess.run(ruff_format.split(), check=True, stdout=subprocess.DEVNULL)
    print("palette.py generation complete")

    # Generate the matplotlib styles
    print("generating matplotlib styles")
    from catppuccin.extras.matplotlib import CATPPUCCIN_STYLE_DIRECTORY
    from catppuccin.palette import PALETTE

    template_text = (
        CATPPUCCIN_STYLE_DIRECTORY / "_catppuccin_template.txt"
    ).read_text()

    for key, palette in asdict(PALETTE).items():
        print(f"- {key}")
        text = template_text
        text = text.replace("<palette>", key)
        for color in palette["colors"]:
            text = text.replace(
                f"<{color}>",
                palette["colors"][color]["hex"].replace("#", ""),
            )
        style_path = CATPPUCCIN_STYLE_DIRECTORY / f"{key}.mplstyle"
        with style_path.open("w", newline="\n") as f:
            f.write(text)
    print("matplotlib styles generation complete")

    # Generate matplotlib assets for the docs
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import catppuccin  # This loads the styles in matplotlib  # noqa: F401

    print("generating matplotlib asset images")
    for palette_name in asdict(PALETTE):
        print(f"- {palette_name}")
        mpl.style.use(palette_name)

        palette_path = Path.cwd() / "assets" / palette_name
        palette_path.mkdir(exist_ok=True, parents=True)

        # Plot palette separately
        print("  - palette")
        fig = plot_palette(palette_name)
        fig.savefig(palette_path / "palette.png", dpi=DPI)

        # Plot examples
        for filename, plot_function in example_plots.items():
            print(f"  - {filename}")
            fig = plot_function()
            fig.savefig(palette_path / f"{filename}.png", dpi=DPI)
            plt.close()
    print("matplotlib asset image generation complete")
