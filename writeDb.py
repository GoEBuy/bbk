#-*- coding:utf-8 -*-

import os
import django
import pdb,traceback

from focus.models import *






#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")




def addUsers():
	pdb.set_trace()
	count = NewUser.objects.all().count()
	print NewUser.objects.all()
	print "count:%d" % (count)

	insertUsers = [("admin","admin"), ("root","root"), ("yangyuanyang","yangyuanyang") ("a","a")]
	for name,pwd in insertUsers:
		NewUser.objects.create(username=name, password=pwd, pwd=pwd,  phone="15011033945", city="beijing", email="8678@qq.com" )

	count = NewUser.objects.all().count()
	print NewUser.objects.all()
	print "count:%d" % (count)
	#f = open('oldblog.txt')
	#for line in f:
	#title,content = line.split('****')
	#Blog.objects.create(title=title,content=content)
	#f.close()



def main():
	addUsers()

if __name__ == "__main__":
	
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")
	django.setup()
	setting.configure()
	main()
	print('Done!')




