"""Code generation script for creating the global palette constant."""

from __future__ import annotations

import json
import subprocess
from dataclasses import asdict
from pathlib import Path
from typing import Any, cast

from catppuccin.extras.pygments import _make_styles
from catppuccin.models import HSL, RGB, Color, Flavor, FlavorColors, Palette

HEADER = '''"""Catppuccin palette definition."""
from catppuccin.models import HSL, RGB, Color, Flavor, FlavorColors, Palette'''

# must match the `ipython.themes` entry points in `pyproject.toml`.
IPYTHON_THEME_DIRECTORY = (
    Path(__file__).parent / "catppuccin" / "extras" / "ipython_themes"
)


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


def ipython_theme(flavor: Flavor) -> dict[str, Any]:
    """Create an IPython theme for a flavor.

    Syntax highlighting comes from the matching pygments style via `base`.
    `extra_style` covers the IPython tokens used for prompts, tracebacks, and
    the debugger.
    """
    c = flavor.colors
    name = f"catppuccin-{flavor.identifier}"
    return {
        "name": name,
        "base": name,
        "extra_style": {
            # prompts
            "Prompt": c.green.hex,
            "PromptNum": f"{c.green.hex} bold",
            "OutPrompt": c.peach.hex,
            "OutPromptNum": f"{c.peach.hex} bold",
            # tracebacks
            "Header": c.red.hex,
            "Topline": c.red.hex,
            "ExcName": f"{c.red.hex} bold",
            "Filename": c.blue.hex,
            "FilenameEm": f"{c.blue.hex} bold",
            "Lineno": c.overlay1.hex,
            "LinenoEm": f"{c.lavender.hex} bold",
            "Line": c.text.hex,
            "TB.Name": c.mauve.hex,
            "TB.NameEm": f"{c.mauve.hex} bold",
            "VName": c.teal.hex,
            "ValEm": f"{c.peach.hex} bold",
            "Normal": "",
            "NormalEm": f"{c.text.hex} bold",
            "Caret": "",
            "TbHighlight": f"bg:{c.surface1.hex}",
            # debugger
            "Breakpoint": "",
            "Breakpoint.Enabled": c.red.hex,
            "Breakpoint.Disabled": c.overlay1.hex,
        },
    }


def ipython_noitalic_theme(flavor: Flavor) -> dict[str, Any]:
    """Create the :noitalic variant of the IPython theme for the given flavor.

    This works by loading the existing theme and returning a modified copy with
    all `italic` parts replaced with `noitalic. It's done this way rather than
    just removing `italic` to ensure it still overrides any italics in the base
    style.
    """
    theme = ipython_theme(flavor)
    noitalic = {
        str(token).removeprefix("Token."): " ".join(
            "noitalic" if part == "italic" else part for part in style.split()
        )
        for token, style in _make_styles(flavor.colors).items()
        if "italic" in style.split()
    }
    return {
        **theme,
        "name": f"{theme['name']}:noitalic",
        "extra_style": {**theme["extra_style"], **noitalic},
    }


def ipython_theme_filename(name: str) -> str:
    """Return the file that IPython loads for a given theme name.

    Practically speaking this means replacing `:` with `-` and appending `.json`.
    """
    return name.replace(":", "-") + ".json"


def load_palette() -> Palette:
    """Build the palette from `./palette.json`."""
    palette_json = load_palette_json()
    return Palette(
        *[
            make_flavor(identifier, fields)
            for identifier, fields in palette_json.items()
        ]
    )


def palette_codegen(palette: Palette) -> str:
    """Generate contents of `catppuccin/palette.py`."""
    lines = [
        HEADER,
        f"PALETTE = {palette!r}",
    ]

    return "\n".join(lines)


def generate_mpl_styles(palette: Palette) -> None:
    """Generate the matplotlib .mplstyle files."""
    template_text = (Path.cwd() / "matplotlib_template.txt").read_text()

    for key, flavor in asdict(palette).items():
        print(f"- {key}")
        text = template_text
        text = text.replace("<palette>", key)
        for color in flavor["colors"]:
            text = text.replace(
                f"<{color}>",
                flavor["colors"][color]["hex"].replace("#", ""),
            )
        style_path = Path.cwd() / "catppuccin" / f"{key}.mplstyle"
        with style_path.open("w", newline="\n") as f:
            f.write(text)


def generate_ipython_themes(palette: Palette) -> None:
    """Generate the IPython theme JSON files."""
    IPYTHON_THEME_DIRECTORY.mkdir(exist_ok=True)
    for flavor in palette:
        for theme in (ipython_theme(flavor), ipython_noitalic_theme(flavor)):
            print(f"- {theme['name']}")
            theme_path = IPYTHON_THEME_DIRECTORY / ipython_theme_filename(theme["name"])
            with theme_path.open("w", newline="\n") as f:
                json.dump(theme, f, indent=2)
                f.write("\n")


def main() -> None:  # noqa: D103
    # we build from the latest palette data rather than a stale `catppuccin.PALETTE`.
    # `catppuccin.PALETTE` gets rewritten below, but even then we'd have to
    # reload a bunch of modules to get it loaded.
    palette = load_palette()

    print("running palette codegen")
    palette_path = Path.cwd() / "catppuccin" / "palette.py"
    with palette_path.open("w", newline="\n") as f:
        f.write(palette_codegen(palette))
    print("formatting with ruff")
    ruff_format = f"ruff format {palette_path}"
    subprocess.run(ruff_format.split(), check=True, stdout=subprocess.DEVNULL)
    print("palette.py generation complete")

    print("generating matplotlib styles")
    generate_mpl_styles(palette)
    print("matplotlib styles generation complete")

    print("generating ipython themes")
    generate_ipython_themes(palette)
    print("ipython themes generation complete")


if __name__ == "__main__":
    main()
