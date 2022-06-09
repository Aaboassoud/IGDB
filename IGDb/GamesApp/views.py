from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Games
#from models import ReviewModel
from .serializers import GamesSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_game(request: Request):
    ''' description
        This function to add a new game to the database and must be authenticated and have permission to add the game.
    '''
    user:User = request.user

    if not user.is_authenticated or not request.user.has_perm('gamesapp.add_games'):
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
    #rating = ReviewModel.objects.filter(user=request.user)
    games = Games.objects.all()
    dataResponse = {
        "msg" : "List of All games",
        "games" : GamesSerializer(instance=games, many=True).data
    }

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
    if not user.is_authenticated or not request.user.has_perm('gamesapp.change_games'):
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    game = Games.objects.get(id=game_id)    
    if user.id != game.user:
        print("doesnt match user")
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
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
    if not user.is_authenticated or not request.user.has_perm('gamesapp.delete_games') or user.id != game.user:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    game.delete()
    return Response({"msg" : "Deleted Successfully"})
