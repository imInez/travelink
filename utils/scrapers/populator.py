import os
import sys
sys.path.append('/home/thetravelink/travelink/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travelink2.settings')
import django
django.setup()
from main.models import Travel


def populate_db(data):
    for offer in data:
      if not Travel.objects.all().filter(site_id=offer.get('id')):
          travel_offer = Travel(site_id=offer.get('id'), added=offer.get('added'), price=offer.get('price'),
                                place=offer.get('place'), img_link=offer.get('img'), title=offer.get('title'),
                                title2=offer.get('title2'), address=offer.get('address'), summary=offer.get('summary'),
                                summary_cont=offer.get('summary_cont'), promo_dates=offer.get('promo_dates'),
                                promo_price=offer.get('promo_price'))
          travel_offer.save()



# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/travelink1.settings')




