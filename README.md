# The Met Art Dataset Builder

A Python toolkit for scraping and filtering artwork metadata and images from the Metropolitan Museum of Art's public API.

## Documentation

A full documentation can be found here: 

[![Documentation](https://img.shields.io/badge/docs-MkDocs-blue.svg)](https://ulisesrey.github.io/the_met_art_dataset/)

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
    "output": "data/dbs/art_db.json"
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

Example output:

```
Full URL sent by Python: https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=True&departmentId=20&q=%2A
✅ Saved 'Hunting and fishing scenes' as 229770.jpg
✅ Saved 'Quilt' as 229936.jpg
✅ Saved 'Cravat end' as 227284.jpg
✅ Saved 'Length of velvet' as 219394.jpg
✅ Saved 'Petticoat panel' as 229993.jpg
✅ Saved 'Aglauros's Vision of the Bridal Chamber of Herse' as 226696.jpg
Photo 488551 not of public domain
Photo 269091 not of public domain
```

### Filtering artwork records

Filter out artwork by department keyword:

```bash
make filter
```

Or with custom parameters:

```bash
uv run the_met_art_dataset/filter.py --input data/dbs/art_db.json --output data/dbs/filtered.json --exclude european
```

## Project Organization

```
.
├── data
│   ├── dbs                     <- JSON databases of scraped artwork metadata
│   └── images                  <- Downloaded artwork images
├── docs                        <- MkDocs project documentation
├── LICENSE                     <- Open-source license
├── Makefile                    <- Commands like `make scrape` or `make filter`
├── pyproject.toml              <- Project configuration and dependencies
├── README.md                   <- Top-level README for developers
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
