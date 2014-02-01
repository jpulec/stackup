import requests
import xml.etree.ElementTree as ET
import datetime
import json
import fuzzyset
from fuzzywuzzy import process
from bs4 import BeautifulSoup
from django.conf import settings

from stackup.apps.main.models import Region, StandardOfLiving, Geocode

def calculate_standards():
    for region in Region.objects.all():
        if region.cl_rent:
            year_rent = region.cl_rent * 12
            for star in range(5):
                if region.crime_score > (5 - star) * 20 and star != 0:
                    try:
                        StandardOfLiving.objects.get(region=region, star_level=star+1).delete()
                    except StandardOfLiving.DoesNotExist as e:
                        print e
                    continue
                standard, created = StandardOfLiving.objects.get_or_create(region=region, star_level=star+1, defaults={'threshold' : year_rent + (star + 1) * region.star_difference})
                standard.threshold = year_rent + (star + 1) * region.star_difference
                standard.save()

def calculate_crime_score():
    url = "http://sanfrancisco.crimespotting.org/crime-data?format=json&count=10000"
    r = requests.get(url)
    data = r.json()
    regions = {}
    for crime in data['features']:
        neighborhood = None
        try:
            neighborhood = Geocode.objects.get(lat=crime['geometry']['coordinates'][1], lng=crime['geometry']['coordinates'][0]).neighborhood
        except Geocode.DoesNotExist as e:
            print e
            geocode_url = "http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=true" % (crime['geometry']['coordinates'][1], crime['geometry']['coordinates'][0]) 
            r = requests.get(geocode_url)
            geo_data = r.json()
            try:
                neighborhood = geo_data['results'][0]['address_components'][2]['long_name']
                Geocode.objects.create(lat=crime['geometry']['coordinates'][1], lng=crime['geometry']['coordinates'][0], neighborhood=neighborhood)
            except Exception as e:
                print e
                continue
        if neighborhood  not in regions:
            regions[neighborhood] = 0
        crime_type = crime['properties']['crime_type']
        if crime_type == 'ROBBERY' or crime_type == 'VEHICLE THEFT' or crime_type == "THEFT" or crime_type == "BURGLARY":
            regions[neighborhood] += 5
        elif crime_type == "NARCOTICS":
            regions[neighborhood] += 3
        elif crime_type == "SIMPLE ASSAULT":
            regions[neighborhood] += 10
        elif crime_type == "ALCOHOL":
            regions[neighborhood] += 2
        elif crime_type == "VANDALISM":
            regions[neighborhood] += 1
        else:
            print crime_type
    fuzzy = [ region.name for region in Region.objects.all() ]
    for k, v in regions.iteritems():
        match = process.extractOne(k.replace("District", "").replace("The", ""), fuzzy)
        if match[1] > 79:
            print k + ":" + unicode(match)
            region = Region.objects.get(name=match[0])
            region.crime_score = v
            region.save()




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
