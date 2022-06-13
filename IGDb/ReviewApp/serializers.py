from rest_framework import serializers
from GamesApp.models import Games
from .models import Comment, Ratings
from GamesApp.serializers import UserSerializerView


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class GamesSerializerView(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['game_title',]

class CommentSerializerView(serializers.ModelSerializer):
    user = UserSerializerView()
    game = GamesSerializerView()
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1
    


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ratings
        fields = '__all__'

class RatingSerializerView(serializers.ModelSerializer):
    game = GamesSerializerView()
    user = UserSerializerView()
    class Meta:
        model = Ratings
        fields = '__all__'