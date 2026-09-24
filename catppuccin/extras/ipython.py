"""IPython extension for Catppuccin themes.

This extension registers Catppuccin themes in IPython's internal
`PyColorize.theme_table` so that they can be used with `%colors` magic command and
configured via a custom `Catppuccin` section in IPython's config file.

Install IPython support with:

```bash
pip install "catppuccin[ipython]"
```

You can use this extension by adding the following to your IPython config file:

```python
c = get_config()
c.InteractiveShellApp.extensions = ["catppuccin.extras.ipython"]
c.TerminalInteractiveShell.true_color = True
# Set this explicitly to apply a flavor when the extension loads.
# Possible values: "latte", "frappe", "macchiato", "mocha"
c.Catppuccin.flavor = "mocha"
```

The reason for using a custom `Catppuccin` section instead of
`TerminalInteractiveShell.colors` is that the latter is validated before
the extension is loaded, which means that the `theme_table`
is not yet populated with Catppuccin themes.

For IPython 8, the extension uses the existing `highlighting_style` setting
instead of the newer theme-table API.
"""

from __future__ import annotations

import warnings
from copy import deepcopy
from typing import TYPE_CHECKING

from catppuccin import PALETTE

if TYPE_CHECKING:
    from IPython.terminal.interactiveshell import TerminalInteractiveShell


VALID_FLAVORS = {flavor.identifier for flavor in PALETTE}


def register_themes() -> bool:
    """Register Catppuccin themes in IPython's ``PyColorize.theme_table``.

    Returns ``True`` when IPython exposes the theme-table API and ``False``
    for older IPython versions that use the ``highlighting_style`` API instead.
    """
    try:
        from IPython.utils.PyColorize import Theme, linux_theme, theme_table
    except ImportError:
        return False

    for flavor in PALETTE:
        theme_name = f"catppuccin-{flavor.identifier}"

        try:
            theme = Theme(
                name=theme_name,
                base=theme_name,
                extra_style=deepcopy(linux_theme.extra_style),
                symbols=deepcopy(linux_theme.symbols),
            )
            theme_table[theme_name] = theme
        except Exception as e:  # noqa: BLE001
            warnings.warn(
                f"Failed to register IPython theme '{theme_name}': {e}",
                RuntimeWarning,
                stacklevel=2,
            )

    return True


def _get_flavor(ipython: TerminalInteractiveShell) -> str | None:
    """Return the explicitly configured Catppuccin flavor, if it is valid."""
    catppuccin_config = ipython.config.get("Catppuccin", {})
    if "flavor" not in catppuccin_config:
        return None

    flavor = catppuccin_config.get("flavor")
    if isinstance(flavor, str):
        flavor = flavor.strip().lower()

    if not isinstance(flavor, str) or flavor not in VALID_FLAVORS:
        warnings.warn(
            f"Invalid Catppuccin flavor {flavor!r}; expected one of: "
            f"{', '.join(sorted(VALID_FLAVORS))}.",
            UserWarning,
            stacklevel=2,
        )
        return None

    return flavor


def load_ipython_extension(ipython: TerminalInteractiveShell) -> None:
    """Load the Catppuccin IPython extension.

    Themes are always registered when supported, but a flavor is applied only
    when ``Catppuccin.flavor`` is explicitly configured.
    """
    theme_table_supported = register_themes()
    flavor = _get_flavor(ipython)
    if flavor is None:
        return

    theme_name = f"catppuccin-{flavor}"
    if theme_table_supported:
        ipython.run_line_magic("colors", theme_name)
    else:
        # IPython 8 validates its legacy ``colors`` trait against a fixed list,
        # but accepts a Pygments style name through ``highlighting_style``.
        ipython.highlighting_style = theme_name
