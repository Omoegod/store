from django.contrib import admin
from blog.models import Article, ArticleBlock, Video, Photo, Tag
from django.urls import reverse


class ArticleBlockInline(admin.StackedInline):
    model = ArticleBlock
    extra = 1

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class ArticleBlockAdmin(admin.ModelAdmin):
    inlines = [VideoInline, PhotoInline]

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleBlockInline]
    prepopulated_fields = {"slug": ["title"]}
    view_on_site = True

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleBlock, ArticleBlockAdmin)
admin.site.register(Video)
admin.site.register(Photo)
admin.site.register(Tag)
