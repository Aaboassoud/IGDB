from django.contrib import admin
from .models import Ratings, Comment

class CommentAdmin(admin.ModelAdmin):
    '''
                Admin interface
    this class to customize the admin interface
    '''
    list_display = ('game','user', 'comment')
    list_filter = ('game',)

class RatingsAdmin(admin.ModelAdmin):
    '''
                Admin interface
    this class to customize the admin interface
    '''
    list_display = ('game', 'rating', 'user')
    list_filter = ('game','rating')




admin.site.register(Ratings, RatingsAdmin)
admin.site.register(Comment, CommentAdmin)