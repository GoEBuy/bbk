# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from users.models import NewUser


class ContactInfo(models.Model):
    name=models.CharField(max_length=30)
    user=models.ForeignKey(NewUser, null=True )
    email = models.EmailField()
    message=models.CharField(max_length=350 )
    create_time = models.DateTimeField(auto_now=True )

    def __str__(self):
        return ("ContactInfo:%s %s %s" %( self.id, self.name, self.message) )

    def printObj(self, sep='\t'):
        """自定义打印对象所有属性 """
        return sep.join(['%s:%s' %item for item in self.__dict__.items() ]  )  

	class Meta:
		verbose_name = u"聯系我們"
		verbose_name_plural = verbose_name

		#添加索引
		indexes=[
		    models.Index(fields=['name'], name='name' ) ,
                ]
