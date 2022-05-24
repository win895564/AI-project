# -*- coding: utf-8 -*-
"""
Created on Tue May 17 19:06:44 2022

@author: user
"""

#沙鹿https://airtw.epa.gov.tw/json/airlist/airlist_26_2022051718.json? 
#西屯https://airtw.epa.gov.tw/json/airlist/airlist_25_2022051718.json?
#忠明https://airtw.epa.gov.tw/json/airlist/airlist_28_2022051718.json?
#大里https://airtw.epa.gov.tw/json/airlist/airlist_7_2022051718.json?
#豐原https://airtw.epa.gov.tw/json/airlist/airlist_74_2022051718.json?
import requests
from datetime import datetime,timezone,timedelta
airquality=[]
def air_catch():
    for _ in range(0,5):
        if _ ==0:
            monitor_key=26
            shalu=[]
            dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
            dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
            
            #print('UTC \t%s\nUTC+8\t%s'%(dt1,dt2))
            #print(dt2.strftime("%Y-%m-%d %H:%M:%S")) # 將時間轉換為 string
            YEAR=str(dt2.year)
            ZERO=str(0)
            MONTH=str(dt2.month)
            DAY=str(dt2.day)
            HOUR=str(dt2.hour-1)
            if len(HOUR)==2:
               r=requests.get(f'https://airtw.epa.gov.tw/json/airlist/airlist_{monitor_key}_{YEAR+ZERO+MONTH+DAY+HOUR}.json?')
               quality=r.json()
            else:
               r=requests.get(f'https://airtw.epa.gov.tw/json/airlist/airlist_{monitor_key}_{YEAR+ZERO+MONTH+DAY+ZERO+HOUR}.json?')
               quality=r.json()
            shalu.append(quality[0]['date'])
            shalu.append(quality[2]['sitename'])
            shalu.append(int(quality[4]['AQI']))
            shalu.append(quality[5]['AVPM25'])
            shalu.append(quality[6]['PM25_FIX'])
            shalu.append(quality[7]['AVPM10'])
            shalu.append(quality[8]['PM10_FIX'])
            shalu.append(quality[9]['AVO3'])
            shalu.append(quality[10]['O3_FIX'])
            shalu.append(quality[11]['AVCO'])
            shalu.append(quality[12]['CO_FIX'])
            shalu.append(quality[13]['SO2_FIX'])
            shalu.append(quality[14]['NO2_FIX'])
            
        elif _ == 1:
            monitor_key=25
            xitun=[]
            dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
            dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
            
            #print('UTC \t%s\nUTC+8\t%s'%(dt1,dt2))
            #print(dt2.strftime("%Y-%m-%d %H:%M:%S")) # 將時間轉換為 string
            YEAR=str(dt2.year)
            ZERO=str(0)
            MONTH=str(dt2.month)
            DAY=str(dt2.day)
            HOUR=str(dt2.hour-1)
            
            if len(HOUR)==2:
               r=requests.get(f'https://airtw.epa.gov.tw/json/airlist/airlist_{monitor_key}_{YEAR+ZERO+MONTH+DAY+HOUR}.json?')
               quality=r.json()
            else:
               r=requests.get(f'https://airtw.epa.gov.tw/json/airlist/airlist_{monitor_key}_{YEAR+ZERO+MONTH+DAY+ZERO+HOUR}.json?')
               quality=r.json()
            xitun.append(quality[0]['date'])
            xitun.append(quality[2]['sitename'])
            xitun.append(int(quality[4]['AQI']))
            xitun.append(quality[5]['AVPM25'])
            xitun.append(quality[6]['PM25_FIX'])
            xitun.append(quality[7]['AVPM10'])
            xitun.append(quality[8]['PM10_FIX'])
            xitun.append(quality[9]['AVO3'])
            xitun.append(quality[10]['O3_FIX'])
            xitun.append(quality[11]['AVCO'])
            xitun.append(quality[12]['CO_FIX'])
            xitun.append(quality[13]['SO2_FIX'])
            xitun.append(quality[14]['NO2_FIX'])
        elif _ == 2:
            monitor_key=28
            zonming=[]
            dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
            dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
            
            #print('UTC \t%s\nUTC+8\t%s'%(dt1,dt2))
            #print(dt2.strftime("%Y-%m-%d %H:%M:%S")) # 將時間轉換為 string
            YEAR=str(dt2.year)
            ZERO=str(0)
            MONTH=str(dt2.month)
            DAY=str(dt2.day)
            HOUR=str(dt2.hour-1)
            
            if len(HOUR)==2:
               r=requests.get(f'https://airtw.epa.gov.tw/json/airlist/airlist_{monitor_key}_{YEAR+ZERO+MONTH+DAY+HOUR}.json?')
               quality=r.json()
            else:
               r=requests.get(f'https://airtw.epa.gov.tw/json/airlist/airlist_{monitor_key}_{YEAR+ZERO+MONTH+DAY+ZERO+HOUR}.json?')
               quality=r.json()
            zonming.append(quality[0]['date'])
            zonming.append(quality[2]['sitename'])
            zonming.append(int(quality[4]['AQI']))
            zonming.append(quality[5]['AVPM25'])
            zonming.append(quality[6]['PM25_FIX'])
            zonming.append(quality[7]['AVPM10'])
            zonming.append(quality[8]['PM10_FIX'])
            zonming.append(quality[9]['AVO3'])
            zonming.append(quality[10]['O3_FIX'])
            zonming.append(quality[11]['AVCO'])
            zonming.append(quality[12]['CO_FIX'])
            zonming.append(quality[13]['SO2_FIX'])
            zonming.append(quality[14]['NO2_FIX'])
        elif _ == 3:
            monitor_key=7
            dali=[]
            dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
            dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
            
            #print('UTC \t%s\nUTC+8\t%s'%(dt1,dt2))
            #print(dt2.strftime("%Y-%m-%d %H:%M:%S")) # 將時間轉換為 string
            YEAR=str(dt2.year)
            ZERO=str(0)
            MONTH=str(dt2.month)
            DAY=str(dt2.day)
            HOUR=str(dt2.hour-1)
            
            if len(HOUR)==2:
               r=requests.get(f'https://airtw.epa.gov.tw/json/airlist/airlist_{monitor_key}_{YEAR+ZERO+MONTH+DAY+HOUR}.json?')
               quality=r.json()
            else:
               r=requests.get(f'https://airtw.epa.gov.tw/json/airlist/airlist_{monitor_key}_{YEAR+ZERO+MONTH+DAY+ZERO+HOUR}.json?')
               quality=r.json()
            dali.append(quality[0]['date'])
            dali.append(quality[2]['sitename'])
            dali.append(int(quality[4]['AQI']))
            dali.append(quality[5]['AVPM25'])
            dali.append(quality[6]['PM25_FIX'])
            dali.append(quality[7]['AVPM10'])
            dali.append(quality[8]['PM10_FIX'])
            dali.append(quality[9]['AVO3'])
            dali.append(quality[10]['O3_FIX'])
            dali.append(quality[11]['AVCO'])
            dali.append(quality[12]['CO_FIX'])
            dali.append(quality[13]['SO2_FIX'])
            dali.append(quality[14]['NO2_FIX'])
        elif _ == 4:
            monitor_key=74
            fengyun=[]
            dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
            dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
            
            #print('UTC \t%s\nUTC+8\t%s'%(dt1,dt2))
            #print(dt2.strftime("%Y-%m-%d %H:%M:%S")) # 將時間轉換為 string
            YEAR=str(dt2.year)
            ZERO=str(0)
            MONTH=str(dt2.month)
            DAY=str(dt2.day)
            HOUR=str(dt2.hour-1)
            
            if len(HOUR)==2:
               r=requests.get(f'https://airtw.epa.gov.tw/json/airlist/airlist_{monitor_key}_{YEAR+ZERO+MONTH+DAY+HOUR}.json?')
               quality=r.json()
            else:
               r=requests.get(f'https://airtw.epa.gov.tw/json/airlist/airlist_{monitor_key}_{YEAR+ZERO+MONTH+DAY+ZERO+HOUR}.json?')
               quality=r.json()
            fengyun.append(quality[0]['date'])
            fengyun.append(quality[2]['sitename'])
            fengyun.append(int(quality[4]['AQI']))
            fengyun.append(quality[5]['AVPM25'])
            fengyun.append(quality[6]['PM25_FIX'])
            fengyun.append(quality[7]['AVPM10'])
            fengyun.append(quality[8]['PM10_FIX'])
            fengyun.append(quality[9]['AVO3'])
            fengyun.append(quality[10]['O3_FIX'])
            fengyun.append(quality[11]['AVCO'])
            fengyun.append(quality[12]['CO_FIX'])
            fengyun.append(quality[13]['SO2_FIX'])
            fengyun.append(quality[14]['NO2_FIX'])
            return shalu,xitun,zonming,dali,fengyun
        