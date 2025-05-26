from django.shortcuts import render, redirect, get_object_or_404
from .models import WatchItem, Review
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

def home(request): # Home view for the application
    return render(request, 'main_app/home.html')

@login_required
def watchitem_index(request): # Index view for displaying all watch items for the logged-in user
    watchitems = WatchItem.objects.filter(user=request.user)
    return render(request, 'main_app/watchitem_list.html', { 'watchitems': watchitems })

@login_required
def watchitem_detail(request, pk): # Detail view for a specific watch item
    watchitem = get_object_or_404(WatchItem, pk=pk, user=request.user)
    return render(request, 'main_app/watchitem_detail.html', { 'watchitem': watchitem })

class WatchItemCreate(CreateView): # Create view for adding a new watch item
    model = WatchItem
    fields = ['title', 'item_type', 'description', 'release_date'] # Fields to be included in the form
    success_url = '/watchitems/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class WatchItemUpdate(UpdateView): # Update view for editing an existing watch item
    model = WatchItem
    fields = ['title', 'item_type', 'description', 'release_date']
    success_url = '/watchitems/'

class WatchItemDelete(DeleteView): # Delete view for removing a watch item
    model = WatchItem
    success_url = '/watchitems/'

def signup(request): # Signup view for creating a new user account
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): # Validate the form data
            # Save the new user and log them in
            user = form.save()
            login(request, user)
            return redirect('watchitem_index')
    else: # If the request is GET, display the signup form
        form = UserCreationForm() # Create a new user creation form instance
    return render(request, 'registration/signup.html', { 'form': form }) 