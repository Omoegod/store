from django.shortcuts import render
from rest_framework import generics, viewsets
from blog.models import Article
from api.serializers import ArticleSerializer


# Create your views here.

class ArticleList(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer