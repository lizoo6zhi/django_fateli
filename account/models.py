from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE)  #第二个参数表述级联删除
    birday = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=20,null=True)

#用户信息模型
class My_Formation(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE)  #第二个参数表述级联删除
    school = models.CharField(max_length=100,blank=True)
    company = models.CharField(max_length=100,blank=True)
    profession = models.CharField(max_length=100,blank=True)

