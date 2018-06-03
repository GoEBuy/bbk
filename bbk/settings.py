#-*- coding:utf-8 -*-


"""

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#from bbk.focus.models import *
#from bbk.users.models import *

#bbk root dir /bbk
BASE_DIR = os.path.dirname(  os.path.dirname(os.path.abspath(__file__) ) )


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'narpk+=p5=zgyy43n+9r#2zig7fq^ez0_!8zz0j0k45=jt_ehe'

DEBUG = True
DEBUG_PDB=False
#DEBUG_PDB=True

ALLOWED_HOSTS = ['*']

#替换默认User
AUTH_USER_MODEL = "users.NewUser"  

#登录地址
LOGIN_URL = "/users/login/"
#?next='article_id'"

# Application definition

INSTALLED_APPS = (

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

##自定義APP模塊
    'focus',
    'users',
    'order',
#    'settings',
    'category',
    'contact', #聯系我們

    #'allauth',
    #'allauth.account',
    #'allauth.socialaccount',
    #'stripe'

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    #'middle.custom_middle.CountOnlineMiddlewareMixin', 
)

ROOT_URLCONF = 'bbk.urls'


#模板引擎
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
		# APP_DIRS 告诉模板引擎是否应该进入每个已安装的应用中查找模板。每种模板引擎后端都定义了一个惯用的名称作为应用内部存放模板的子目录名称。
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
	#{
	#	'BACKEND': 'django.template.backends.jinja2.Jinja2',
	#		'DIRS': [	'/home/html/jinja2', ],
	#},
]




WSGI_APPLICATION = 'bbk.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
	'default': {  
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'bbk', #你的数据库名称 数据库需要自己提前建好
		'USER': 'root', #你的数据库用户名
		'PASSWORD': 'root', #你的数据库密码
		'HOST': 'localhost', #你的数据库主机，留空默认为localhost
		'PORT': '3306', #你的数据库端口
	},
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #},
	'mysql': {  
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'bbk', #你的数据库名称 数据库需要自己提前建好
		'USER': 'root', #你的数据库用户名
		'PASSWORD': 'root', #你的数据库密码
		'HOST': 'localhost', #你的数据库主机，留空默认为localhost
		#'HOST': '192.168.1.160', #你的数据库主机，留空默认为localhost
		'PORT': '3306', #你的数据库端口
		 'OPTIONS': { 'init_command': 'SET default_storage_engine=INNODB,character_set_connection=utf8,collation_connection=utf8_unicode_ci;' }
	}
}

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'verbose': {
			'format': '%(levelname)s %(asctime)s [%(filename)s:%(lineno)d] [%(module)s] %(process)d %(thread)d %(message)s'
		},
		'simple': {
			'format': '%(levelname)s %(message)s'
		},
	},
	'handlers': {
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter':'simple'
		},
		'file': {
			'level': 'DEBUG',
			'class': 'logging.FileHandler',
			'filename': 'logs/debug.log',
			'formatter':'verbose'
		},
		'email': {
			'level': 'ERROR',
			'class': 'django.utils.log.AdminEmailHandler',
			'include_html' : True,
		},
		'error': {
			'level':'ERROR',
			'class':'logging.handlers.TimedRotatingFileHandler',
			'filename': 'logs/error.log',
			'backupCount': 5,
			'formatter':'verbose',
		},
		'time_rotatedfile': {
			'level':'DEBUG',
			'class':'logging.handlers.TimedRotatingFileHandler',
			'filename':'logs/bbk.log',
			#'when':'D',
			#'interval':1
		},
	},
	'loggers': {
		'django': {
			'handlers': ['console', 'file', 'time_rotatedfile', 'error' ],
			'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
		},
	},
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

#LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = True 

USE_I18N = True

USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join( os.path.dirname(BASE_DIR), 'static').replace('\\','/')

STATICFILES_DIRS = [
    
    '/var/www/static/',
    os.path.join( BASE_DIR, 'static')
]

#static用来放网站自己的图片、js、css等
#media用来放用户上传的图片、文件等
MEDIA_URL = '/media/'  
MEDIA_ROOT = os.path.join( os.path.dirname(BASE_DIR), 'media').replace('\\', '/')  

# 头像存放目录（当然也可以使用OSS等云存储，这里存储到本地）
#/static/img
AVATAR_FILE_PATH = os.path.join(BASE_DIR, 'static', 'img')


# 缓存相关
CACHES = {
# 默认配置，cache 单独使用
    "default": {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    },

    "file": {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    },


	#"default": {
	#	"BACKEND": "django_redis.cache.RedisCache",
	#	"LOCATION": "redis://127.0.0.1:6379/1",
	#	"OPTIONS": {
	#		"CLIENT_CLASS": "django_redis.client.DefaultClient",
	#	}
	#},
# 新增配置让session 使用，
	#"session": {
        #      'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        #              'LOCATION': 'unix:/tmp/memcached.sock',
	#},
    "session": {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    },

	#"session1": {
	#	"BACKEND": "django_redis.cache.RedisCache",
	#	"LOCATION": "redis://127.0.0.1:6379/0",
	#	"OPTIONS": {
	#		"CLIENT_CLASS": "django_redis.client.DefaultClient",
	#	}
	#}
}
# session 相关配置
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"
SESSION_COOKIE_NAME = "sessionid"
SESSION_COOKIE_PATH = "/"
SESSION_COOKIE_AGE = 60 * 200 
## 用户刷新页面，重新设置缓存时间
#SESSION_SAVE_EVERY_REQUEST = True


# 分页器配置
#PRE_PAGE_COUNT = 15
#PAGER_NUMS = 7

# 邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
## SMTP服务器
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
# TODO
# 发送邮件的邮箱
EMAIL_HOST_USER = '857659628@qq.com'
## 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'younger646689'
## 收件人看到的发件人
EMAIL_FROM = 'bbk<857659628@sina.com>'


#CELERY_BEAT_SCHEDULE = {
#    # 周期性任务
#    'task-one': {
#        'task': 'app.tasks.print_hello',
#        'schedule': 5.0, # 每5秒执行一次
#        # 'args': ()
#    },
#    # 定时任务
#    'task-two': {
#        'task': 'app.tasks.print_hello',
#        'schedule': crontab(minute=0, hour='*/3,10-19'),
#        # 'args': ()
#    }
#}



