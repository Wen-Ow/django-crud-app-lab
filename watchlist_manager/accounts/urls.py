
from .views import registerView, loginView, logoutView
from django.urls import path

urlpatterns = [
    path('register/', registerView, name='register'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
]
