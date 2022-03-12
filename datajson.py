# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:27:15 2022

@author: user
"""
from openpyxl import Workbook 
import re
import requests
from requests_html import HTMLSession
wb=Workbook()
ws=wb.active

head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
url='https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/427399ff97c2860b7656e42e2e95e0ad?q=VTJGc2RHVmtYMTkrV3R1aHVZZnpzbFlrc2RxSUM4Q2tuYWxJRURZYUxjV3gzYS82SGF5TFo0VWlaMWJPby8vSnQrMzRKWENIKzluMWsxaXRWbkRsb0h2TkUwL2lxSXBLaEVRSzJOVW1jeTJTQjJXTjRzRHpvZURHS2YvRlhvTnBjVnhoM09HaEFxelp6Sm5Odnl1TjlUUHoxZE4yY3ZJSUs5YXRqYkgzR256MGlVMTdoM3pVbFYvZVpDM1FUNHRzZTB1Smc5NWhvNC90SFBMY21sa1F2K2dzRG9McnduejlrZGJuZUl6a0dCblRxa3BWamxJMTJDTzJqUWw5eTRkd0lhQ1BFWWJ3d2ZBMGZ0cVNYbXRBNE5XUzJJREU0ODJFaDFpdUJOTjBqT3h6UnFnSXNNMXY1d1VVSE1Uc2FWekM0TlVwSldUZ1NoSVEvMWtGeWRhVmJnTHl4bHViMGJ5ajBJajdtSEgzVHJMY0xlTkhJTFdXeGw0RGtmSHl4c25OallMbGY5MVlYaXhmbGZ3VmdqTmdxSlZ1U0pSaTUxSXpObjcvaWc3b1pPTjJYeTZ3MUlrV1B6QnNQay9Ca2llWWw1VFlVdGxFL0ljZ0J2U2xkRmQ1WGtYVmI4aEczT3RDeUdpVjJvMDVDOXhJVlJmWlJGbEpCUTV4YUdTdHExS2ZrM1lmYnIxMllTdU9reGxaMW12QWZCME1FOXdRZlZMZW1VQXVtRVFGcEZJPQ=='
r=requests.get(url=url,headers=head)
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
        course.append(str(int(s1)/10000))
        course.append(data['s'])
        ws.append(course)

wb.save('shalu.xlsx')
print('已存為shalu.xlxs')    

    
    
