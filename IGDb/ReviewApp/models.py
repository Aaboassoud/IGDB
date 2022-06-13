from django.db import models
from django.contrib.auth.models import User 
from GamesApp.models import Games

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)

    def __str__(self):
        return (self.game.game_title)

class Ratings(models.Model):
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)

    def __str__(self):
        return self.game.game_title