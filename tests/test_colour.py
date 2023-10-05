import pytest

from catppuccin.colour import Colour


def test_colour_to_rgb():
    assert Colour(12, 123, 234).rgb == (12, 123, 234)


def test_colour_to_rgba():
    assert Colour(12, 123, 234, 35).rgba == (12, 123, 234, 35)


def test_colour_to_rgba_default():
    assert Colour(12, 123, 234).rgba == (12, 123, 234, 255)


def test_colour_to_hsl():
    assert Colour(12, 123, 234).hsl == (210, 0.90, 0.48)


def test_colour_to_hsla():
    assert Colour(12, 123, 234, 35).hsla == (210, 0.90, 0.48, 35)


def test_colour_to_hsla_default():
    assert Colour(12, 123, 234).hsla == (210, 0.90, 0.48, 255)


def test_rgb_colour_to_hex():
    assert Colour(0x12, 0xEB, 0x77).hex == "12eb77"


def test_rgba_colour_to_hex():
    assert Colour(0x12, 0xEB, 0x77, 0x35).hex == "12eb7735"


def test_hex_to_colour():
    assert Colour.from_hex("12eb77") == Colour(0x12, 0xEB, 0x77)


def test_hex_to_colour_with_alpha():
    assert Colour.from_hex("12eb7735") == Colour(0x12, 0xEB, 0x77, 0x35)


def test_invalid_hex():
    for invalid_value in ("1234567", "12345", "Z00000", "ABCDEG", "0F7CBJ"):
        with pytest.raises(ValueError):
            assert Colour.from_hex(invalid_value)


def test_equality():
    assert Colour.from_hex("12eb77") == Colour.from_hex("12eb77")
    assert Colour(0x12, 0xEB, 0x77) == Colour(0x12, 0xEB, 0x77)

    with pytest.raises(ValueError):
        assert Colour(0x12, 0xEB, 0x77) == 42


def test_opacity():
    colour = Colour(0x12, 0xEB, 0x77).opacity(0.5)
    assert colour == Colour(0x12, 0xEB, 0x77, 0x7F)


def test_opacity_invalid():
    with pytest.raises(ValueError):
        Colour(0x12, 0xEB, 0x77).opacity(1.5)
