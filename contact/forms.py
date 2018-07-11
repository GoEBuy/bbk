#-*- coding:utf-8 -*-

from django import forms

class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, help_text='',
        widget=forms.TextInput(
                    attrs={'placeholder': '用户名','class':"form-control"} ),
            error_messages = {
                'required': '用户名不能为空',
                }
            )
    email = forms.EmailField(required=True,
        widget=forms.TextInput(
                    attrs={'placeholder': '邮箱','class':"form-control"} ),
            error_messages = {
                'required': '邮箱不能为空',
                }
            )


    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'cols':'80','rows':'8'} ),
            error_messages = {
                'required': '内容不能为空',
                'min_length':'字数最少为5个字符',
                'max_length':'字数最多为300个字符',
                }
            )
