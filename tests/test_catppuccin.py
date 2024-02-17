from catppuccin import PALETTE


def test_some_colors() -> None:
    assert PALETTE.mocha.colors.teal.hex == "#94e2d5"
    assert PALETTE.latte.colors.mauve.rgb.r == 136
    assert PALETTE.latte.colors.mauve.rgb.g == 57
    assert PALETTE.latte.colors.mauve.rgb.b == 239


def test_iterate_palette() -> None:
    order = [PALETTE.latte, PALETTE.frappe, PALETTE.macchiato, PALETTE.mocha]
    for i, flavor in enumerate(PALETTE):
        assert order[i] == flavor
    assert list(PALETTE) == order


def test_iterate_flavor_colors() -> None:
    colors = PALETTE.latte.colors
    order = [
        colors.rosewater,
        colors.flamingo,
        colors.pink,
        colors.mauve,
        colors.red,
        colors.maroon,
        colors.peach,
        colors.yellow,
        colors.green,
        colors.teal,
        colors.sky,
        colors.sapphire,
        colors.blue,
        colors.lavender,
        colors.text,
        colors.subtext1,
        colors.subtext0,
        colors.overlay2,
        colors.overlay1,
        colors.overlay0,
        colors.surface2,
        colors.surface1,
        colors.surface0,
        colors.base,
        colors.mantle,
        colors.crust,
    ]
    for i, color in enumerate(colors):
        assert order[i] == color
    assert list(colors) == order
