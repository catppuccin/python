"""Rich themes for all Catppuccin flavors."""
from rich.theme import Theme

from catppuccin import PALETTE
from catppuccin.models import FlavorColors


def _make_theme(colors: FlavorColors) -> Theme:
    return Theme(
        {
            "rosewater": f"#{colors.rosewater.hex}",
            "flamingo": f"#{colors.flamingo.hex}",
            "pink": f"#{colors.pink.hex}",
            "mauve": f"#{colors.mauve.hex}",
            "red": f"#{colors.red.hex}",
            "maroon": f"#{colors.maroon.hex}",
            "peach": f"#{colors.peach.hex}",
            "yellow": f"#{colors.yellow.hex}",
            "green": f"#{colors.green.hex}",
            "teal": f"#{colors.teal.hex}",
            "sky": f"#{colors.sky.hex}",
            "sapphire": f"#{colors.sapphire.hex}",
            "blue": f"#{colors.blue.hex}",
            "lavender": f"#{colors.lavender.hex}",
            "text": f"#{colors.text.hex}",
            "subtext1": f"#{colors.subtext1.hex}",
            "subtext0": f"#{colors.subtext0.hex}",
            "overlay2": f"#{colors.overlay2.hex}",
            "overlay1": f"#{colors.overlay1.hex}",
            "overlay0": f"#{colors.overlay0.hex}",
            "surface2": f"#{colors.surface2.hex}",
            "surface1": f"#{colors.surface1.hex}",
            "surface0": f"#{colors.surface0.hex}",
            "base": f"#{colors.base.hex}",
            "mantle": f"#{colors.mantle.hex}",
            "crust": f"#{colors.crust.hex}",
        },
    )


latte = _make_theme(PALETTE.latte.colors)
frappe = _make_theme(PALETTE.frappe.colors)
macchiato = _make_theme(PALETTE.macchiato.colors)
mocha = _make_theme(PALETTE.mocha.colors)
