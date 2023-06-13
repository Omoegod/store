from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    extended_title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title   

class ArticleBlock(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    block_title = models.CharField(max_length=200)
    block_body = models.TextField()

    def __str__(self):
        return self.block_title  
    
class Video(models.Model):
    article_block = models.ForeignKey(ArticleBlock, on_delete=models.CASCADE)
    video_url = models.URLField()
     

class Photo(models.Model):
    article_block = models.ForeignKey(ArticleBlock, on_delete=models.CASCADE)
    photo_url = models.URLField()
      

