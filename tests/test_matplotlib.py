import matplotlib as mpl
import matplotlib.pyplot as plt
import pytest

from catppuccin import PALETTE
from catppuccin.models import Flavor


@pytest.mark.parametrize("flavor", list(PALETTE), ids=lambda f: f.identifier)
def test_matplotlib_uses_style(flavor: Flavor) -> None:
    plt.style.use(flavor.matplotlib_style)


@pytest.mark.parametrize("flavor", list(PALETTE), ids=lambda f: f.identifier)
def test_matplotlib_cmaps(flavor: Flavor) -> None:
    cmap = flavor.cmap
    assert cmap in list(mpl.colormaps)
