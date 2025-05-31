from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Watchlist(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50) # Required
    description = models.TextField(blank=True) # optional
    watched = models.BooleanField(default=False) # Default to False
    rating = models.IntegerField(null=True, blank=True) # Optional rating field
    release_year = models.IntegerField(null=True, blank=True) # Optional release year
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Link to the user who created the watchlist
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.title