import requests
import xml.etree.ElementTree as ET
import datetime
from django.conf import settings

from stackup.apps.main.models import Region, StandardOfLiving

def scrape_trulia():
    neighborhoods_url = "http://api.trulia.com/webservices.php?library=LocationInfo&function=getNeighborhoodsInCity&city=San Francisco&state=CA&apikey=%s" % settings.TRULIA_API
    r = requests.get(neighborhoods_url)
    tree = ET.fromstring(r.text)
    for neighborhood in tree.iter('neighborhood'):
        n, created = Region.objects.get_or_create(name=neighborhood.find('name').text)
        if not n.trulia_id:
            n.trulia_id = neighborhood.find('id').text
            n.save()
    for region in Region.objects.all():
        stats_url = "http://api.trulia.com/webservices.php?library=TruliaStats&function=getNeighborhoodStats&neighborhoodId=%s&startDate=%s&endDate=%s&apikey=%s" % (region.trulia_id, datetime.date.today() - datetime.timedelta(days=100), datetime.date.today(), settings.TRULIA_API,)
        r = requests.get(stats_url)
        tree = ET.fromstring(r.text)
        for subcategory in tree.iter('subcategory'):
            if subcategory.find('type').text == "1 Bedroom Properties":
                region.trulia_rent = subcategory.find('averageListingPrice').text
                region.save()


def calculate_standards():
    for region in Region.objects.all():
        if region.trulia_rent:
            rent = region.trulia_rent / 100 #divide out cents
            year_rent = rent * 12
            for star in range(5):
                standard, created = StandardOfLiving.objects.get_or_create(region=region, star_level=star+1, defaults={'threshold' : year_rent + (star + 1) * region.star_difference})
                standard.threshold = year_rent + (star + 1) * region.star_difference
                standard.save()
