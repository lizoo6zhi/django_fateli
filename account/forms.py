from django import forms
from django.contrib.auth.models import User  #默认用户模型User
from django.core.exceptions import ValidationError
from .models import UserProfile
import re

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="PassWord",widget=forms.PasswordInput)
    password2 = forms.CharField(label="ConfirmPassword",widget=forms.PasswordInput)

    class Meta:
        model = User #决定表单的内容会写到哪个数据库表中的哪些记录中
        fields = ("username","email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] != cd["password2"]:
            raise forms.ValidationError("passwords do not match")
        return cd["password2"]
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birday','phone')