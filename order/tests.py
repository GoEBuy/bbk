#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

#from bbk.users.models import NewUser as User
from models import *

import pdb, traceback
import django.utils.timezone as timezone

#https://docs.djangoproject.com/en/1.9/topics/testing/tools/


class SimpleTest(TestCase):

    def setUp(self):
        print "setUp"
        pass

    # def testUser(self):
    #     print "testUser"
    #
    #     count = User.objects.all().count()
    #     print User.objects.all()
    #     print "count:%d" % (count)
    #     # User.model()
    #     User.objects.create(username="yyy", phone="15011033945", city="beijing", email="8678@qq.com")
    #     User.objects.create(username="yyf", phone="13323323796", city="shanxi", email="867628@qq.com")
    #     User.objects.create(username="apple", phone="15011033945", city="shanghai", email="867628@qq.com")
    #     count = User.objects.all().count()
    #     print User.objects.all()
    #     print "count:%d" %(count)
    #     # User1 = User.objects.get(pk=1)
    #     # print "get user", User1
    #     # User1.delete()
    #     # count = User.objects.all().count()
    #     # print User.objects.all()
    #     # print "count:%d" %(count)
    #     pass

    #def testAddCate(self, pcate_id=-1):
    #    print "testAddCate"



    #    count = Category.objects.all().count()
    #    print Category.objects.all()
    #    print "count:%d" % (count)

    #    Category.objects.create(cate_id=-1, pcate_id=-1, cate_name="root", state=1, cate_desc="root category",
    #                            update_time=timezone.now)
    #    count = Category.objects.all().count()
    #    print Category.objects.all()
    #    print "count:%d" % (count)
    #    # User.model()
    #    pcate = Category.objects.get(pk=pcate_id)
    #    print "pcate: ", pcate
    #    #
    #    Category.objects.create(cate_id=1, pcate=pcate, cate_name="transport", state=1, cate_desc="交通运输",
    #                            update_time=timezone.now)
    #    Category.objects.create(cate_id=2, pcate=pcate, cate_name="bussiness", state=1, cate_desc="电脑办公",
    #                           )
    #    Category.objects.create(cate_id=3, pcate_id=-1, cate_name="house", state=1, cate_desc="房产",
    #                           )
    #    Category.objects.create(cate_id=4, pcate_id=-1, cate_name="guide", state=1, cate_desc="当地向导",
    #                           )
    #    count = Category.objects.all().count()
    #    print Category.objects.all()
    #    print ("Category count:%d" % (count))

    #def testDelUser(self):
    #    print "testDelUser"
    #    # count = User.objects.all().count()
    #    # print User.objects.all()
    #    # print "count:%d" % (count)
    #    # # User.model()
    #    # User1 = User.objects.get( id=1)
    #    # print "get user", User1
    #    # User1.delete()
    #    # count = User.objects.all().count()
    #    # print User.objects.all()
    #    # print "count:%d" % (count)
    #    # count = User.objects.all().count()
    #    # print User.objects.all()
    #    # print "count:%d" %(count)
    #    pass

# def
