from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Comment, Rating
from models import Games
from .serializers import CommentSerializer, RatingSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_comment(request: Request, game_id):
    ''' description
        This function to add a new Comment to the database and must be authenticated.
    '''
    user:User = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    game = Games.objects.get(id=game_id)
    request.data.update(user=request.user.id, game=game)
    
    new_comment = CommentSerializer(data=request.data)
    if new_comment.is_valid():
        new_comment.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "Comment" : new_comment.data
        }
        return Response(dataResponse)
    else:
        print(new_comment.errors)
        dataResponse = {"msg" : "couldn't create a Comment"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def reviews(request : Request, game_id):

    comments = Comment.objects.filter(game=game_id)
    dataResponse = {
        "msg" : "List of All Comments",
        "Comments" : CommentSerializer(instance=comments, many=True).data
    }

    return Response(dataResponse)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_comment(request: Request, comment_id):
    '''
        description
        This function to delete a comment and must be authenticated.
    '''
    user:User = request.user
    comment = Comment.objects.get(id=comment_id) 
    if not user.is_authenticated or user.id != comment.user:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    comment.delete()
    return Response({"msg" : "Deleted Successfully"})

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_rating(request: Request, game_id):
    ''' description
        This function to add a new rating to the database and must be authenticated and have permission to add rating.
    '''
    user:User = request.user

    if not user.is_authenticated or not request.user.has_perm('reviewapp.add_rating'):
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    game = Games.objects.get(id=game_id)
    request.data.update(user=request.user.id)

    new_rate = RatingSerializer(data=request.data, game=game)
    if new_rate.is_valid():
        new_rate.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "Ratings" : new_rate.data
        }
        return Response(dataResponse)
    else:
        print(new_rate.errors)
        dataResponse = {"msg" : "couldn't create a Rating"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def rating_comment(request : Request,game_id):

    ratings_comments = Rating.objects.filter(game=game_id)
    dataResponse = {
        "msg" : "List of All Ratings Comments",
        "Ratings Comments" : CommentSerializer(instance=ratings_comments, many=True).data
    }
    return Response(dataResponse)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_rating(request: Request, rating_id):
    '''
        description
        This function to delete a rating and must be authenticated.
    '''
    user:User = request.user
    rating = Rating.objects.get(id=rating_id) 
    if not user.is_authenticated or user.id != rating.user:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    rating.delete()
    return Response({"msg" : "Deleted Successfully"})