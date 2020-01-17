import requests
from bs4 import BeautifulSoup
import re
import datetime


class Scraper:
    """ Scraper customized for wakacyjni piraci """
    def __init__(self):
        self.pages = range(1, 2)
        self.offers = []


    def convert_date(self, date):
        now = datetime.datetime.now()
        number, time, text = date.split(' ')
        number=int(number)

        if 'min' in time:
            added = now - datetime.timedelta(minutes=number)
        elif 'godz' in time:
            added =  now - datetime.timedelta(hours=number)
        elif 'dzień' in time or 'dni' in time:
            added = now - datetime.timedelta(days=number)
        elif 'tydz' in time or 'tyg' in time:
            added = now - datetime.timedelta(days=7*number)
        elif 'mies' in time:
            added = datetime.datetime(now.year, now.month-number, now.day, now.hour, now.minute)
        return added.strftime('%Y-%m-%d %H:%M')

    def scrape(self):
        for page in self.pages:
            wp = f'https://www.wakacyjnipiraci.pl/?page={str(page)}'
            source = requests.get(wp).text
            soup = BeautifulSoup(source, 'lxml')
            for item in soup.find_all(class_='sc-1vhgtvv-3 guGzEY'):
                try:
                    text = item.find(class_='sc-1wzqm87-1 ffFVpK')
                    site_id = text['data-deal-id']
                    added = text.find(class_='te7pni-0 uLlo').text
                    location, city, country = '','',''
                    address = text['href']
                    title = text.find(class_='sc-1wzqm87-4 eCZHnk').text
                    price = int(''.join(re.findall(r'\d+',text.find(class_='iuh6hk-1 csqdQc').text)))
                    img = text.find('noscript').img['src']
                except KeyError:
                    pass
                else:
                    # a date needs to be formatted to fit DateTimeField
                    added_date_time = self.convert_date(added)
                    self.offers.append({'id': site_id, 'added': added_date_time, 'address': address, 'location': location, 'city': city,
                                   'country': country, 'title': title, 'price': price, 'img': img})
        return self.offers


