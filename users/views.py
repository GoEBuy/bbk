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
import pdb, traceback
from .models import NewUser
import markdown2, urlparse

from django.db.models import Q

# Create your views here.


def index(request):
	context={}
	return render(request, 'index.html', context)
	#latest_article_list = Article.objects.query_by_time()
	#loginform = LoginForm()
	#context = {'latest_article_list': latest_article_list, 'loginform':loginform}
	#return render(request, 'index.html', context)
