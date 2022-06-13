from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Games, Wishlist
from .serializers import GamesSerializer, GamesSerializerView, WishListSerializer, WishListSerializerView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core import serializers

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_game(request: Request):
    ''' description
        This function to add a new game to the database and must be authenticated and have permission to add the game.
    '''
    user:User = request.user

    if not user.is_authenticated or not request.user.has_perm('GamesApp.add_games'):
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data.update(user=request.user.id)
    new_game = GamesSerializer(data=request.data)
    if new_game.is_valid():
        new_game.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "game" : new_game.data
        }
        return Response(dataResponse)
    else:
        print(new_game.errors)
        dataResponse = {"msg" : "couldn't create a Game!"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_games(request : Request):
    if 'search' in request.query_params:
        search_phrase = request.query_params['search']
        games = Games.objects.filter(game_title__contains=search_phrase)
    else:
        games = Games.objects.all()
    
    dataResponse = {
        "msg" : "List of All games",
        "games" : GamesSerializerView(instance=games, many=True).data
    }

    return Response(dataResponse)



@api_view(['GET'])
def all_gamers(request : Request):

    gamers = User.objects.filter(groups__name = "Developer")
    gamers_json = serializers.serialize('json', gamers)
    print(gamers.username,"WOW!!!")
    dataResponse = {
        "msg" : "List of All games",
        "games" : ""
    }, gamers_json

    return Response(dataResponse)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def edit_game(request : Request, game_id):
    '''
        description
        This function to update a game and must be authenticated and have permission to update the game.
    '''
    user:User = request.user
    if not user.is_authenticated or not request.user.has_perm('GamesApp.change_games'):
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    game = Games.objects.get(id=game_id)

    if user != game.user:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data.update(user=request.user.id)
    updated_game = GamesSerializer(instance=game, data=request.data)
    if updated_game.is_valid():
        updated_game.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_game.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_game(request: Request, game_id):
    '''
        description
        This function to delete a game and must be authenticated and have permission to delete the game.
    '''
    user:User = request.user
    game = Games.objects.get(id=game_id) 
    if not user.is_authenticated or not request.user.has_perm('GamesApp.delete_games') or user != game.user:
        return Response({"msg" : "Not Allowed, You must have permission to delete"}, status=status.HTTP_401_UNAUTHORIZED)

    game.delete()
    return Response({"msg" : "Deleted Successfully"})

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_to_wishlist(request: Request, game_id):
    ''' description
    to add a game to wishlist
    '''
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    game1 = Games.objects.get(id=game_id)
    request.data.update(user=request.user.id, game=game1.id)
    wishlist = WishListSerializer(data=request.data)
    if wishlist.is_valid():
        wishlist.save()
        dataResponse = {
        "msg" : "Created Successfully",
        "game" : wishlist.data
        }
        return Response(dataResponse)
    else:
        print(wishlist.errors)
        dataResponse = {"msg" : "couldn't add wishlist"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def wishlist(request: Request):
    user:User = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    games = Wishlist.objects.filter(user=user.id)
    dataResponse = {
        "msg" : "List of Wislist games",
        "games" : WishListSerializerView(instance=games, many=True).data
    }

    return Response(dataResponse)