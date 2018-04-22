#-*- coding:utf-8 -*-

from django.conf.urls import include, url
from . import views
#from .views import *

app_name = 'users'

urlpatterns = [

	#ex /users/ [?cate=<cate_id>&city=<city_name>&]
    url(r'^$', views.index, name='index'),

	#ex: /users/<id> [?cate=<cate_id>&city=<city_name>&] 
	url('^(?P<id>\d+)/', views.detail, name='detail'),

	#url(r'', views.index.as_view() ),

	#ex: /register
    url(r'^register/$', views.register, name='register'),

    url(r'^login/$', views.login, name='login'),

    url(r'^logout/$', views.logout, name='logout'),

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
]
