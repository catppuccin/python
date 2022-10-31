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

```python
>>> from catppuccin import Flavour
>>> Flavour.latte().mauve.hex
'8839ef'
>>> Flavour.mocha().teal.rgb
(148, 226, 213)
```

`Flavour` is a [`dataclass`](https://docs.python.org/3/library/dataclasses.html),
so you can inspect its fields to get access to the full set of colour names and values:

```python
>>> from dataclasses import fields
>>> flavour = Flavour.frappe()
>>> for field in fields(flavour):
        colour = getattr(flavour, field.name)
        print(f"{field.name}: #{colour.hex}")
rosewater: #f2d5cf
flamingo: #eebebe
pink: #f4b8e4
...
base: #303446
mantle: #292c3c
crust: #232634
```

## Contribution

If you are looking to contribute, please read through our
[CONTRIBUTING.md](https://github.com/catppuccin/.github/blob/main/CONTRIBUTING.md)
first!

### Development

This project is maintained with [Poetry](https://python-poetry.org). If you
don't have Poetry yet, you can install it using the [installation
instructions](https://python-poetry.org/docs/#installation).

Install the project's dependencies:

```bash
poetry install
```

#### Code Standards

Before committing changes, it is recommended to run the following tools to
ensure consistency in the codebase.

```bash
isort .
black .
pylint catppuccin.py
mypy .
pytest --cov
```

These tools are all installed as part of the `dev` dependency group with
Poetry. You can use `poetry shell` to automatically put these tools in your
path.


## 💝 Thanks to

-   [backwardspy](https://github.com/backwardspy)

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
