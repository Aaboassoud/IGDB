from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken

from .serializers import UserRegisterSerializer, UserInfoSerializer, UserInfoSerializerView
# Create your views here.

@api_view(['POST'])
def register_user(request : Request):
    
    user_serializer  = UserRegisterSerializer(data=request.data)
    if user_serializer.is_valid():
        new_user = User.objects.create_user(**user_serializer.data)
        new_user.save()
        return Response({"msg" : "created user successfuly"})
    else:
        print(user_serializer.errors)
        return Response({"msg" : "Couldn't create user"}, status= status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request : Request):

    if 'username' in request.data and 'password' in request.data:
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user is not None:
            #create the token , then give the token to the user in the response
            token = AccessToken.for_user(user)
            responseData = {
                "msg" : "Your token is ready",
                "token" : str(token)
            }
            return Response(responseData)


    return Response({"msg" : "please provide your username & password"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def edit_personal_info(request: Request):
    '''Edit the personal information'''

    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    user_info = User.objects.get(id=request.user.id)
    request.data.update(user=request.user.id)
    updated_info = UserInfoSerializer(instance=user_info, data=request.data)
    if updated_info.is_valid():
        updated_info.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_info.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def personal_info(request: Request):
    '''show personal information'''

    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    user_info = User.objects.get(id=request.user.id)
    
    responseData = {
        "msg" : "My Personal Information",
        "games" : UserInfoSerializerView(instance=user_info).data
    }

    return Response(responseData)