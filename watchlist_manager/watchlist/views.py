from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import WatchlistForm

# Create your views here.
@login_required(login_url='login')
def add_watchlist(request):
    if request.method == 'POST':
        form = WatchlistForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("Form is valid")
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            # Redirect to a success page or the watchlist detail page
            return redirect('home')
        else:
            print(form.errors)
            # If form is not valid, render the form with errors
            context = {
                'form': form,
                'error': 'Please correct the errors below.'
            }
            return render(request, 'watchlist/add.html', context)
    
    form = WatchlistForm()
    context = {
        'form': form,
    }
    return render(request, 'watchlist/add.html', context)