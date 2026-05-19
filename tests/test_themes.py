from eumaps.themes import list_themes


def test_list_themes():
    themes = list_themes()
    assert "publication" in themes
