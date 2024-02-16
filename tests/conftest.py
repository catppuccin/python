"""Test fixtures & helpers."""
import json
from typing import Dict, cast
from urllib.request import urlopen

import pytest

ColorJSON = Dict[str, str]
FlavorJSON = Dict[str, ColorJSON]
PaletteJSON = Dict[str, FlavorJSON]


@pytest.fixture()
def palette_json() -> PaletteJSON:
    """Download & return the palette JSON from github."""
    return cast(
        PaletteJSON,
        json.loads(
            urlopen(
                "https://raw.githubusercontent.com/catppuccin/palette/ec883a880bc24d43a01c78e7d9602abf6b1780dd/palette.json",
            ).read(),
        ),
    )
