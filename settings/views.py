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
from utils import save_avatar_file
# Create your views here.

logger = logging.getLogger(__name__)

DEBUG_PDB =settings.DEBUG_PDB



def user_settings(request):
    if DEBUG_PDB:
        pdb.set_trace()

    pass

def user_settings_avatar(request):
    if DEBUG_PDB:
        pdb.set_trace()
    if request.method == 'GET':
        user_obj = NewUser.objects.filter(id=request.session.get('user_info')['id']).first()
        return render(request, 'users/setting_avatar.html', locals() )
    if request.method == 'POST':
        has_error=True
        user_obj = NewUser.objects.filter(id=request.session.get('user_info')['id']).first()
        obj = AvatarSettingsForm(request.POST, request.FILES)
        if obj.is_valid():
            avatar= request.FILES['avatar']
            if avatar.size<2*1024*1024:
                avatar_path = save_avatar_file(avatar)
                user_obj.save()
                request.session['user_info']['img'] = user_obj.img
                has_error=False
            else:
                avatar_size_error='頭像文件大小不能超過2M'

        return render(request, 'settings/setting_avatar.html', locals() )
    pass

def user_settings_password(request):
    pass

def user_settings_email(request):
    pass

def user_settings_phone(request):
    pass

 
