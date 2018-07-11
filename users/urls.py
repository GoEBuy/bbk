#-*- coding:utf-8 -*-

from django.conf.urls import include, url
from . import views
#from .views import *

app_name = 'users'

urlpatterns = [

    #公共参数 city, plat
    #可选参数page

    #ex /users/ [?cate=<cate_id>&city=<city_name>&plat=<plat>]
    #内行人首页
    url(r'^$', views.index, name='index'),

    #ex: /users/<id> [?cate=<cate_id>&city=<city_name>&] 
    #内行人详情页
    url('^(?P<id>\d+)/', views.detail, name='detail'),

	#url(r'', views.index.as_view() ),

    #ex: /register [plat=<plat>]
    url(r'^register/$', views.register, name='register'),

    #ex: /login
    url(r'^login/$', views.login, name='login'),

    #ex: /logout
    url(r'^logout/$', views.logout, name='logout'),
    
    url(r'^settings/$', views.user_settings, name='settings' ),

    url(r'^settings_avatar/$', views.user_settings_avatar, name='settings_avatar' ) , 
    url(r'^settings_password/$', views.user_settings_password, name='settings_password' ), 
    url(r'^resetting_password/$', views.user_settings_password, name='resetting_password' ), 
    url(r'^settings_email/$', views.user_settings_email, name='settings_email' ),
    url(r'^settings_phone/$', views.user_settings_email, name='settings_phone' ),

    #TODO
    #ex: /uid/nodes
    # 我收藏的节点
    #path('^(?P<uid>\d+)/nodes', MyFavoriteNodeView.as_view(), name='my_nodes'),

    #ex: /uid/topics
    # 我收藏的主题
    #path('^(?P<uid>\d+)/topics', MyFavoriteTopicView.as_view(), name='my_topics'),

    #ex: /uid/following
    # 我关注的人的信息
    #path('^(?P<uid>\d+)/following', MyFollowingView.as_view(), name='my_following'),

    #ex: /uid/followed
    # 我关注的人的信息
    #path('^(?P<uid>\d+)/followed', MyFollowingView.as_view(), name='my_followed'),
    #url(r'^settings/$', views.user_settings, name='settings'),


	#url('user/add/', AuthorCreate.as_view(), name='author-add'),
	#url('user/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),

	

    ##TODO
    #url(r'^$', views.index.as_view(), name='index'),
	#url('^(?P<pk>\d+)/', views.detail.as_view(), name='detail'),
    ##分类列表页面
    #url(r'^(?P<cate_name>\w+)/$', views.cate-list, name='cate-list')

    ##内行人列表页面
    #url(r'^persons/', views.cate-list, name='cate-list')

    ##内行人搜索页面
    #url(r'^persons-search/', views.persons-search, name='persons-search')

    ##内行人详情页面
    #url(r'^persons-detail/', views.persons-detail, name='persons-detail')


    # url(r'^(?P<article_id>[0-9]+)/comment/$', views.comment, name='comment', namespace='focus'),
    # url(r'^(?P<article_id>[0-9]+)/keep/$', views.get_keep, name='keep', namespace='focus'),
    # url(r'^(?P<article_id>[0-9]+)/poll/$', views.get_poll_article, name='poll', namespace='focus'),
    # url(r'^(?P<article_id>[0-9]+)/$', views.article, name='article', namespace='focus'),
    #

] #end
