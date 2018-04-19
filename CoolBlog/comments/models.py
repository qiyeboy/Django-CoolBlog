from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
from home.models import Article


@python_2_unicode_compatible
class Comments(models.Model):
    # 父评论id
    parent_id = models.PositiveIntegerField(verbose_name="父评论id",default=0)
    #昵称
    nick_name = models.CharField(max_length=20, verbose_name="昵称")
    #email
    email = models.EmailField(max_length=50,verbose_name="邮箱",null=True, blank=True)
    # url
    url = models.URLField(max_length=200, verbose_name="网站",null=True, blank=True)
    #内容
    text = models.TextField(verbose_name="内容")
    #文章
    article = models.ForeignKey(Article,verbose_name="文章")
    #创建时间
    created_time = models.DateTimeField(verbose_name="创建时间",default=datetime.now)

    class Meta:
        verbose_name="评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name

