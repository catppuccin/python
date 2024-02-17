from catppuccin.extras.rich_ctp import latte, mocha


def test_mocha_colors() -> None:
    assert mocha.styles["base"].color.triplet.hex == "#1e1e2e"  # type: ignore [union-attr]
    assert mocha.styles["text"].color.triplet.hex == "#cdd6f4"  # type: ignore [union-attr]


def test_latte_colors() -> None:
    assert latte.styles["base"].color.triplet.hex == "#eff1f5"  # type: ignore [union-attr]
    assert latte.styles["text"].color.triplet.hex == "#4c4f69"  # type: ignore [union-attr]
