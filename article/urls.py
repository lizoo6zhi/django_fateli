from django.conf.urls import url
from .views import article_column
urlpatterns = [
    url(r'^article-column/',article_column, name='article-column'),
]
