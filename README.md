# eumaps-py

Publication-ready EU and NUTS choropleth maps in Python.

## Why eumaps-py?

`eumaps-py` is a lightweight helper for common EU choropleth workflows. It loads official GISCO NUTS boundaries, joins them with tabular data, and produces clean map outputs with minimal boilerplate.

## Installation

```bash
pip install eumaps-py
```

## Quick example

```python
import pandas as pd
from eumaps import choropleth

df = pd.DataFrame({
    "NUTS_ID": ["NL22", "BE10", "DE11", "FR10"],
    "value": [10, 20, 15, 25],
})

fig, ax = choropleth(data=df, region_col="NUTS_ID", value_col="value", nuts_level=2)
```

## Development

```bash
pip install -e ".[dev,docs,interactive]"
pytest
ruff check .
mkdocs build
```
