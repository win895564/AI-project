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
rd_csv=pd.read_csv("./taichung.csv")

fmap=folium.Map(location=[24.1449332,120.6789071],zoom_start=13)#給一個地圖開啟預設座標
marker_cluster = MarkerCluster().add_to(fmap)#鄰近經緯度作一個範圍

# =============================================================================

for address,lat,lng,orderdate,htype,totalprice in zip(rd_csv['address'],rd_csv['lat'],rd_csv['lng'],rd_csv['orderdate'],rd_csv['type'],rd_csv['totalprice']):
        if htype=='1':
            htype='華廈(10層含以下有電梯)'
        elif htype=='2':
             htype='透天厝'
        elif htype=='3':
             htype='公寓(5樓含以下無電梯)'
        elif htype=='4':
             htype='住宅大樓(11層含以上有電梯)'
        elif htype=='5':
             htype='套房(1房(1廳)1衛)'
        elif htype=='6':
             htype='店面（店舖)'
        elif htype=='7':
             htype='其他'
        elif htype=='8':
             htype='倉庫'
        elif htype=='9':
             htype='廠辦'
        elif htype=='10':
             htype='工廠'
        elif htype=='11':
             htype='辦公商業大樓'

        ifram=folium.IFrame('地址：'+str(address)+'<br>'
                            +'交易日期：'+str(orderdate)+'<br>'
                            +'總售價(萬)：'+str(totalprice)+'<br>'
                            +'類型：'+str(htype)+'<br>'
                            )#訊息框架 可設定html
        Popup=folium.Popup(ifram,min_width=300,max_width=400)#設定訊息框架屬性
        print(address)
        folium.Marker(location=[lat,lng]
                        ,icon=None
                        ,popup=Popup).add_to(marker_cluster)
        
 



     
#=============================================================================
    
minimap = MiniMap()
fmap.add_child(child = minimap)
#fmap=folium.Map(location=[24.1449332,120.6789071],tiles='Stamen Terrain',zoom_start=13)
#m = fmap.add_child(folium.Marker(location=[24.1449332,120.6789071],icon=None, popup='中區'))
fmap.save('414.html')


    