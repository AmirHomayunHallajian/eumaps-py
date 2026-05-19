from __future__ import annotations

import warnings

import matplotlib.pyplot as plt

from .boundaries import load_nuts
from .exceptions import RegionMatchWarning
from .themes import apply_theme
from .validation import check_unmatched_regions, validate_columns


def choropleth(
    data,
    value_col: str,
    region_col: str = "NUTS_ID",
    nuts_level: int = 2,
    year: int = 2021,
    resolution: str = "20M",
    boundaries=None,
    boundary_region_col: str = "NUTS_ID",
    scheme: str | None = None,
    k: int = 5,
    cmap: str = "viridis",
    title: str | None = None,
    subtitle: str | None = None,
    source_note: str | None = None,
    theme: str = "publication",
    missing_color: str = "lightgrey",
    edgecolor: str = "white",
    linewidth: float = 0.2,
    figsize: tuple[float, float] = (10, 10),
    ax=None,
    legend: bool = True,
    return_gdf: bool = False,
):
    validate_columns(data, [region_col, value_col])

    if boundaries is None:
        boundaries = load_nuts(level=nuts_level, year=year, resolution=resolution)

    validate_columns(boundaries, [boundary_region_col])

    data_copy = data.copy()
    boundaries_copy = boundaries.copy()

    unmatched = check_unmatched_regions(data_copy[region_col], boundaries_copy[boundary_region_col])
    if unmatched:
        warnings.warn(
            f"{len(unmatched)} region code(s) did not match boundaries. Examples: {unmatched}",
            RegionMatchWarning,
            stacklevel=2,
        )

    gdf = boundaries_copy.merge(
        data_copy,
        left_on=boundary_region_col,
        right_on=region_col,
        how="left",
    )

    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure

    kwargs = {
        "column": value_col,
        "ax": ax,
        "cmap": cmap,
        "legend": legend,
        "edgecolor": edgecolor,
        "linewidth": linewidth,
        "missing_kwds": {"color": missing_color, "label": "No data"},
    }
    if scheme is not None:
        kwargs["scheme"] = scheme
        kwargs["k"] = k

    gdf.plot(**kwargs)
    apply_theme(fig=fig, ax=ax, theme=theme, title=title, subtitle=subtitle, source_note=source_note)

    if return_gdf:
        return fig, ax, gdf
    return fig, ax
