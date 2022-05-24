# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 11:49:38 2022

@author: user
"""

from bs4 import BeautifulSoup as bs
import requests

def catch():
    News=[]
    r=requests.get('https://www.storm.mg/category/k4747')
    soup=bs(r.text,'html.parser')
    soup_img=soup.find_all('img',class_='card_img')
    soup_link=soup.find_all('a',class_='card_link link_title')
    soup_title=soup.find_all(class_='card_title')
    soup_substance=soup.find_all('a',class_='card_substance')
    soup_time=soup.find_all('span',class_='info_time')
    
    for link,img,title ,sub ,s_time in zip(soup_link,soup_img,soup_title,soup_substance,soup_time):
        News.append([title.text,sub.text,link.get('href'),str(img.get('src')).replace('150x150','855x445') ,s_time.text])
    del News[0]    
    return News
    

    
