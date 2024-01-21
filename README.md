# Analyze

```
poetry install
```

```
poetry run python src/index_analyze/download_data.py  > data/nasdaq-comp.json
cat data/nasdaq-comp.json | poetry run python src/index_analyze/main.py
```
