from django.shortcuts import render
from watchlist.models import Watchlist

def home(request): # Home view for the application
    if request.user.is_authenticated:
        watchlist_items = Watchlist.objects.filter(user=request.user)  # Fetch watchlist items for the logged-in user
        context = {
            'watchlist_items': watchlist_items  # Pass the watchlist items to the template context
        }
        return render(request, 'main_app/home.html', context)  # Render the home template with the context data
    else:
        return render(request, 'main_app/home.html')
