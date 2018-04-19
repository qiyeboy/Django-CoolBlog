from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from comments.forms import CommentsForm
from comments.models import Comments
from home.models import Article

class CommentView(View):
    '''
    提交评论
    '''
    def post(self,request,article_id):
        comment_form = CommentsForm(request.POST)
        article = get_object_or_404(Article, pk=article_id)

        if comment_form.is_valid() and article:

            parent_id = request.POST.get("parent_id", "")
            nick_name = request.POST.get("nick_name", "")
            email = request.POST.get("email", "")
            url = request.POST.get("url", "")
            text = request.POST.get("text", "")
            comment = Comments()
            comment.nick_name =nick_name
            comment.parent_id = parent_id
            comment.email = email
            comment.url = url
            comment.text = text
            comment.article = article
            comment.save()
        return redirect(article.get_absolute_url()+"#comment")


