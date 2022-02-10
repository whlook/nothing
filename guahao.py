#!/usr/bin/env python
# coding: utf-8

import sys
import time
import datetime
import http.client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_webservertime(host):
    try:
        conn=http.client.HTTPConnection(host)
        conn.request("GET", "/")
        r = conn.getresponse()
        ts =  r.getheader('date')
        ltime= time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
        ttime=time.localtime(time.mktime(ltime)+8*60*60)
        #dat="date %u-%02u-%02u"%(ttime.tm_year,ttime.tm_mon,ttime.tm_mday)
        #tm="time %02u:%02u:%02u"%(ttime.tm_hour,ttime.tm_min,ttime.tm_sec)
        return [ttime.tm_hour,ttime.tm_min,ttime.tm_sec]
    except:
        return False

#wait for time close
while(True):
    webtime = get_webservertime("www.114yygh.com")
    print('webtime:'+str(webtime[0])+'h'+str(webtime[1])+'m'+str(webtime[2])+'s')
    if webtime != False:
        if webtime[0] < 14:
            time.sleep(1800)
            continue
        if webtime[0] < 15:
            time.sleep(600)
            continue
        if webtime[1] < 17:
            time.sleep(30)
            continue
        else:
            break
    else:
        exit("get web time error")

print('============ start login ============')
opt=webdriver.ChromeOptions()
opt.headless=False
chrome = webdriver.Chrome(options=opt)

#login
try:
    chrome.get("http://www.114yygh.com/account/login.htm")
    mobileIn = chrome.find_element_by_id("mobileNo")
    mobileIn.send_keys('12345678901')
    login1 = chrome.find_element_by_id("login_1")
    login1.click()
    pwd_login = chrome.find_element_by_id("pwd_login")
    pwd_login.click()
    pwd = chrome.find_element_by_id("pwd")
    pwd.send_keys("xxxpasswd")
    login2 = chrome.find_element_by_id("loginStep2_pwd")
    login2.click()
    print('============ login success ============')
except:
    exit("login error")

#select date
chrome.get("http://www.114yygh.com/dpt/calendar/12-200004219.htm")
time.sleep(5)

while(True):
    webtime = get_webservertime("www.114yygh.com")
    print('webtime:'+str(webtime[0])+'h'+str(webtime[1])+'m'+str(webtime[2])+'s')
    if webtime != False:
        if webtime[1] < 59:
            time.sleep(10)
            continue
        else:
            break
    else:
        exit("get web time error")

while(True):
    try:
        exp_day = chrome.find_element_by_xpath("//li[@data-id='2019-08-27']")
        exp_day.click()
        print("finding doctors list")
        doctors_list = chrome.find_elements_by_class_name('ksorder_djgh_dr1')
        for doctor in doctors_list:
            name=u'某某某'
            if name in str(doctor.text):
                print(doctor.text)
                yygh = doctor.find_element_by_link_text(u'预约挂号')
                yygh.click()
                break
            else:
                print("no")
    except:
        continue

#success get in, confirm info
select_wang = chrome.find_element_by_name('123456789')
select_wang.click()
print("sending sms code")
get_sms_code = chrome.find_element_by_id('send_sms_code_btn')
get_sms_code.click()
alert = chrome.switch_to.alert
alert.accept()
sms_input = chrome.find_element_by_id("sms_code")
sms_input.click()
print(" input your sms code now")
time.sleep(600)
