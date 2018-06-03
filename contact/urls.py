#-*- coding:utf-8 -*-

from django.conf.urls import include, url
from . import views

app_name = 'contact'

urlpatterns = [


    #ex: /contact
    url(r'^$', views.contact, name='contact'),



] #end
