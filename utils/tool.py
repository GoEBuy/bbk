#-*- coding:utf-8 -*-


def handle_uploaded_file(f):
	with open('some/file/name.txt', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

			

def get_mac_address():
	"""通用方法,借助uuid模块"""
　　import uuid
      node = uuid.getnode()
	  #mac = uuid.UUID(int = node)
      mac = uuid.UUID(int = node).hex[-12:]
　　return mac


def get_mac_address():
    """ 按照操作系统平台来 """
    import sys
    import os
    mac = None
    if sys.platform == "win32":
        for line in os.popen("ipconfig /all"):
            print line
            if line.lstrip().startswith("Physical Address"):
                mac = line.split(":")[1].strip().replace("-", ":")
                break
			if line.lstrip().startswith("物理地址"):
                mac = line.split(":")[1].strip().replace("-", ":")
                break
    else:
        for line in os.popen("/sbin/ifconfig"):
            if 'Ether' in line:
                mac = line.split()[4]
                break
    return mac