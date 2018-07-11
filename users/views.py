#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
import django.contrib.auth #import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
#from django.views.decorators.cache import cache_page
from .models import *  #模型
#import markdown2, urlparse
#from django.db.models import Q
from django.views.decorators.http import require_http_methods

from django.views.generic import ListView, DetailView
from django.contrib.sites.shortcuts import get_current_site
import logging
import pdb, traceback

# Create your views here.
from io import BytesIO
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
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


def register(request):
    DEBUG_PDB=True
    if DEBUG_PDB:
        pdb.set_trace()

    msg=None

    if request.method == 'GET':
            #plat= request.GET.get('plat', '0')
            #if plat=='2':
            #    resp = {'errorcode':200, 'msg':'ok', 'result':100 }
            ##返回json对象
            #response  = JsonResponse(resp)
            #return response
            form = RegisterForm()
            return render(request, 'users/register.html', context = {'form': form})
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        if form.is_valid():
            if plat in form.cleaned_data:
                plat  = form.cleaned_data['plat']
            else:
                plat='0'
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                if plat=="2":
                    resp = {'errorcode':500, 'msg':'invalid password', 'result':None }
                    ##返回json对象
                    response  = JsonResponse(resp)
                    return response
                msg="two password is not equal"
                return render(request, 'register.html', {'form': form, 'msg': msg })
            else:
                #注冊成功
                if NewUser.objects.filter(username=username).exists():
                    #用户名已存在
                    return render(request, 'users/register.html', {'form': form})

                user = NewUser.objects.create_user(username= username, email= email, password = password1, pwd=password1 )
                user.save()
                userinfo=None
                try:
                    userinfo = user.userinfo
                except:
                    # 注册成功，创建用户details 表
                    userinfo = UserInfo.objects.create(user_id=user.id)
                if plat=="2":
                    result = json.dumps({"username":username})
                    resp = {'errorcode':200, 'msg':'register succ', 'result':result }
                    ##返回json对象
                    response  = JsonResponse(resp)
                    return response
                #跳轉至登錄頁面
            return redirect( reverse('users:login'), {'success': "you have successfully registered!", "username":username})
        else:
            return render(request, 'users/register.html', {'form': form})

def login(request):
    DEBUG_PDB = True
    if DEBUG_PDB:
        pdb.set_trace()

    #resp = {'errorcode':200, 'msg':'ok', 'result':100 }
    #返回json对象
    #respnse  = JsonResponse(resp)
    #return HttpResponse(json.dumps(resp), content_type="application/json")
    current_site = get_current_site(request)
    if request.method == 'GET':
        #request get请求参数 返回QueryDict
        plat = request.GET.get('plat','0')
        if plat=='2':
            resp = {'errorcode':200, 'msg':'ok', 'result':None}
            #返回json对象
            response  = JsonResponse(resp)
            return response
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
    if form.is_valid():
            plat = '0'
            if 'plat' in form.cleaned_data:
                plat = form.cleaned_data['plat'].encode('utf-8')
            username = form.cleaned_data['username'].encode('utf-8')
            password = form.cleaned_data['password1'].encode('utf-8')
            user = django.contrib.auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                    userinfo=None
                    try:
                        userinfo = user.userinfo
                    except:
                        pass
                    # 账号密码正确，登录成功 修改最后登录时间
                    django.contrib.auth.login(request, user)
                    #user.last_login = datetime.datetime.now()
                    # 获取用户本次session_key 记录到数据库中，以便在其他地方修改此用户的session 信息
                    user.session = request.session.session_key
                    #保存user_info session
                    user.save()

                    #獲取用戶詳細信息， 注冊時已經創建， 這裏是防止admin等用戶未創建產生的BUG
                    if UserInfo.objects.filter(user_id=user.id).exists():
                        userinfo = UserInfo.objects.get(user_id = user.id )
                    else:
                        userinfo = UserInfo.objects.create(user_id=user.id)

                    #用戶籤到信息
                    signed_status = False
                    if SignedInfo.objects.filter(user_id=user.id, date=datetime.datetime.now().strftime('%Y-%m-%d'), status=True ).exists():
                        signed_info = SignedInfo.objects.get(user_id=user.id, date= datetime.datetime.now().strftime('%Y-%m-%d'), status=True )

                        if signed_info:
                            signed_status=True


                    # 获取用户基础信息，存放到session中，方便频繁调用
                    user.password=None
                    user.pwd=None
                    #查看內存大小
                    #import sys
                    #print sys.getsizeof(user)
                    user_info={
                        'id':user.id,
                        'username': username,
                        'user':user,
                        'userinfo':userinfo,
                        'daily_mission':signed_status,
                            }
                    #保存至session
                    request.session['user_info'] = user_info

                    #登錄後頁面跳轉， 默認转到主页
                    if request.POST.get('next', None ):
                        next_url = request.POST.get('next')
                    elif userinfo.my_home:
                        next_url = userinfo.my_home
                    else:
                        next_url = reverse( 'users:index')

                    #如果用戶定義了登錄後跳轉，則跳轉到用戶制定的頁面

                    return redirect( next_url, locals() )
                    if plat=='2':
                            result={'user_info':user_info}
                            resp = {'errorcode':200, 'msg':'ok', 'result': result, 'next':None}
                            #返回json对象
                            response  = JsonResponse(resp)
                            return response
            else:
                #登錄失敗
                if plat=='2':
                        resp = {'errorcode':500, 'msg':'login error', 'result': None}
                        #返回json对象
                        response  = JsonResponse(resp)
                        return response
                    #重新登录
                return render(request, 'users/login.html', {'form': form, 'error': "password or username is not true!"})

    else:
                #表單錯誤
        return render(request, 'users/login.html', {'form': form})


