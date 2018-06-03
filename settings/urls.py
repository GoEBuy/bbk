#-*- coding:utf-8 -*-

from django.conf.urls import include, url
import views

app_name  = 'settings'

urlpatterns = [

#ex /settings/

    # 用户设置
    #url(r'^settings/$', views.user_settings, name='settings'),
    url(r'^$', views.user_settings, name='settings'),

    # 用户头像设置
    #settings/avatar
    url(r'^avatar',views.user_settings_avatar, name='settings_avatar'),

    ## 用户手机设置
    #url(r'^settings/phone', views.phoneSettingView, name='settings_phone'),

    ### 用户Email设置
    #url(r'^settings/email', views.user_settings_email, name='settings_email'),

    ## 密码修改
    #url(r'^settings/password', views.user_settings_password, name='settings_password'),


        ]
