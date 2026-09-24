from __future__ import annotations

import importlib
import sys
from typing import Any, cast
from unittest.mock import MagicMock

import pytest
from pygments.styles import get_style_by_name
from pygments.token import Keyword

from catppuccin import PALETTE
from catppuccin.extras.ipython import load_ipython_extension, register_themes


def _get_theme_table() -> dict[str, Any] | None:
    try:
        module = importlib.import_module("IPython.utils.PyColorize")
        theme_table = module.theme_table
    except (AttributeError, ImportError):
        return None
    else:
        return cast("dict[str, Any]", theme_table)


def _mock_shell(flavor: str | int | None = None) -> MagicMock:
    shell = MagicMock()
    shell.config = {}
    if flavor is not None:
        shell.config["Catppuccin"] = {"flavor": flavor}
    shell.highlighting_style = None
    return shell


def test_ipython_themes_registered() -> None:
    """Test that Catppuccin themes are registered with correct metadata."""
    theme_table = _get_theme_table()
    if theme_table is None:
        pytest.skip("requires IPython with the theme-table API")

    assert register_themes() is True

    for flavor in PALETTE:
        theme_name = f"catppuccin-{flavor.identifier}"
        assert theme_name in theme_table
        theme = theme_table[theme_name]
        assert theme.name == theme_name
        assert theme.base == theme_name
        formatter_style = theme._formatter.style  # noqa: SLF001
        assert formatter_style.style_for_token(Keyword) == get_style_by_name(
            theme_name,
        ).style_for_token(Keyword)


def test_load_ipython_extension_uses_supported_api() -> None:
    """Use the theme-table API on IPython 9 and highlighting_style on IPython 8."""
    theme_table_supported = register_themes()
    shell = _mock_shell("mocha")

    load_ipython_extension(shell)

    if theme_table_supported:
        shell.run_line_magic.assert_called_once_with("colors", "catppuccin-mocha")
        assert shell.highlighting_style is None
    else:
        shell.run_line_magic.assert_not_called()
        assert shell.highlighting_style == "catppuccin-mocha"


def test_load_ipython_extension_does_not_select_without_flavor() -> None:
    shell = _mock_shell()

    load_ipython_extension(shell)

    shell.run_line_magic.assert_not_called()
    assert shell.highlighting_style is None


@pytest.mark.parametrize("flavor", ["mocah", "", 42])
def test_load_ipython_extension_warns_for_invalid_flavor(flavor: str | int) -> None:
    shell = _mock_shell(flavor)

    with pytest.warns(UserWarning, match="Invalid Catppuccin flavor"):
        load_ipython_extension(shell)

    shell.run_line_magic.assert_not_called()
    assert shell.highlighting_style is None


def test_register_themes_without_ipython(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that register_themes exits gracefully when IPython is unavailable."""
    monkeypatch.setitem(sys.modules, "IPython.utils.PyColorize", None)

    assert register_themes() is False


def test_register_themes_handles_exception(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that register_themes handles exceptions during theme registration."""
    if _get_theme_table() is None:
        pytest.skip("requires IPython with the theme-table API")

    def mock_deepcopy(_: object) -> None:
        raise RuntimeError

    monkeypatch.setattr("catppuccin.extras.ipython.deepcopy", mock_deepcopy)

    with pytest.warns(RuntimeWarning, match="Failed to register IPython theme"):
        assert register_themes() is True
