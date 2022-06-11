from rest_framework import serializers
from .models import Comment, Ratings


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ratings
        fields = '__all__'