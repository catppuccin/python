"""Rich themes for all Catppuccin flavors."""
from rich.theme import Theme

from catppuccin.flavor import Flavor


def _make_theme(flavor: Flavor) -> Theme:
    return Theme(
        {
            "rosewater": f"#{flavor.rosewater.hex}",
            "flamingo": f"#{flavor.flamingo.hex}",
            "pink": f"#{flavor.pink.hex}",
            "mauve": f"#{flavor.mauve.hex}",
            "red": f"#{flavor.red.hex}",
            "maroon": f"#{flavor.maroon.hex}",
            "peach": f"#{flavor.peach.hex}",
            "yellow": f"#{flavor.yellow.hex}",
            "green": f"#{flavor.green.hex}",
            "teal": f"#{flavor.teal.hex}",
            "sky": f"#{flavor.sky.hex}",
            "sapphire": f"#{flavor.sapphire.hex}",
            "blue": f"#{flavor.blue.hex}",
            "lavender": f"#{flavor.lavender.hex}",
            "text": f"#{flavor.text.hex}",
            "subtext1": f"#{flavor.subtext1.hex}",
            "subtext0": f"#{flavor.subtext0.hex}",
            "overlay2": f"#{flavor.overlay2.hex}",
            "overlay1": f"#{flavor.overlay1.hex}",
            "overlay0": f"#{flavor.overlay0.hex}",
            "surface2": f"#{flavor.surface2.hex}",
            "surface1": f"#{flavor.surface1.hex}",
            "surface0": f"#{flavor.surface0.hex}",
            "base": f"#{flavor.base.hex}",
            "mantle": f"#{flavor.mantle.hex}",
            "crust": f"#{flavor.crust.hex}",
        },
    )


latte = _make_theme(Flavor.latte())
frappe = _make_theme(Flavor.frappe())
macchiato = _make_theme(Flavor.macchiato())
mocha = _make_theme(Flavor.mocha())
