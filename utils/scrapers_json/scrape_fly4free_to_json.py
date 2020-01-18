import requests
from bs4 import BeautifulSoup


class Scraper:
    """ Scraper customized for fly4free """
    def __init__(self):
        self.type1_all = []
        self.type2_all = []
        self.type3_all = []
        self.all_types = []
        self.pages = range(1, 3)

    def get_month(self, value):
        """ Translate month from str to number """
        months = {'stycznia': '01', 'lutego': '02', 'marca': '03', 'kwietnia': '04', 'maja': '05', 'czerwca': '06',
                  'lipca': '07', 'sierpnia': '08', 'września': '09', 'października': '10', 'listopada': '11',
                  'grudnia': '12'}
        if value in months:
            return months[value]

    def get_data(self, value):
        """ Format acquired date string to fit DateTimeField """
        value = value.strip()
        date_value, time_value = value.split(',')
        time_value = time_value.strip()
        hour, minute = time_value.split(':')
        day, m, year = date_value.split(' ')
        month = self.get_month(m)
        return f'{year}-{month}-{day} {hour}:{minute}'

    def scrape(self):
        """ Scrape the data """
        for p in self.pages:
            fly4free = f'https://www.fly4free.pl/page/{p}/'
            source = requests.get(fly4free).text
            soup = BeautifulSoup(source, 'lxml')

            # type 1 = travel + attractions ||  just travel
            # type 2 = poland
            # type 3 = travel + accommodation

            for i in range(1, 4):
                for item in soup.find_all(class_='item--type-'+str(i)):
                    if item.find(class_='item__soldout'):
                        continue
                    added = item.find('div', class_='item__date')['title']
                    item_type = f'type{p}'
                    site_id = item['data-pid']
                    price = item.find('div', class_='item__price').text
                    place = item.find('h3', class_='item__route').text
                    title = item.find('h2', class_='item__title').a.text
                    img = item.find('div', class_='item__thumb').img['data-src']
                    title2 = item.find('a', class_='item__details').text
                    address = item.find('a', class_='item__details')['href']

                    details = requests.get(address).text
                    details_soup = BeautifulSoup(details, 'lxml')
                    try:
                        summary = details_soup.find('div', class_='promoSummaryHeader__price text-right').text
                    except AttributeError:
                        summary = ''
                    try:
                        summary_cont = details_soup.find('div', class_='promoSummary__content').text
                    except AttributeError:
                        summary_cont = ''
                    try:
                        promo_dates = details_soup.find('div', class_='promo__dates').text
                    except AttributeError:
                        promo_dates = ''
                    try:
                        promo_price = details_soup.find('div', class_='promo__price--amount').text
                    except AttributeError:
                        promo_price = ''

                    added_date_time = self.get_data(added)
                    self.all_types.append(
                        {'id': site_id, 'added': added_date_time, 'item_type': item_type, 'price': price,
                         'place': place, 'img': img, 'title': title, 'title2': title2,
                         'address': address, 'summary': summary, 'summary_cont': summary_cont,
                         'promo_dates': promo_dates, 'promo_price': promo_price})
        return self.all_types


# with open('data/fly4free/type1.json', 'w') as file:
#     json.dump(type1_all, file)
#
# with open('data/fly4free/type2.json', 'w') as file:
#     json.dump(type2_all, file)
#
# with open('data/fly4free/type3.json', 'w') as file:
#     json.dump(type2_all, file)