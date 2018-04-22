#-*- coding:utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from focus import urls as focus_urls
from users import urls as users_urls
from users import views
from users.urls import *





urlpatterns = [

	# ex: /
	url(r'^$',  views.index, name='home'),
	#ex: /admin/
	url(r'^admin/', include(admin.site.urls)),

	#ex: /focus/
	url(r'^focus/', include(focus_urls)),

	#ex: /users/
	url(r'^users/', include(users_urls)),

	#url(r'^cate/', include() ),

	#url(r'^admin/',  views.index, name='home'),
	# url(r'^blog/', include('blog.urls')),
	#url(r'^$', views.index, name='index'),
]
