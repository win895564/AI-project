# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:28:16 2022

@author: user
"""

import numpy as np
#import joblib module
import joblib
import datetime



def pre_date(area,orderdate,age,htype,totalarea,build,lobby,bathroom):
    loadModel=joblib.load('taizh_house.pkl')
    date = datetime.date.today()
    year = date.strftime("%Y")
    input_list=[area,orderdate,age,htype,totalarea,build,lobby,bathroom]
    input_array=np.array(input_list).reshape(1,-1)
    pred=loadModel.predict(input_array)
    return pred
def pre_data2(zcode,age,htype,totalarea,room,lobby,bathroom,parking,elevator,manage):
    loadModel=joblib.load('SVRL04.pkl')
    time_list=[11106,11107,11108,11109,
               11110,11111,11112,11201,
               11202,11203,11204,11205,
               11206,11207,11208,11209,
               11210,11211,11212,11301,
               11302,11303,11304,11305,
               11306,11307,11308,11309,
               11310,11311,11312]
    time_tmp=[]
    pred_tmp=[]
    
    for _ in time_list:
        
        zcode=int(zcode)
        orderdate=_
        age=int(age)+0.1
        htype=int(htype)
        totalarea=float(totalarea)
        room=int(room)
        lobby=int(lobby)
        bathroom=int(bathroom)
        land=1
        build=1
        parking=int(parking)
        elevator=int(elevator)
        manage=int(manage)
        TAIEC=-5.3
        CCI=10.21
        SALARY=5.7
        input_list=[443012,443,2028,12,30,2,30,6,2,1,1,1,1,1,0]
        input_list=[zcode,orderdate,age,htype,
                    totalarea,room,lobby,bathroom,
                    land,build,parking,elevator,
                    manage,TAIEC,CCI,SALARY]
        input_array=np.array(input_list).reshape(1,-1)
        pred=list(loadModel.predict(input_array))
        pdarea=int(pred[0])/totalarea
        pred_tmp.append(round(pdarea,1))
        time_tmp.append(str(_+191100))
    return pred_tmp,time_tmp

def linear_svr(zcode_6,zcode_3,totalarea,htype,age,room,lobby,bathroom,parking,elevator,manage):
    loadModel=joblib.load('SVRL07.pkl')
    year_list=[2022,2023,2024,2025,2026,2027,2028]
    month_list=[i for i in range(1,13)]
    time_tmp=[]
    pred_tmp=[]
    for _ in year_list:
        zcode_6=int(zcode_6)
        zcode_3=int(zcode_3)
        year=_
        month=12
        totalarea=float(totalarea)
        htype=int(htype)
        age=int(age)
        room=int(room)
        lobby=int(lobby)
        bathroom=int(bathroom)
        land=1
        build=1
        parking=int(parking)
        elevator=int(elevator)
        manage=int(manage)
        input_list=[zcode_6,zcode_3,year,month,totalarea,htype,age,room,lobby,bathroom,land,build,parking,elevator,manage]
        input_array=np.array(input_list).reshape(1,-1)
        pred=list(loadModel.predict(input_array))
        pdarea=int(pred[0])/totalarea
        pred_tmp.append(str(round(pdarea,1)))
    for y in year_list:
        time_tmp.append(str(y))
        
    return pred_tmp,time_tmp

def light_GBM():
    loadModel=joblib.load('LGBM03.pkl')
    input_list=[443012,443,2028,12,30,2,30,6,2,1,1,1,1,1,0]
    input_array=np.array(input_list).reshape(1,-1)
    pred=list(loadModel.predict(input_array))
