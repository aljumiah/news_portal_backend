from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_regex = RegexValidator(
    regex=r'^(9665)(5|0|3|6|4|9|1|8|7)([0-9]{7})$', message="Phone number must be entered in the format: '966 55 5555555'. Up to 14 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=False, unique=False, null=False)  # validators should be a list
    national_id_regex = RegexValidator(
        regex=r'^([0-9]{10})$')
    national_id = models.CharField(
        validators=[national_id_regex], max_length=10, blank=False, unique=False, null=False)  # validators should be a list
    birth_date = models.DateField('Date of Birth',null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class Article(models.Model):
    title = models.CharField(max_length=120,blank=True, null=True)
    content = models.TextField(blank=True, null=True,)
    created_on = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length = 250,blank=True, null=True)
    urlToImage = models.URLField(max_length = 250,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=120,blank=True, null=True)
    publishedAt = models.CharField(max_length=120,blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class FavoriteArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.article.title