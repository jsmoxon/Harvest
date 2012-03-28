import urllib
import json as json

api_address_0 = "http://maps.googleapis.com/maps/api/geocode/json?address="
api_address_1 = "&sensor=false"

def geo_code(address, city, state, zip):
    link = str(api_address_0+address+" "+city+" "+state+" "+zip+api_address_1)
    open = urllib.urlopen(link)
    result = json.load(open)
    try:
        lat = result['results'][0]['geometry']['location']['lat']
        lng = result['results'][0]['geometry']['location']['lng']
    except:
        lat = 37.92977070
        lng = -122.32791480
    list = [lat, lng]
    return list
