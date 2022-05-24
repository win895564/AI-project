# -*- coding: utf-8 -*-
"""
Created on Mon May 16 20:45:51 2022

@author: user
"""

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import os 

print('Start to catch air_quality ....')
PATH='K:/Users/user/Desktop/chromedriver.exe'

town_list=[]


driver = webdriver.Chrome(PATH)
driver.get('https://airtw.epa.gov.tw/')#進入首頁
time.sleep(2)
country=driver.find_element_by_xpath('//*[@id="ddl_county"]/option[8]')
country.click()

for i in range(1,6):
            township=driver.find_element_by_xpath(f'//*[@id="ddl_site"]/option[{i}]')
            township.click()
            town_name=[]
            time.sleep(2)
            monitor_time=driver.find_element_by_xpath('//*[@id="th_area"]/div/div[1]/aside/div/div[2]/div[1]')
            air_quality=driver.find_element_by_xpath('//*[@id="aqicircle"]/div')
            
            PM2_5=driver.find_element_by_xpath('//*[@id="th_area"]/div/div[1]/aside/div/div[2]/ul/li[1]')
            
            PM10=driver.find_element_by_xpath('//*[@id="th_area"]/div/div[1]/aside/div/div[2]/ul/li[2]')
            
            O3=driver.find_element_by_xpath('//*[@id="th_area"]/div/div[1]/aside/div/div[2]/ul/li[3]')
            
            CO=driver.find_element_by_xpath('//*[@id="th_area"]/div/div[1]/aside/div/div[2]/ul/li[4]')
            
            SO2=driver.find_element_by_xpath('//*[@id="th_area"]/div/div[1]/aside/div/div[2]/ul/li[5]')
            
            NO2=driver.find_element_by_xpath('//*[@id="th_area"]/div/div[1]/aside/div/div[2]/ul/li[6]')
            
            
            import re
            
            town_name.append(re.split("\n",monitor_time.text))
            town_name.append(re.split("\n",air_quality.text))
            town_name.append(re.split("\n",PM2_5.text))
            town_name.append(re.split("\n",PM10.text))
            town_name.append(re.split("\n",O3.text))
            town_name.append(re.split("\n",CO.text))
            town_name.append(re.split("\n",SO2.text))
            town_name.append(re.split("\n",NO2.text))
            
            town_list.append(town_name)
            print(town_name)
            
        
        
driver.quit()  