#-*- coding:utf-8 -*-

import os
import django

#在导入任何模块之前 设置变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbk.settings")
django.setup()
#setting.configure()

import pdb,traceback

from users import views
from order import views
from focus import views

from django.urls import reverse
from django.template import engines
from django.template.loader import get_template, select_template 
from django.shortcuts import render_to_response 
from django.template import Context  


import urllib3, requests

FLAG_DEBUG=True


def testUser_login():
    url="http://localhost:8000/users/login"
    pass

def testGet(url,params, isJson=False):
    r = requests.get(url, params=params)
    if r.status_code==200:
        pass
        if isJson:
            try:
                r = r.json
            except:
                pass
        return r 
    else:
        print "get faild for url:"+ url
        return None
        pass
    pass


def testPost(url, params, isJson=False):
    r = requests.post(url, data=params)
    if r.status_code==200:
        pass
        if isJson:
            try:
                r = r.json
            except:
                pass
        return r
    else:
        print "get faild for url:"+ url
        return None
        pass
    pass
   

###############################################
url="http://localhost:8000/users/login"
username="yyy"
password="yyy"
data={'username': username, 'password1':password }

testPost(url, data)

