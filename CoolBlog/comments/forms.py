#coding:utf-8
from captcha.fields import CaptchaField
from django import forms

__author__ = 'qiye'
__date__ = '2018/3/12 17:41'

class CommentsForm(forms.Form):
    nick_name = forms.CharField(required=True,max_length=20)
    email = forms.EmailField(required=False,max_length=50)
    url = forms.URLField(required=False,max_length=200)
    text = forms.CharField(required=True,widget=forms.Textarea)
    captcha = CaptchaField()
