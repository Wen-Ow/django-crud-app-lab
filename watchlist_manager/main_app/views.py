# main_app/views.py

from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'base.html')
