#coding:utf-8

# Create your views here.
from django.shortcuts import render
from home.models import Article
def index(request):
    articles = Article.objects.all().order_by('-created_time')
    return render(request,'home/index.html',context={ 'articles':articles})