@login_required
@require_http_methods(["GET", "POST"])
def logout(request):
    DEBUG_PDB=True
    if DEBUG_PDB:
        import pdb
        pdb.set_trace()
    # 如果用户登录了
    django.contrib.auth.logout(request)
    if request.session.get('user_info', None):
        # 删除登录用户统计信息
        online_key = 'count_online_id_{_id}_session_{_session}'.format(
            _id=request.session.get('user_info')['id'], _session=request.session.session_key)
        cache.delete(online_key)
        # 清除 session 信息
        request.session.flush()
    return render(request, 'users/logout.html')



@require_http_methods(["GET", "POST"])
def index(request):
	""" 展现当前分类的所有内行人员"""
	logger.debug('index')
        if DEBUG_PDB:
            pdb.set_trace()


        if request.user.is_authenticated:
            #for loggined users
            pass
        else:
            pass
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

	context={
                context_object_name:user_list,
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
@login_required
def user_settings(request):
    DEBUG_PDB=True
    if DEBUG_PDB:
        pdb.set_trace()

    if request.method == 'GET':
            form = SettingsForm()
            user_detail_obj = request.session.get('user_info')['user']
            if not user_detail_obj:
                user_detail_obj = NewUser.objects.get(user_id=request.session.get('user_info' )['id'] )
            user_info_obj = request.session.get('user_info')['userinfo']
            if not user_info_obj:
                user_info_obj = UserInfo.objects.get(user_id=request.session.get('userinfo')['id'])
            return render(request, 'users/settings.html', locals() )
    if request.method == 'POST':
            form = SettingsForm(request.POST)
            if form.is_valid():
                    #userid = request.POST.get('user_id')
                    username = form.cleaned_data['username'].encode('utf-8')
                    #NewUser.objects.

            return render(request, 'users/settings.html', locals() )
    pass

@require_http_methods(["GET", "POST"])
def getUserPrefList(ListView):
	model = UserStar
	context_object_name = 'userstar_list'


@require_http_methods(["GET", "POST"])
@login_required
def user_settings_avatar(request):
    if DEBUG_PDB:
        pdb.set_trace()


    if request.method == 'GET':
        user_obj = NewUser.objects.get(id=request.session.get('user_info')['id'] )
        user_obj.password=None
        try:
            userinfo = user_obj.userinfo
            return render(request, 'users/setting_avatar.html', {'user':user_obj,'userinfo':userinfo } )
        except:
            return render(request, 'users/setting_avatar.html', {'user':user_obj,'userinfo':None} )
            pass
        pass
    if request.method == 'POST':
        has_error=True
        user_obj = NewUser.objects.get(id=request.session.get('user_info')['id'] )
        obj = AvatarSettingsForm(request.POST, request.FILES)
        if obj.is_valid():
            avatar= request.FILES['avatar']
            if avatar.size<2*1024*1024:
                from utils.tool import save_avatar_file
                avatar_path = save_avatar_file(avatar)
                logger.debug('save avatar file:'+avatar_path )
                user_obj.save()
                #request.session['user_info']['userinfo']['img'] = user_obj.img
                has_error=False
            else:
                avatar_size_error='頭像文件大小不能超過2M'

        return render(request, 'users/setting_avatar.html', locals() )




@login_required
def user_settings_password(request):
    if DEBUG_PDB:
        pdb.set_trace()

    if request.method == 'GET':
        return redirect( reverse( 'users:settings' ))
    elif request.method =='POST':
        form = PasswordSettingsForm(request.POST)
        has_err= False
        if form.is_valid():
            password_cur=form.cleaned_data['password_current']
            password_new = form.cleaned_data['password_new']
            password_again = form.cleaned_data['password_again']
            #判斷密碼是否正確
            username = request.settings.get('user_info')['username']
            user_obj = django.contrib.auth.authenticate(username=username, password=password_cur)

            if user_obj is not None:
                if password_new == password_again:
                    #修改密碼
                    user_obj.set_password(password_new)
                    user_obj.pwd=password_new
                    user_obj.save()
                    has_password_error = False
                else:
                    has_err=True
                    password_error="您兩次輸入的密碼不一樣"
            else:
                has_err = True
                password_error="您輸入的用戶密碼不正確"
            password_cur=None
            password_new = None
            return render( request, 'users/setting_password.html', locals()  )
        else:
            password_cur=None
            password_new = None
            return render( request, 'users/setting_password.html', locals()  )

@login_required
def user_settings_email(request):
    pass

@login_required
def user_settings_phone(request):
    pass

@login_required
@require_http_methods(["GET", "POST"])
def following(request):
    if request.method == 'GET':
        pass
    elif request.method =='POST':
        pass
    pass

@login_required
@require_http_methods(["GET", "POST"])
def unfollowing(request):
    if request.method == 'GET':
        pass
    elif request.method =='POST':
        pass
    pass
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
