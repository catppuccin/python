from catppuccin import PALETTE


def test_some_colors() -> None:
    assert PALETTE.mocha.colors.teal.hex == "#94e2d5"
    assert PALETTE.latte.colors.mauve.rgb.r == 136
    assert PALETTE.latte.colors.mauve.rgb.g == 57
    assert PALETTE.latte.colors.mauve.rgb.b == 239
