#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from bbk.users.models import NewUser as User
from models import *

import pdb, traceback
import django.utils.timezone as timezone

#https://docs.djangoproject.com/en/1.9/topics/testing/tools/

#python manage.py test

#python manage.py test SimpleTest.tests

#python manage.py test bbk.order.SimpleTestCase

#python manage.py test.bbk.order.SimpleTestCase.testFindUser


class SimpleTestCase(TestCase):

	#def setUp(self):
	#	print "setUp"
	#	pass


	#def getCount(self, Entity):
	#	manager = Entity.objects
	#	cnt = manager.all().count()
	#	return cnt 

	#def testFindUser(self):
	#	print "testFindUser"
	#	manager = User.objects
	#	pdb.set_trace()
	#	user = manager.get(pk=1)
	#	print user
	#	print manager.exists(pk=1)
	#	print manager.exists(username='yyy', password='yyy')
    #	#user.set_password(raw_password):

	#	#user.check_password(raw_password):
	#

	#def testAddUser(self):
	#	 print "testAddUser"

	#	 count = User.objects.all().count()
	#	 print User.objects.all()
	#	 print "count:%d" % (count)
	#	 # User.model()
	#	 User.objects.get_or_create(username="yyy", phone="15011033945", city="beijing", email="8678@qq.com")
	#	 User.objects.get_or_create(username="yyf", phone="13323323796", city="shanxi", email="867628@qq.com")
	#	 User.objects.get_or_create(username="apple", phone="15011033945", city="shanghai", email="867628@qq.com")
	#	 count = getCount(User)  
	#	 #print User.objects.all()
	#	 print "count:%d" %(count)
	#	 # User1 = User.objects.get(pk=1)
	#	 # print "get user", User1
	#	 # User1.delete()
	#	 # count = User.objects.all().count()
	#	 # print User.objects.all()
	#	 # print "count:%d" %(count)
	#	 pass

	#def testAddCate(self, pcate_id=-1):
	#	print "testAddCate"

	#	count = Category.objects.all().count()
	#	print Category.objects.all()
	#	print "count:%d" % (count)

	#	#Category.objects.get_or_create(cate_id=-1, pcate_id=-1, cate_name="root", state=1, cate_desc="root category", update_time=timezone.now)
	#	count = Category.objects.all().count()
	#	print Category.objects.all()
	#	print "count:%d" % (count)
	#	pcate = Category.objects.get(pk=pcate_id)
	#	print "pcate: ", pcate
	#	
	#	Category.objects.get_or_create(cate_id=1, pcate=pcate, cate_name="transport", state=1, cate_desc="交通运输",
	#							update_time=timezone.now)
	#	Category.objects.get_or_create(cate_id=2, pcate=pcate, cate_name="bussiness", state=1, cate_desc="电脑办公",
	#						   )
	#	Category.objects.get_or_create(cate_id=3, pcate_id=-1, cate_name="house", state=1, cate_desc="房产",
	#						   )
	#	Category.objects.get_or_create(cate_id=4, pcate_id=-1, cate_name="guide", state=1, cate_desc="当地向导",
	#						   )
	#	count = Category.objects.all().count()
	#	print Category.objects.all()
	#	print ("Category count:%d" % (count))

	#def testDelUser(self):
	#	print "testDelUser"
	#	manager=User.objects
	#	count = manager.all().count()
	#	# print User.objects.all()
	#	print "count:%d" % (count)
	#	# User1 = User.objects.get( id=1)
	#	# print "get user", User1
	#	# User1.delete()
	#	# count = User.objects.all().count()
	#	# print User.objects.all()
	#	# print "count:%d" % (count)
	#	# count = User.objects.all().count()
	#	# print User.objects.all()
	#	# print "count:%d" %(count)
	#	pass

