import sys
from unittest.mock import MagicMock

import pytest
from IPython.utils.PyColorize import theme_table

from catppuccin import PALETTE
from catppuccin.extras.ipython import load_ipython_extension, register_themes

pytest.importorskip("IPython")


def test_ipython_themes_registered() -> None:
    """Test that Catppuccin themes are registered in IPython's theme_table."""
    register_themes()

    for flavor in PALETTE:
        theme_name = f"catppuccin-{flavor.identifier}"
        assert theme_name in theme_table
        theme = theme_table[theme_name]
        assert theme.base == theme_name


def test_load_ipython_extension_runs_magic() -> None:
    """Test that extension runs the %colors magic with the correct flavor."""
    mock_shell = MagicMock()
    mock_shell.config = {
        "Catppuccin": {
            "flavor": "mocha",
        },
    }

    load_ipython_extension(mock_shell)

    assert "catppuccin-mocha" in theme_table
    mock_shell.run_line_magic.assert_called_once_with("colors", "catppuccin-mocha")


def test_register_themes_without_ipython(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that register_themes exits gracefully when IPython is not available."""
    monkeypatch.setitem(sys.modules, "IPython.utils.PyColorize", None)
    register_themes()


def test_register_themes_handles_exception(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that register_themes handles exceptions during theme registration."""

    def mock_deepcopy(_: object) -> None:
        raise RuntimeError

    monkeypatch.setattr("catppuccin.extras.ipython.deepcopy", mock_deepcopy)

    with pytest.warns(RuntimeWarning, match="Failed to register IPython theme"):
        register_themes()
