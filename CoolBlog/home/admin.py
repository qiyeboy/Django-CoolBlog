from django.contrib import admin

# Register your models here.
from home.models import Category, Tag, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category','getTagsName','author']

    def getTagsName(self,obj):
        #obj即为Article类的实例
        tag_name=''
        for tag in obj.tags.all():#查询
            tag_name+=tag.name+' '
        return tag_name
    getTagsName.short_description  = "标签"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Article,ArticleAdmin)


