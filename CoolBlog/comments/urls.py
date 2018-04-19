#coding:utf-8
from django.conf.urls import url

from comments.views import CommentView

__author__ = 'qiye'
__date__ = '2018/3/12 18:15'

app_name = 'comments'
urlpatterns = [
    url(r'^post/(?P<article_id>\d+)/$', CommentView.as_view(),name='comment_post'),



]