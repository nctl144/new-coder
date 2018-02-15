#!usr/bin/env bash

# be sure to change both virtualenv directory and scrape/living_social
# directory to where your venv and code is.
source $WORKON_HOME/scrape/bin/activate
cd /Users/nguyenlam/Desktop/new-coder/scrape_workspace/scraper_app
scrapy crawl livingsocial
