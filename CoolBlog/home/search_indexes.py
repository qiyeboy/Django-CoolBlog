#coding:utf-8
from home.models import Article

__author__ = 'qiye'
__date__ = '2018/4/18 17:22'


from haystack import indexes

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    # 对title字段进行索引
    title = indexes.CharField(model_attr='title')
    # 文章内容
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all().order_by('-created_time')