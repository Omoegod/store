from django.urls import re_path, include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()

router.register('article', views.ArticleList, basename='article')

urlpatterns = [
    re_path(r'^article$', views.ArticleList.as_view({'get': 'list'}), name='article-list'),
    re_path(r'^rest/', include(router.urls))
]