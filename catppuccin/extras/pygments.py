# ruff: noqa: ERA001
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
    Other,
    Punctuation,
    String,
    Text,
    Whitespace,
    _TokenType,
)

from catppuccin import PALETTE

if TYPE_CHECKING:
    from catppuccin.models import FlavorColors


def _make_styles(colors: FlavorColors) -> dict[_TokenType, str]:
    # https://pygments.org/docs/tokens/
    return {
        Comment: colors.overlay2.hex,
        Comment.Hashbang: colors.overlay2.hex,
        Comment.Multiline: colors.overlay2.hex,
        Comment.Preproc: colors.pink.hex,
        Comment.Single: colors.overlay2.hex,
        Comment.Special: colors.overlay2.hex,
        Generic: colors.text.hex,
        Generic.Deleted: colors.red.hex,
        Generic.Emph: f"{colors.text.hex} underline",
        Generic.Error: colors.text.hex,
        Generic.Heading: f"{colors.text.hex} bold",
        Generic.Inserted: f"{colors.text.hex} bold",
        Generic.Output: colors.overlay0.hex,
        Generic.Prompt: colors.text.hex,
        Generic.Strong: colors.text.hex,
        Generic.Subheading: f"{colors.text.hex} bold",
        Generic.Traceback: colors.text.hex,
        Error: colors.text.hex,
        # `as`
        Keyword: colors.mauve.hex,
        Keyword.Constant: colors.mauve.hex,
        Keyword.Declaration: f"{colors.mauve.hex} italic",
        # `from`, `import`
        Keyword.Namespace: colors.mauve.hex,
        Keyword.Pseudo: colors.pink.hex,
        Keyword.Reserved: colors.mauve.hex,
        Keyword.Type: colors.yellow.hex,
        Literal: colors.text.hex,
        Literal.Date: colors.text.hex,
        # from xxx import NAME
        # NAME = NAME
        # NAME.NAME()
        Name: colors.text.hex,
        Name.Attribute: colors.green.hex,
        # `len`, `print`
        Name.Builtin: f"{colors.red.hex} italic",
        # `self`
        Name.Builtin.Pseudo: colors.red.hex,
        # class Name.Class:
        Name.Class: colors.yellow.hex,
        Name.Constant: colors.text.hex,
        Name.Decorator: colors.text.hex,
        Name.Entity: colors.text.hex,
        Name.Exception: colors.yellow.hex,
        # def __Name.Label__(
        Name.Function: colors.blue.hex,
        Name.Label: f"{colors.teal.hex} italic",
        Name.Namespace: colors.text.hex,
        Name.Other: colors.text.hex,
        Name.Tag: colors.blue.hex,
        Name.Variable: f"{colors.text.hex} italic",
        Name.Variable.Class: f"{colors.yellow.hex} italic",
        Name.Variable.Global: f"{colors.text.hex} italic",
        Name.Variable.Instance: f"{colors.text.hex} italic",
        Number: colors.peach.hex,
        Number.Bin: colors.peach.hex,
        Number.Float: colors.peach.hex,
        Number.Hex: colors.peach.hex,
        Number.Integer: colors.peach.hex,
        Number.Integer.Long: colors.peach.hex,
        Number.Oct: colors.peach.hex,
        # `=`
        Operator: colors.sky.hex,
        # `not`, `in`
        Operator.Word: colors.mauve.hex,
        Other: colors.text.hex,
        # `(`, `)`, `,`, `[`, `]`, `:`
        Punctuation: colors.overlay2.hex,
        String: colors.green.hex,
        String.Backtick: colors.green.hex,
        String.Char: colors.green.hex,
        String.Doc: colors.green.hex,
        String.Double: colors.green.hex,
        String.Escape: colors.pink.hex,
        String.Heredoc: colors.green.hex,
        String.Interpol: colors.green.hex,
        String.Other: colors.green.hex,
        String.Regex: colors.pink.hex,
        String.Single: colors.green.hex,
        String.Symbol: colors.red.hex,
        Text: colors.text.hex,
        Whitespace: colors.text.hex,
    }


class LatteStyle(Style):
    """Catppuccin Latte pygments style."""

    _colors = PALETTE.latte.colors

    background_color = _colors.base.hex
    highlight_color = _colors.surface0.hex
    line_number_background_color = _colors.mantle.hex
    line_number_color = _colors.text.hex
    line_number_special_background_color = _colors.mantle.hex
    line_number_special_color = _colors.text.hex

    styles = _make_styles(_colors)


class FrappeStyle(Style):
    """Catppuccin Frappé pygments style."""

    _colors = PALETTE.frappe.colors

    background_color = _colors.base.hex
    highlight_color = _colors.surface0.hex
    line_number_background_color = _colors.mantle.hex
    line_number_color = _colors.text.hex
    line_number_special_background_color = _colors.mantle.hex
    line_number_special_color = _colors.text.hex

    styles = _make_styles(_colors)


class MacchiatoStyle(Style):
    """Catppuccin Macchiato pygments style."""

    _colors = PALETTE.macchiato.colors

    background_color = _colors.base.hex
    highlight_color = _colors.surface0.hex
    line_number_background_color = _colors.mantle.hex
    line_number_color = _colors.text.hex
    line_number_special_background_color = _colors.mantle.hex
    line_number_special_color = _colors.text.hex

    styles = _make_styles(_colors)


class MochaStyle(Style):
    """Catppuccin Mocha pygments style."""

    _colors = PALETTE.mocha.colors

    background_color = _colors.base.hex
    highlight_color = _colors.surface0.hex
    line_number_background_color = _colors.mantle.hex
    line_number_color = _colors.text.hex
    line_number_special_background_color = _colors.mantle.hex
    line_number_special_color = _colors.text.hex

    styles = _make_styles(_colors)
