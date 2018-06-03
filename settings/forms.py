#encoding:utf-8

import re
from django import forms
from django.core.exceptions import ValidationsError

class AvatarSettingsForm(forms.Form):
    avatar = forms.ImageField(error_messages={'requried':'文件不能爲空', 'invalid':'無效的頭文件'} )








