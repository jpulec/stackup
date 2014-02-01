import requests
import xml.etree.ElementTree as ET
import datetime
from bs4 import BeautifulSoup
from django.conf import settings

from stackup.apps.main.models import Region, StandardOfLiving

def calculate_standards():
    for region in Region.objects.all():
        if region.cl_rent:
            year_rent = region.cl_rent * 12
            for star in range(5):
                standard, created = StandardOfLiving.objects.get_or_create(region=region, star_level=star+1, defaults={'threshold' : year_rent + (star + 1) * region.star_difference})
                standard.threshold = year_rent + (star + 1) * region.star_difference
                standard.save()


def scrape_craigslist_neighborhoods():
    url = "http://sfbay.craigslist.org/sfc/apa/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    nh = soup.find(id='nh')
    for n in nh.find_all('option'):
        if n['value']:
            region, created = Region.objects.get_or_create(name=n.string, cl_id=n['value'])

def calculate_avg_rent():
    url = "http://sfbay.craigslist.org/search/apa/sfc?nh=%s"
    for region in Region.objects.all():
        r = requests.get(url % region.cl_id)
        soup = BeautifulSoup(r.text)
        rows = soup.find(id='toc_rows')
        content = rows.find('div', class_='content')
        total_price = 0
        total_number = 0
        for row in content.find_all('p', class_="row"):
            try:
                price = row.find('span', class_='l2').find('span', class_='price').string
                total_price += int(price[1:])
                total_number += 1
            except Exception as e:
                print e
        if total_number > 0:
            region.cl_rent = int( total_price / total_number )
            region.save()
