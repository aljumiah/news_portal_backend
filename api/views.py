from django.shortcuts import render
from api.models import Article,FavoriteArticle,User
from rest_framework.generics import (ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView,CreateAPIView,)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import (ArticleListFavoriteSerializer,UserSerializer,ArticleListSerializer,ArticleFavoriteSerializer,UserRegisterSerializer,ArticleDetailSerializer)
from urllib import request
import ssl
from .permissions import IsOwner
from newsapi import NewsApiClient
# Init
newsapi = NewsApiClient(api_key='0b1319f118aa4afeb13db8a33c06292f')
top_headlines = newsapi.get_sources()
news = newsapi.get_everything(q='bitcoin',sources='bbc-news,the-verge',domains='bbc.co.uk,techcrunch.com')


class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    
class ArticleListView(ListAPIView):
    for article in news['articles']:
        Article.objects.create(title=article['title'],content=article['content'],url=article['url'], urlToImage=article['urlToImage'], description=article['description'], author=article['author'], publishedAt=article['publishedAt']) 
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [AllowAny,]
    
class ArticleDetail(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'article_id' 
    permission_classes = [AllowAny, ] 
    
class MyFavoritesDeleteView(DestroyAPIView):
    queryset = FavoriteArticle.objects.all()
    serializer_class = ArticleFavoriteSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'article_id'
    permission_classes = [IsAuthenticated, IsOwner]
    
class ArticleFavoriteCreateView(CreateAPIView):
    serializer_class = ArticleFavoriteSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class MyFavoritesListView(ListAPIView):
    # queryset = ArticleFavoriteSerializer.objects.all()
    serializer_class = ArticleListFavoriteSerializer
    permission_classes = [IsAuthenticated, IsOwner]   
    
    def get_queryset(self):
        return FavoriteArticle.objects.filter(user=self.request.user.id) 
    
class ProfileListView(ListAPIView):
    # queryset = ArticleFavoriteSerializer.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]    
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id) 
        