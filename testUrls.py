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
from django.shortcuts import render_to_response 
from django.template import Context  

FLAG_DEBUG=True

def printReverseUrl(nameUrl):
	try:
		print "url[%s]: %s" %(nameUrl, reverse ('users:register') )
	except Exception as e:
		print traceback.sys_exc()

def printTemplateRender(template, context=None, saveFmt=False, **kawgs):
	""" 打印渲染后的模板 """
	if not context:
		if kawgs:
			context = Context(kawgs)
		else:
			context = Context({})

	html = get_template(template).render(context).encode('utf-8')
	print ("html for template:", template)
	print html
	if saveFmt:
		#"save formate html"
		with open(template+'.fmt', 'w') as fout:
			fout.write(html+'\n')
			fout.close()


def testUsers():
	pdb.set_trace()
	#print reverse ('users:register')
	#print reverse ('users:login')
	printReverseUrl('users:register')
	printReverseUrl('users:login')

	#print get_template('users/login.html')
	#print get_template('users/index.html')
	#printTemplateRender('users/login.html')
	from users.models import NewUser 
	user = NewUser.objects.get(pk=1)
	printTemplateRender('users/user_detail.html', context={'user':user}, saveFmt=True )
	pass

def main():
	testUsers()


if __name__ == "__main__":
	
	main()
	print('Done!')
