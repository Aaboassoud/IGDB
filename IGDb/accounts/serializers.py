from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password','first_name', 'last_name']

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name']

class UserInfoSerializerView(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name']