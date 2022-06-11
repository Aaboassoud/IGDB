from django.urls import path
from . import views

urlpatterns = [
    path('review/add/comment',views.add_comment,name='add_comment'),
    path('review/all',views.reviews,name='reviews'),
    path('review/add/rating',views.add_rating,name='add_rating'),
    path('review/delete/comment',views.delete_comment,name='delete_comment'),
    path('review/game/rating',views.rating_comment,name='rating_comment'),
    path('review/delete/rating',views.delete_rating,name='delete_rating'),
    
]
