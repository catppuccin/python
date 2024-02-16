"""Test fixtures & helpers."""
import json
from typing import cast
from urllib.request import urlopen

import pytest

ColourJSON = dict[str, str]
FlavourJSON = dict[str, ColourJSON]
PaletteJSON = dict[str, FlavourJSON]


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
