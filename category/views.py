# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
import django.contrib.auth #import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
#from django.views.decorators.cache import cache_page
from .models import *  #模型
from django.views.decorators.http import require_http_methods

from django.views.generic import ListView, DetailView
from django.contrib.sites.shortcuts import get_current_site
import logging
import pdb, traceback

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from utils.check_code import create_validate_code
from .forms import *
from .models import *
from users.models import Category

from django.conf import settings #读取setting配置

logger = logging.getLogger(__name__)

DEBUG_PDB =settings.DEBUG_PDB



def index(request, catename=None):
    logger.debug('index')
    pdb.set_trace()
    if DEBUG_PDB:
        pdb.set_trace()

    if request.user.is_authenticated:
        #for loggined users
        pass
    else:
        pass
    qset = Category.objects.all()
    if qset.exists():
        for p in qset.values():
            print p

    else:
        pass
	#return redirect( reverse('users:login'), {'success': "you have successfully registered!", "username":username})
    pass
