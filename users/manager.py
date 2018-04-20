#-*- coding:utf-8 -*-
from django.db import models


class UserManager(models.Manager):
	pass
	
	#:def 

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
