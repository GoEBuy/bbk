#-*- coding:utf-8 -*-

import os
import django

#在导入任何模块之前 设置变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbk.settings")
django.setup()
#setting.configure()


from django.db.models import Avg, Sum, Max, Min


import pdb,traceback

from order.models import *
from users.models import *
from users import UserManager

from django.db.models import Manager
import django.utils.timezone as timezone


FLAG_DEBUG=True


def getEntityCount(entity):
	count = entity.all().count()
	print entity.all()
	#print "count:%d" % (count)
	return count
	
def testFindUser():
	print "testFindUser"
	manager = NewUser.objects
	#print manager.values('id','username', 'password').filter(username='yyy', password='yyy').exists()
	#wrong print manager.exists(username='yyy', password='yyy')
	#print manager.filter(pk=2).exists()
	print user.printObj()
	
def getUserListByCate():
	cate_id=1
	qset= UserStar.objects.filter(cate_id=str(cate_id))
	if qset.exists():
		useridList = [p.user_id for p in qset ]
		for k, v in NewUser.objects.in_bulk(useridList).iteritems():

			print k, v

def getUsersByIdList():
	manager=NewUser.objects
	idlist=[1,2,3]
	#select in 
	dict_users= manager.in_bulk(idlist)
	for k, v in dict_users.iteritems():
		print k, v
	
def getUserById():
	manager=NewUser.objects
	if manager.filter(username="admin",password="admin").exists():
		print "exists"
	else:
		print "not exist"
	
def addUserInfo():
	user = NewUser.objects.get(pk=2)
	#NewUser.objects.get(id__
	userinfo = UserInfo.objects.get(user_id=2)
	user.userinfo = UserInfo.objects.create(user_id=1, truename='root true name')
	user.save()
	user.userinfo.truename='root true name update'
	user.save()



	

def addUsers():
	#count = NewUser.objects.all().count()
	#print NewUser.objects.all()
	count = getEntityCount(NewUser.objects)
	print "count:%d" % (count)

	insertUsers = [("admin","admin"), ("root","root"), ("yyy", "yyy"), ("yyf", "yyf"), ("yangyuanyang","yangyuanyang"), ("a","a")]
	for i in xrange(len(insertUsers) ):
		name, pwd = insertUsers[i]
		#NewUser.objects.get_or_create(username=name, pwd=pwd) #返回的是tuple,：(对象, 是否是创建的) 
		#NewUser.objects.getorcreate()
		#NewUser.objects.bulk_create([]) #数据批量导入bulk_create()
		
		if not NewUser.getUser(name, pwd):
			NewUser.objects.create(username=name, password=pwd, pwd=pwd,  phone="15011033945" ) #, city="beijing", email="8678@qq.com" )
		else:
			print "username:%s exists" %(name)

	count = getEntityCount(NewUser.objects)
	print "count:%d" % (count)

	#f = open('oldblog.txt')
	#for line in f:
	#title,content = line.split('****')
	#Blog.objects.create(title=title,content=content)
	#f.close()

def updateCate(id,  cate_name=None, cate_desc=None):
	cate = Category.objects.get(pk=id)
	cate.cate_name=cate_name
	cate.cate_desc=cate_desc
	cate.save()


def addCate():
	count = getEntityCount(Category.objects)
	print "count:%d" % (count)

	#root_cate=Category.objects.get(pk=-1)
	#Category.objects.create( pcate= root_cate, cate_name="buz", state=1, cate_desc="商务办公", update_time=timezone.now ) 
	Category.objects.get_or_create(cate_id=-1, cate_name="root cate" , cate_desc="root cate" )

	root_cate=Category.objects.get(pk=-1)

	insertCates = [(1, root_cate, "transport", "交通运输" ), (2, root_cate, "house", "房产销售" ), (3, root_cate, "bussiness", "电脑办公"), (4, root_cate, "guide", "当地向导")]

	for i in xrange(len(insertCates) ):
		print insertCates[i]
		cate_id, pcate, cate_name, cate_desc = insertCates[i]
		try:
			Category.objects.get_or_create(pk=cate_id)
			print "category:%s exists" %(cate_id)
		except Category.DoesNotExist:
			Category.objects.create(cate_id=cate_id, pcate=pcate, cate_name=cate_name, state=1, cate_desc=cate_desc, update_time=timezone.now ) 
		#else:

	count = getEntityCount(Category.objects)
	print "count:%d" % (count)

	cate1=Category.objects.get(pk=1)
	insertCates1 = [(5, cate1, "ershoucar", "二手车" ), (6, cate1, "newcar", "新车" ) ]

	for i in xrange(len(insertCates1) ):
		print insertCates1[i]
		cate_id, pcate, cate_name, cate_desc = insertCates1[i]
		try:
			Category.objects.get(pk=cate_id)
			print "category:%s exists" %(cate_id)
		except Category.DoesNotExist:
			Category.objects.create(cate_id=cate_id, pcate=cate1, cate_name=cate_name, state=1, cate_desc=cate_desc, update_time=timezone.now ) 
		#else:

	count = getEntityCount(Category.objects)
	print "count:%d" % (count)

