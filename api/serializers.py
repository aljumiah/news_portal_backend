from rest_framework import serializers
from api.models import Article,FavoriteArticle,User
# from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
        
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','phone_number','national_id','birth_date','token','password']
        
    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        phone_number = validated_data['phone_number']
        national_id = validated_data['national_id']
        birth_date = validated_data['birth_date']
        password = validated_data['password']
        email = validated_data['email']
        
        new_user = User(email=email,username=username,first_name=first_name,last_name=last_name,phone_number=phone_number,national_id=national_id,birth_date=birth_date,password=password)
        new_user.set_password(password)
        new_user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)

        validated_data["token"] = token
        return validated_data
    
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','phone_number','national_id','birth_date']
        
class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
           
class ArticleFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteArticle
        fields = '__all__'

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        
class ArticleListFavoriteSerializer(serializers.ModelSerializer):
    article = ArticleDetailSerializer()
    class Meta:
        model = FavoriteArticle
        fields = '__all__'

        

        

        