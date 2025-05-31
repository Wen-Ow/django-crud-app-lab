from django.urls import path, include
from .views import add_watchlist

urlpatterns = [
    path('add/', add_watchlist, name='add_watchlist'),
   
]