def getSubCates():
	manager = Category.objects
	print manager.values_list("cate_id", "cate_name", "pcate_id").filter(pcate_id=1)
	pass


def getCatePrefsForUser():
	""" 多表关联查询 查询用户所有内行行业及相应分值"""
	# __:两个下划线可以生成连接查询，查询关联的字段信息
	# _set:提供了对象访问相关联表数据的方法。但这种方法只能是相关类访问定义了关系的类（主键类访问外键类）
	manager = UserStar.objects
	manager.filter(user__id='1').values()
	manager.filter(user__id=1).values()
	if manager.filter(user__id='2').exists():
		print manager.filter(user__id='2')

def getPCates():
	manager= Category.objects
	cate = manager.get(pk=5)
	pcate = manager.get(cate_id=cate.pcate.cate_id)
	print pcate
	pcate1 = manager.get(cate_id=pcate.pcate.cate_id)
	print pcate1

def updateUserPref():
	print "updateUserPref"
	#user= NewUser.objects.get(pk=1)
	user = NewUser.getUser("admin","admin")
	if UserStar.objects.filter(user_id=1, cate_id=1).exists():
		userstar = UserStar.objects.get(user_id=user.id, cate_id=1)
		userstar.star_service=5
		userstar.save()
	print userstar

def getUserPrefList():
	user = NewUser.objects.get(pk=1)
	qset = user.preflist.values()
	if qset.exists():
		for p in qset:
			print p


def getStarService(user_id, cate_id):
	manager = NewUser.objects
	avg_service = manager.star_service(user_id, cate_id)
	avg_personal = manager.star_personal(user_id, cate_id)
	avg_total = manager.star_total(user_id, cate_id)
	pass

	#avg_service =0
	#avg_personal =0
	#avg_total =0
	#user = NewUser.objects.get(pk=1)
	##多表关联， 通过关联表反向查询
	#qset =UserStar.objects.filter(user__id=1)
	#if qset.exists():
	#	avg_service = qset.values_list('star_service').aggregate(Avg('star_service')).values()[0]
	#	avg_personal = qset.values_list('star_personal').aggregate(Avg('star_personal')).values()[0]
	#	#servicelist=[f.star_service for f in qset.values('star_service') ]
	#	#personallist=[f.star_personal for f in qset.values('star_personal') ]
	#	#avg_service = mean(servicelist)
	#	#avg_personal = mean(personallist)
	#	avg_total = (avg_service+avg_personal)/2
	print "avg_service:%f avg_personal:%f avg_total :%f" %(avg_service ,avg_personal, avg_total)
	#return avg_service



def addUserPref():
	""" 用户内行专业CRUD """
	manager = UserStar.objects
	count = getEntityCount(UserStar.objects)
	print "count:%d" % (count)

	user = NewUser.getUser("admin","admin")
	cate1=Category.objects.get(pk=1)
	cate2=Category.objects.get(pk=2)
	cate3=Category.objects.get(pk=3)
	insertCates1 = [(cate1, 3, 2, "cate 1 desc"), (cate2, 1, 5, "cate 2 desc" ), (cate3, 2,5, "cate 3 desc") ]

	for i in xrange(len(insertCates1) ):
		print insertCates1[i]
		cate, star_service , star_personal, desc = insertCates1[i]
		try:
			#多对多关系表,由第三方关系表添加
			manager.get_or_create(user=user, cate = cate, star_personal=star_personal, star_service = star_service, desc = desc)
			user.is_pref=1
			user.save()
			#print "category:%s exists" %(cate_id)
		except Exception as e:
			print "err", e
			continue

	count = getEntityCount( UserStar.objects)
	print "count:%d" % (count)

	pass


