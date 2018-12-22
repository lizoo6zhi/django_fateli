from django.contrib import admin
from .models import BlogModel
from account.models import My_Formation,UserProfile

# Register your models here.
admin.site.register(BlogModel)

class UserInfoAdmin(admin.ModelAdmin):
    list_display=('user','school','company','profession')

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user','birday','phone')

admin.site.register(My_Formation, UserInfoAdmin)
admin.site.register(UserProfile, UserProfileAdmin)