# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:50:50 2022

@author: user
"""
from wtforms import Form, StringField, TextAreaField, validators,SubmitField,PasswordField,SelectField
import pymysql
import pandas as pd
def readsql(selectarea):#實價登錄查詢
    connection = pymysql.connect(host='3.114.122.242',
                                 port=3307,
                                 user='root',
                                 password='password',
                                 database='taichung',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.SSCursor)
    with connection:
        #with connection.cursor object cursor session
        with connection.cursor() as cursor:
            # 使用 cursor.execute() 執行select sql script
            

            sql = "select * from `%s`" %(selectarea)
            
            cursor.execute(sql)
            #使用 cursor.fetchall() 從cursor中取出資料
            #return value 'rows' --> tuple of tuples
            rows=cursor.fetchall() 
    # connection is not autocommit by default. So you must commit to save your changes.
        connection.commit()
    return list(rows)
def taichung_mean():#查詢各行政區筆數
    tai_list=['中區','東區','南區','西區','北區',
              '北屯區','西屯區','南屯區','太平區','大里區',
              '霧峰區','烏日區','豐原區','后里區','石岡區',
              '東勢區','和平區','新社區','潭子區','大雅區',
              '神岡區','大肚區','沙鹿區','龍井區','梧棲區',
              '清水區','大甲區','外埔區','大安區'
              ]
    tai_return=[]
    tmp_df=[]
    for i in tai_list:
               tmp_df=pd.DataFrame(readsql(i)
                                   ,columns=['address',#list_of_tuple to dataframe
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
              
               tai_return.append(len(tmp_df))
    return tai_return,tai_list
               
def insert_data(Name,Email,Subject,Comment):#留言頁面
    connection = pymysql.connect(host='3.114.122.242',
                                 port=3307,
                                 user='root',
                                 password='password',
                                 database='taichung',
                                 charset='utf8mb4')
    with connection:
        #with connection.cursor object cursor session
        with connection.cursor() as cursor:
            # 使用 cursor.execute() 執行select sql script
            

            sql = "INSERT INTO `memberinfo` (`mem_name`, `email`, `job`,`message`,`nowtime`) VALUES (%s, %s,%s,%s,NOW())"
            
            cursor.execute(sql, (Name,Email,Subject,Comment))
            #使用 cursor.fetchall() 從cursor中取出資料
            #return value 'rows' --> tuple of tuples
            rows=cursor.fetchall() 
    # connection is not autocommit by default. So you must commit to save your changes.
        connection.commit()

def insert_mem(name,email,hash_password,IP):#註冊帳號
    connection = pymysql.connect(host='3.114.122.242',
                                 port=3307,
                                 user='root',
                                 password='password',
                                 database='taichung',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.SSCursor)
    with connection:
        #with connection.cursor object cursor session
        with connection.cursor() as cursor:
            # 使用 cursor.execute() 執行select sql script
            
            sql_time="SET time_zone = '+8:00'" #設定時區為台灣
            sql = "INSERT INTO `users` (`name`, `email`, `password`,`reg_time`,`IP`) VALUES (%s,%s,%s,NOW(),%s)"
            cursor.execute(sql_time)
            cursor.execute(sql,(name, email, hash_password,IP))
            #使用 cursor.fetchall() 從cursor中取出資料
            #return value 'rows' --> tuple of tuples
            rows=cursor.fetchall() 
    # connection is not autocommit by default. So you must commit to save your changes.
        connection.commit()
def login(email)  :#登入帳號
    connection = pymysql.connect(host='3.114.122.242',
                                 port=3307,
                                 user='root',
                                 password='password',
                                 database='taichung',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.SSCursor)
    with connection:
        #with connection.cursor object cursor session
        with connection.cursor() as cursor:
            # 使用 cursor.execute() 執行select sql script
            

            sql = "SELECT * FROM users WHERE email=%s"
            
            cursor.execute(sql,(email))
            #使用 cursor.fetchall() 從cursor中取出資料
            #return value 'rows' --> tuple of tuples
            rows=cursor.fetchone() 
    # connection is not autocommit by default. So you must commit to save your changes.
        connection.commit()
    return rows

def Register(name,email)  :#註冊驗證
    connection = pymysql.connect(host='3.114.122.242',
                                 port=3307,
                                 user='root',
                                 password='password',
                                 database='taichung',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.SSCursor)
    with connection:
        #with connection.cursor object cursor session
        with connection.cursor() as cursor:
            # 使用 cursor.execute() 執行select sql script
            

            sql = "SELECT * FROM users WHERE name=%s or email=%s"
            
            cursor.execute(sql,(name,email))
            #使用 cursor.fetchall() 從cursor中取出資料
            #return value 'rows' --> tuple of tuples
            rows=cursor.fetchone() 
    # connection is not autocommit by default. So you must commit to save your changes.
        connection.commit()
    return rows


def Insert_search_keyword(session_name,address,age,htype,totalarea,room,lobby,bathroom,parking,elevator,manage):
    connection = pymysql.connect(host='3.114.122.242',
                                 port=3307,
                                 user='root',
                                 password='password',
                                 database='taichung',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.SSCursor)
    with connection:
        #with connection.cursor object cursor session
        with connection.cursor() as cursor:
            # 使用 cursor.execute() 執行select sql script
            
            sql_time="SET time_zone = '+8:00'"
            sql = "INSERT INTO `member_search` (`name`, `address`,`age`,`htype`,`totalarea`,`room`,`lobby`,`bathroom`,`parking`,`elevator`,`manage`,`ttime`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())"
            cursor.execute(sql_time)
            cursor.execute(sql,(session_name,address,age,htype,totalarea,room,lobby,bathroom,parking,elevator,manage))
            #使用 cursor.fetchall() 從cursor中取出資料
            #return value 'rows' --> tuple of tuples
            rows=cursor.fetchone() 
    # connection is not autocommit by default. So you must commit to save your changes.
        connection.commit()
    return rows
def Member_search(name):
    connection = pymysql.connect(host='3.114.122.242',
                                 port=3307,
                                 user='root',
                                 password='password',
                                 database='taichung',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.SSCursor)
    with connection:
        #with connection.cursor object cursor session
        with connection.cursor() as cursor:
            # 使用 cursor.execute() 執行select sql script
            

            sql = "SELECT * FROM member_search WHERE name=%s"
            
            cursor.execute(sql,(name))
            #使用 cursor.fetchall() 從cursor中取出資料
            #return value 'rows' --> tuple of tuples
            rows=cursor.fetchall() 
    # connection is not autocommit by default. So you must commit to save your changes.
        connection.commit()
    return list(rows)
def Member_Delete(ID,name):
    connection = pymysql.connect(host='3.114.122.242',
                                 port=3307,
                                 user='root',
                                 password='password',
                                 database='taichung',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.SSCursor)
    with connection:
        #with connection.cursor object cursor session
        with connection.cursor() as cursor:
            # 使用 cursor.execute() 執行select sql script
            

            sql = "DELETE FROM usersearch WHERE ID=%s and name=%s"
            
            cursor.execute(sql,(ID,name))
            #使用 cursor.fetchall() 從cursor中取出資料
            #return value 'rows' --> tuple of tuples
            rows=cursor.fetchall() 
    # connection is not autocommit by default. So you must commit to save your changes.
        connection.commit()
    return list(rows)
def reviewform(Form):
    country=SelectField('country',choice=['Dajia','大甲'])
    srcbar=StringField('輸入地址',[validators.DataRequired(message='Not Null')])