from django.db import models
from tinymce.models import HTMLField 


class Tag(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    extended_title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    is_published = models.BooleanField(default=False)
    article_block = models.OneToOneField('ArticleBlock', on_delete=models.CASCADE, blank=True, null=True, related_name='articles')
    video_block = models.ManyToManyField('Video', blank=True, null=True)
    image_block = models.ManyToManyField('Photo', blank=True, null=True)

    def __str__(self):
        return self.title   

class ArticleBlock(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    block_title = models.CharField(max_length=200)
    block_body = models.TextField()
    content =  HTMLField()
    def __str__(self):
        return self.block_title  
    

class Video(models.Model):
    article_block = models.ForeignKey(ArticleBlock, on_delete=models.CASCADE)
    video_url = models.URLField()
     

class Photo(models.Model):
    article_block = models.ForeignKey(ArticleBlock, on_delete=models.CASCADE)
    photo_url = models.URLField()
      

