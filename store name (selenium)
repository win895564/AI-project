from selenium import webdriver
from bs4 import BeautifulSoup 
import requests


driver=webdriver.Chrome()
driver.get('https://www.google.com.tw/maps/search/%E5%9E%82%E6%A5%8A%E9%87%8C+%E5%85%A8%E5%AE%B6/@23.4734576,120.4184991,14z/data=!3m1!4b1?hl=zh-TW')
soup = BeautifulSoup(driver.page_source,"lxml")
all_reviews = soup.find_all(class_='MVVflb-haAclf V0h1Ob-haAclf-d6wfac MVVflb-haAclf-uxVfW-hSRGPd')
for i in all_reviews:
    print(i.text)

