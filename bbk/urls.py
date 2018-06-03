#-*- coding:utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from focus import urls as focus_urls
from users import urls as users_urls
from category import urls as cates_urls
from users import views as users_views
from contact import urls as contact_urls





urlpatterns = [

	# ex: /
	url(r'^$',  users_views.index, name='home'),
	#ex: /admin/
	url(r'^admin/', include(admin.site.urls)),

	#ex: /focus/
	url(r'^focus/', include(focus_urls)),

	#ex: /users/
	url(r'^users/', include(users_urls)),

	url(r'^cates/', include(cates_urls)),

	url(r'^contact/', include(contact_urls )),

#	url(r'^settings/', include(settings_urls)),



	#url(r'^admin/',  views.index, name='home'),
	# url(r'^blog/', include('blog.urls')),
	#url(r'^$', views.index, name='index'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 
    
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
