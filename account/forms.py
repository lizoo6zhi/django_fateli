from django import forms
from django.contrib.auth.models import User  #默认用户模型User
from django.core.exceptions import ValidationError
from .models import UserProfile,My_Formation
import re

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="PassWord",widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    class Meta:
        model = User #决定表单的内容会写到哪个数据库表中的哪些记录中
        fields = ("username","email")

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd["password"] != cd["confirm_password"]:
            raise forms.ValidationError("passwords do not match")
        return cd["confirm_password"]


class BaseForm(forms.ModelForm):
    def error_detail(self):
        error_response = {}
        error_response['status'] = 2
        error_response['msg'] = 'form validate error'
        error_response['data'] = self.errors
        print('errors:', self.errors)
        print('errors.as_data:', self.errors.as_data)
        return error_response

# 电话号码验证器
from django.core.exceptions import ValidationError
import re
def mobile_validate(value):
        mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
        if not mobile_re.match(value):
            raise ValidationError('phone format error')

from django.forms.widgets import DateInput
class UserProfileForm(BaseForm):
    birday = forms.DateField(widget=DateInput(attrs={'placeholder': u'格式：1970-1-1'}))
    phone = forms.CharField(label="phone", validators=[mobile_validate,], widget=forms.TextInput)

    class Meta:
        model = UserProfile
        fields = ('birday','phone')

    def clean(self):
        if not self.errors:
            pass
        return self.cleaned_data

class My_Information_Form(forms.ModelForm):
    class Meta:
        model = My_Formation
        fields = ("school","company", "profession")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)