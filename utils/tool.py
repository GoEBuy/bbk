#-*- coding:utf-8 -*-

from uuid import uuid4
import uuid
import os
from django.conf import settings #读取setting配置


def handle_uploaded_file(f):
	with open('some/file/name.txt', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

			

#def get_mac_address():
#	"""通用方法,借助uuid模块"""
#    #import uuid
#    node = uuid.getnode()
#    #mac = uuid.UUID(int = node)
#    mac = uuid.UUID(int = node).hex[-12:]
#　　return mac


#def get_mac_address():
#    """ 按照操作系统平台来 """
#    import sys
#    import os
#    mac = None
#    if sys.platform == "win32":
#        for line in os.popen("ipconfig /all"):
#            print line
#            if line.lstrip().startswith("Physical Address"):
#                mac = line.split(":")[1].strip().replace("-", ":")
#                break
#			if line.lstrip().startswith("物理地址"):
#                mac = line.split(":")[1].strip().replace("-", ":")
#                break
#    else:
#        for line in os.popen("/sbin/ifconfig"):
#            if 'Ether' in line:
#                mac = line.split()[4]
#                break
#    return mac

def gender_random_code():
    random_code=str(uuid4()).split("-")[0]
    return random_code

def save_avatar_file(file):
    # file_con = file.content_type
    random_code = gender_random_code()
    file_type = file.name.split('.')[-1]
    save_file_name = random_code + '.' + file_type
    file_path = os.path.join( settings.AVATAR_FILE_PATH, save_file_name)
    # print(file_path)
    with open(file_path, 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)
    return '/static/img/' + save_file_name
