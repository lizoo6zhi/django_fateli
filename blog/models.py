from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
""" 
    编写博客数据模型,包括文章标题、作者、发布时间、内容

    ForeignKey的to_delete参数说明：
    CASCADE:这就是默认的选项，级联删除，你无需显性指定它。
    PROTECT: 保护模式，如果采用该选项，删除的时候，会抛出ProtectedError错误。
    SET_NULL: 置空模式，删除的时候，外键字段被设置为空，前提就是blank=True, null=True,定义该字段的时候，允许为空。
    SET_DEFAULT: 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。
    SET(): 自定义一个值，该值当然只能是对应的实体了

"""
class BlogModel(models.Model):
    blog_title = models.CharField(max_length = 300)
    blog_content = models.TextField()
    blog_author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='blog_posts')
    blog_publish_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-blog_publish_time",)

