#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
#
#from bbk.focus.models import Article, Comment, Poll, NewUser
#from bbk.focus.forms import CommmentForm, LoginForm, RegisterForm, SetInfoForm, SearchForm

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import * 
import markdown2, urlparse

from django.db.models import Q
from django.views.decorators.http import require_http_methods

from django.views.generic import ListView, DetailView

import logging
import pdb, traceback

# Create your views here.

logger = logging.getLogger(__name__)





@require_http_methods(["GET", "POST"])
def index(request):
	""" 展现当前分类的所有内行人员"""
	logger.debug('index')
	context_object_name = 'user_list'
	template_name ='users/user_list.html'	
	user_list = NewUser.objects.all()
	cate_id = request.GET.get('cate', -1)
	logger.debug("cate: %s" %(str(cate_id)) )
	if cate_id and cate_id<>-1:
		qset= UserStar.objects.filter(cate_id=str(cate_id))
	else:
		qset = UserStar.objects.all()
	if qset.exists():
		useridList = [p.user_id for p in qset ]
		user_list = NewUser.objects.in_bulk(useridList).values()
	else:
		user_list=None
	pref_desc="没有填写内行行业"
	star_serviceDict={}
	star_personalDict={}
	star_totalDict={}
	for u in user_list:
		#if UserInfo.objects.filter(user__id=u.id).exists():
		#	userinfo = UserInfo.objects.get(user__id=u.id)
		star_service1 = NewUser.objects.star_service(u.id)
		star_personal1 = NewUser.objects.star_personal(u.id)
		star_total1 = NewUser.objects.star_total(u.id)
		star_serviceDict[u.id]=star_service1
		star_personalDict[u.id]=star_personal1
		star_totalDict[u.id]=star_total1

		num_following = NewUser.objects.getFollowingNum(u.id, cate_id)

	context={context_object_name:user_list,
	'star_serviceDict':star_serviceDict,
	'star_personalDict':star_personalDict,
	'star_totalDict':star_totalDict,
	'num_following':num_following
	}
	return render(request, template_name, context)

def detail(request, id=None):
	""" 展现内行人信息"""
	logger.debug('detail')
	context_object_name = 'user'
	template_name ='users/user_detail.html'	

	qset =  NewUser.objects.filter(pk=id)
	if qset.exists():
		user= qset[0] 
	
	context={context_object_name:user}
	return render(request, template_name, context)


@require_http_methods(["GET", "POST"])
def getUserPrefList(ListView):
	model = UserStar
	context_object_name = 'userstar_list'


# class
#class index(ListView):
#	""" 展现当前分类的所有内行人员"""
#	logger.debug('index')
#	model=NewUser
#	context_object_name = 'user_list'
#	template_name ='users/user_list.html'	
#
#	def get_queryset(self, *args,**kwargs ):
#		""" 返回自定义过滤条件的queryset"""
#		
#		pass
#		#userList = NewUser.objects.filter() 
#		#return Book.objects.filter(publisher=self.publisher)
#

#class
#class detail(DetailView):
#	logger.debug('getUserDetail')
#	#model = NewUser 
#
#
#	#变量别名
#	context_object_name = 'user'
#		
#	template_name ='users/user_detail.html'	
#
#	def get_object(self):
#		## Call the superclass
#		#object = super(detail, self).get_object()
#		# Record the last accessed date
#		#object.last_accessed = timezone.now()
#		#object.save()
#		# Return the object
#		object = NewUser.objects.get(pk=1)
#		return object
#
	##present some extra information beyond that provided by the generic view.
	#def get_context_data(self, **kwargs):
	#	# Call the base implementation first to get a context
	#	context = super().get_context_data(**kwargs)
	#	return context
	#	# Add in a QuerySet of all the prefs 
	#	context['user'] = NewUser.objects.filter(pk=1)
	#	return context
	##context_object_name = 'user'
	#template_name ='users/user_detail.html'	




		
