<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://www.python.org/">Python</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
	<a href="https://github.com/catppuccin/python/stargazers"><img src="https://img.shields.io/github/stars/catppuccin/python?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
	<a href="https://github.com/catppuccin/python/issues"><img src="https://img.shields.io/github/issues/catppuccin/python?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
	<a href="https://github.com/catppuccin/python/contributors"><img src="https://img.shields.io/github/contributors/catppuccin/python?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

## Installation

Install with `pip` or your preferred dependency management tool.

```bash
pip install catppuccin
```

## Usage

Get access to the palette with the `catppuccin.PALETTE` constant:

```python
from catppuccin import PALETTE

PALETTE.latte.colors.mauve.hex
# '#8839ef'
PALETTE.mocha.colors.teal.rgb
# RGB(r=148, g=226, b=213)
```

The `Palette` data structure matches [the palette JSON](https://github.com/catppuccin/palette/blob/main/palette.json).

### Iteration

Both `Palette` and `FlavorColors` can be iterated to yield flavors and colors respectively:

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

### dataclasses

`Palette`, `Flavor`, `Color` et cetera are all [`dataclasses`](https://docs.python.org/3/library/dataclasses.html),
so you can also inspect and iterate their fields using methods from the dataclass module.

For example, to list all color names and their hex codes:

```python
from dataclasses import fields
from catppuccin import PALETTE

flavor = PALETTE.frappe
for field in fields(flavor.colors):
    color = getattr(flavor.colors, field.name)
    print(f"{field.name}: {color.hex}")

# rosewater: #f2d5cf
# flamingo: #eebebe
# pink: #f4b8e4
# ...
# base: #303446
# mantle: #292c3c
# crust: #232634
```

## Pygments Styles

This package provides a Pygments style for each of the four Catppuccin flavors.

Install Catppuccin with the `pygments` feature to include the relevant dependencies:

```bash
pip install catppuccin[pygments]
```

The styles are registered as importlib entrypoints, which allows Pygments to
find them by name:

```python
from pygments.styles import get_style_by_name

get_style_by_name("catppuccin-frappe")
# catppuccin.extras.pygments.FrappeStyle
```

The following style names are available:

- `catppuccin-latte`
- `catppuccin-frappe`
- `catppuccin-macchiato`
- `catppuccin-mocha`

They can also be accessed by directly importing them:

```python
from catppuccin.extras.pygments import MacchiatoStyle
```

### IPython

A minimal configuration:

```python
c.TerminalInteractiveShell.true_color = True
c.TerminalInteractiveShell.highlighting_style = "catppuccin-mocha"
```

Putting this into your [IPython configuration](https://ipython.readthedocs.io/en/stable/config/intro.html)
and ensuring `catppuccin[pygments]` is installed in the same environment will
give you Catppuccin Mocha syntax highlighting in the REPL. See [here](https://github.com/backwardspy/dots/blob/f6991570d6691212e27e266517656192f910ccbf/dot_config/ipython/profile_default/ipython_config.py)
for an example of a more complete configuration.

## Matplotlib

The library tries to register styles and colormaps if `matplotlib` is installed.
See the examples below for some use cases:

1. Load a style, using `mpl.style.use`

   ```python
   import catppuccin
   import matplotlib as mpl
   import matplotlib.pyplot as plt

   mpl.style.use(catppuccin.PALETTE.mocha.identifier)
   plt.plot([0,1,2,3], [1,2,3,4])
   plt.show()
   ```

1. Mix it with different stylesheets!

   ```python
   import catppuccin
   import matplotlib as mpl
   import matplotlib.pyplot as plt

   mpl.style.use(["ggplot", catppuccin.PALETTE.mocha.identifier])
   plt.plot([0,1,2,3], [1,2,3,4])
   plt.show()
   ```

1. Load individual colors

   ```python
   import matplotlib.pyplot as plt
   import catppuccin
   from catppuccin.extras.matplotlib import load_color

   color = load_color(catppuccin.PALETTE.latte.identifier, "peach")
   plt.plot([0,1,2,3], [1,2,3,4], color=color)
   plt.show()
   ```

1. Define custom colormaps

   ```python
   import matplotlib.pyplot as plt
   import numpy as np
   import catppuccin
   from catppuccin.extras.matplotlib import get_colormap_from_list

   cmap = get_colormap_from_list(
       catppuccin.PALETTE.frappe.identifier,
       ["red", "peach", "yellow", "green"],
   )
   rng = np.random.default_rng()
   data = rng.integers(2, size=(30, 30))

   plt.imshow(data, cmap=cmap)
   plt.show()
   ```

## Contribution

If you are looking to contribute, please read through our
[CONTRIBUTING.md](https://github.com/catppuccin/.github/blob/main/CONTRIBUTING.md)
first!

### Development

This project is maintained with [uv](https://docs.astral.sh/uv/). If you
don't have uv yet, you can install it using the [installation
instructions](https://docs.astral.sh/uv/getting-started/installation/).

Install the project's dependencies including extras:

```bash
uv sync --all-extras
```

#### Codegen

[`catppuccin/palette.py`](./catppuccin/palette.py) is generated by a [build script](`./build.py`) based on the contents of [`palette.json`](./palette.json).

To update after downloading a new palette JSON file:

```console
uv run build.py
```

Formatting this file is done manually as with any other file, see [`Code Standards`](#code-standards) below.

#### Code Standards

All of the tools listed in this section are automatically installed by uv as
part of the `dev` dependency group.

##### Unit Tests

Tests are run with [`pytest`](https://docs.pytest.org/en/stable/).

To run tests and display coverage:

```console
$ pytest --cov catppuccin
```

##### Type Checking

Type checking is performed by [`mypy`](https://www.mypy-lang.org/).

To run type checks:

```console
$ mypy .
```

##### Lints and Formatting

Code linting and formatting is done by [`ruff`](https://docs.astral.sh/ruff/).

To lint the code:

```console
$ ruff check
```

To format the code:

```console
$ ruff format
```

## 💝 Thanks to

- [backwardspy](https://github.com/backwardspy)
- [Bram de Wilde](https://github.com/brambozz)
- [miloth](https://github.com/miloth)

&nbsp;

<p align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>
<p align="center">
	Copyright &copy; 2022-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
</p>
<p align="center">
	<a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>
