from django.shortcuts import render
from .models import BlogModel
from django.http import HttpResponse

# Create your views here.
from django.views import View
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
@login_required
def blog_title(request):
    blogs = BlogModel.objects.all()
    return render(request, 'titles.html', {'blogs':blogs})

def blog_content(request,article_id):
    article = BlogModel.objects.get(id=article_id)
    return render(request, 'content.html', {'article':article})
        
