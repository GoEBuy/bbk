# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import  ContactInfo


import pdb, traceback
import django.utils.timezone as timezone

#https://docs.djangoproject.com/en/1.9/topics/testing/tools/

class SimpleTest(TestCase):

    def setUp(self):
        print "setUp"
        pass

    def testContactInfo(self):
        print "testContactInfo"
        count = ContactInfo.objects.all().count()

        print "count:%d" % (count)
        ContactInfo.objects.create(user_id='new', name='new', email='857659628@qq.com', message='test message')
        count = ContactInfo.objects.all().count()

        print "count:%d" % (count)
