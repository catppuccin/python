import pytest
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
