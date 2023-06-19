from rest_framework import serializers

from blog.models import Article
from blog.models import Photo, ArticleBlock, Video, Tag


# class ArticleSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Article
#         fields = ['title', 'slug', 'extended_title', 'description', 'tags', 'is_published']

# class ArticleBlockSerializer(serializers.HyperlinkedModelSerializer):
#     article_block = ArticleSerializer()
#     class Meta:
#         model = ArticleBlock
#         fields = ['article_block', 'block_title', 'content']        

# class VideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Video
#         fields = '__all__'

# class PhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Photo
#         fields = '__all__'

# class TagsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = '__all__'        



# class ArticleSerializer(serializers.ModelSerializer):
#     article_blocks = serializers.StringRelatedField(many=True)
#     videos = serializers.StringRelatedField(many=True)
#     photos = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Article
#         fields = ['title', 'slug', 'extended_title', 'description', 'tags', 'is_published', 'article_blocks', 'videos', 'photos']

# class ArticleBlockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ArticleBlock
#         fields = ['article_block', 'block_title', 'content']

# class VideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Video
#         fields = ['article_block', 'video_url']

# class PhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Photo
#         fields = ['article_block', 'photo_url']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ArticleBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleBlock 
        fields = '__all__'       

class ArticleDataSerializer(serializers.Serializer):
    article = ArticleSerializer(many=True)
    article_block = ArticleBlockSerializer(many=True)
