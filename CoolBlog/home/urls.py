#coding:utf-8
from django.conf.urls import url
from home import views
from home.views import CategoryListView, TagListView

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^article/(?P<id>\d+)/$',views.detail, name='detail'),

    url(r'^tag/(?P<id>\d+)/$',TagListView.as_view(), name='tag'),

    url(r'^category/(?P<id>\d+)/$',CategoryListView.as_view(), name='category'),

    url(r'^article/search/$',views.full_search, name='full_search')


]

