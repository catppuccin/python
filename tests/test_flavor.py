from catppuccin.flavor import Flavor
from tests.conftest import FlavorJSON, PaletteJSON


def validate_flavor(flavor: Flavor, flavor_json: FlavorJSON) -> None:
    for color_name, color_json in flavor_json.items():
        color = getattr(flavor, color_name)
        assert f"#{color.hex}" == color_json["hex"], color_name


def test_latte(palette_json: PaletteJSON) -> None:
    validate_flavor(Flavor.latte(), palette_json["latte"])


def test_frappe(palette_json: PaletteJSON) -> None:
    validate_flavor(Flavor.frappe(), palette_json["frappe"])


def test_macchiato(palette_json: PaletteJSON) -> None:
    validate_flavor(Flavor.macchiato(), palette_json["macchiato"])


def test_mocha(palette_json: PaletteJSON) -> None:
    validate_flavor(Flavor.mocha(), palette_json["mocha"])
