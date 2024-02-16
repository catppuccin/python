import pytest

from catppuccin.color import Color


def test_color_to_rgb() -> None:
    assert Color(12, 123, 234).rgb == (12, 123, 234)


def test_color_to_rgba() -> None:
    assert Color(12, 123, 234, 35).rgba == (12, 123, 234, 35)


def test_color_to_rgba_default() -> None:
    assert Color(12, 123, 234).rgba == (12, 123, 234, 255)


def test_color_to_hsl() -> None:
    assert Color(12, 123, 234).hsl == (210, 0.90, 0.48)


def test_color_to_hsla() -> None:
    assert Color(12, 123, 234, 35).hsla == (210, 0.90, 0.48, 35)


def test_color_to_hsla_default() -> None:
    assert Color(12, 123, 234).hsla == (210, 0.90, 0.48, 255)


def test_rgb_color_to_hex() -> None:
    assert Color(0x12, 0xEB, 0x77).hex == "12eb77"


def test_rgba_color_to_hex() -> None:
    assert Color(0x12, 0xEB, 0x77, 0x35).hex == "12eb7735"


def test_hex_to_color() -> None:
    assert Color.from_hex("12eb77") == Color(0x12, 0xEB, 0x77)


def test_hex_to_color_with_alpha() -> None:
    assert Color.from_hex("12eb7735") == Color(0x12, 0xEB, 0x77, 0x35)


def test_invalid_hex() -> None:
    for invalid_value in ("1234567", "12345", "Z00000", "ABCDEG", "0F7CBJ"):
        with pytest.raises(ValueError, match=r"(must be \d or \d)|(invalid format)"):
            assert Color.from_hex(invalid_value)


def test_equality() -> None:
    assert Color.from_hex("12eb77") == Color.from_hex("12eb77")
    assert Color(0x12, 0xEB, 0x77) == Color(0x12, 0xEB, 0x77)

    some_non_color = 42

    with pytest.raises(TypeError, match="equality with non-color"):
        assert Color(0x12, 0xEB, 0x77) == some_non_color


def test_opacity() -> None:
    color = Color(0x12, 0xEB, 0x77).opacity(0.5)
    assert color == Color(0x12, 0xEB, 0x77, 0x7F)


def test_opacity_invalid() -> None:
    with pytest.raises(ValueError, match="must be between"):
        Color(0x12, 0xEB, 0x77).opacity(1.5)
