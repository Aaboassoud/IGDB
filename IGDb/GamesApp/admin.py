from django.contrib import admin
from .models import Games, Wishlist

class GamesAdmin(admin.ModelAdmin):
    list_display = ('game_title', 'company', 'rating', 'date_realeased')
    date_hierarchy = 'date_realeased'

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('game', 'user')

admin.site.register(Games, GamesAdmin)
admin.site.register(Wishlist, WishlistAdmin)