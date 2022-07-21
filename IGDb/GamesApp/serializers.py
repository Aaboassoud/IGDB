from .models import Games, Wishlist
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializerView(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username',]

class GamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Games
        fields = '__all__'

class GamesSerializerView(serializers.ModelSerializer):

    
    class Meta:
        model = Games
        fields = ['id','game_title', 'rating', 'company', 'date_realeased', 'description', 'user', 'image']
        depth = 1
    user = UserSerializerView()

class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wishlist
        fields = '__all__'

class WishListSerializerView(serializers.ModelSerializer):
    game = GamesSerializerView()
    class Meta:
        model = Wishlist
        fields = ['game','id']