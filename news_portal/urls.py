"""news_portal_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import (ProfileListView,ArticleListView,UserRegisterAPIView,ArticleFavoriteCreateView,ArticleDetail,MyFavoritesListView,MyFavoritesDeleteView)
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/login/', obtain_jwt_token, name='login'),
    path('api/register/', UserRegisterAPIView.as_view(), name='register'),
    
    path('api/articles/', ArticleListView.as_view(), name='article-list'),
    path('api/profile/', ProfileListView.as_view(), name='user-profile'),
    path('api/articles/<int:article_id>', ArticleDetail.as_view(), name='article-detail'),
    path('api/my-favorite/<int:article_id>/delete', MyFavoritesDeleteView.as_view(), name='my-favorite-delete'),
    path('api/favorites/', ArticleFavoriteCreateView.as_view(), name='create-favorite'), 
    path('api/my-favorite/', MyFavoritesListView.as_view(), name='my-favorite'), 
]
