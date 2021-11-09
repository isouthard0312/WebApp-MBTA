# Useful URLs (you need to add the appropriate parameters for your requests)
import requests
import json
from pprint import pprint
import urllib.request
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "sojSRbboeBG051BY1bDEYiC8Rz1OkDAy"
MBTA_API_KEY = "15fe15f4c764417f9de1742a3f12ede6"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    url_map = urllib.request.urlopen(url)
    response_text = url_map.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    
    url = urllib.request.urlopen(
        f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}')
    response_text = url.read().decode('utf-8')
    response_data = json.loads(response_text)
    dict_values = response_data["results"][0]["locations"][0]["displayLatLng"]
    lat = dict_values.pop('lat') #this separates the values that were given from the response data.
    lng = dict_values.pop('lng')
    print(f"Latitude: {lat}")
    print(f"Longitude: {lng}") 
    



def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    #/Stop/ApiWeb_StopController_index for URL
    See https://api-v3.mbta.com/docs/swagger/index.html
    formatting requirements for the 'GET /stops' API.
    """
    url = urllib.request.urlopen(
        f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}')
    response_text = url.read().decode('utf-8')
    response_data = json.loads(response_text)
    print('The nearest station is: ')
    Name_of_station = print(response_data["data"][0]["attributes"]["name"])
    return Name_of_station


def wheelchair(latitude, longitude):
    url = urllib.request.urlopen(
         f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}')
    response_text = url.read().decode('utf-8')
    response_data = json.loads(response_text)
    Wheelchair_accessible = print(response_data["data"][0]["attributes"]["wheelchair_boarding"])
    print(f'Wheelchair Accessible?: {Wheelchair_accessible} ')
    # for Wheelchair_accessible in response_data:
    #     if Wheelchair_accessible == 1:
    #             return 'yes' #this is not working - trying to make it so that if the wheelchair seats exceed or equal one it will print yes for wheelchair accesibility.
    # return Wheelchair_accessible


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    
    url_map = urllib.request.urlopen(f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}')
    response_text_map = url_map.read().decode('utf-8')
    response_data_map = json.loads(response_text_map)
    dict_values = response_data_map["results"][0]["locations"][0]["displayLatLng"]
    lat = dict_values.pop('lat') 
    lng = dict_values.pop('lng')
    url_mbta = urllib.request.urlopen(f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={lng}')
    response_text_mbta = url_mbta.read().decode('utf-8')
    response_data_mbta = json.loads(response_text_mbta)
    print('The nearest station is: ')
    Name_of_station = print(response_data_mbta["data"][0]["attributes"]['name']) #index here causing problems
    print('Wheelchair Accessible?: ')
    Wheelchair_accessible = print(response_data_mbta["data"][0]["attributes"]["wheelchair_boarding"])
    return Name_of_station, Wheelchair_accessible
    
   




def main():
    """
    You can test all the functions here
    # """
    # get_lat_long('Boston,MA') #no spaces
    # for MapQuest
    # get_json('http://www.mapquestapi.com/geocoding/v1/address?key=sojSRbboeBG051BY1bDEYiC8Rz1OkDAy&location=Boston,MA')
    # for MBTA 
    # get_json('https://api-v3.mbta.com/stops?api_key=15fe15f4c764417f9de1742a3f12ede6&sort=distance&filter%5Blatitude%5D=42.358894&filter%5Blongitude%5D=-71.056742')
    # get_nearest_station("42.358413", "-71.056499")
    # wheelchair("42.358413", "-71.056499")
    # find_stop_near('Boston,MA') 
    # find_stop_near('Wellesley,MA')
    # find_stop_near('Cambrige,MA')
    
if __name__ == '__main__':
    main()
