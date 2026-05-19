import matplotlib
matplotlib.use("Agg")

import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon

from eumaps.choropleth import choropleth


def test_choropleth_returns_figure_axis():
    boundaries = gpd.GeoDataFrame(
        {
            "NUTS_ID": ["AA01", "AA02"],
            "geometry": [
                Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                Polygon([(1, 0), (2, 0), (2, 1), (1, 1)]),
            ],
        },
        crs="EPSG:4326",
    )
    data = pd.DataFrame({"NUTS_ID": ["AA01", "AA02"], "value": [1.0, 2.0]})
    fig, ax = choropleth(data=data, value_col="value", boundaries=boundaries)
    assert fig is not None
    assert ax is not None
