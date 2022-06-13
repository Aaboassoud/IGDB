from django.urls import path
from . import views

urlpatterns = [
    path('add/comment/<game_id>',views.add_comment,name='add_comment'),
    path('all/<game_id>',views.reviews,name='reviews'),
    path('delete/comment/<comment_id>',views.delete_comment,name='delete_comment'),
    path('add/rating/<game_id>',views.add_rating,name='add_rating'),
    path('ratings/<game_id>',views.rating,name='rating_comment'),
    path('delete/rating/<rating_id>',views.delete_rating,name='delete_rating'),
    path('update/ratings',views.update_rating,name='update_rating'),
    
]
