# the_met_art_dataset

A Python toolkit for scraping and filtering artwork metadata and images from the Metropolitan Museum of Art's public API.

## Installation

```bash
uv sync
```

## Usage

### Scraping artwork

Configure your scraping parameters in `the_met_art_dataset/config.json`:

```json
{
    "isHighlight": "true",
    "departmentId": 19,
    "q": "*",
    "limit": 200,
    "output": "data/raw/art_db.json"
}
```

Then run:

```bash
make scrape
```

Or directly:

```bash
uv run the_met_art_dataset/scraper.py -config the_met_art_dataset/config.json
```

### Filtering artwork records

Filter out artwork by department keyword:

```bash
make filter
```

Or with custom parameters:

```bash
uv run the_met_art_dataset/filter.py --input data/raw/art_db.json --output data/raw/filtered.json --exclude asian
```

## Project Organization

```
├── LICENSE                     <- Open-source license
├── Makefile                    <- Commands like `make scrape` or `make filter`
├── README.md                   <- Top-level README for developers
├── data
│   └── raw                     <- Original, immutable data dump
├── docs                        <- MkDocs project documentation
├── images                      <- Sample artwork images
├── pyproject.toml              <- Project configuration and dependencies
├── references                  <- Data dictionaries and manuals
└── the_met_art_dataset         <- Source code
    ├── __init__.py
    ├── config.json             <- Scraper configuration
    ├── filter.py               <- Filter artwork by department
    └── scraper.py              <- Scrape Met Museum API
```

## Modules

- `scraper.py` — Scrapes artwork metadata and images from the Met Museum public API
- `filter.py` — Filters artwork records by excluding specific department keywords

## Author
Ulises Rey

--------
