from django.contrib import admin
from .models import Article,User,FavoriteArticle

admin.site.register(Article)
admin.site.register(User)
admin.site.register(FavoriteArticle)