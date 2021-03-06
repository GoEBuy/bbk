#-*- coding:utf-8 -*-

import re
from django import forms
from django.core.exceptions import ValidationError
from .models import UserInfo, NewUser
from django.forms import widgets

########### users forms ######################

def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


def user_unique_validate(username):
    user_obj = NewUser.objects.filter(username=username).first()
    if user_obj:
        raise ValidationError('用户名已经存在')


def username_rule_validate(value):
    """ 自定义表单格式验证 """
    # 先设定一个正则，非 [a-z][0-9]
    username_re = re.compile(r'\W|[A-Z]')
    # 判断如果查找所有的数据后有正则中的指定的字符串
    if username_re.findall(value):
        # 说明匹配，但是匹配就是非[a-z][0-9]  而我们想要的是[a-z][0-9]
        raise ValidationError('用户名格式错误 只能在[a-z][0-9]中选择')
    # 不匹配，说明 value 全在 [a-z][0-9] 这个范围里


def email_unique_validate(email):
    user_obj = NewUser.objects.filter(email=email).first()
    if user_obj:
        raise ValidationError('Email已经存在，请换一个')


class SettingsForm(forms.Form):
    location = forms.CharField(required=False, max_length=50, error_messages={'max_length':'最多50位'} )

    pass

#     password = forms.CharField(min_length=6, max_length=50, required=True,
#                                error_messages={'required': '密码不能为空',
#                                                'min_length': '密码不能少于6位',
#                                                'max_length': '密码最多50位'})
#     email = forms.EmailField(validators=[email_unique_validate, ], required=True,
#                              error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'})
#     mobile = forms.CharField(validators=[mobile_validate, ], required=True,
#                              error_messages={'required': '手机号不能为空'})


# class SigninForm(forms.Form):
#     username = forms.CharField(required=True, max_length=50,
#                                error_messages={'required': '用户名不能为空'}, )
#     password = forms.CharField(min_length=6, max_length=50, required=True,
#                                error_messages={'required': '密码不能为空',
#                                                'invalid': '密码格式错误',
#                                                'min_length': '密码不能少于6位'})


#validators = [
 # 下面的正则内容一目了然，我就不注释了
 #        RegexValidator(r'((?=.*\d))^.{6,12}$', '必须包含数字'),
 #      RegexValidator(r'((?=.*[a-zA-Z]))^.{6,12}$', '必须包含字母'),
 #   RegexValidator(r'((?=.*[^a-zA-Z0-9]))^.{6,12}$', '必须包含特殊字符'),
 #    RegexValidator(r'^.(\S){6,10}$', '密码不能包含空白字符'),
 # ,  # 用于对密码的正则验证

class RegisterForm(forms.Form):
    username = forms.CharField(
                label='username',
                validators=[user_unique_validate, username_rule_validate, ],
                max_length=100,
                widget=forms.TextInput(
                    attrs={'id':'username', 'onblur': 'authentication()','placeholder': '用户名为8-12个字符','class':"form-control"} ),
            error_messages = {
                'required': '用户名不能为空',  'min_length': '用户名最少为6个字符',  'max_length': '用户名最多不超过为20个字符',
                }
            )
    email = forms.EmailField( required=True, widget = forms.TextInput(attrs={'class': "form-control", 'placeholder': '请输入邮箱'} ),
            error_messages = {'required': '邮箱不能为空', 'invalid':'请输入正确的邮箱格式'} )
    password1 = forms.CharField(
                required=True,
                widget=forms.PasswordInput(attrs={'class':"form-control"}),
                error_messages = {'required': '密码不能为空!', 'min_length': '密码最少为6个字符','max_length': '密码最多不超过为12个字符!', 'invalid': '密码格式错误' } )
    password2 = forms.CharField( required=True, widget=forms.PasswordInput(attrs={'class':"form-control"} ),
            error_messages={'required':'请确认密码', }

            )

    def clean(self):
        """自定义form验证 """
        try:
            import pdb
            pdb.set_trace()
            password1= self.cleaned_data['password1']
            password2= self.cleaned_data['password2']
            if password1<> password2:
                raise forms.ValidationError("输入密码不一致")
            return self.cleaned_data
            pass
        except Exception as e:
            print "except:"+ str(e)
            raise forms.ValidationError("form validate error:" +str(e) )
        return self.cleaned_data
