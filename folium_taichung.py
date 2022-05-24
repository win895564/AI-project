# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:37:47 2022

@author: user
"""
import openpyxl
import pandas as pd
import folium
from folium.plugins import HeatMap
from folium.plugins import MiniMap
from folium.plugins import MarkerCluster
import time
import sys

def folium_dumps(input_csv):
    #filename=input('輸入:')
    
    rd_csv=input_csv
    
    fmap=folium.Map(location=[24.3777332,120.6113777],zoom_start=13)#給一個地圖開啟預設座標
    marker_cluster = MarkerCluster().add_to(fmap)#鄰近經緯度作一個範圍
    
    # =============================================================================
    
    for address,lat,lng,orderdate,age,htype,totalprice,singleprice,totalarea,build,lobby,bathroom in zip(rd_csv['address'],rd_csv['lat'],rd_csv['lng'],rd_csv['orderdate'],rd_csv['age'],rd_csv['type'],rd_csv['totalprice'],rd_csv['singleprice'],rd_csv['totalarea'],rd_csv['build'],rd_csv['lobby'],rd_csv['bathroom']):
        
        htype=str(htype).replace('1','華廈(10層含以下有電梯)')    
        htype=str(htype).replace('2','透天厝')   
        htype=str(htype).replace('3','公寓(5樓含以下無電梯)')   
        htype=str(htype).replace('4','住宅大樓(11層含以上有電梯)')   
        htype=str(htype).replace('5','套房(1房(1廳)1衛)')   
        htype=str(htype).replace('6','店面（店舖)')   
        htype=str(htype).replace('7','其他')   
          
        
    
        ifram=folium.IFrame('地址：'+str(address)+'<br>'
                                +'交易日期：'+str(orderdate)+'<br>'
                                +'屋齡：'+str(age)+'<br>'
                                +'類型：'+str(htype)+'<br>'
                                +'總售價(萬)：'+str(totalprice)+'<br>'
                                +'單價(坪/萬)：'+str(singleprice)+'<br>'
                                +'總面積(坪)：'+str(totalarea)+'<br>'
                                +'房：'+str(build)+'<br>'
                                +'廳：'+str(lobby)+'<br>'
                                +'衛：'+str(bathroom)+'<br>'
                  
                                
                                )#訊息框架 可設定html語法
        Popup=folium.Popup(ifram,min_width=400,max_width=450)#設定訊息框架屬性
        
        folium.Marker(location=[lat,lng]
                            ,icon=None
                            ,popup=Popup).add_to(marker_cluster)
            
     
    
    
    
         
    #=============================================================================
        
    minimap = MiniMap()
    fmap.add_child(child = minimap)
    #fmap=folium.Map(location=[24.1449332,120.6789071],tiles='Stamen Terrain',zoom_start=13)
    #m = fmap.add_child(folium.Marker(location=[24.1449332,120.6789071],icon=None, popup='中區'))
    return fmap._repr_html_()
    #fmap.save(f'./folium_html/{filename}.html')


    