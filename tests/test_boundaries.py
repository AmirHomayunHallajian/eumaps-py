from eumaps.boundaries import build_nuts_url, load_countries


def test_build_nuts_url():
    url = build_nuts_url(level=2, year=2021, resolution="20M")
    assert url.endswith("NUTS_RG_20M_2021_4326_LEVL_2.geojson")


def test_load_countries_calls_nuts(monkeypatch):
    called = {}

    def fake_load_nuts(**kwargs):
        called.update(kwargs)
        return "ok"

    monkeypatch.setattr("eumaps.boundaries.load_nuts", fake_load_nuts)
    result = load_countries(year=2021, resolution="20M", crs="EPSG:4326", cache=True)
    assert result == "ok"
    assert called["level"] == 0
