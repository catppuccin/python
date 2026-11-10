import pytest

from catppuccin import PALETTE, ColorName, FlavorName


def test_some_colors() -> None:
    assert PALETTE.mocha.colors.teal.hex == "#94e2d5"
    assert PALETTE.latte.colors.mauve.rgb.r == 136
    assert PALETTE.latte.colors.mauve.rgb.g == 57
    assert PALETTE.latte.colors.mauve.rgb.b == 239

    assert PALETTE.latte.colors.surface0.identifier == "surface0"
    assert PALETTE.latte.colors.surface0.name == "Surface 0"


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


def test_name_enums_match_models() -> None:
    assert [flavor.identifier for flavor in PALETTE] == list(FlavorName)
    for flavor in PALETTE:
        assert [color.identifier for color in flavor.colors] == list(ColorName)


@pytest.mark.parametrize("flavor", list(FlavorName))
def test_lookup_flavor(flavor: FlavorName) -> None:
    assert PALETTE[flavor] is getattr(PALETTE, flavor)
    assert PALETTE[str(flavor)] is PALETTE[flavor]


@pytest.mark.parametrize("color", list(ColorName))
def test_lookup_color(color: ColorName) -> None:
    colors = PALETTE.mocha.colors
    assert colors[color] is getattr(colors, color)
    assert colors[str(color)] is colors[color]


@pytest.mark.parametrize("name", ["", "Mocha", "colors", "__iter__", "red"])
def test_lookup_unknown_flavor(name: str) -> None:
    with pytest.raises(KeyError):
        PALETTE[name]


@pytest.mark.parametrize("name", ["", "Red", "accent", "__iter__", "mocha"])
def test_lookup_unknown_color(name: str) -> None:
    with pytest.raises(KeyError):
        PALETTE.mocha.colors[name]
