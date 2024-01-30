"""
Pygments styles for all Catppuccin flavours.
"""
from typing import Dict

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
    Whitespace,
    Other,
    _TokenType,
)

from catppuccin.flavour import Flavour


def _make_styles(flavour: Flavour) -> Dict[_TokenType, str]:
    return {
        Comment: f"#{flavour.overlay0.hex}",
        Comment.Hashbang: f"#{flavour.overlay0.hex}",
        Comment.Multiline: f"#{flavour.overlay0.hex}",
        Comment.Preproc: f"#{flavour.pink.hex}",
        Comment.Single: f"#{flavour.overlay0.hex}",
        Comment.Special: f"#{flavour.overlay0.hex}",

        Generic: f"#{flavour.text.hex}",
        Generic.Deleted: f"#{flavour.red.hex}",
        Generic.Emph: f"#{flavour.text.hex} underline",
        Generic.Error: f"#{flavour.text.hex}",
        Generic.Heading: f"#{flavour.text.hex} bold",
        Generic.Inserted: f"#{flavour.text.hex} bold",
        Generic.Output: f"#{flavour.overlay0.hex}",
        Generic.Prompt: f"#{flavour.text.hex}",
        Generic.Strong: f"#{flavour.text.hex}",
        Generic.Subheading: f"#{flavour.text.hex} bold",
        Generic.Traceback: f"#{flavour.text.hex}",

        Error: f"#{flavour.text.hex}",

        # `as`
        Keyword: f"#{flavour.mauve.hex}",
        Keyword.Constant: f"#{flavour.pink.hex}",
        Keyword.Declaration: f"#{flavour.teal.hex} italic",
        # `from`, `import`
        Keyword.Namespace: f"#{flavour.mauve.hex}",
        Keyword.Pseudo: f"#{flavour.pink.hex}",
        Keyword.Reserved: f"#{flavour.pink.hex}",
        Keyword.Type: f"#{flavour.teal.hex}",

        Literal: f"#{flavour.text.hex}",
        Literal.Date: f"#{flavour.text.hex}",

        # from xxx import NAME
        # NAME = NAME
        # NAME.NAME()
        Name: f"#{flavour.text.hex}",
        Name.Attribute: f"#{flavour.green.hex}",
        # `len`, `print`
        Name.Builtin: f"#{flavour.peach.hex} italic",
        # `self`
        Name.Builtin.Pseudo: f"#{flavour.red.hex}",
        # class Name.Class:
        Name.Class: f"#{flavour.yellow.hex}",
        Name.Constant: f"#{flavour.text.hex}",
        Name.Decorator: f"#{flavour.text.hex}",
        Name.Entity: f"#{flavour.text.hex}",
        Name.Exception: f"#{flavour.text.hex}",
        # def __Name.Label__(
        Name.Function: f"#{flavour.sapphire.hex}",
        Name.Label: f"#{flavour.teal.hex} italic",
        Name.Namespace: f"#{flavour.text.hex}",
        Name.Other: f"#{flavour.text.hex}",
        Name.Tag: f"#{flavour.pink.hex}",
        Name.Variable: f"#{flavour.crust.hex} italic",
        Name.Variable.Class: f"#{flavour.crust.hex} italic",
        Name.Variable.Global: f"#{flavour.crust.hex} italic",
        Name.Variable.Instance: f"#{flavour.crust.hex} italic",

        Number: f"#{flavour.peach.hex}",
        Number.Bin: f"#{flavour.peach.hex}",
        Number.Float: f"#{flavour.peach.hex}",
        Number.Hex: f"#{flavour.peach.hex}",
        Number.Integer: f"#{flavour.peach.hex}",
        Number.Integer.Long: f"#{flavour.peach.hex}",
        Number.Oct: f"#{flavour.peach.hex}",

        # `=`
        Operator: f"#{flavour.sky.hex}",
        # `not`, `in`
        Operator.Word: f"#{flavour.mauve.hex}",

        Other: f"#{flavour.text.hex}",

        # `(`, `)`, `,`, `[`, `]`, `:`
        Punctuation: f"#{flavour.overlay2.hex}",

        String: f"#{flavour.green.hex}",
        String.Backtick: f"#{flavour.green.hex}",
        String.Char: f"#{flavour.green.hex}",
        String.Doc: f"#{flavour.green.hex}",
        String.Double: f"#{flavour.green.hex}",
        String.Escape: f"#{flavour.green.hex}",
        String.Heredoc: f"#{flavour.green.hex}",
        String.Interpol: f"#{flavour.green.hex}",
        String.Other: f"#{flavour.green.hex}",
        String.Regex: f"#{flavour.green.hex}",
        String.Single: f"#{flavour.green.hex}",
        String.Symbol: f"#{flavour.green.hex}",

        Text: f"#{flavour.text.hex}",

        Whitespace: f"#{flavour.text.hex}"

    }


class LatteStyle(Style):  # pylint: disable=too-few-public-methods
    """Catppuccin Latte pygments style."""

    _flavour = Flavour.latte()

    background_color = f"#{_flavour.base.hex}"
    line_number_background_color = f"#{_flavour.mantle.hex}"
    line_number_color = f"#{_flavour.text.hex}"

    styles = _make_styles(_flavour)


class FrappeStyle(Style):  # pylint: disable=too-few-public-methods
    """Catppuccin Frappé pygments style."""

    _flavour = Flavour.frappe()

    background_color = f"#{_flavour.base.hex}"
    line_number_background_color = f"#{_flavour.mantle.hex}"
    line_number_color = f"#{_flavour.text.hex}"

    styles = _make_styles(_flavour)


class MacchiatoStyle(Style):  # pylint: disable=too-few-public-methods
    """Catppuccin Macchiato pygments style."""

    _flavour = Flavour.macchiato()

    background_color = f"#{_flavour.base.hex}"
    line_number_background_color = f"#{_flavour.mantle.hex}"
    line_number_color = f"#{_flavour.text.hex}"

    styles = _make_styles(_flavour)


class MochaStyle(Style):  # pylint: disable=too-few-public-methods
    """Catppuccin Mocha pygments style."""

    _flavour = Flavour.mocha()

    background_color = f"#{_flavour.base.hex}"
    line_number_background_color = f"#{_flavour.mantle.hex}"
    line_number_color = f"#{_flavour.text.hex}"

    styles = _make_styles(_flavour)
