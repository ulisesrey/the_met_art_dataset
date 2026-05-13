# Getting Started

## Installation

```bash
uv sync
```

## Configuration

Edit `the_met_art_dataset/config.json` to set your scraping parameters:

```json
{
    "isHighlight": "true",
    "departmentId": 19,
    "q": "*",
    "limit": 200,
    "output": "data/dbs/art_db.json"
}
```

| Field | Description |
|---|---|
| `isHighlight` | Only return highlighted objects (`"true"` / `"false"`) |
| `departmentId` | Filter by [Met department ID](https://metmuseum.github.io/#departments) |
| `q` | Search query string (`"*"` returns all) |
| `limit` | Maximum number of objects to scrape |
| `output` | Path to the output JSON file |

## Scraping

```bash
make scrape
```

Or directly:

```bash
uv run the_met_art_dataset/scraper.py -config the_met_art_dataset/config.json
```

Example output:

```
Full URL sent by Python: https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=True&departmentId=20&q=%2A
✅ Saved 'Hunting and fishing scenes' as 229770.jpg
✅ Saved 'Quilt' as 229936.jpg
✅ Saved 'Cravat end' as 227284.jpg
Photo 488551 not of public domain
Photo 269091 not of public domain
```

Images are saved to `data/images/` and metadata to the path defined in `output`.

## Filtering

```bash
make filter
```

Or with custom parameters:

```bash
uv run the_met_art_dataset/filter.py \
  --input data/dbs/art_db.json \
  --output data/dbs/filtered.json \
  --exclude asian
```
