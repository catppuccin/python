import matplotlib as mpl
import matplotlib.pyplot as plt
import pytest

from catppuccin import PALETTE
from catppuccin.extras.matplotlib import style_name
from catppuccin.models import Flavor


@pytest.mark.parametrize("flavor", list(PALETTE), ids=lambda f: f.identifier)
def test_matplotlib_uses_style(flavor: Flavor) -> None:
    plt.style.use(style_name(flavor))


@pytest.mark.parametrize("flavor", list(PALETTE), ids=lambda f: f.identifier)
def test_matplotlib_cmaps(flavor: Flavor) -> None:
    assert style_name(flavor) in list(mpl.colormaps)


@pytest.mark.parametrize("flavor", list(PALETTE), ids=lambda f: f.identifier)
def test_matplotlib_cmap_uses_flavor_colors(flavor: Flavor) -> None:
    cmap = mpl.colormaps[style_name(flavor)]
    assert mpl.colors.to_hex(cmap(0.0)) == flavor.colors.blue.hex
    assert mpl.colors.to_hex(cmap(1.0)) == flavor.colors.red.hex


@pytest.mark.parametrize("flavor", list(PALETTE), ids=lambda f: f.identifier)
def test_matplotlib_style_sets_cmap(flavor: Flavor) -> None:
    with plt.style.context(style_name(flavor)):
        assert mpl.rcParams["image.cmap"] == style_name(flavor)
