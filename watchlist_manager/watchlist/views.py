from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import WatchlistForm
from .models import Watchlist

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

@login_required(login_url='login')
def watchlist_detail(request, pk):
    # Fetch the watchlist item by primary key (pk)
    try:
        watchlist_item = Watchlist.objects.get(pk=pk, user=request.user)
    except Watchlist.DoesNotExist:
        return render(request, 'watchlist/not_found.html', {'error': 'Watchlist item not found.'})

    context = {
        'watchlist_item': watchlist_item,
    }
    return render(request, 'watchlist/view.html', context)

@login_required(login_url='login')
def edit_watchlist(request, pk):
    try:
        watchlist_item = Watchlist.objects.get(pk=pk, user=request.user)
    except Watchlist.DoesNotExist:
        return render(request, 'watchlist/not_found.html', {'error': 'Watchlist item not found.'})

    if request.method == 'POST':
        form = WatchlistForm(request.POST, instance=watchlist_item)
        if form.is_valid():
            form.save()
            return redirect('watchlist_details', pk=watchlist_item.pk)
    else:
        form = WatchlistForm(instance=watchlist_item)

    context = {
        'form': form,
        'watchlist_item': watchlist_item,
    }
    return render(request, 'watchlist/edit.html', context)

@login_required(login_url='login')
def delete_watchlist(request, pk):
    try:
        watchlist_item = Watchlist.objects.get(pk=pk, user=request.user)
        watchlist_item.delete()
        return redirect('home')
    except Watchlist.DoesNotExist:
        return render(request, 'watchlist/not_found.html', {'error': 'Watchlist item not found.'})