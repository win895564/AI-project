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
print('輸入url:')
url=input()
print('輸入檔名:')
file_name=input()
#url='https://lvr.land.moi.gov.tw/SERVICE/QueryPrice/d5e11d41d43c30db850da4a09bbe59ce?q=VTJGc2RHVmtYMS9NWEZyditJVzRJaUpHT3pEMDhJMHY1T3BjdFF5MWlMYzJPTWhlM2tzV1JBeGVkUDhxb2JXMEhwMmJFb1JzV3JIUEk5dmttMGtsTk81aW1qVUVvLzdrb3d2azJiblRGOVlaQmk0UGxTUmVSNk5RMkYxOWJZTnF0R0wxMXJBb2xnd2xpVUxBSGpncVlJSnhsRFluSG0vdEp4K09OeGFNRXFJbVV2QzMxY2dXWFplb2EzNldQbUk3WGYzWVE3SDM0bno4TTlnR2tkemxvM0JBNEVmVS9ieEpFamUrcnh4S2E1TDFyaUtLRVdXem9abEIrS1huaVhpNzQ0dkRzUmZ2ZjFVKzJHL1VPemxxbHpXQ21tbTNHUUtGcmNvbmJnenhDQ2RBWGI3K0FmclBDMXlZVWtQa3dMUDNmK3pIbnpDOWlJMTBRSVMybDJ1SENUeFA0TXllQW8rTXpoUGlkWWs3VnZoSTAyNUE0VXhxUTdLM3BXYkJDejhzMUh0Y2ZyY2VpU2pCV3l3YW8xQmVwUk5oQXViS2RJMUtxVWRTdnUrZ1hnamVySXlKa0w5alp6MTU3WDUzQzByY1dwcFRGU3FpZkdUVkhYczJ2NnB0V1gvUmVkclpTMGNxTDdGVU1rLzIyWCtHbG1TM2d0TVJSbU9CS0hsQytxejZXWlBGRGFQbytMQ0labVZmdld0dHhrUzlwa0k1SzlaelZEMnVqS0JGTWlrPQ=='
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
        a_tmp=re.split('#',data['a'])
        course.append(a_tmp[1])
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
        a_tmp=re.split('#',data['a'])
        course.append(a_tmp[1])#地址格是為xxxx#xxxx 一方面有編碼問題 另一方面是
        course.append(data['e'])
        course.append(data['g'])
        course.append(data['pu'])
        course.append(data['tp'])
        course.append(str(round(int(s1)/10000,2)))
        course.append(data['s'])
        ws.append(course)

wb.save(f'{file_name}.xlsx')
print('儲存完成!')  

    
    