def addUserFollowing():
	user1 = NewUser.objects.get(pk=1)
	print user1
	user2 = NewUser.objects.get(pk=2)
	print user2
	user3 = NewUser.objects.get(pk=3)
	print user3
	user4 = NewUser.objects.get(pk=4)
	print user4
	user5 = NewUser.objects.get(pk=5)
	print user5

	manager = UserFollowing.objects
	try:
		following_list=[(user1, user2), (user1,user3), (user1, user4), (user1,user5), (user2, user3), (user2, user4) ]
		for k,v in following_list:
			manager.create(user=k, following=v, add_time=timezone.now  )
			#manager.get_or_create(user=k, following=v, add_time=timezone.now  )

		#manager.create(user=user1, following=user2, add_time=timezone.now , update_time=timezone.now)
		#manager.create(user=user1, following=user3, add_time=timezone.now , update_time=timezone.now)
		#manager.create(user=user1, following=user4, add_time=timezone.now , update_time=timezone.now)
		#manager.create(user=user1, following=user5, add_time=timezone.now , update_time=timezone.now)
		#manager.create(user=user2, following=user3, add_time=timezone.now , update_time=timezone.now)
		#manager.create(user=user2, following=user4, add_time=timezone.now , update_time=timezone.now)
	except Exception as e:
		print "err", e

	pass

def updateUserFollowing():
	
	manager = UserFollowing.objects
	print "update before", manager.get(pk=1).update_time
	manager.filter(pk=1).update(update_time=timezone.now() )
	print "update affter", manager.get(pk=1).update_time


def findUserFollowing():
	""" 获取user的所有关注 """
	user_id =1
	manager = UserFollowing.objects
	user1 = NewUser.objects.get(pk=1)
	print user1

	# 获取user的所有关注着
	print manager.filter(following=user1).values()

	#获取该用户所有关注的人
	print manager.filter(user=user1).values()
	print manager.filter(user_id= user_id).values()
	print manager.filter(following_id= user_id).values()

	for f in manager.filter(following= user1 ).values():
		print f

	for f in manager.filter(user = user1).values():
		print f
	

def deleteUserFollowing():
	user_id =1
	manager = UserFollowing.objects
	user1 = NewUser.objects.get(pk=1)
	print user1


	user2 = NewUser.objects.get(pk=2)
	print user2

	manager.filter(user=user1, following = user2)
	manager.delete(user=user1, following=user2)
	manager.filter(user_id=user1.id, following = user2.id).values()

#def addUsers1():
#	defaults = {'first_name': 'Bob'}
#	try:
#		obj = Person.objects.get(first_name='John', last_name='Lennon')
#		for key, value in defaults.items():
#			setattr(obj, key, value)
#			obj.save()
#	except Person.DoesNotExist:
#		new_values = {'first_name': 'John', 'last_name': 'Lennon'}
#		new_values.update(defaults)
#		obj = Person(**new_values)
#		obj.save()



def addOrder():
	manager = Order.objects
	print "count", getEntityCount(manager)

	user = NewUser.objects.get(pk=1)
	cate = Category.objects.get(pk=2)
	print "user:", user
	obj = manager.get_or_create( order_price='15.0', remark='add order', buyer = user, cate_id=3  )
	obj = manager.get_or_create( order_price='15.0', remark='add order', buyer = user, cate=cate  )

	print "count", getEntityCount(manager)



def main():
	
	#addOrder()
	#testFindUser()
	#addUserInfo()

	#getUserListByCate()
	#getUserById()
	#addUsers()
	#getUsersByIdList()

	#addCate()
	#updateCate(1,"transport", "交通运输")
	#updateCate(2,"house", "房产销售")
	#updateCate(3,"bussiness", "电脑办公")
	#updateCate(4,"guide", "当地向导")
	#getSubCates()
	#getPCates()

	getStarService(1, -1)
	#getUserPrefList()
	#addUserPref()
	#updateUserPref()

	#getCatePrefsForUser()
	#addUserFollowing()
	#updateUserFollowing()
	#findUserFollowing()
	#deleteUserFollowing()

if __name__ == "__main__":
	
	main()
	print('Done!')




