#-*- coding:utf-8 -*-

import os
import django

#在导入任何模块之前 设置变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbk.settings")
django.setup()
#setting.configure()

import pdb,traceback

from users import views
from order import views
from focus import views

from django.urls import reverse
from django.template import engines
from django.template.loader import get_template, select_template 

FLAG_DEBUG=True



def testUsers():
	pdb.set_trace()
	reverse ('users:register')
	print reverse ('users:login')

	get_template('users/index.html')
	get_template('users/login.html')
	pass

def main():
	testUsers()


if __name__ == "__main__":
	
	main()
	print('Done!')
