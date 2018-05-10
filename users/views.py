#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import *  #模型
import markdown2, urlparse

from django.db.models import Q
from django.views.decorators.http import require_http_methods

from django.views.generic import ListView, DetailView

import logging
import pdb, traceback

# Create your views here.
from io import BytesIO
from django.shortcuts import render, HttpResponse, redirect
from utils.check_code import create_validate_code
from .forms import *

from django.conf import settings #读取setting配置

logger = logging.getLogger(__name__)

DEBUG_PDB =settings.DEBUG_PDB


def check_code(request):
	"""
	验证码
	:param request:
	:return:
	"""
	stream = BytesIO()
	img, code = create_validate_code()
	img.save(stream, 'PNG')
	request.session['CheckCode'] = code
	return HttpResponse(stream.getvalue())


def login(request):
        if DEBUG_PDB:
            pdb.set_trace()

	if request.method == 'GET':
		form = LoginForm()
		return render(request, 'users/login.html', {'form': form})
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username'].encode('utf-8')
			password = form.cleaned_data['password1'].encode('utf-8')
			#user = authenticate(username=username, password=password)
			user = NewUser.objects.getUser(username, password)
			if user is not None and user.is_active:
                                #保存session
                                #request.session
                                #转到主页
				return redirect( reverse('users:index' ), locals() )
			else:
                                #重新登录
				return render(request, 'users/login.html', {'form': form, 'error': "password or username is not ture!"})

		else:
			return render(request, 'users/login.html', {'form': form})


@login_required
def logout(request):
	pass
	#url = request.POST.get('source_url', '/focus/')
	#logout(request)
	#return redirect(url)


def register(request):
	#pdb.set_trace()
	error1 = "this name is already exist"
	valid = "this name is valid"

	if request.method == 'GET':
		#if a GET (or any other method) we'll create a blank form
		form = RegisterForm()
		return render(request, 'users/register.html', context = {'form': form})
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password1 = form.cleaned_data['password1']
			password2 = form.cleaned_data['password2']
			if password1 != password2:
				return render(request, 'register.html', {'form': form, 'msg': "two password is not equal"})
			else:
				user = NewUser.objects.create(username= username, email= email, password = password1, pwd=password1 )
				user.save()
				return redirect( reverse('users:login'), {'success': "you have successfully registered!", "username":username})
		else:
			return render(request, 'users/register.html', {'form': form})


@require_http_methods(["GET", "POST"])
def index(request):
	""" 展现当前分类的所有内行人员"""
	logger.debug('index')
        if DEBUG_PDB:
            pdb.set_trace()
	context_object_name = 'user_list'
	template_name ='users/index.html'	
	#template_name ='users/user_list.html'	
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
	logger.debug("render %s" %(template_name) )
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



class UserManager(models.Manager):

	@classmethod
	def star_service(cls, id, cate_id=None):
		avg_service =0
		if cate_id and cate_id>=0:
			from .models import *
			qset =UserStar.objects.filter(user__id=id, cate_id=cate_id)
		else:
			from .models import *
			qset =UserStar.objects.filter(user__id=id)
		if qset.exists() :
			avg_service = round( qset.values_list('star_service').aggregate(models.Avg('star_service')).values()[0], 1)

		return avg_service

	@classmethod
	def star_personal(cls, id, cate_id=None):
		avg_personal=0
		if cate_id and cate_id>=0:
			from .models import *
			qset =UserStar.objects.filter(user__id=id, cate_id=cate_id)
		else:
			from .models import *
			qset =UserStar.objects.filter(user__id=id)
		if qset.exists():
			avg_personal = round( qset.values_list('star_personal').aggregate(models.Avg('star_personal')).values()[0], 1)
		return avg_personal

	@classmethod
	def star_total(cls, id ,cate_id=None):
		return round( (UserManager.star_personal(id, cate_id)+UserManager.star_service(id, cate_id) )/2 ,1)

	@classmethod
	def getCommentNum(cls, id, cate_id=None):
		pass


	@classmethod
	def getFollowedNum(cls, id, cate_id=None):
		"""关注此用户的人数"""
		count =0
		if cate_id and cate_id>=0:
			from .models import *
			qset =UserFollowing.objects.filter(following_id=id, cate_id=cate_id)
		else:
			from .models import *
			qset = UserFollowing.objects.filter(following_id= id)
		if qset.exists():
			count = qset.count()
		return count

	@classmethod
	def getFollowingNum(cls, id, cate_id=None):
		count =0
		if cate_id and cate_id>=0:
			from .models import *
			qset =UserFollowing.objects.filter(user_id=id, cate_id=cate_id)
		else:
			from .models import *
			qset = UserFollowing.objects.filter(user_id= id)
		if qset.exists():
			count = qset.count()
		return count

	@classmethod
	def getUser(cls, username, password):
		try:
			user = NewUser.objects.get(Q(username=username) & Q(password=password))
		except Exception as e:
			print "error:", e
			return None
		else:
			return user



	#def getPrefDesc(self, user_id):
	#	try:
	#		user = NewUser.objects.get(pk=user_id)
	#		user.preflist.values()
	#	excep as Exception e:
	#		"not find"
	#		return None
		

	pass
	


		
