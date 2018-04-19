#coding:utf-8
import xadmin
from xadmin import views

from home.models import Category, Tag, Article

__author__ = 'qiye'
__date__ = '2018/4/19 12:18'

class BaseSetting(object):
    enable_themes = True #开启主题
    use_bootswatch = True#调出主题菜单,显示更多主题

class GlobalSetting(object):
    site_title="七夜后台管理系统"
    site_footer = "七夜安全"
    menu_style = "accordion"

class CategoryAdmin(object):
    search_fields = ['name']
    list_display = ['name']
    list_filter = ['name']

class TagAdmin(object):
    search_fields = ['name']
    list_display = ['name']
    list_filter = ['name']

class ArticleAdmin(object):
    search_fields = ['title','body','excerpt','category__name','tags__name','author__first_name','views']
    list_display = ['title','body','created_time','modified_time','excerpt','category','tags','author','views']
    list_filter = ['title','body','created_time','modified_time','excerpt','category','tags','author','views']

xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Article,ArticleAdmin)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)