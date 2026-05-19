import pandas as pd
import pytest

from eumaps.exceptions import ColumnValidationError, RegionValidationError
from eumaps.validation import check_unmatched_regions, validate_columns, validate_nuts_level, validate_resolution


def test_validate_nuts_level_invalid():
    with pytest.raises(RegionValidationError):
        validate_nuts_level(4)


def test_validate_resolution_invalid():
    with pytest.raises(RegionValidationError):
        validate_resolution("99M")


def test_validate_columns():
    df = pd.DataFrame({"a": [1]})
    with pytest.raises(ColumnValidationError):
        validate_columns(df, ["missing"])


def test_check_unmatched_regions():
    unmatched = check_unmatched_regions(["A", "B"], ["A", "C"])
    assert unmatched == ["B"]
