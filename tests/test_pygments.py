from pygments.token import Text

from catppuccin.extras.pygments import LatteStyle, MochaStyle


def test_mocha_style_colors() -> None:
    style = MochaStyle()
    assert style.background_color == "#1e1e2e"
    assert style.styles[Text] == "#cdd6f4"


def test_latte_style_colors() -> None:
    style = LatteStyle()
    assert style.background_color == "#eff1f5"
    assert style.styles[Text] == "#4c4f69"
