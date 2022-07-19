from django.contrib import admin
from .models import Games, Wishlist

class GamesAdmin(admin.ModelAdmin):
    '''
                Admin interface
    this class to customize the admin interface
    
    '''
    list_display = ('game_title', 'company', 'rating', 'date_realeased', 'id')
    list_filter = ('company', 'rating')
    search_fields = ('game_title__contains',)
    date_hierarchy = 'date_realeased'


class WishlistAdmin(admin.ModelAdmin):
    '''
                Admin interface
    this class to customize the admin interface
    '''
    list_display = ('game', 'user')

admin.site.register(Games, GamesAdmin)
admin.site.register(Wishlist, WishlistAdmin)