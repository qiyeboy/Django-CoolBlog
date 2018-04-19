#coding:utf-8

# Create your views here.
from haystack.forms import SearchForm
from pure_pagination import Paginator, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from comments.forms import CommentsForm
from home.models import Article, Category, Tag


def index(request):
    articles = Article.objects.all().order_by('-created_time')
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(articles, 2, request=request)
    articles = p.page(page)

    return render(request,'home/index.html',context={ 'articles':articles})

def detail(request, id):
    # try:
    #     article = Article.objects.get(pk=id)
    # except Article.DoesNotExist:
    #     raise Http404

    article = get_object_or_404(Article, pk=id)
    article.views += 1
    article.save()
    commentsForm = CommentsForm()
    return render(request, 'home/article.html', context={'article': article,'commentsForm':commentsForm})


class CategoryListView(View):

    def get(self,request,id):
        '''
        通过分类获取文章列表
        :param request:
        :param id:
        :return:
        '''
        category = Category.objects.get(id=int(id))
        articles = category.article_set.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(articles, 2, request=request)
        articles = p.page(page)
        return render(request, 'home/article_list.html', context={'articles': articles,'obj':category})


class TagListView(View):

    def get(self,request,id):
        '''
        通过标签获取文章列表
        :param request:
        :param id:
        :return:
        '''
        tag = Tag.objects.get(id=int(id))
        articles = tag.tags_article.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(articles, 2, request=request)
        articles = p.page(page)
        return render(request, 'home/article_list.html', context={'articles': articles,'obj':tag})

def full_search(request):
    """全局搜索"""
    keywords = request.GET['q']
    form = SearchForm(request.GET)
    articles = form.search()

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(articles, 1, request=request)
    articles = p.page(page)
    return render(request, 'home/article_search_list.html',
                  context={'articles': articles, 'keywords': '关键字 \'{}\' 搜索结果'.format(keywords)})
