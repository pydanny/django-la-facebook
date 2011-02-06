from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User)
    bio = models.TextField()
    name = models.CharField(max_length=255)