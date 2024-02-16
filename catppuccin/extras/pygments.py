"""Pygments styles for all Catppuccin flavors."""
from __future__ import annotations

from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Text,
    Token,
    _TokenType,
)

from catppuccin.flavor import Flavor


def _make_styles(flavor: Flavor) -> dict[_TokenType, str]:
    return {
        Token: f"#{flavor.text.hex}",
        Text: f"#{flavor.text.hex}",
        Error: f"#{flavor.red.hex}",
        Keyword: f"#{flavor.mauve.hex}",
        Keyword.Constant: f"#{flavor.peach.hex}",
        Keyword.Declaration: f"#{flavor.blue.hex}",
        Keyword.Namespace: f"#{flavor.teal.hex}",
        Keyword.Pseudo: f"#{flavor.mauve.hex}",
        Keyword.Reserved: f"#{flavor.mauve.hex}",
        Keyword.Type: f"#{flavor.blue.hex}",
        Name: f"#{flavor.peach.hex}",
        Name.Attribute: f"#{flavor.blue.hex}",
        Name.Constant: f"#{flavor.yellow.hex}",
        Name.Decorator: f"#{flavor.blue.hex}",
        Name.Function: f"#{flavor.blue.hex}",
        Name.Function.Magic: f"#{flavor.sky.hex}",
        Name.Label: f"#{flavor.blue.hex}",
        Name.Tag: f"#{flavor.mauve.hex}",
        Literal: f"#{flavor.text.hex}",
        String: f"#{flavor.green.hex}",
        Number: f"#{flavor.peach.hex}",
        Punctuation: f"#{flavor.text.hex}",
        Operator: f"#{flavor.sky.hex}",
        Comment: f"#{flavor.overlay0.hex}",
        Generic.Heading: f"#{flavor.blue.hex} bold",
    }


class LatteStyle(Style):
    """Catppuccin Latte pygments style."""

    _flavor = Flavor.latte()

    background_color = f"#{_flavor.base.hex}"
    line_number_background_color = f"#{_flavor.mantle.hex}"
    line_number_color = f"#{_flavor.text.hex}"

    styles = _make_styles(_flavor)


class FrappeStyle(Style):
    """Catppuccin Frappé pygments style."""

    _flavor = Flavor.frappe()

    background_color = f"#{_flavor.base.hex}"
    line_number_background_color = f"#{_flavor.mantle.hex}"
    line_number_color = f"#{_flavor.text.hex}"

    styles = _make_styles(_flavor)


class MacchiatoStyle(Style):
    """Catppuccin Macchiato pygments style."""

    _flavor = Flavor.macchiato()

    background_color = f"#{_flavor.base.hex}"
    line_number_background_color = f"#{_flavor.mantle.hex}"
    line_number_color = f"#{_flavor.text.hex}"

    styles = _make_styles(_flavor)


class MochaStyle(Style):
    """Catppuccin Mocha pygments style."""

    _flavor = Flavor.mocha()

    background_color = f"#{_flavor.base.hex}"
    line_number_background_color = f"#{_flavor.mantle.hex}"
    line_number_color = f"#{_flavor.text.hex}"

    styles = _make_styles(_flavor)
