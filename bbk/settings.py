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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'narpk+=p5=zgyy43n+9r#2zig7fq^ez0_!8zz0j0k45=jt_ehe'

DEBUG = True

ALLOWED_HOSTS = ['*']

#替换默认User
AUTH_USER_MODEL = "users.NewUser"  

#登录地址
LOGIN_URL = "/focus/"
#LOGIN_URL = "/users/login/"
#?next='article_id'"

# Application definition

INSTALLED_APPS = (

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'focus',
	'users',
	'order',

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
			'format': '%(levelname)s %(asctime)s %(filename)s[%(lineno)d] %(module)s %(process)d %(thread)d %(message)s'
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
			'handlers': ['console', 'file', 'time_rotatedfile' ],
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

STATIC_ROOT = os.path.join(BASE_DIR, 'static') 
