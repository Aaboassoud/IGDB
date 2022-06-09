from django.db import models
from django.contrib.auth.models import User 

class Games(models.Model):
    CHOICES = (
        ('Sony', 'Sony'),
        ('Microsoft', 'Microsoft'),
        ('Activision Blizzard', 'Activision Blizzard'),
        ('Electronic Arts', 'Electronic Arts'),
        ('Epic Games', 'Epic Games'),
        ('Ubisoft', 'Ubisoft')
    )
    game_title = models.CharField(max_length=124)
    description = models.TextField(blank=True)
    date_realeased = models.DateTimeField()
    company = models.CharField(max_length=250,choices = CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    modfiy = models.DateTimeField(auto_now=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)#.annotate(avg_review=Avg('rates_rating'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)