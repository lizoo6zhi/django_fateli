from django.contrib import admin
from .models import BlogModel
from account.models import My_Formation,UserProfile
from article.models import ArticleColumn
# Register your models here.
admin.site.register(BlogModel)

class UserInfoAdmin(admin.ModelAdmin):
    list_display=('user','school','company','profession')

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user','birday','phone')

class ArticleColumnAdmin(admin.ModelAdmin):
    list_display=('column','created','user')
    list_filter=('column',)

admin.site.register(My_Formation, UserInfoAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ArticleColumn, ArticleColumnAdmin)