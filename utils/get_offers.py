"""A script to manage scrapers and db populator"""

from scrapers.scrape_fly4free import Scraper as s_f4f
from scrapers.scrape_wp import Scraper as s_wp
from scrapers.populator import populate_db

if __name__ == '__main__':
    populate_db(s_f4f().scrape())
    populate_db(s_wp().scrape())


