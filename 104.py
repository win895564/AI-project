from selenium import webdriver
from selenium.webdriver.chrome import options 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
import os 
from openpyxl import Workbook
PATH='K:/Users/user/Desktop/chromedriver.exe'
driver = webdriver.Chrome(PATH)
# driver.minimize_window()
driver.get('https://www.104.com.tw/jobs/main/')#進入首頁
print('目前網站為:'+driver.title)
print('請輸入欲查詢關鍵字:')
inputkey= input()
key=driver.find_element_by_id('ikeyword')

key.send_keys(inputkey)
key.send_keys('\ue007')
in_unicode=inputkey.encode('unicode_escape')

cmpnames=driver.find_elements_by_class_name('b-list-inline')
jobnames=driver.find_elements_by_class_name('js-job-item')
salarys=driver.find_elements_by_class_name('job-list-tag')
page=driver.find_elements_by_class_name('page-select')
print('=====正在執行查詢作業=====')


print(f'=====查詢到{page[-1]}頁=====')
print (type(page))

# =============================================================================
# 滾輪至底部
# js="var q=document.documentElement.scrollTop=10000"  
# driver.execute_script(js)
# time.sleep(1)
# js="var q=document.documentElement.scrollTop=10000"  
# driver.execute_script(js)
# time.sleep(1)
# js="var q=document.documentElement.scrollTop=10000"  
# driver.execute_script(js)
# =============================================================================
time.sleep(5)


#b-block--top-bord job-list-item b-clearfix js-job-item
#job-list-item 工作內容
#b-list-inline.b-clearfix 為公司名稱 產業別 經歷 學歷
#b-content 薪資 工作內容 
# =============================================================================
# for jobname in jobnames:
#     count+=1
#     if(count %2)!=0:
#         jobname2=jobname.text
#     else:
#         jobname2+=jobname.text
#         print(f'第{count / 2}筆資料為: \n'+jobname2)
# =============================================================================
#js-job-item 職位 公司名 產業別 縣市 學經歷 工作內容*
#job-list-tag  整排salary資訊*

#b-tit 為日期+職位名稱*
#b-list-inline 公司名稱 縣市 產業別 經歷 學歷*
#list01=['1','2','3','4','5','6','7','8','','']

wb=Workbook()
ws=wb.active


count=0
for jobname in jobnames:
    if jobname==' ': #前面幾筆會抓到空資料
        pass
    else:
        course=[]
        count+=1
        course.append(f'第{count}筆資料為: '+jobname.text)
        ws.append(course)
        
        #print(f'第{count}筆資料為: \n'+jobname.text)
wb.save(f'{inputkey}.xlsx')    
print('=====查詢動作已完成=====\n\n\n')  
print(f'查詢到 {str(count)} 筆資料 已存為 {inputkey}.xlsx')
driver.quit()

