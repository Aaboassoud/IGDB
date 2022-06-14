from django.contrib.auth.models import User
from django.db import models

class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    trophies = models.IntegerField()
