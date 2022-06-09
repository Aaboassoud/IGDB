from django.urls import path
from . import views

urlpatterns = [
    path('games/add',views.add_game,name='add'),
    path('games/all',views.all_games,name='all'),
    path('games/edit',views.edit_game,name='edit'),
    path('games/delete',views.delete_game,name='delete'),
    
]
