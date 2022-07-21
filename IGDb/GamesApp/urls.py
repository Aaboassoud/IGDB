from django.urls import path
from . import views

urlpatterns = [
    path('games/add',views.add_game,name='add'),
    path('games/all',views.all_games,name='all'),
    path('games/edit/<game_id>',views.edit_game,name='edit'),
    path('games/details/<game_id>',views.game_details,name='game_details'),
    path('games/delete/<game_id>',views.delete_game,name='delete'),
    path('games/add/wishlist/<game_id>',views.add_to_wishlist,name='add_wishlist'),
    path('games/delete/wishlist/<game_id>',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('games/my_wishlist',views.wishlist,name='my_wishlist'),
    path('gamers/all',views.all_gamers,name='all_gamers'),
    
]
