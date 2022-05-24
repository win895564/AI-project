# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:44:28 2022

@author: user
"""
# hash密碼
import bcrypt

# 解析 URL
from urllib import parse

# mysql connector

# flask
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
from datetime import timedelta#設定自動登出
app.permanent_session_lifetime = timedelta(minutes=180)#設定自動登出

import pymysql
import app_module as m
import pandas as pd


tmp=[]
Gmaps=[]
import requests
from pyecharts import options as opts
from pyecharts.faker import Faker
from jinja2 import Markup
from pyecharts.globals import ThemeType
import pyecharts.options as opts
from pyecharts.charts import Line
import creatmodule as ct #pyechart圖表製作
import Newcatch #新聞爬取
import Str_Q2B #全形轉半形
import folium_taichung
import import_model 
import air_quality_requests as air_requests #爬取空汙監測站資料
import re


# 註冊頁面
@app.route('/register', methods=["GET", "POST"])
def register():
    
    if request.method == 'GET':
        return render_template("register.html")
    else:
        name = request.form['name']
        email = request.form['email']
        validation=m.Register(name,email)
        if validation==None  :
               name = request.form['name']
               email = request.form['email']
               password = request.form['password'].encode('utf-8')
               hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
               import CatchIP
               IP=CatchIP.catch_ip()
               m.insert_mem(name, email, hash_password,IP)
               session['name'] = request.form['name']
               session['email'] = request.form['email']
               return redirect(url_for('login'))
        else:
            return render_template('error.html',error_code=False)



# 登入頁面
@app.route('/login', methods=["GET", "POST"])
def login():
    
    if request.method == 'POST':
        email = request.form['email']
        print("email:",email)
        password = request.form['password'].encode('utf-8')
        user = m.login(email)

        if user == None:
            return render_template("error.html",error_code=True)
        if len(user) != 0:
            if bcrypt.hashpw(password, user[3].encode('utf-8')) == user[3].encode('utf-8'):
                session['name'] = user[1]
                session['email'] = user[2]
                return render_template("home.html")
            else:
                return render_template("error.html",error_code=True)
    else:
        return render_template("login.html")
# 登出
@app.route('/logout')
def logout():
    session.clear()
    return render_template("home.html")



@ app.route('/index',methods=['GET','POST'])
def index(): 
    if request.method=='GET':
        
        mapaddress="https://maps.google.com/?q=台中市&output=svembed"
        form=m.reviewform(request.form)
        News=Newcatch.catch()
        details=m.readsql('和平區')
        tmp_df=pd.DataFrame(details,columns=['address',#list_of_tuple to dataframe
                                               'orderdate',#must set columns name
                                               'age',
                                               'type',
                                               'totalprice',
                                               'singleprice',
                                               'totalarea',
                                               'build',
                                               'lobby',
                                               'bathroom'])
              
              #list_of_tuple 轉為dataframe格是為object 須轉為int or float ..
              #tmp_df['orderdate']=tmp_df['orderdate'].astype('int64')
        tmp_df.orderdate=tmp_df.orderdate.astype('int64')
            
              
        tmp_df.age=tmp_df.age.astype('int64')
        tmp_df.type=tmp_df.type.astype('int64')
        tmp_df.totalprice=tmp_df.totalprice.astype('float64')
        tmp_df.singleprice=tmp_df.singleprice.astype('float64')
        tmp_df.totalarea=tmp_df.totalarea.astype('float64')
        tmp_df.build=tmp_df.build.astype('int64')
        tmp_df.lobby=tmp_df.lobby.astype('int64')
        tmp_df.bathroom=tmp_df.bathroom.astype('int64')
        group=tmp_df['singleprice'].groupby(tmp_df['orderdate'])
        grouped=round(group.mean(),2)
        group_index=[]
        group_value=[]
              ##此處必須轉為str
        for i,j in zip(list(grouped.index),list(grouped.values)):
            group_index.append(str(i))
            group_value.append(str(j))
                
         #import creatmodule creat embed map
        data_plot=ct.Js_line(group_index,group_value,'和平區')

        x_data= ['1919', '5451','11653','9314','14940','33208','25128','17341','14917',
                 '12460',
                 '2356',
                 '6658',
                 '7114',
                 '1404',
                 '150',
                 '1037',
                 '3',
                 '318',
                 '5612',
                 '4340',
                 '1808',
                 '2087',
                 '6353',
                 '4023',
                 '3570',
                 '5965',
                 '2245',
                 '836',
                 '169']
        y_data=['中區', '東區', '南區', '西區', '北區', '北屯區', '西屯區', '南屯區', '太平區', '大里區', '霧峰區', '烏日區', '豐原區', '后里區', '石岡區', '東勢區', '和平區', '新社區', '潭子區', '大雅區', '神岡區', '大肚區', '沙鹿區', '龍井區', '梧棲區', '清水區', '大甲區', '外埔區', '大安區']
        data=[]
        for i,j in zip(y_data,x_data):
            data.append((i,j))
            
        data_world=ct.Creat_WorldCloud(data)      
        return render_template('index.html',form=form,mapaddress=mapaddress,data_plot=data_plot,data_world=data_world)
    else:
        tmp.clear()
        
        form=m.reviewform(request.form)
        if request.method == 'POST' :
           
           selectarea=request.form.get('selectarea')
           searchvalue=Str_Q2B.strB2Q(request.form['srcbar'])
           print(selectarea)
          
           mapaddress=f"https://maps.google.com/?q={searchvalue}&output=svembed"
     
           
           if request.values.get('mapbtn') and selectarea!='' :
                   return redirect(url_for('show_map',selectarea=selectarea))#指定導向路徑 並帶參數
       
           if request.values.get('srcbtn') :
               if len(searchvalue)==0:
                   searchvalue="---"
               details=m.readsql(selectarea)

               for i in details:
           
                   if searchvalue in i[0]:
                       Gmaps.append(f'https://maps.google.com/?q={i[0]}&output=svembed')
                       tmp.append(i)
               tmp_df=pd.DataFrame(tmp,columns=['address',#list_of_tuple to dataframe
                                                'orderdate',#must set columns name
                                                'age',
                                                'type',
                                                'totalprice',
                                                'singleprice',
                                                'totalarea',
                                                'build',
                                                'lobby',
                                                'bathroom'])
               
               #list_of_tuple 轉為dataframe格是為object 須轉為int or float ..
               #tmp_df['orderdate']=tmp_df['orderdate'].astype('int64')
               tmp_df.orderdate=tmp_df.orderdate.astype('int64')
             
               
               tmp_df.age=tmp_df.age.astype('int64')
               tmp_df.type=tmp_df.type.astype('int64')
               tmp_df.totalprice=tmp_df.totalprice.astype('float64')
               tmp_df.singleprice=tmp_df.singleprice.astype('float64')
               tmp_df.totalarea=tmp_df.totalarea.astype('float64')
               tmp_df.build=tmp_df.build.astype('int64')
               tmp_df.lobby=tmp_df.lobby.astype('int64')
               tmp_df.bathroom=tmp_df.bathroom.astype('int64')
               group=tmp_df['singleprice'].groupby(tmp_df['orderdate'])
               grouped=round(group.mean(),2)
               group_index2=[]
               group_value2=[]
               ##此處必須轉為str
               for i,j in zip(list(grouped.index),list(grouped.values)):
                   group_index2.append(str(i))
                   group_value2.append(str(j))
# =============================================================================
#                c = Bar()
#                c.add_xaxis(group_index)#需為list
#                c.add_yaxis("總數", group_value)#需為lis
#                
#                c.set_global_opts(
#                             title_opts=opts.TitleOpts(title="查詢結果:", subtitle="#"),
#                             toolbox_opts=opts.ToolboxOpts(),
#                             legend_opts=opts.LegendOpts(is_show=False))
#                     
#         
#                data_plot = c.dump_options()
# =============================================================================
               data_plot=ct.Js_line(group_index2,group_value2,searchvalue)
               x_data= ['1919', '5451','11653','9314','14940','33208','25128','17341','14917',
                      '12460',
                      '2356',
                      '6658',
                      '7114',
                      '1404',
                      '150',
                      '1037',
                      '3',
                      '318',
                      '5612',
                      '4340',
                      '1808',
                      '2087',
                      '6353',
                      '4023',
                      '3570',
                      '5965',
                      '2245',
                      '836',
                      '169']
               y_data=['中區', '東區', '南區', '西區', '北區', '北屯區', '西屯區', '南屯區', '太平區', '大里區', '霧峰區', '烏日區', '豐原區', '后里區', '石岡區', '東勢區', '和平區', '新社區', '潭子區', '大雅區', '神岡區', '大肚區', '沙鹿區', '龍井區', '梧棲區', '清水區', '大甲區', '外埔區', '大安區']
               data=[]
               for i,j in zip(y_data,x_data):
                   data.append((i,j))
                 
               data_world=ct.Creat_WorldCloud(data)   
               #folium_data=folium_taichung.folium_dumps(tmp_df)
               return render_template('index.html',form=form,details=tmp,mapaddress=mapaddress,data_plot=data_plot,data_world=data_world)
@ app.route('/Show_map<string:selectarea>',methods=['GET','POST'])#後面必須加參數名稱
def show_map(selectarea):#地圖導覽的route

    return render_template(f'/folium_html/{selectarea}.html')

    
@ app.route('/',methods=['GET','POST'])
def main():
    if request.method=='GET':
        return render_template('main.html')
    else:
        if request.method=='POST' and request.values.get('hprice'):
            return redirect(url_for('index'))


@ app.route('/house_forecast',methods=['GET','POST'])
def forecast():
    s,x,z,d,f=air_requests.air_catch()
    pred_code=0
    
    if request.method=='GET':
        News=Newcatch.catch()
        News_activate=[]
        News_activate.append(News[0])
      
        return render_template('News.html',News_activate=News_activate,News=News[1:],s_=s,x_=x,z_=z,d_=d,f_=f)
    else:
        if request.method=='POST' :
            if request.values.get('predict_button'):
# =============================================================================
#                 address=request.form.get('address')
#                 r=requests.get(f"http://zip5.5432.tw/zip5json.py?adrs=台中市{address}")
#                 add_convert=r.json()
#                 orderdate=request.form.get('orderdate')
#                 age=request.form.get('age')
#                 htype=request.form['htype']
#                 totalarea=request.form.get('totalarea')
#                 room=request.form.get('room')
#                 lobby=request.form.get('lobby')
#                 bathroom=request.form.get('bathroom')
#                 pred=import_model.pre_date(add_convert,orderdate,age,htype,totalarea,room,lobby,bathroom)
#                 News=Newcatch.catch()
#                 News_activate=[]
#                 News_activate.append(News[0])
# =============================================================================
                News=Newcatch.catch()
                News_activate=[]
                News_activate.append(News[0])
                address=request.form.get('address')
                
                r=requests.get(f"http://zip5.5432.tw/zip5json.py?adrs={address}")
                add_convert=r.json()

                
                import random#產生隨機數 用於如果6碼API無回傳值 則隨機產生
                if len(add_convert['zipcode6'])==0:
                    zcode_6=random.randrange(400000,4400000)
                    zcode_3=random.randrange(400,440)
                    pred_code=1
                else:
                    zcode_6=str(add_convert['zipcode6'])
                    zcode_3=zcode_6[:3]
                    
                age=request.form.get('age')
                htype=request.form['htype']
                totalarea=request.form.get('totalarea')
                room=request.form.get('room')
                lobby=request.form.get('lobby')
                bathroom=request.form.get('bathroom')
                
                if request.form.get('parking')==None:
                    parking=0
                else:
                    parking=1
                
                if request.form.get('elevator')==None:
                    elevator=0
                else:
                    elevator=1
                if request.form.get('manage')==None:
                    manage=0
                else:
                    manage=1
                #import_model.linear_svr(433110,433,30,2,30,6,2,1,1,1,1)
                pred_tmp,time_tmp=import_model.linear_svr(int(zcode_6),int(zcode_3),age,htype,totalarea,room,lobby,bathroom,parking,elevator,manage)
                pred_plot_code=ct.Forecast_js(address,pred_tmp, time_tmp)

                if pred_tmp !=None and len(session)!=0:#如果有登入會員
                    session_name=session['name']
                    m.Insert_search_keyword(session_name, address, age, htype, totalarea, room, lobby, bathroom, parking, elevator, manage)
                    return render_template('News.html',News_activate=News_activate,News=News[1:],pred=pred_plot_code,pred_code=pred_code,s_=s,x_=x,z_=z,d_=d,f_=f)
                
                return render_template('News.html',News_activate=News_activate,News=News[1:],pred=pred_plot_code,pred_code=pred_code,s_=s,x_=x,z_=z,d_=d,f_=f)
@ app.route('/team',methods=['GET','POST'])
def team():
    if request.method=='POST':
       if request.values.get('send_message'):
           Name=request.form['Name']
           Email=request.form['Email']
           Subject=request.form['Subject']
           Comment=request.form['Comment']
           
           m.insert_data(Name,Email,Subject,Comment)
    return render_template('team.html')   

@ app.route('/member',methods=['GET','POST'])
def member():
    if request.method=='POST':
        name=session['name']
        ID= request.values.get('value')
        print(ID)
        print(name)
        
    if len(session)!=0:
        name=session['name']
        membersearch=m.Member_search(name)
        return render_template('member.html',membersearch=membersearch)
    return render_template('member.html')




if __name__ == '__main__':
    app.config['SECRET_KEY']='secretkey'
    app.run(debug=True,port=80)
