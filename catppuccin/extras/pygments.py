"""
Pygments styles for all Catppuccin flavours.
"""
from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
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
    }


class LatteStyle(Style):  # pylint: disable=too-few-public-methods
    """Catppuccin Latte pygments style."""

    styles = _make_styles(Flavour.latte())


class FrappeStyle(Style):  # pylint: disable=too-few-public-methods
    """Catppuccin Frappé pygments style."""

    styles = _make_styles(Flavour.frappe())


class MacchiatoStyle(Style):  # pylint: disable=too-few-public-methods
    """Catppuccin Macchiato pygments style."""

    styles = _make_styles(Flavour.macchiato())


class MochaStyle(Style):  # pylint: disable=too-few-public-methods
    """Catppuccin Mocha pygments style."""

    styles = _make_styles(Flavour.mocha())
