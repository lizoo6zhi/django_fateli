from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone,text
from django.urls.base import reverse

# Create your models here.
class ArticleColumn(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='article_column')
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

class ArticlePost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='article_post')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn, on_delete=models.CASCADE, related_name='article_column_column')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("title",)
        index_together = (("id","slug"),)

    def save(self, *args, **wargs):
        self.slug = text.slugify(self.title)
        super().save(*args, **wargs)

    def get_absolute_url(self):
        return reverse('article:article_content', args=[self.id, self.slug])