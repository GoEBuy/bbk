#-*- coding:utf-8 -*-

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")
django.setup()
#setting.configure()

import pdb,traceback

from focus.models import *
from django.db.models import Manager

import django.utils.timezone as timezone


def getEntityCount(entity):
	count = entity.all().count()
	print entity.all()
	#print "count:%d" % (count)
	return count
	




def addUsers():
	pdb.set_trace()
	#count = NewUser.objects.all().count()
	#print NewUser.objects.all()
	count = getEntityCount(NewUser.objects)
	print "count:%d" % (count)

	insertUsers = [("admin","admin"), ("root","root"), ("yangyuanyang","yangyuanyang"), ("a","a")]
	for i in xrange(len(insertUsers) ):
		name, pwd = insertUsers[i]
		if not NewUser.getUser(name, pwd):
			NewUser.objects.create(username=name, password=pwd, pwd=pwd,  phone="15011033945", city="beijing", email="8678@qq.com" )
		else:
			print "username:%s exists" %(name)

	count = getEntityCount(NewUser.objects)
	print "count:%d" % (count)

	#f = open('oldblog.txt')
	#for line in f:
	#title,content = line.split('****')
	#Blog.objects.create(title=title,content=content)
	#f.close()


def addCate():
	count = getEntityCount(Category.objects)
	print "count:%d" % (count)

	pdb.set_trace()
	root_cate=Category.objects.get(pk=-1)

	insertCates = [(1, root_cate, "transport", "交通运输" ), (2, root_cate, "house", "房产销售" ), (3, root_cate, "bussiness", "电脑办公"), (4, root_cate, "guide", "当地向导")]

	for i in xrange(len(insertCates) ):
		print insertCates[i]
		cate_id, pcate, cate_name, cate_desc = insertCates[i]
		try:
			Category.objects.get(pk=cate_id)
			print "category:%s exists" %(cate_id)
		except Category.DoesNotExist:
			Category.objects.create(cate_id=cate_id, pcate=pcate, cate_name=cate_name, state=1, cate_desc=cate_desc, update_time=timezone.now ) 
		#else:

	count = getEntityCount(Category.objects)
	print "count:%d" % (count)

	cate1=Category.objects.get(pk=1)
	insertCates1 = [(5, cate1, "ershoucar", "二手车" ), (6, cate1, "newcar", "新车" ) ]

	for i in xrange(len(insertCates1) ):
		print insertCates1[i]
		cate_id, pcate, cate_name, cate_desc = insertCates1[i]
		try:
			Category.objects.get(pk=cate_id)
			print "category:%s exists" %(cate_id)
		except Category.DoesNotExist:
			Category.objects.create(cate_id=cate_id, pcate=cate1, cate_name=cate_name, state=1, cate_desc=cate_desc, update_time=timezone.now ) 
		#else:

	count = getEntityCount(Category.objects)
	print "count:%d" % (count)



def addUserPref():
	""" 用户内行专业CRUD """
	pass


def main():
	#addUsers()

	addCate()

if __name__ == "__main__":
	
	main()
	print('Done!')




