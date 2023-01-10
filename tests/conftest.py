import json
from typing import Dict
from urllib.request import urlopen

import pytest

ColourJSON = Dict[str, str]
FlavourJSON = Dict[str, ColourJSON]
PaletteJSON = Dict[str, FlavourJSON]


@pytest.fixture
def palette_json() -> PaletteJSON:
    url = "https://raw.githubusercontent.com/catppuccin/palette/ec883a880bc24d43a01c78e7d9602abf6b1780dd/palette.json"
    return json.loads(urlopen(url).read())
