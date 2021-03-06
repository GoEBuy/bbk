# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q
#import UserManager
from django.contrib.auth.models import  BaseUserManager, AbstractBaseUser, AbstractUser, UserManager


#null: default False
#blank :  False
#db_column: The name of the database column to use for this field. If this isn’t given, Django will use the field’s name.
#db_index: If True, a database index will be created for this field

#Field.error_messages
#Error message keys include null, blank, invalid, invalid_choice, unique, and unique_for_date

# Create your models here.

class UserManager(UserManager):

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



	#def getPrefDesc(self, user_id):
	#	try:
	#		user = NewUser.objects.get(pk=user_id)
	#		user.preflist.values()
	#	excep as Exception e:
	#		"not find"
	#		return None


	pass


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
	cate_desc = models.CharField(max_length=50, null=True, verbose_name=u"备注" )
	state = models.IntegerField(choices =choices_state,  default=1, verbose_name=u"类别状态")

	update_time =  models.DateTimeField(auto_now=True)

	def __str__(self):
		return ("Category:%s %s %s" %( self.cate_id,
		( self.pcate.cate_id if self.pcate  else "none" ), self.cate_name ) )

	def printObj(self, sep='\t'):
		"""自定义打印对象所有属性 """
		return sep.join(['%s:%s' %item for item in self.__dict__.items() ]  )

	#def get_absolute_url(self):
	#	return reverse('author-detail', kwargs={'pk': self.pk})


	class Meta:
		verbose_name = u"分类"
		verbose_name_plural = verbose_name

		#添加索引
		indexes=[
		models.Index(fields=['pcate'], name='idx_pcate' ) ,
		models.Index(fields=['cate_name'], name='idx_cate_name' ) ]


class NewUser(AbstractUser):
	""" 用户 """
	VERIFY_STATUS = (
		(0, u"未验证"),
		(1, u"已验证")
	)
    #增加user其他字段
    #username = models.CharField( max_length=150, unique=True,
    #   # help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #    validators=[AbstractUser.username_validator],
    #    error_messages={
    #        'unique': "A user with that username already exists.",
    #    },
    #)
	pwd = models.CharField(max_length=20, blank=False, default="", verbose_name=u'密码')
	phone = models.CharField(max_length=30,  blank=True, verbose_name=u'手机')
	session = models.CharField(max_length=50, null=True, blank=True, default="", help_text=u"用户登录时会写入当前session_key")

	level= models.IntegerField(default=0, help_text=u'用户等级')
	is_pref= models.BooleanField(default=False, help_text='是否是内行人')
	#多对多关系表 用户内行行业列表
	preflist= models.ManyToManyField( Category, through="UserStar", through_fields=('user', 'cate' ) )
	num_following = models.IntegerField(default=0, verbose_name=u"关注人数" )
	num_followed = models.IntegerField(default=0, verbose_name=u"被关注人数" )

	def __str__(self):
		return "id:%d name:%s" %(self.id, self.username)

	def printObj(self, sep='\t'):
		"""自定义打印对象所有属性 """
		return sep.join(['%s:%s' %item for item in self.__dict__.items() ]  )

	class Meta:
		verbose_name = u"用户"
		verbose_name_plural = verbose_name

	#使用自定义的Manager
	objects = UserManager()
	#objects = UserManager.UserManager()



	def count_user(self):
		return NewUser.objects.count()


class UserInfo(models.Model):
    """用戶詳情表"""
    VERIFY_STATUS = (
        (0, u"未验证"),
        (1, u"已验证")
    )
    user = models.OneToOneField(NewUser)
    truename =  models.CharField(max_length=20,  blank=True, default="", help_text=u'真实姓名')
    birthdate = models.DateField(null=True, blank=True, help_text=u'出生日期' )
    is_validate = models.IntegerField(choices=VERIFY_STATUS, default=0, help_text=u'姓名是否验证')
    email_verify = models.IntegerField(choices=VERIFY_STATUS, default=0, help_text=u"Email是否已经验证")
    mobile_verify = models.IntegerField(choices=VERIFY_STATUS, default=0, help_text=u"Mobile是否已经验证")

    city = models.CharField(max_length=50, blank=True, help_text=u'所在地')
    address = models.CharField(max_length=150, blank=True, verbose_name=u'地址')
    img = models.ImageField(upload_to="imgs/img_user", blank=True, verbose_name=u"头像")
    profile = models.CharField('profile', default='',max_length=256)
    my_home = models.CharField(max_length=30, null=True, blank=True, default="", verbose_name="登录后首页跳转")
    gender = models.CharField(
        max_length=1,
        choices=(
            ('F', 'Female'),
            ('M', 'male'),
            ('U', 'Unknown'),
        ),
        default='M',
    )
    bio = models.CharField(max_length=300, null=True, blank=True, default="", verbose_name=u"个人简介")
	#register_ip=models.CharField(max_length=30, blank=True, default='', help_text=u'注册ip' )
    add_time = models.DateTimeField(auto_now_add=True, help_text=u"添加时间")
    update_time = models.DateTimeField(auto_now=True, help_text=u"更新时间")

    def __str__(self):
        return "id:%d name:%s" %(self.id, self.user)

    def printObj(self, sep='\t'):
        """自定义打印对象所有属性 """
        return sep.join(['%s:%s' %item for item in self.__dict__.items() ]  )

    class Meta:
        verbose_name = u"用户详细信息表"
        verbose_name_plural = verbose_name



