# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from users.models import *

# Create your models here.

class Address(models.Model):
	#id
	user = models.ForeignKey(NewUser, related_name='address_buyer') #user_id
	phone = models.CharField(max_length=20, blank=False, verbose_name='收货人联系电话')
	phone_bak = models.CharField(max_length=20, verbose_name='备用联系电话')
	country= models.CharField(max_length=10, default='')
	province = models.CharField(max_length=10, default='')
	city = models.CharField(max_length=10, default='')
	area = models.CharField(max_length=10, default='')
	street = models.CharField(max_length=10, default='')
	zipcode = models.CharField(max_length=10, default='')
	is_default_address = models.BooleanField( default=False)
	create_time =  models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return ("UserStar:%s %s %s" %( self.user, self.cate, self.desc ) )

	def printObj(self, sep='\n'):
		"""自定义打印对象所有属性 """
		return sep.join(['%s:%s' %item for item in user.__dict__items() ]  )  

	class Meta:
		verbose_name = "收货地址表"
		verbose_name_plural = verbose_name

		#添加索引
		#indexes=[
		#models.Index(fields=['pcate'], name='idx_pcate' ) , 
		#models.Index(fields=['cate_name'], name='idx_cate_name' ) ]



class Logistics(models.Model):	

	choices_express_type=(
		(0,'ems'),
		(1,'epress'),
		(2,'other'),
		(3,'none'),
	)
	
	#id
	#express_id = models.OneToOneField(Express, verbose_name='物流表')
	buyer = models.ForeignKey(NewUser, verbose_name='收货人姓名', related_name='logistics_buyer') #buyer_id
	buyer_phone = models.CharField(max_length=20, blank=False, verbose_name='收货人联系电话')
	buyer_phone_bak = models.CharField(max_length=20, verbose_name='备用联系电话')

	seller = models.ForeignKey(NewUser, verbose_name='商家', related_name='logistics_seller') #seller_id	
	seller_phone = models.CharField(max_length=20, blank=False, verbose_name='收货人联系电话')
	seller_phone_bak = models.CharField(max_length=20, verbose_name='备用联系电话')

	address=models.CharField(max_length=50, verbose_name='收货地址')
	zipcode =models.CharField(max_length=15, verbose_name='邮政编码') #blank=False
	express_type = models.IntegerField(choices= choices_express_type, default=3, verbose_name='物流方式')
	desc = models.CharField(max_length=150, verbose_name='描述')

	def printObj(self, sep='\n'):
		"""自定义打印对象所有属性 """
		return sep.join(['%s:%s' %item for item in user.__dict__items() ]  )  

	class Meta:
		verbose_name = "物流表"
		verbose_name_plural = verbose_name

	#添加索引
	#indexes=[
	#models.Index(fields=['pcate'], name='idx_pcate' ) , 
	#models.Index(fields=['cate_name'], name='idx_cate_name' ) ]



class Order(models.Model):

	choices_state=(
		(0, '未付款')  , 
		(1, '已付款'),
		(2, '进行中'),
		(3, '已完成'),
		(4, '退货申请'),
		(5, '退货中'),
		(6, '已退货'),
		(7, '取消交易'),
		(8, '其他'),
		(9, '未知'),
	)

	choices_payment=(
		(0,'现金'),
		(1,'微信'),
		(2,'支付宝'),
		(3,'第三方支付'),
		(4,'其他'),
		(5, '未知'),
	)
	"""订单表"""
	order_id = models.AutoField(primary_key=True)
	order_state= models.IntegerField( choices=choices_state, default=0, blank=False, verbose_name="订单状态" )
	order_price= models.CharField(max_length=30, default=0, blank=False, verbose_name="订单价格")
	address = models.OneToOneField( Address, null=True, verbose_name='收货地址表')
	cate = models.OneToOneField(Category, to_field="cate_id", verbose_name="分类" )
	logistics= models.OneToOneField(Logistics, verbose_name='物流', null=True) #logistics_id
	pay_channel=models.IntegerField(choices=choices_payment, default=0, blank=False, verbose_name='支付渠道')
	
	create_time =  models.DateTimeField(auto_now_add=True)
	pay_time =  models.DateTimeField(auto_now=True)
	deal_time=   models.DateTimeField(auto_now=True, verbose_name='订单交易时间')
	buyer = models.ForeignKey(NewUser, related_name='buyer')
	#seller  = models.ForeignKey(NewUser)
	remark=models.CharField(max_length=250, verbose_name='用户备注')

	def __str__(self):
		return ("Order:%s buyer:%s order_state:%s" %( self.order_id,	self.buyer, self.order_state ) )

	def printObj(self, sep='\n'):
		"""自定义打印对象所有属性 """
		return sep.join(['%s:%s' %item for item in user.__dict__items() ]  )  


	class Meta:
		verbose_name = "订单表"
		verbose_name_plural = verbose_name

		#添加索引
		#indexes=[
		#models.Index(fields=['pcate'], name='idx_pcate' ) , 
		#models.Index(fields=['cate_name'], name='idx_cate_name' ) ]





class OrderRemark(models.Model):
	#id
	order = models.OneToOneField(Order,  to_field="order_id")
	num_remark = models.IntegerField(default=0, verbose_name="评论数量")
	seller = models.ForeignKey(NewUser, verbose_name='卖家' , related_name="orderremark_seller")
	buyer =  models.ForeignKey(NewUser, verbose_name='买家', related_name="orderremark_buyer")
	content = models.CharField(max_length=300, verbose_name='评价内容' )
	cate = models.ForeignKey(Category)
	score_service= models.IntegerField(default=3, verbose_name='服务态度')
	score_personal = models.IntegerField(default=3, verbose_name='专业程度')
	add_time= models.DateTimeField(auto_now_add=True, verbose_name="评价时间")
	update_time= models.DateTimeField(auto_now=True, verbose_name="评价时间")
	state= models.IntegerField(default=1,  verbose_name="是否展现")

	def __str__(self):
		return ("OrderRemark:%s %s %s" %( self.seller, self.cate, self.buyer ) )

	def printObj(self, sep='\n'):
		"""自定义打印对象所有属性 """
		return sep.join(['%s:%s' %item for item in user.__dict__items() ]  )  


	class Meta:
		verbose_name = "订单评价表"
		verbose_name_plural = verbose_name
		#unique_together = ('user', 'remark_user' )
			
		#默认降序排序
		ordering =['-id']

#
#    ## 计算关注人数总数
#    #def count_remarkusers(self):
#    #    return ContactRemark.objects.filter(user=self).count()
#
#    ## 计算被关注数量
#    #def count_follower(self):
#    #    return ContactRemark.objects.filter(remark_user=self).count()




