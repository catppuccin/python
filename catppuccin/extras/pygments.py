"""Pygments styles for all Catppuccin flavours."""
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

from catppuccin.flavour import Flavour


def _make_styles(flavour: Flavour) -> dict[_TokenType, str]:
    return {
        Token: f"#{flavour.text.hex}",
        Text: f"#{flavour.text.hex}",
        Error: f"#{flavour.red.hex}",
        Keyword: f"#{flavour.mauve.hex}",
        Keyword.Constant: f"#{flavour.peach.hex}",
        Keyword.Declaration: f"#{flavour.blue.hex}",
        Keyword.Namespace: f"#{flavour.teal.hex}",
        Keyword.Pseudo: f"#{flavour.mauve.hex}",
        Keyword.Reserved: f"#{flavour.mauve.hex}",
        Keyword.Type: f"#{flavour.blue.hex}",
        Name: f"#{flavour.peach.hex}",
        Name.Attribute: f"#{flavour.blue.hex}",
        Name.Constant: f"#{flavour.yellow.hex}",
        Name.Decorator: f"#{flavour.blue.hex}",
        Name.Function: f"#{flavour.blue.hex}",
        Name.Function.Magic: f"#{flavour.sky.hex}",
        Name.Label: f"#{flavour.blue.hex}",
        Name.Tag: f"#{flavour.mauve.hex}",
        Literal: f"#{flavour.text.hex}",
        String: f"#{flavour.green.hex}",
        Number: f"#{flavour.peach.hex}",
        Punctuation: f"#{flavour.text.hex}",
        Operator: f"#{flavour.sky.hex}",
        Comment: f"#{flavour.overlay0.hex}",
        Generic.Heading: f"#{flavour.blue.hex} bold",
    }


class LatteStyle(Style):
    """Catppuccin Latte pygments style."""

    _flavour = Flavour.latte()

    background_color = f"#{_flavour.base.hex}"
    line_number_background_color = f"#{_flavour.mantle.hex}"
    line_number_color = f"#{_flavour.text.hex}"

    styles = _make_styles(_flavour)


class FrappeStyle(Style):
    """Catppuccin Frappé pygments style."""

    _flavour = Flavour.frappe()

    background_color = f"#{_flavour.base.hex}"
    line_number_background_color = f"#{_flavour.mantle.hex}"
    line_number_color = f"#{_flavour.text.hex}"

    styles = _make_styles(_flavour)


class MacchiatoStyle(Style):
    """Catppuccin Macchiato pygments style."""

    _flavour = Flavour.macchiato()

    background_color = f"#{_flavour.base.hex}"
    line_number_background_color = f"#{_flavour.mantle.hex}"
    line_number_color = f"#{_flavour.text.hex}"

    styles = _make_styles(_flavour)


class MochaStyle(Style):
    """Catppuccin Mocha pygments style."""

    _flavour = Flavour.mocha()

    background_color = f"#{_flavour.base.hex}"
    line_number_background_color = f"#{_flavour.mantle.hex}"
    line_number_color = f"#{_flavour.text.hex}"

    styles = _make_styles(_flavour)
