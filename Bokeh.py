# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 16:46:21 2022

@author: user
"""

from bokeh.plotting import figure, show

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from bokeh.models import DatetimeTickFormatter
df1= pd.read_csv('433沙鹿區.csv',encoding='utf-8')
df1['orderdate']=df1['orderdate']+191100#將日期轉為西元年
df1['orderdate']=pd.to_datetime(df1['orderdate'],format='%Y%m')#將日期轉為datetime格式
df2=df1[['orderdate','singleprice']]#裁切交易日期跟單價
group=df2['singleprice'].groupby(df2['orderdate'])
grouped=group.mean()#須將group 建立一個變數物件才能顯示 x.index or x.values

x=grouped.index
y=grouped.values

p = figure(title="台中全區", x_axis_label='年度', y_axis_label='單坪價格(萬元)',width=1000)
p.xaxis[0].formatter=DatetimeTickFormatter(months=["%d %b %Y"],years=["%d %b %Y"])#bokeh時間固定格式
# add a line renderer with legend and line thickness
p.line(x,y,  legend="Temp.", line_width=3)
# show the results

#熱力圖
plt.figure(figsize=(11,7))

show(p)
