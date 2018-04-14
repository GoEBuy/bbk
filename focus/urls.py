
from django.conf.urls import include, url
from . import views

app_name = 'focus'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),


	#TODO
	#分类列表页面
	url(r'^(?P<cate_name>\w+)/$', views.cate-list, name='cate-list')

	#内行人列表页面
	url(r'^persons/', views.cate-list, name='cate-list')

	#内行人搜索页面
	url(r'^persons-search/', views.persons-search, name='persons-search')

	#内行人详情页面
	url(r'^persons-detail/', views.persons-detail, name='persons-detail')


    # url(r'^(?P<article_id>[0-9]+)/comment/$', views.comment, name='comment', namespace='focus'),
    # url(r'^(?P<article_id>[0-9]+)/keep/$', views.get_keep, name='keep', namespace='focus'),
    # url(r'^(?P<article_id>[0-9]+)/poll/$', views.get_poll_article, name='poll', namespace='focus'),
    # url(r'^(?P<article_id>[0-9]+)/$', views.article, name='article', namespace='focus'),
    #
]
