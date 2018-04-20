#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

class NewUserAdmin(admin.ModelAdmin):
	list_display = ('id', 'username',  'last_login', 'email', 'is_staff',
					"phone",  'date_joined' )


#admin.site.register(NewUser,  NewUserAdmin)
#admin.site.register(Category)
#admin.site.register(UserStar)
