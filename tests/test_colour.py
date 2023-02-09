import pytest

from catppuccin.colour import Colour


def test_colour_to_rgb():
    assert Colour(12, 123, 234).rgb == (12, 123, 234)


def test_colour_to_hex():
    assert Colour(0x12, 0xEB, 0x77).hex == "12eb77"


def test_hex_to_color():
    assert Colour.from_hex("12eb77") == Colour(0x12, 0xEB, 0x77)


def test_invalid_hex():
    for invalid_value in ("1234567", "12345", "Z00000", "ABCDEG", "0F7CBJ"):
        with pytest.raises(ValueError):
            assert Colour.from_hex(invalid_value)


def test_equality():
    assert Colour.from_hex("12eb77") == Colour.from_hex("12eb77")
    assert Colour(0x12, 0xEB, 0x77) == Colour(0x12, 0xEB, 0x77)

    with pytest.raises(ValueError):
        assert Colour(0x12, 0xEB, 0x77) == 42
