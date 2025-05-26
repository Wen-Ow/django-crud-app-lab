# main_app/models.py
from django.db import models
from django.contrib.auth.models import User

class WatchItem(models.Model): 
    TYPE_CHOICES = [('Movie', 'Movie'), ('TV Series', 'TV Series')] # Define choices for item_type
    
    title = models.CharField(max_length=200) 
    item_type = models.CharField(max_length=10, choices=TYPE_CHOICES) 
    description = models.TextField(blank=True) # Optional description field
    release_date = models.DateField() # Date when the item was released
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Link to the user who added the item

    def __str__(self): # String representation of the model
        return self.title

class Review(models.Model):
    watch_item = models.ForeignKey(WatchItem, on_delete=models.CASCADE, related_name='reviews') # Link to the watch item being reviewed
    comment = models.TextField() # Review comment
    rating = models.IntegerField() # Rating out of 5
    created_at = models.DateTimeField(auto_now_add=True) # Timestamp when the review was created

    def __str__(self): # String representation of the review
        return f"{self.rating} - {self.comment[:30]}" # Show first 30 characters of the comment