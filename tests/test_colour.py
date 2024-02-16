import pytest

from catppuccin.colour import Colour


def test_colour_to_rgb() -> None:
    assert Colour(12, 123, 234).rgb == (12, 123, 234)


def test_colour_to_rgba() -> None:
    assert Colour(12, 123, 234, 35).rgba == (12, 123, 234, 35)


def test_colour_to_rgba_default() -> None:
    assert Colour(12, 123, 234).rgba == (12, 123, 234, 255)


def test_colour_to_hsl() -> None:
    assert Colour(12, 123, 234).hsl == (210, 0.90, 0.48)


def test_colour_to_hsla() -> None:
    assert Colour(12, 123, 234, 35).hsla == (210, 0.90, 0.48, 35)


def test_colour_to_hsla_default() -> None:
    assert Colour(12, 123, 234).hsla == (210, 0.90, 0.48, 255)


def test_rgb_colour_to_hex() -> None:
    assert Colour(0x12, 0xEB, 0x77).hex == "12eb77"


def test_rgba_colour_to_hex() -> None:
    assert Colour(0x12, 0xEB, 0x77, 0x35).hex == "12eb7735"


def test_hex_to_colour() -> None:
    assert Colour.from_hex("12eb77") == Colour(0x12, 0xEB, 0x77)


def test_hex_to_colour_with_alpha() -> None:
    assert Colour.from_hex("12eb7735") == Colour(0x12, 0xEB, 0x77, 0x35)


def test_invalid_hex() -> None:
    for invalid_value in ("1234567", "12345", "Z00000", "ABCDEG", "0F7CBJ"):
        with pytest.raises(ValueError, match=r"(must be \d or \d)|(invalid format)"):
            assert Colour.from_hex(invalid_value)


def test_equality() -> None:
    assert Colour.from_hex("12eb77") == Colour.from_hex("12eb77")
    assert Colour(0x12, 0xEB, 0x77) == Colour(0x12, 0xEB, 0x77)

    some_non_colour = 42

    with pytest.raises(TypeError, match="equality with non-colour"):
        assert Colour(0x12, 0xEB, 0x77) == some_non_colour


def test_opacity() -> None:
    colour = Colour(0x12, 0xEB, 0x77).opacity(0.5)
    assert colour == Colour(0x12, 0xEB, 0x77, 0x7F)


def test_opacity_invalid() -> None:
    with pytest.raises(ValueError, match="must be between"):
        Colour(0x12, 0xEB, 0x77).opacity(1.5)
