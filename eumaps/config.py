from pathlib import Path

CACHE_DIR = Path.home() / ".cache" / "eumaps"
VALID_NUTS_LEVELS = {0, 1, 2, 3}
VALID_RESOLUTIONS = {"01M", "03M", "10M", "20M", "60M"}
