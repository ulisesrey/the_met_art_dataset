#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = the_met_art_dataset
PYTHON_VERSION = 3.12
PYTHON_INTERPRETER = uv run

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python dependencies
.PHONY: requirements
requirements:
	uv sync

## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Scrape artwork from the Met Museum API
.PHONY: scrape
scrape:
	$(PYTHON_INTERPRETER) the_met_art_dataset/scraper.py -config the_met_art_dataset/config.json

## Filter artwork records by department keyword
.PHONY: filter
filter:
	$(PYTHON_INTERPRETER) the_met_art_dataset/filter.py

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)
