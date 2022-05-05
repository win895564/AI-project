# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:03:49 2022

@author: user
"""

import requests



def getGeoCoord(API_KEY,address):
    params = {
        'key': API_KEY,
        'address': address
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        result = data['results'][0]
        location = result['geometry']['location']
        return location['lat'], location['lng']
    else:
        return
    
