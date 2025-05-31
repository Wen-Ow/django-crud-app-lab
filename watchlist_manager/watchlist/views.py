from django.shortcuts import render, redirect

# Create your views here.
def add_watchlist(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'watchlist/add.html')