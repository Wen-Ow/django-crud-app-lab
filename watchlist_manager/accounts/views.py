from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth import authenticate, login, logout
# Register View
def registerView(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = RegisterUserForm()
    if request.method == 'POST':
        # Handle registration logic here
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            # If form is not valid, render the form with errors
            context = {
                'form': form,
                'error': 'Please correct the errors below.'
            }
            return render(request, 'accounts/register.html', context)
    else:
        context = {
            'form': form
        }
        # Render registration form
        return render(request, 'accounts/register.html', context)


def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    # Handle login logic here
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home or another page after login
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'accounts/login.html')  # Render login form
    
def logoutView(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout