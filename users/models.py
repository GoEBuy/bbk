# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models import Q


#null: default False
#blank :  False
#db_column: The name of the database column to use for this field. If this isn’t given, Django will use the field’s name.
#db_index: If True, a database index will be created for this field

#Field.error_messages
#Error message keys include null, blank, invalid, invalid_choice, unique, and unique_for_date

# Create your models here.

class Category(models.Model):
	""" 行业分类 """
	choices_state = (
				  ('0', 'nouse'),
				  ('1', 'inuse'),
				  # ('2', 'Unknown'),
			  ),

	# 如果没有models.AutoField，默认会创建一个id的自增列
	cate_id =  models.AutoField( primary_key=True ) #unique=True,
	cate_name=  models.CharField(max_length=20, null=False, blank=False )
	# 一对一关系, 级联删除, default=-1, on_delete=models.CASCADE
	pcate = models.ForeignKey('self', null=True )
	cate_desc = models.CharField(max_length=50, null=True, verbose_name="备注" )
	state = models.IntegerField(choices =choices_state,  default=1, verbose_name="类别状态")
	update_time =  models.DateTimeField(auto_now=True)

	def __str__(self):
		return ("Category:%s %s %s" %( self.cate_id, self.pcate.cate_id, self.cate_name ) )

	class Meta:
		verbose_name = "分类"
		verbose_name_plural = verbose_name

		#添加索引
		indexes=[
		models.Index(fields=['pcate'], name='idx_pcate' ) , 
		models.Index(fields=['cate_name'], name='idx_cate_name' ) ]


class NewUser(AbstractUser):
	""" 用户 """
	VERIFY_STATUS = (
		(0, "未验证"),
		(1, "已验证")
	)
    #增加user其他字段
    #username = models.CharField( max_length=150, unique=True,
    #    blank=False,
    #    default="",
    #   # help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #    validators=[AbstractUser.username_validator],
    #    error_messages={
    #        'unique': "A user with that username already exists.",
    #    },
    #)
	truename =  models.CharField(max_length=20,  blank=False,default="", verbose_name=u'真实姓名')
	pwd = models.CharField(max_length=20, blank=False, default="", verbose_name=u'')
	is_validate = models.IntegerField(choices=VERIFY_STATUS, default=0, verbose_name=u'姓名是否验证')
	phone = models.CharField(max_length=30,  blank=True, verbose_name=u'手机')
	email_verify = models.IntegerField(choices=VERIFY_STATUS, default=0, verbose_name="Email是否已经验证")
	mobile_verify = models.IntegerField(choices=VERIFY_STATUS, default=0, verbose_name="Mobile是否已经验证")

	city = models.CharField(max_length=50, blank=True, verbose_name=u'所在地')
	address = models.CharField(max_length=150, blank=True, verbose_name=u'地址')
	img = models.ImageField(upload_to="imgs/img_user", blank=True, default="" , verbose_name="头像")
	session = models.CharField(max_length=50, null=True, blank=True, default="",
							   verbose_name="用户登录时会写入当前session_key")
	update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
	profile = models.CharField('profile', default='',max_length=256)
	gender = models.CharField(
		max_length=1,
		choices=(
			('F', 'Female'),
			('M', 'male'),
			('U', 'Unknown'),
		),
		default='M',
	)

	#多对多关系表 用户内行行业列表
	preflist= models.ManyToManyField( Category, through="UserStar", through_fields=('user', 'cate' ) )
	num_following = models.IntegerField(default=0, verbose_name="关注人数" )
	num_followed = models.IntegerField(default=0, verbose_name="被关注人数" )

	def __str__(self):
		return "id:%d name:%s" %(self.id, self.username)

	class Meta:
		verbose_name = "用户"
		verbose_name_plural = verbose_name


	def count_user(self):
		return NewUser.objects.count()

	@classmethod
	def getUser(cls, username, password):
		try:
			user = NewUser.objects.get(Q(username=username) & Q(password=password))
		except Exception as e:
			print "error:", e
			return None
		else:
			return user
		# def delete_user(self, pk=0):
		#     NewUser.objects.get(pk=0)
		#     return NewUser.objects.filter(pk=0).remove()



# class UserLoginInfo(models.Model):
#     """用户登录信息表"""
#     user_id = models.OneToOneField(NewUser, on_delete=models.CASCADE, primary_key=True,  )
#     login_time = models.DateTimeField(auto_now=True, verbose_name="最后一次登录时间")
#     login_cnt = models.IntegerField(default=0, verbose_name="登录次数")
#
#     def __str__(self):
#         return "UserLoginInfo:%s-%s-%s" %(self.user_id, self.login_time, self.login_cnt)
#
#     class Meta:
#         verbose_name = "用户登录信息表"
#         verbose_name_plural = verbose_name


class UserStar(models.Model):
	"""用户星级表"""
#多对多关系
	user = models.ForeignKey(NewUser)
	#user = models.OneToOneField(NewUser)
#user = models.ForeignKey(NewUser, to_field="id", unique=True )
	cate = models.ForeignKey(Category, related_name="cate") 
	star_service = models.IntegerField(default=1,  verbose_name="服务态度")
	star_personal = models.IntegerField(default=1, verbose_name="专业程度")
	desc = models.CharField(max_length=300, default="",verbose_name="用户内行行业自我描述")

	def __str__(self):
		return ("UserStar:%s %s %s" %( self.user, self.cate, self.desc ) )

	class Meta:
		verbose_name = "用户星级表"
		verbose_name_plural = verbose_name

		unique_together= ("user", "cate")



#多对多关系表
class UserFollowing(models.Model):
	"""
	关注信息表
	用户的Following 和 Block 关系表
	"""
	CHOICES = (
		(-1, "None"),
		(0, "False"),
		(1, "True"),
	)

	user = models.ForeignKey(NewUser, verbose_name="用户", on_delete=models.CASCADE, related_name="follower")
	following = models.ForeignKey(NewUser, verbose_name="自己关注的那个用户", on_delete=models.CASCADE,
								  related_name="following")
	is_following = models.IntegerField(choices=CHOICES, default=-1, verbose_name="是否Following")
	is_block = models.IntegerField(choices=CHOICES, default=-1, verbose_name="是否Block")
	add_time = models.DateTimeField( auto_now_add=True, verbose_name="添加时间")
	update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

	class Meta:
		verbose_name = "用户的Following 和 Block 关系表"
		verbose_name_plural = verbose_name
		unique_together = ('user', 'following',)

	def __str__(self):
		return "%s %s" %(self.user.username, self.following.username)

# 计算关注人数总数
	def count_following(self):
		return UserFollowing.objects.filter(user=self, is_following=1).count()

# 计算被关注数量
	def count_follower(self):
		return UserFollowing.objects.filter(following=self, is_following=1).count()

	@classmethod
	def count_following(cls, user):
		UserFollowing.objects.filter(user=user, is_following=1).distinct().count()

	@classmethod
	def count_follower(cls, user):
		return UserFollowing.objects.filter(following=self, is_following=1).count()
