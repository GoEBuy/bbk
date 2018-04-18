#-*- coding:utf-8 -*-

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbk.settings")
django.setup()
#setting.configure()

import pdb,traceback

#from focus.models import *
from users.models import *
from django.db.models import Manager

import django.utils.timezone as timezone


def getEntityCount(entity):
	count = entity.all().count()
	print entity.all()
	#print "count:%d" % (count)
	return count
	

def getUsersByIdList():
	manager=NewUser.objects
	idlist=[1,2,3]
	dict_users= manager.in_bulk(idlist)
	for k, v in dict_users.iteritems():
		print k, v
	
def getUserById():
	manager=NewUser.objects
	if manager.filter(username="admin",password="admin").exists():
		print "exists"
	else:
		print "not exist"
	

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
			NewUser.objects.create(username=name, password=pwd, pwd=pwd,  phone="15011033945", city="beijing", email="8678@qq.com" )
		else:
			print "username:%s exists" %(name)

	count = getEntityCount(NewUser.objects)
	print "count:%d" % (count)

	#f = open('oldblog.txt')
	#for line in f:
	#title,content = line.split('****')
	#Blog.objects.create(title=title,content=content)
	#f.close()


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

def getPCates():
	manager= Category.objects
	cate = manager.get(pk=5)
	pcate = manager.get(cate_id=cate.pcate.cate_id)
	print pcate
	pcate1 = manager.get(cate_id=pcate.pcate.cate_id)
	print pcate1


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
			manager.create(user=user, cate = cate, star_personal=star_personal, star_service = star_service, desc = desc)
			#Category.objects.get(pk=cate_id)
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
			manager.get_or_create(user=k, following=v, add_time=timezone.now  )

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

def main():
	#getUserById()
	#addUsers()
	#getUsersByIdList()

	#addCate()
	#getSubCates()
	getPCates()
	#addUserPref()


	#addUserFollowing()
	#updateUserFollowing()
	#findUserFollowing()
	#deleteUserFollowing()

if __name__ == "__main__":
	
	main()
	print('Done!')




