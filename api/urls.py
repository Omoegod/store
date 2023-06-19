from django.urls import re_path, include, path
from rest_framework import routers

from api.views import ArticleObject, ArticleBlockDetail

# router = routers.DefaultRouter()

# router.register('article', ArticleObject, basename='article')

# urlpatterns = [
#     re_path(r'^article$', ArticleObject.as_view(), name='article')
# ]
urlpatterns = [
    #path('articles/', ArticleBlockObject.as_view({'get': 'list'})),
    path('article/', ArticleObject.as_view({'get': 'list'})),
    # path('articles/<int:pk>/', ArticleDetail.as_view()),
    # path('article-blocks/<int:pk>/', ArticleBlockDetail.as_view()),
    # path('videos/<int:pk>/', VideoDetail.as_view()),
    # path('photos/<int:pk>/', PhotoDetail.as_view()),
]