from django.contrib import admin
from .models import Ratings, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('game','user', 'comment')

class RatingsAdmin(admin.ModelAdmin):
    list_display = ('game', 'rating', 'user')



admin.site.register(Ratings, RatingsAdmin)
admin.site.register(Comment, CommentAdmin)