class SignedInfo(models.Model):
    """
    用户签到
    """
    CHOICES_TYPE = (
        (False, "未签到"),
        (True, "已经签到")
    )
    user = models.OneToOneField(NewUser)
    status = models.BooleanField(choices=CHOICES_TYPE, verbose_name="是否签到")
    #datefields yyyy-mm-dd
    date = models.DateField(auto_now=True, verbose_name="签到日期")
    signed_day = models.IntegerField(default=0, verbose_name="连续签到天数")
    add_time = models.DateTimeField(auto_now=True, verbose_name="时间")

    class Meta:
        verbose_name = "用户签到"
        verbose_name_plural = verbose_name
        unique_together = ('user', 'signed_day')

    def __str__(self):
        return self.user.username

    def printObj(self, sep='\t'):
            """自定义打印对象所有属性 """
            return sep.join(['%s:%s' %item for item in self.__dict__.items() ]  )


class OpenUser(models.Model):
	#id
	user= models.OneToOneField(NewUser)
	open_type=models.IntegerField(default=0,
		choices=(
			(0, 'unknown'),
			(1, 'qq'),
			(2, 'wechat'),
			(3, 'taobao'),
			(4, 'skype'),
			(5, 'linkin'),
			(6, u'未知'),
		), verbose_name=u'开放帐号类型'
	)
	def __str__(self):
		return "OpenUser user:%s" %(self.id, self.user)
	def printObj(self, sep='\t'):
		"""自定义打印对象所有属性 """
		return sep.join(['%s:%s' %item for item in self.__dict__.items() ]  )

	class Meta:
		verbose_name = u"用户开放登录帐号表"
		verbose_name_plural = verbose_name

class UserValidateInfo(models.Model):
	#id
	user = models.OneToOneField(NewUser)
	valid_type=models.IntegerField(default=0,
		choices=(
			(0, u'身份证'),
			(1, u'护照'),
			(2, u'学生证'),
			(3, u'工作证'),
			(4, u'士兵证'),
			(5, u'手机号'),
			(6, u'邮箱'),
			(7, u'未知'),
		), verbose_name=u'认证类型'
	)
	cert_no=models.CharField(max_length=50, default="", blank=False , verbose_name=u'认证号码' )
	valid_state =models.IntegerField(
		choices=(
			(0, u'未认证'),
			(1, u'认证中'),
			(2, u'已认证'),
			(3, u'未知'),
			(4, u'士兵证'),
			(5, u'手机号'),
			(6, u'邮箱'),
		),  default=0, verbose_name=u'认证状态'
	)
	valid_captcha=models.CharField(max_length=15, default='', verbose_name=u'认证验证码')
	valid_captcha_exp =models.CharField(max_length=25, default='', verbose_name=u'认证验证码过期时间')

	submit_time = models.DateTimeField(auto_now=True, verbose_name=u"申请验证时间")
	audit_time = models.DateTimeField(auto_now=True, verbose_name=u"审核时间")
	create_time = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")

	def __str__(self):
		return "UserValidateInfo user:%s" %(self.id, self.user)

	def printObj(self, sep='\t'):
		"""自定义打印对象所有属性 """
		return sep.join(['%s:%s' %item for item in self.__dict__.items() ]  )
	class Meta:
		verbose_name = u"用户身份认证资料表"
		verbose_name_plural = verbose_name


#class UserPoints(models.Model):
#	#id
#	user = models.OneToOneField(NewUser)
#	points= models.IntegerField(default=0, verbose_name='积分')
#	points_frozen=models.IntegerField(default=0, verbose_name='冻结积分')
#	points_consumed=models.IntegerField(default=0, verbose_name='已消费积分')
#	def __str__(self):
#		return "UserPoints user:%s" %(self.id, self.user)
#
#	class Meta:
#		verbose_name = "用户积分表"
#		verbose_name_plural = verbose_name


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
	star_service = models.IntegerField(default=1,  verbose_name=u"服务态度")
	star_personal = models.IntegerField(default=1, verbose_name=u"专业程度")
	desc = models.CharField(max_length=300, default="",verbose_name=u"用户内行行业自我描述")

	def __str__(self):
		return ("UserStar:%s %s %s" %( self.user, self.cate, self.desc ) )
	def printObj(self, sep='\t'):
		"""自定义打印对象所有属性 """
		return sep.join(['%s:%s' %item for item in self.__dict__.items() ]  )

	class Meta:
		verbose_name = u"用户星级表"
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

	user = models.ForeignKey(NewUser, verbose_name=u"用户", on_delete=models.CASCADE, related_name="follower")
	following = models.ForeignKey(NewUser, verbose_name=u"自己关注的那个用户", on_delete=models.CASCADE,
								  related_name="following")
	is_following = models.IntegerField(choices=CHOICES, default=-1, verbose_name=u"是否Following")
	is_block = models.IntegerField(choices=CHOICES, default=-1, verbose_name=u"是否Block")
	add_time = models.DateTimeField( auto_now_add=True, verbose_name=u"添加时间")
	update_time = models.DateTimeField(auto_now=True, verbose_name=u"更新时间")

	def __str__(self):
		return "%s %s" %(self.user.username, self.following.username)
	def printObj(self, sep='\t'):
		"""自定义打印对象所有属性 """
		return sep.join(['%s:%s' %item for item in self.__dict__.items() ]  )

	class Meta:
		verbose_name = u"用户的Following 和 Block 关系表"
		verbose_name_plural = verbose_name
		unique_together = ('user', 'following',)

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
		return UserFollowing.objects.filter(following='self', is_following=1).count()






class CateManager(models.Manager):
	pass

