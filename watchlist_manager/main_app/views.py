from django.shortcuts import render

def home(request): # Home view for the application
    return render(request, 'main_app/home.html')
