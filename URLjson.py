#This module interacts with the Open
#MapQuest APIs.
#It builds the URLS, makes HTTP requests, and
#parses JSON responses.

import json
import urllib.parse
import urllib.request
from collections import namedtuple

def build_url():
    '''This function builds the URL to recieve information and directions of a
    specific route'''
    MapURL = namedtuple('MapURL', ['url', 'key'])
    url = MapURL(url = 'http://open.mapquestapi.com/directions/v2/route?', key = '680m6kbIdrSAKoAM403LJLGIzVyqzRSr')
    return url

def build_elevation_url():
    '''This function builed the URL to recieve the elevation
    of a specific location.'''
    MapURL = namedtuple('MapURL', ['url', 'key'])
    url = MapURL(url = 'http://open.mapquestapi.com/elevation/v1/profile?', key = '680m6kbIdrSAKoAM403LJLGIzVyqzRSr')
    return url
    
def request_page(arg):
    '''This function requests the page from the MapQuest API
    and then converts it into a dictionary by calling the json.loads function
    on it'''
    response = urllib.request.urlopen(arg)
    data = response.read()
    string_data = data.decode(encoding = 'utf-8')
    info = parse_json(string_data)
    return info
    
def request_elevation_page(arg):
    '''This function requests the elevation page from the MapQuest API and then
    converts it into a dictionary by calling the json.loads function on it'''
    response = urllib.request.urlopen(arg)
    data = response.read()
    string_data = data.decode(encoding = 'utf-8')
    info = parse_json(string_data)
    return info

def complete_url(start : str, to : str):
    '''This function returns the dictionary containing the information and directions
    of a route'''
    arg = build_url()
    search = urllib.parse.urlencode([('key', arg.key), ('from', start), ('to', to)])
    URL = arg.url + search
    info = request_page(URL)
    return info
    
def complete_elevation_url(lat: str, long: str):
    '''This function returns the dictionary conaining the elevation
    pertaining to a specific location.'''
    arg = build_elevation_url()
    search = urllib.parse.urlencode([('key', arg.key), ('unit', 'f')])
    search +='&latLngCollection='
    latslngs = str(lat) + ',' + str(long)
    search+=latslngs
    URL = arg.url + search
    info = request_elevation_page(URL)
    return info
    
    
def parse_json(arg):
    '''This function converts the returned page into a dictionary'''
    obj = json.loads(arg)
    return obj
