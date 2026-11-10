"""🐍 Soothing pastel theme for Python.

## Basic Usage

Get access to the palette with the `catppuccin.PALETTE` constant:

```python
from catppuccin import PALETTE

PALETTE.latte.colors.mauve.hex
# '#8839ef'
PALETTE.mocha.colors.teal.rgb
# RGB(r=148, g=226, b=213)
```

The `Palette` data structure matches [the palette
JSON](https://github.com/catppuccin/palette/blob/main/palette.json).

## Iteration

Both `Palette` and `FlavorColors` can be iterated to yield flavors and colors
respectively:

```python
for flavor in PALETTE:
    print(flavor.name)

# Latte
# Frappé
# Macchiato
# Mocha

for color in PALETTE.latte.colors:
    print(f"{color.name}: {color.hex}")

# Rosewater: #f2d5cf
# Flamingo: #eebebe
# Pink: #f4b8e4
# ...
# Base: #303446
# Mantle: #292c3c
# Crust: #232634
```

## Lookup by name

Flavors and colors can also be looked up via the `FlavorName` and `ColorName`
enums:

```python
from catppuccin import PALETTE, ColorName, FlavorName

PALETTE[FlavorName.MOCHA].colors[ColorName.RED].hex
# '#f38ba8'
PALETTE["latte"].colors["mauve"].hex
# '#8839ef'

def accent(flavor: FlavorName, color: ColorName) -> str:
    return PALETTE[flavor].colors[color].hex
```

## Dataclasses

`Palette`, `Flavor`, `Color` et cetera are all
[`dataclasses`](https://docs.python.org/3/library/dataclasses.html),
so you can also inspect and iterate their fields using methods from the
dataclass module.

For example, to list all color names and their hex codes:

```python
from dataclasses import fields
from catppuccin import PALETTE

flavor = PALETTE.frappe
for field in fields(flavor.colors):
    color = flavor.colors[field.name]
    print(f"{field.name}: {color.hex}")

# rosewater: #f2d5cf
# flamingo: #eebebe
# pink: #f4b8e4
# ...
# base: #303446
# mantle: #292c3c
# crust: #232634
```

## Types

This package is fully type annotated with data structures located in [the models
module](./catppuccin/models.html).

## Integrations

This package includes optional support for several libraries. Click a link below
to see the documentation for that integration.

- [matplotlib](./catppuccin/extras/matplotlib.html)
- [pygments](./catppuccin/extras/pygments.html)
- [rich](./catppuccin/extras/rich_ctp.html)

"""

import importlib.util

from catppuccin.models import ColorName as ColorName
from catppuccin.models import FlavorName as FlavorName
from catppuccin.palette import PALETTE as PALETTE

# Register colormaps if matplotlib is available
if importlib.util.find_spec("matplotlib") is not None:
    import catppuccin.extras.matplotlib  # noqa: F401
