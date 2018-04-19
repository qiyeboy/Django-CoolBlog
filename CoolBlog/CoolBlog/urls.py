"""CoolBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from CoolBlog.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('home.urls')),
    url(r'^comment/',include('comments.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
    url(r'^search/', include('haystack.urls')),#搜索功能的添加
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # 配置上传文件的访问处理
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT})
]

