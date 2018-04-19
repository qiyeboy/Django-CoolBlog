from django.contrib import admin

# Register your models here.
from comments.models import Comments


class CommentsAdmin(admin.ModelAdmin):
    search_fields = ['parent_id','nick_name','email','url','text','article']
    list_display = ['parent_id','nick_name','email','url','text','article','created_time']
    list_filter = ['parent_id','nick_name','email','url','text','article','created_time']



admin.site.register(Comments,CommentsAdmin)