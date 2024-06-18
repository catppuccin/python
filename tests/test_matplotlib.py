from dataclasses import asdict

import matplotlib as mpl
import pytest

import catppuccin


@pytest.mark.parametrize(
    "name",
    [
        catppuccin.PALETTE.__getattribute__(key).identifier
        for key in asdict(catppuccin.PALETTE)
    ],
)
def test_matplotlib_uses_style(name: str) -> None:
    """Test that the matplotlib style is set to the given name."""
    mpl.style.use(name)
