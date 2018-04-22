#-*- coding:utf-8 -*-
from django.db import models

from .models import *


class UserManager(models.Manager):

	@classmethod
	def star_service(cls, id, cate_id=None):
		avg_service =0
		if cate_id and cate_id>=0:
			from .models import *
			qset =UserStar.objects.filter(user__id=id, cate_id=cate_id)
		else:
			from .models import *
			qset =UserStar.objects.filter(user__id=id)
		if qset.exists() :
			avg_service = round( qset.values_list('star_service').aggregate(models.Avg('star_service')).values()[0], 1)

		return avg_service

	@classmethod
	def star_personal(cls, id, cate_id=None):
		avg_personal=0
		if cate_id and cate_id>=0:
			from .models import *
			qset =UserStar.objects.filter(user__id=id, cate_id=cate_id)
		else:
			from .models import *
			qset =UserStar.objects.filter(user__id=id)
		if qset.exists():
			avg_personal = round( qset.values_list('star_personal').aggregate(models.Avg('star_personal')).values()[0], 1)
		return avg_personal

	@classmethod
	def star_total(cls, id ,cate_id=None):
		return round( (UserManager.star_personal(id, cate_id)+UserManager.star_service(id, cate_id) )/2 ,1)

	@classmethod
	def getCommentNum(cls, id, cate_id=None):
		pass


	@classmethod
	def getFollowedNum(cls, id, cate_id=None):
		"""关注此用户的人数"""
		count =0
		if cate_id and cate_id>=0:
			from .models import *
			qset =UserFollowing.objects.filter(following_id=id, cate_id=cate_id)
		else:
			from .models import *
			qset = UserFollowing.objects.filter(following_id= id)
		if qset.exists():
			count = qset.count()
		return count

	@classmethod
	def getFollowingNum(cls, id, cate_id=None):
		count =0
		if cate_id and cate_id>=0:
			from .models import *
			qset =UserFollowing.objects.filter(user_id=id, cate_id=cate_id)
		else:
			from .models import *
			qset = UserFollowing.objects.filter(user_id= id)
		if qset.exists():
			count = qset.count()
		return count

	@classmethod
	def getUser(cls, username, password):
		try:
			user = NewUser.objects.get(Q(username=username) & Q(password=password))
		except Exception as e:
			print "error:", e
			return None
		else:
			return user



	#def getPrefDesc(self, user_id):
	#	try:
	#		user = NewUser.objects.get(pk=user_id)
	#		user.preflist.values()
	#	excep as Exception e:
	#		"not find"
	#		return None
		

	pass
	
	#:def 


class CateManager(models.Manager):
	pass

	#def query_by_column(self, column_id):
	#	query = self.get_queryset().filter(column_id=column_id)
	#	return query

	#def query_by_user(self, user_id):
	#	user = User.objects.get(id=user_id)
	#	article_list = user.article_set.all()
	#	return article_list

	#def query_by_polls(self):
	#	query = self.get_queryset().order_by('poll_num')
	#	return query

	#def query_by_time(self):
	#	query = self.get_queryset().order_by('-pub_date')
	#	return query

	#def query_by_keyword(self, keyword):
	#	query = self.get_queryset().filter(title__contains=keyword)
	#	return query
