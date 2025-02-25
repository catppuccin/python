"""Functions to plot some images using matplotlib.

The generated plots are in the `assets` directory.
"""

from __future__ import annotations

from dataclasses import asdict

import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

from catppuccin.palette import PALETTE

SEED = 0
POINTS = 50


def plot_palette(palette_name: str) -> plt.Figure:  # type: ignore [name-defined]
    """Plot a palette with color names and hex values."""
    colors = asdict(PALETTE.__getattribute__(palette_name).colors)

    # Create figure and adjust figure height to number of colormaps
    nrows = len(colors)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh, left=0.2, right=0.99)

    axs[0].set_title(palette_name, fontsize=14)

    for ax, color_name in zip(axs, colors):
        ax.hlines(0, 0, 1, colors=colors[color_name]["hex"], linewidth=15)
        ax.text(
            -0.01,
            0.5,
            f"{color_name} {colors[color_name]['hex']}",
            va="center",
            ha="right",
            fontsize=10,
            transform=ax.transAxes,
        )

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    fig.tight_layout()

    return fig


def example_plot() -> plt.Figure:  # type: ignore [name-defined]
    """Generate a plot with multiple sin functions with phase shifts."""
    x = np.linspace(0.0, 1.0, num=101)
    phases = np.linspace(0.0, -0.8, num=5)
    np.sin(2 * np.pi * x)

    fig = plt.figure()
    for idx, phase in enumerate(phases):
        plt.plot(x, np.sin(2 * np.pi * x + phase), label=f"Color {idx + 1}")
    plt.grid()
    plt.legend()

    return fig


def example_scatter() -> plt.Figure:  # type: ignore [name-defined]
    """Generate a scatter plot with two sets of random data."""
    rng = np.random.default_rng(SEED)
    x = rng.random(POINTS)

    fig = plt.figure()
    plt.scatter(x, rng.random(POINTS))
    plt.scatter(x, rng.random(POINTS))

    return fig


def example_boxplot() -> plt.Figure:  # type: ignore [name-defined]
    """Generate a boxplot with random data."""
    rng = np.random.default_rng(SEED)
    bars = 4
    nominal_values = rng.random(bars)
    distributions = rng.random((bars, POINTS))

    fig = plt.figure()
    plt.boxplot(nominal_values + distributions.T, patch_artist=True)
    return fig


def example_bar() -> plt.Figure:  # type: ignore [name-defined]
    """Generate a bar plot with random data."""
    rng = np.random.default_rng(SEED)
    bars = 10
    x = np.arange(bars).astype(np.float64) + 0.5
    y = rng.random(bars)

    fig = plt.figure()
    plt.bar(x, y)
    return fig


def example_patches() -> plt.Figure:  # type: ignore [name-defined]
    """Generate a plot with two arrows."""
    fig, ax = plt.subplots()
    arrow_1 = mpatches.FancyArrowPatch((0, 1), (1, 0), mutation_scale=100)
    arrow_2 = mpatches.FancyArrowPatch((0, 0), (1, 1), mutation_scale=100)
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
    ax.add_patch(arrow_1)
    ax.add_patch(arrow_2)

    return fig


def example_imshow() -> plt.Figure:  # type: ignore [name-defined]
    """Generate an image plot with random data."""
    rng = np.random.default_rng(SEED)
    data = rng.random((30, 30))

    fig, ax = plt.subplots()
    im = ax.imshow(data)
    ax.tick_params(
        left=False, right=False, labelleft=False, labelbottom=False, bottom=False
    )

    fig.colorbar(im, ax=ax, ticks=[])

    return fig


def plot_examples(colormap_list: list[str]) -> None:
    """Plot data with associated colormap."""
    rng = np.random.default_rng(SEED)
    data = rng.random((30, 30))
    n = len(colormap_list)
    fig, axs = plt.subplots(
        1, n, figsize=(n * 2 + 2, 3), constrained_layout=True, squeeze=False
    )
    for [ax, cmap] in zip(axs.flat, colormap_list):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=0.0, vmax=1.0)
        fig.colorbar(psm, ax=ax)
    plt.show()


example_plots = {
    "plot": example_plot,
    "scatter": example_scatter,
    "boxplot": example_boxplot,
    "bar": example_bar,
    "patches": example_patches,
    "imshow": example_imshow,
}

if __name__ == "__main__":
    palette_name = "mocha"
    mpl.style.use(palette_name)
    plot_palette(palette_name)
    plt.show()
    example_plot()
    plt.show()
    example_scatter()
    plt.show()
    example_boxplot()
    plt.show()
    example_bar()
    plt.show()
    example_patches()
    plt.show()
    example_imshow()
    plt.show()
    plot_examples(list(asdict(PALETTE).keys()))
    plt.show()
