from django import forms
from django.db import models
from tinymce.widgets import TinyMCE

from blog.models import ArticleBlock, Article

from tinymce.widgets import TinyMCE


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'extended_title', 'description', 'tags', 'is_published', 'article_block', 'video_block', 'image_block']        

class ArticleBlockForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['article_block', 'video_block', 'image_block'] 

class CombinedArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'extended_title', 'description', 'tags', 'is_published', 'article_block', 'video_block', 'image_block']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.update(ArticleForm().fields)
        self.fields.update(ArticleBlockForm().fields)               