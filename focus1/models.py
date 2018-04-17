#-*- coding: utf-8 -*-

import datetime
from django.db.models import Q
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


#null: default False
#blank :  False
#db_column: The name of the database column to use for this field. If this isn’t given, Django will use the field’s name.
#db_index: If True, a database index will be created for this field

#Field.error_messages
#Error message keys include null, blank, invalid, invalid_choice, unique, and unique_for_date


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
	pcate = models.ForeignKey('self')
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





#用户邀请表
#class Contact(models.Model):
#    CHOICES_ORDER_TYPE = (
#        (0, "0"),
#        (1, "1")
#    )
#    #　related_name  设置从关联对象到自身的关系的名称，若值为'+'  则关联对象与自身无逆向关系
#    #contact = models.AutoField( primary_key=True )
#    user = models.OneToOneField(NewUser, related_name="user")
#    contact_user = models.ForeignKey(NewUser, related_name="contact_users")
#    cate = models.OneToOneField(Category, to_field="cate_id", verbose_name="分类"  )
#    contact_date = models.DateTimeField(auto_now=True, verbose_name="邀请时间")
#    task_date = models.DateTimeField(auto_now=True, verbose_name="任务时间")
#    contact_type = models.IntegerField(choices=CHOICES_ORDER_TYPE,  default=0, verbose_name="类型" )
#
#    class Meta:
#        verbose_name = "用户邀请表"
#        verbose_name_plural = verbose_name
#
##订单评价表
#class ContactRemark(models.Model):
#    #ForeignKey.to_field 关联到的关联对象的字段名称。默认地，Django 使用关联对象的主键。
#    contact = models.OneToOneField(Contact, to_field="id")
#    num_remark = models.IntegerField(default=0, verbose_name="评论数量")
#    user = models.ForeignKey(NewUser, related_name="seller")
#	remark_user =  models.ForeignKey(NewUser, related_name="remarkuser")
#    content = models.CharField(max_length=300 )
#    add_time= models.DateTimeField(auto_now_add=True, verbose_name="评价时间")
#	update_time= models.DateTimeField(auto_now=True, verbose_name="评价时间")
#    state= models.IntegerField(default=1,  verbose_name="是否展现")
#    class Meta:
#        verbose_name = "订单评价表"
#        verbose_name_plural = verbose_name
#
#        unique_together = ('user', 'remark_user' )
#
#    ## 计算关注人数总数
#    #def count_remarkusers(self):
#    #    return ContactRemark.objects.filter(user=self).count()
#
#    ## 计算被关注数量
#    #def count_follower(self):
#    #    return ContactRemark.objects.filter(remark_user=self).count()

#
#class UserManager(models.Manager):
#
#    def query_by_column(self, column_id):
#        query = self.get_queryset().filter(column_id=column_id)
#        return query
#
#    def query_by_user(self, user_id):
#        user = User.objects.get(id=user_id)
#        article_list = user.article_set.all()
#        return article_list
#
#    def query_by_polls(self):
#        query = self.get_queryset().order_by('poll_num')
#        return query
#
#    def query_by_time(self):
#        query = self.get_queryset().order_by('-pub_date')
#        return query
#
#    def query_by_keyword(self, keyword):
#        query = self.get_queryset().filter(title__contains=keyword)
#        return query
#
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

#class NewUser(AbstractUser):
#    #增加user其他字段
#    profile = models.CharField('profile', default='',max_length=256)

#    def __str__(self):
#        return self.username

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
	user = models.ManyToManyField('NewUser', blank=True)
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
	user = models.ForeignKey('NewUser', null=True)
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
	user = models.ForeignKey('NewUser', null=True)
	article = models.ForeignKey(Article, null=True)
	comment = models.ForeignKey(Comment, null=True)
