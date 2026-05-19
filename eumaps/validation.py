from __future__ import annotations

from collections.abc import Iterable

from .config import VALID_NUTS_LEVELS, VALID_RESOLUTIONS
from .exceptions import ColumnValidationError, RegionValidationError


def validate_nuts_level(level: int) -> None:
    if level not in VALID_NUTS_LEVELS:
        raise RegionValidationError(
            f"Invalid nuts level {level!r}. Expected one of {sorted(VALID_NUTS_LEVELS)}."
        )


def validate_resolution(resolution: str) -> None:
    if resolution not in VALID_RESOLUTIONS:
        raise RegionValidationError(
            f"Invalid resolution {resolution!r}. Expected one of {sorted(VALID_RESOLUTIONS)}."
        )


def validate_columns(data, required_cols: list[str]) -> None:
    missing = [col for col in required_cols if col not in data.columns]
    if missing:
        raise ColumnValidationError(
            f"Missing required columns {missing}. Available columns: {list(data.columns)}"
        )


def check_unmatched_regions(
    data_regions: Iterable,
    boundary_regions: Iterable,
    max_examples: int = 10,
) -> list[str]:
    data_set = {str(x) for x in data_regions if x is not None}
    boundary_set = {str(x) for x in boundary_regions if x is not None}
    unmatched = sorted(data_set - boundary_set)
    return unmatched[:max_examples]