# 获取表单提示信息
    def getFormTips(form):
        errors = form._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        err = errors.pop()
        if err:
            print type(err)
            if isinstance(err, str):
                print 'str'
            else:
                err = err.message
        print err
        return err
        # 设置表单提示信息
    def setFormTips(form, content):
        if content and len(content)>0:
            errors = form._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
            errors.append(content)




class LoginForm(forms.Form):
	username = forms.CharField(label='username',
            validators=[ username_rule_validate, ],
            max_length=100,
            widget=forms.TextInput(attrs={'id':'username', 'onblur': 'authentication()','placeholder': '用户名为8-12个字符', 'class':'form-control' }) ,
            error_messages = {'required': '用户名不能为空',  'min_length': '用户名最少为6个字符',  'max_length': '用户名最不超过为20个字符'}
            )
	 #, error_messages = {'required': '邮箱不能为空', 'invalid':'请输入正确的邮箱格式'} )
	password1 = forms.CharField(
            widget=forms.PasswordInput(attrs={'class':'form-control'}),
            error_messages = {'required': '密码不能为空!', 'min_length': '密码最少为6个字符','max_length': '密码最多不超过为12个字符!',}
            )


class SetInfoForm(forms.Form):
	username = forms.CharField()

class CommmentForm(forms.Form):
	comment = forms.CharField(label='', widget=forms.Textarea(attrs={'cols': '60', 'rows': '6'}))

class SearchForm(forms.Form):
	keyword = forms.CharField(widget=forms.TextInput)


def clean_username(self):
# 对username的扩展验证，查找用户是否已经存在
	username = self.cleaned_data.get('username')
	users = NewUser.objects.filter(username=username).count()
	if users:
	  raise ValidationError('用户已经存在！')
	return username


class AvatarSettingsForm(forms.Form):
    avatar = forms.ImageField(error_messages={'requried':'文件不能爲空', 'invalid':'無效的頭文件'} )


class PhoneSettingsForm(forms.Form):
    new_phone_number = forms.CharField(validators=[mobile_validate, ], required=True,
                                       error_messages={'required': '手机号不能为空'})
    password = forms.CharField(required=True, error_messages={'required': '密码不能为空'})


class EmailSettingsForm(forms.Form):
    new_email = forms.EmailField(validators=[email_unique_validate, ], required=True,
                                 error_messages={'required': '邮箱不能为空',
                                                 'invalid': '无效的邮箱地址'})
    password = forms.CharField(required=True, error_messages={'required': '密码不能为空'})


class PasswordSettingsForm(forms.Form):
    password_new = forms.CharField(min_length=6, max_length=50, required=True,
                                   error_messages={'required': '新密码不能为空',
                                                   'invalid': '新密码格式错误',
                                                   'min_length': '新密码不能少于6位'})
    password_again = forms.CharField(min_length=6, max_length=50, required=True,
                                     error_messages={'required': '第二次密码不能为空',
                                                     'invalid': '第二次密码格式错误',
                                                     'min_length': '第二次密码不能少于6位'})
    password_current = forms.CharField(min_length=6, max_length=50, required=True,
                                       error_messages={'required': '当前密码不能为空',
                                                       'invalid': '当前密码格式错误',
                                                       'min_length': '当前密码不能少于6位'})


# def clean_email(self):
#     # 对email的扩展验证，查找用户是否已经存在
#     email = self.cleaned_data.get('email')
#     email_count = NewUser.objects.filter(email=email).count() #从数据库中查找是否用户已经存在
#     if email_count:
#     raise ValidationError('该邮箱已经注册！')
# return email
