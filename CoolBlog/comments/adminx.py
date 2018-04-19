#coding:utf-8
import xadmin

from comments.models import Comments

__author__ = 'qiye'
__date__ = '2018/4/19 12:18'

class CommentsAdmin(object):
    search_fields = ['parent_id','nick_name','email','url','text','article__title']
    list_display = ['parent_id','nick_name','email','url','text','article','created_time']
    list_filter = ['parent_id','nick_name','email','url','text','article','created_time']

xadmin.site.register(Comments,CommentsAdmin)



