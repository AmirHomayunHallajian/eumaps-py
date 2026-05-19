class EuMapsError(Exception):
    """Base error for eumaps."""


class BoundaryDownloadError(EuMapsError):
    """Raised when boundary data cannot be loaded."""


class ColumnValidationError(EuMapsError):
    """Raised when required columns are missing."""


class RegionValidationError(EuMapsError):
    """Raised when region or resolution inputs are invalid."""


class RegionMatchWarning(UserWarning):
    """Warning for unmatched region identifiers."""
