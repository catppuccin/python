from catppuccin import Flavour
from catppuccin.hsl import rgb_to_hsl

mocha = Flavour.mocha()
latte = Flavour.latte()


def test_rgb_to_hsl() -> None:
    hsl = rgb_to_hsl(*mocha.mauve.rgb)
    assert hsl == (267, 0.84, 0.81)

    hsl = rgb_to_hsl(*latte.text.rgb)
    assert hsl == (234, 0.16, 0.35)
