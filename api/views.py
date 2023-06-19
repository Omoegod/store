from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, generics, mixins
from blog.models import Article, ArticleBlock, Video, Photo
from api.serializers import ArticleSerializer, ArticleBlockSerializer, ArticleDataSerializer
from drf_multiple_model.views import ObjectMultipleModelAPIView
from collections import namedtuple
from django.http import JsonResponse

# Create your views here.

# class ArticleObject(ObjectMultipleModelAPIView):
#     querylist = [ {'queryset': Article.objects.all(), 'serializer_class': ArticleSerializer},
#                  {'queryset': ArticleBlock.objects.all(), 'serializer_class': ArticleBlockSerializer}]

ArticleData = namedtuple('ArticleData', ('article', 'article_block'))

class ArticleObject(viewsets.ViewSet):
    

    def list(self, request):
        articledata = ArticleData(article=Article.objects.all(),
                                  article_block=ArticleBlock.objects.all())
        serializer = ArticleDataSerializer(articledata)

        return JsonResponse(serializer.data)

    
# class ArticleObject(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer 

# class ArticleBlockObject(viewsets.ModelViewSet):
#     queryset = ArticleBlock.objects.all()
#     serializer_class = ArticleBlockSerializer     
    
# class ArticleDetail(generics.RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

class ArticleBlockDetail(generics.RetrieveAPIView):
    queryset = ArticleBlock.objects.all().values()
    serializer_class = ArticleBlockSerializer

# class VideoDetail(generics.RetrieveAPIView):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer

# class PhotoDetail(generics.RetrieveAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer    

    
