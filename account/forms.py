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
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birday','phone')

    def clean(self):
        cd = self.cleaned_data
        return cd

class My_Information_Form(forms.ModelForm):
    class Meta:
        model = My_Formation
        fields = ("school","company", "profession")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)