# insert data from fly4free

# import json
# from main.models import Travel
#
#
# with open('../data/fly4free/type1.json') as data:
#      offers = json.load(data)
#
# for o in offers:
#   if not Travel.objects.all().filter(site_id=o['id']):
#       o = Travel(site_id=o['id'], added=o['added'], price=o['price'], place=o['place'], img_link=o['img'], title=o['title'], title2=o['title2'], address=o['address'], summary=o['summary'], summary_cont=o['summary_cont'], promo_dates=o['promo_dates'], promo_price=o['promo_price'])
#       o.save()
#


# insert data from wakacyjnipiraci
# import json
# from main.models import Travel
#
#
# with open('../data/wp/data_wp.json') as data:
#      offers = json.load(data)
#
# for o in offers:
#   if not Travel.objects.all().filter(site_id=o['id']):
#       o = Travel(site_id=o['id'], added=o['added'], price=o['price'], place=o['city'], img_link=o['img'], title=o['title'], address=o['address'])
#       o.save()
#

# update added
# import json
# from main.models import Travel

# import json
# from main.models import Travel

# for o in offers:
#   if Travel.objects.all().filter(site_id=o['id']):
#   offer = Travel.objects.all().filter(site_id=o['id']).first()
#   offer.added = o['added']
#   offer.save()




