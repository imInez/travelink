"""A script to manage scrapers and db populator"""
from utils.scrapers.scrape_fly4free import Scraper as scraper_f4f
from utils.scrapers.scrape_wp import Scraper as scraper_wp
from utils.scrapers.populator import populate_db

if __name__ == '__main__':
    populate_db(scraper_f4f.scrape())
    populate_db(scraper_wp.scrape())


