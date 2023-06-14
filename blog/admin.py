from django.contrib import admin
from blog.models import Article, ArticleBlock, Video, Photo, Tag
from tinymce.widgets import TinyMCE

from blog.forms import ArticleForm





class ArticleBlockInline(admin.StackedInline):
    model = ArticleBlock
    extra = 1
    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     if isinstance(db_field, models.TextField):
    #         return db_field.formfield(widget=TinyMCE)
    #     return super().formfield_for_dbfield(db_field, **kwargs)


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class ArticleInline(admin.TabularInline):
    model = ArticleBlock
    extra = 1   

class ArticleBlockAdmin(admin.ModelAdmin):
    inlines = [VideoInline, PhotoInline]
    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     if isinstance(db_field, models.TextField):
    #         return db_field.formfield(widget=TinyMCE)
    #     return super().formfield_for_dbfield(db_field, **kwargs)
    


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleBlockInline]
    prepopulated_fields = {"slug": ["title"]}
    view_on_site = True
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'extended_title', 'description', 'tags', 'is_published')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('article_block', 'video_block', 'image_block'),
        }),
    )
    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     if isinstance(db_field, models.TextField):
    #         return db_field.formfield(widget=TinyMCE)
    #     return super().formfield_for_dbfield(db_field, **kwargs)

class ContentAdmin(admin.ModelAdmin):
    form = ArticleForm



admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleBlock, ArticleBlockAdmin)
admin.site.register(Video)
admin.site.register(Photo)
admin.site.register(Tag)
