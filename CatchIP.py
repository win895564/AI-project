# -*- coding: utf-8 -*-
"""
Created on Thu May  5 01:00:05 2022

@author: user
"""
from bs4 import BeautifulSoup as bs
import requests 
def catch_ip():
    r=requests.get('https://myip.com.tw/')
    soup=bs(r.text,'html.parser')
    soup_ip=soup.find('font')
    IP=soup_ip.text
    return IP
