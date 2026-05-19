from __future__ import annotations

import geopandas as gpd

from .config import CACHE_DIR
from .exceptions import BoundaryDownloadError
from .validation import validate_nuts_level, validate_resolution

GISCO_NUTS_BASE = "https://gisco-services.ec.europa.eu/distribution/v2/nuts/geojson"


def build_nuts_url(level: int, year: int, resolution: str) -> str:
    validate_nuts_level(level)
    validate_resolution(resolution)
    return f"{GISCO_NUTS_BASE}/NUTS_RG_{resolution}_{year}_4326_LEVL_{level}.geojson"


def load_nuts(
    level: int = 2,
    year: int = 2021,
    resolution: str = "20M",
    crs: str = "EPSG:4326",
    cache: bool = True,
) -> gpd.GeoDataFrame:
    validate_nuts_level(level)
    validate_resolution(resolution)

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = CACHE_DIR / f"nuts_{resolution}_{year}_level_{level}.geojson"

    try:
        if cache and cache_path.exists():
            gdf = gpd.read_file(cache_path)
        else:
            gdf = gpd.read_file(build_nuts_url(level=level, year=year, resolution=resolution))
            if cache:
                gdf.to_file(cache_path, driver="GeoJSON")

        if crs is not None:
            gdf = gdf.to_crs(crs)
        return gdf
    except Exception as exc:  # pragma: no cover
        raise BoundaryDownloadError(
            f"Could not load NUTS boundaries for level={level}, year={year}, resolution={resolution}."
        ) from exc


def load_countries(
    year: int = 2021,
    resolution: str = "20M",
    crs: str = "EPSG:4326",
    cache: bool = True,
) -> gpd.GeoDataFrame:
    return load_nuts(level=0, year=year, resolution=resolution, crs=crs, cache=cache)
