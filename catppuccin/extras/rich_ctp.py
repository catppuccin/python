"""Rich themes for all Catppuccin flavors."""

from rich.theme import Theme

from catppuccin import PALETTE
from catppuccin.models import FlavorColors


def _make_theme(colors: FlavorColors) -> Theme:
    return Theme(
        {
            "rosewater": colors.rosewater.hex,
            "flamingo": colors.flamingo.hex,
            "pink": colors.pink.hex,
            "mauve": colors.mauve.hex,
            "red": colors.red.hex,
            "maroon": colors.maroon.hex,
            "peach": colors.peach.hex,
            "yellow": colors.yellow.hex,
            "green": colors.green.hex,
            "teal": colors.teal.hex,
            "sky": colors.sky.hex,
            "sapphire": colors.sapphire.hex,
            "blue": colors.blue.hex,
            "lavender": colors.lavender.hex,
            "text": colors.text.hex,
            "subtext1": colors.subtext1.hex,
            "subtext0": colors.subtext0.hex,
            "overlay2": colors.overlay2.hex,
            "overlay1": colors.overlay1.hex,
            "overlay0": colors.overlay0.hex,
            "surface2": colors.surface2.hex,
            "surface1": colors.surface1.hex,
            "surface0": colors.surface0.hex,
            "base": colors.base.hex,
            "mantle": colors.mantle.hex,
            "crust": colors.crust.hex,
        },
    )


latte = _make_theme(PALETTE.latte.colors)
frappe = _make_theme(PALETTE.frappe.colors)
macchiato = _make_theme(PALETTE.macchiato.colors)
mocha = _make_theme(PALETTE.mocha.colors)
