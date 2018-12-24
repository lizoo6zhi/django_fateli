from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import ArticleColumn
from .forms import ArticleColumnForm

@login_required
@csrf_exempt
def article_column(request):
    if request.method == "GET":
        columns = ArticleColumn.objects.filter(user=request.user)
        if columns:
            print('columns:',columns[0].column)
        column_from = ArticleColumnForm(data=request.GET)
        return render(request, 'article/article_column.html', {'columns':columns, 'column_form':column_from})
    elif request.method == "POST":
        column_name = request.POST['column']
        print('recive column_name:', column_name)
        exists = ArticleColumn.objects.filter(user_id=request.user.id, column=column_name)
        if exists:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user, column=column_name)
            return HttpResponse('1')

@login_required
@csrf_exempt
def edit_article_column(request):
    atticle_colum = ArticleColumn()
    if request.method == "POST":
        column_name = request.POST['column_name']
        column_id = request.POST['column_id']
        exists = ArticleColumn.objects.filter(user_id=request.user.id, column=column_name)
        if exists:
            return HttpResponse('2')
        else:
            line = ArticleColumn.objects.get(id=column_id)
            line.column = column_name
            line.save()
            return HttpResponse('1')

@login_required
@csrf_exempt
def delete_article_column(request):
    atticle_colum = ArticleColumn()
    if request.method == "POST":
        column_id = request.POST['column_id']
        try:
            exists = ArticleColumn.objects.get(id=column_id)
        except:
            return HttpResponse('2')
        else:
            exists.delete()
            return HttpResponse('1')



