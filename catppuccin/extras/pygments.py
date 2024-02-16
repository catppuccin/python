"""Pygments styles for all Catppuccin flavors."""
from __future__ import annotations

from typing import TYPE_CHECKING

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

from catppuccin import PALETTE

if TYPE_CHECKING:
    from catppuccin.models import FlavorColors


def _make_styles(colors: FlavorColors) -> dict[_TokenType, str]:
    return {
        Token: colors.text.hex,
        Text: colors.text.hex,
        Error: colors.red.hex,
        Keyword: colors.mauve.hex,
        Keyword.Constant: colors.peach.hex,
        Keyword.Declaration: colors.blue.hex,
        Keyword.Namespace: colors.teal.hex,
        Keyword.Pseudo: colors.mauve.hex,
        Keyword.Reserved: colors.mauve.hex,
        Keyword.Type: colors.blue.hex,
        Name: colors.peach.hex,
        Name.Attribute: colors.blue.hex,
        Name.Constant: colors.yellow.hex,
        Name.Decorator: colors.blue.hex,
        Name.Function: colors.blue.hex,
        Name.Function.Magic: colors.sky.hex,
        Name.Label: colors.blue.hex,
        Name.Tag: colors.mauve.hex,
        Literal: colors.text.hex,
        String: colors.green.hex,
        Number: colors.peach.hex,
        Punctuation: colors.text.hex,
        Operator: colors.sky.hex,
        Comment: colors.overlay0.hex,
        Generic.Heading: f"{colors.blue.hex} bold",
    }


class LatteStyle(Style):
    """Catppuccin Latte pygments style."""

    _colors = PALETTE.latte.colors

    background_color = _colors.base.hex
    line_number_background_color = _colors.mantle.hex
    line_number_color = _colors.text.hex

    styles = _make_styles(_colors)


class FrappeStyle(Style):
    """Catppuccin Frappé pygments style."""

    _colors = PALETTE.frappe.colors

    background_color = _colors.base.hex
    line_number_background_color = _colors.mantle.hex
    line_number_color = _colors.text.hex

    styles = _make_styles(_colors)


class MacchiatoStyle(Style):
    """Catppuccin Macchiato pygments style."""

    _colors = PALETTE.macchiato.colors

    background_color = _colors.base.hex
    line_number_background_color = _colors.mantle.hex
    line_number_color = _colors.text.hex

    styles = _make_styles(_colors)


class MochaStyle(Style):
    """Catppuccin Mocha pygments style."""

    _colors = PALETTE.mocha.colors

    background_color = _colors.base.hex
    line_number_background_color = _colors.mantle.hex
    line_number_color = _colors.text.hex

    styles = _make_styles(_colors)
