from django.contrib import admin
from blog.models import Article, ArticleBlock, Video, Photo, Tag
from tinymce.widgets import TinyMCE


class ArticleBlockInline(admin.StackedInline):
    model = ArticleBlock
    extra = 1

class VideoInline(admin.StackedInline):
    model = Video
    extra = 1

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1

class ArticleInline(admin.StackedInline):
    model = ArticleBlock
    extra = 1   

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleBlockInline, VideoInline, PhotoInline]
    prepopulated_fields = {"slug": ["title"]}
    view_on_site = True
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'extended_title', 'description', 'tags', 'is_published')
        }),
    )



admin.site.register(Article, ArticleAdmin)
# admin.site.register(ArticleBlock)
# admin.site.register(Video)
# admin.site.register(Photo)
admin.site.register(Tag)
