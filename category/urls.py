#encoding:utf-8

from django.conf.urls import include, url
import views

app_name  = 'cate'

urlpatterns = [

    #ex: /category
    url(r'^$', views.index, name='all'),

    url(r'^(?P<catename>.*)/', views.index, name='cate'),
    #######
    #ex: /transport
    #url(r'^transport/', views.index, name='transport', kwargs={'catename':'transport'}),

    ##ex: /housedesign
    #url(r'^housedesign/', views.index, name='housedesign'),
    ##ex: /guide
    #url(r'^guide/', views.index, name='guide'),
]
