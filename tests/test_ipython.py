from types import SimpleNamespace

import pytest
from IPython.terminal.interactiveshell import TerminalInteractiveShell
from IPython.utils.PyColorize import theme_table
from pygments.styles import get_style_by_name
from pygments.token import Keyword, Token

from catppuccin import PALETTE
from catppuccin.models import Flavor


@pytest.mark.parametrize("flavor", list(PALETTE), ids=lambda f: f.identifier)
def test_ipython_theme_is_registered(flavor: Flavor) -> None:
    name = f"catppuccin-{flavor.identifier}"
    assert name in theme_table

    theme = theme_table[name]
    assert theme.name == name
    assert theme.base == name

    styles = theme.as_pygments_style().styles
    # syntax highlighting comes from the pygments style
    assert styles[Keyword] == get_style_by_name(name).styles[Keyword]
    # rest is ipython-specific
    assert styles[Token.TbHighlight] == f"bg:{flavor.colors.surface1.hex}"
    assert styles[Token.Prompt] == flavor.colors.green.hex


@pytest.mark.parametrize("flavor", list(PALETTE), ids=lambda f: f.identifier)
def test_ipython_noitalic_theme_is_registered(flavor: Flavor) -> None:
    base_name = f"catppuccin-{flavor.identifier}"
    name = f"{base_name}:noitalic"
    assert name in theme_table

    theme = theme_table[name]
    assert theme.name == name
    assert theme.base == base_name

    styles = theme.as_pygments_style().styles
    italic = {
        token: style
        for token, style in theme_table[base_name].as_pygments_style().styles.items()
        if "italic" in style.split()
    }

    # sanity check that our style actually has italics in the first place
    assert italic

    for token, style in italic.items():
        assert styles[token] == style.replace("italic", "noitalic")
    assert not [token for token, style in styles.items() if "italic" in style.split()]


@pytest.mark.parametrize(
    ("theme_name", "italic"),
    [("catppuccin-mocha", True), ("catppuccin-mocha:noitalic", False)],
)
def test_ipython_input_line_italics(theme_name: str, italic: bool) -> None:  # noqa: FBT001
    shell = SimpleNamespace(colors=theme_name, highlighting_style_overrides={})
    make_style = TerminalInteractiveShell._make_style_from_name_or_cls  # noqa: SLF001
    style = make_style(shell, "legacy")  # type: ignore[no-untyped-call, arg-type]
    attrs = style.get_attrs_for_style_str("class:pygments.name.builtin")
    assert attrs.italic is italic
    assert attrs.color == PALETTE.mocha.colors.red.hex.removeprefix("#")
