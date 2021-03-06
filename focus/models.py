#-*- coding: utf-8 -*-

import datetime
from django.db.models import Q
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
####################################################################################################################################################

#自定义
class ArticleManager(models.Manager):

	def query_by_column(self, column_id):
		query = self.get_queryset().filter(column_id=column_id)
		return query

	def query_by_user(self, user_id):
		user = User.objects.get(id=user_id)
		article_list = user.article_set.all()
		return article_list

	def query_by_polls(self):
		query = self.get_queryset().order_by('poll_num')
		return query

	def query_by_time(self):
		query = self.get_queryset().order_by('-pub_date')
		return query

	def query_by_keyword(self, keyword):
		query = self.get_queryset().filter(title__contains=keyword)
		return query

class Column(models.Model):
	name = models.CharField('column_name', max_length=256)
	intro = models.TextField('introduction', default='')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'column'
		verbose_name_plural = 'column'
		ordering = ['name']

class Article(models.Model):
	#一对多
	column = models.ForeignKey(Column, blank=True, null=True, verbose_name = 'belong to')
	title = models.CharField(max_length=256)
	#一对多
	author = models.ForeignKey('Author')
	#多对多
	user = models.ManyToManyField('users.NewUser', blank=True)
	content = models.TextField('content')
	pub_date = models.DateTimeField(auto_now_add=True, editable=True)
	update_time = models.DateTimeField(auto_now=True, null=True)
	published = models.BooleanField('notDraft', default=True)
	poll_num = models.IntegerField(default=0)
	comment_num = models.IntegerField(default=0)
	keep_num = models.IntegerField(default=0)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'article'
		verbose_name_plural = 'article'

	objects = ArticleManager()


class Comment(models.Model):
    #多对多关系 中间关系表
	user = models.ForeignKey('users.NewUser', null=True)
	article = models.ForeignKey(Article, null=True)
	content = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True, editable=True)
	poll_num = models.IntegerField(default=0)
	def __str__(self):
		return self.content



class Author(models.Model):
	name = models.CharField(max_length=256)
	profile = models.CharField('profile', default='',max_length=256)
	password = models.CharField('password', max_length=256)
	register_date = models.DateTimeField(auto_now_add=True, editable=True)

	def __str__(self):
		return self.name

#点赞
class Poll(models.Model):
	#多对多  中间关系表
	user = models.ForeignKey('users.NewUser', null=True)
	article = models.ForeignKey(Article, null=True)
	comment = models.ForeignKey(Comment, null=True)
