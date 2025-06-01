from django.urls import path, include
from .views import add_watchlist, watchlist_detail, edit_watchlist, delete_watchlist

urlpatterns = [
    path('add/', add_watchlist, name='add_watchlist'),
    path('view/<str:pk>/', watchlist_detail, name="watchlist_details"),  # Include watchlist detail URLs
    path('edit/<str:pk>/', edit_watchlist, name="edit_watchlist"),  # Include watchlist edit URLs
    path('delete/<str:pk>/', delete_watchlist, name="delete_watchlist"),  # Include watchlist delete URLs
   
]

