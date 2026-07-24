"""IPython extension for Catppuccin themes.

This extension registers Catppuccin themes in IPython's internal
`PyColorize.theme_table` so that they can be used with `%colors` magic command and
configured via custom `Catppuccin` section in IPython's config file.

You can use this extension by adding the following to your IPython config file:

```python
c = get_config()
c.InteractiveShellApp.extensions = ["catppuccin.extras.ipython"]
c.TerminalInteractiveShell.true_color = True
# Optional: Set the flavor to use (default is "mocha")
# possible values: "latte", "frappe", "macchiato", "mocha"
c.Catppuccin.flavor = "mocha"
```

The reason for using a custom `Catppuccin` section instead of
`TerminalInteractiveShell.colors` is that the latter is validated before
the extension is loaded, which means that the `theme_table`
is not yet populated with Catppuccin themes.
"""

from __future__ import annotations

import warnings
from copy import deepcopy
from typing import TYPE_CHECKING

from catppuccin import PALETTE

if TYPE_CHECKING:
    from IPython.core.interactiveshell import InteractiveShell


def register_themes() -> None:
    """Register Catppuccin flavors into IPython's `PyColorize.theme_table`."""
    try:
        from IPython.utils.PyColorize import linux_theme, theme_table
    except ImportError:
        return

    for flavor in PALETTE:
        theme_name = f"catppuccin-{flavor.identifier}"

        try:
            theme = deepcopy(linux_theme)
            theme.base = theme_name
            theme_table[theme_name] = theme
        except Exception as e:  # noqa: BLE001
            warnings.warn(
                f"Failed to register IPython theme '{theme_name}': {e}",
                RuntimeWarning,
                stacklevel=2,
            )


def load_ipython_extension(ipython: InteractiveShell) -> None:
    """Load the Catppuccin IPython extension.

    This function registers Catppuccin themes and sets the IPython color scheme
    based on the custom `Catppuccin` section in the IPython config file.
    """
    register_themes()

    config = getattr(ipython, "config", {})
    # Read from 'Catppuccin.flavor' because 'TerminalInteractiveShell.colors'
    # is validated before this extension loads and populates 'theme_table'.
    catppuccin_config = config.get("Catppuccin", {})
    flavor = catppuccin_config.get("flavor", "mocha").strip().lower()
    if flavor and flavor in (f.identifier for f in PALETTE):
        ipython.run_line_magic("colors", f"catppuccin-{flavor}")
