from django.conf.urls import url
from .views import blog_title,blog_content

urlpatterns = [
    url(r'^$',blog_title, name='blog_titles'),
    url(r'(?P<article_id>\d)', blog_content, name='blog_article'),
]