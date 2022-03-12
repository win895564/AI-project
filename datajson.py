# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:27:15 2022

@author: user
"""
from selenium import webdriver
from openpyxl import Workbook 
import re
import requests
from requests_html import HTMLSession
wb=Workbook()
ws=wb.active
opt=webdriver.ChromeOptions()
opt.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62')
opt.add_argument("disable-blink-features=AutomationControlled")

url='https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/418a148edffc9b673ffd70f20d0f7ff3?q=VTJGc2RHVmtYMS9ESG04Qjg2UXlsbVd1QklrY2dYTW9DUW1mcGJoSzdaeVo4dkVteUtvNnBOSzdRYkh0NjNDOGV5a1owOHhxclB2dGxjSXdSUTdsb2dqelJPYkNPVGdwdE52a2NrNll3cjExdmh5TUUvd1pFTzNsNnhiaHBzL0NlZHd0Rk5zQVEwa0U0YlBOYXdhaGErV2hPbDRmQy9FbHJCU2Q3Mm04UHEySWxQeW1lNHhNOXBIWEhxYWRHVmk4YmZqUGxPVi9yWk0wbGE4dm5yTXZuQk52NlEvb3RWK1FKLzlHTjhMT3BQakpGUE5xYitOK0ZlTU9tZE9JSmpzbzcvcmhCYjF1T3BsWVB0YjRZZmtXZVFuWUs0VmJ3R2s2ZVN1VHNPc1N6MUtZbjU1RmZJcWtiTjl2WnlmNFlhU3h4ZC9XSC9HaWFPdTN1eE0wWjZGRm1jcmQ4WFhMOEw3SUwzOGVvd1lpMDdSWE1zNEI5MnhVRGRJN3ZDeDIyMVVlemdZekRvK2JQcG9aaXRnWDJhL2NlTldqY3ExRWN3c1NvSGw0Vnd1R21WQW5IZ2hXa3J6QjBFZVpZdGZMUlpNRUJWbEJ0OGpVcXBzWVFWdnA3bDJuMnVmWjJtU0E5a2RTWTI2TllYRkZreU1CVWZYRmNham5Ta3krWlRQMnc4Y08rRXRZOGF2eXJaMTNxekhySWNBbFhlSThSU2dTaUZPRHZpdUphaWMyc1NvPQ=='

r=requests.get(url)

root_json=r.json()
title=['地段位置','交易日期','屋齡','主要用途','總售價(萬元)','單價(萬元)/坪','總面積(坪)']
ws.append(title)
count=0
print(f'查詢到:{len(root_json)}筆資料')

for data in root_json:
    if len(data['p']) ==0:
        count+=1
        course=[]
        course.append(data['a'])
        course.append(data['e'])
        course.append(data['g'])
        course.append(data['pu'])
        course.append(data['tp'])
        course.append(data['p'])
        course.append(data['s'])
        ws.append(course)

    else:
        s=str(data['p'])
        s1=s.replace(r',','')
        count+=1
        course=[]
        
        course.append(data['a'])
        course.append(data['e'])
        course.append(data['g'])
        course.append(data['pu'])
        course.append(data['tp'])
        course.append(str(round(int(s1)/10000,2)))
        course.append(data['s'])
        ws.append(course)

wb.save('test.xlsx')
print('儲存完成!')    


    
    
