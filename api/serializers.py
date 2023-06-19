from rest_framework import serializers

from blog.models import Article
from blog.models import Photo, ArticleBlock, Video, Tag

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class ArticleBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleBlock
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    articles = ArticleBlockSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'extended_title', 'description', 'tags', 'is_published','photos', 'videos', 'articles')