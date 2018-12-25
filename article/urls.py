from django.conf.urls import url
from .views import article_column,edit_article_column,delete_article_column,article_post,article_title,article_content
urlpatterns = [
    url(r'^article-column/',article_column, name='article_column'),
    url(r'^edit-article-column',edit_article_column, name='edit_article-column'),
    url(r'^delete-article-column',delete_article_column, name='delete_article_column'),
    url(r'^article-post/$', article_post, name='article_post'),
    url(r'^article-title/', article_title,name='article_title'),
    url(r'^article-content/(?P<id>\d+)/(?P<slug>[-\w]+)/$', article_content, name='article_content'),
]
