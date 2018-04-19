#coding:utf-8
from django import template

from comments.models import Comments
from home.models import Category, Tag, Article

__author__ = 'qiye'
__date__ = '2018/3/3 16:58'


register = template.Library()

@register.simple_tag
def get_all_category():
    '''
    获取所有分类
    :return:
    '''

    return Category.objects.all()


@register.simple_tag
def get_article_count(category):
    '''
    获取指定分类下文章的数量
    :return:
    '''
    article_count = category.article_set.count()
    return article_count


@register.simple_tag
def get_all_tags():
    '''
    获取所有标签
    :return:
    '''
    return Tag.objects.all()


@register.simple_tag
def get_hot_articles():
    '''
    获取最热的文章,按照访问数量获取，仅取前5个
    :return:
    '''
    return Article.objects.all().order_by('-views')[:5]


@register.simple_tag
def get_all_comments(article):
    '''
    获取所有标签
    :return:
    '''
    return article.comments_set.all()

@register.simple_tag
def get_comments_count(article):
    '''
    获取所有标签
    :return:
    '''
    return article.comments_set.count()

@register.simple_tag
def get_recent_comments():
    '''
    获取所有标签
    :return:
    '''
    recent_comments = Comments.objects.all().order_by('-created_time')[:5]

    return recent_comments