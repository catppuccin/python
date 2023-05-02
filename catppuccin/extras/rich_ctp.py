from rich import print
from rich.theme import Theme

from catppuccin.flavour import Flavour

print("[italic red] Hello [/italic red]")

def _make_styles(flavour: Flavour) -> Theme:
    return {
        Theme({
    "red": f"#{flavour.red.hex}",
    "base": f"#{flavour.base.hex}",
    "subtext0": f"#{flavour.subtext0.hex}",
    "rosewater": f"#{flavour.rosewater.hex}",
    "flamingo": f"#{flavour.flamingo.hex}",
    "pink": f"#{flavour.pink.hex}",
    "mauve": f"#{flavour.mauve.hex}",
    "maroon": f"{flavour.maroon.hex}",
    "peach": f"#{flavour.peach.hex}",
    "yellow": f"#{flavour.yellow.hex}",
    "green": f"#{flavour.green.hex}",
    "teal": f"#{flavour.teal.hex}",
    "sky": f"#{flavour.sky.hex}",
    "sapphire": f"#{flavour.sapphire.hex}",
    "blue": f"#{flavour.blue.hex}",
    "lavender": f"#{flavour.lavender.hex}",
    "text": f"#{flavour.text.hex}",
    "subtext1": f"#{flavour.subtext1.hex}",
    "overlay2": f"#{flavour.overlay2.hex}",
    "overlay1": f"#{flavour.overlay1.hex}",
    "overlay0": f"#{flavour.overlay0.hex}",
    "surface2": f"#{flavour.surface2.hex}",
    "surface1": f"#{flavour.surface1.hex}",
    "surface0": f"#{flavour.surface0.hex}",
    "mantle": f"#{flavour.mantle.hex}",
    "crust": f"#{flavour.crust.hex}"
    })
}