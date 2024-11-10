from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login


# Signin view for login functionality
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) 
            return redirect('home')  
    else:
        form = AuthenticationForm()

    return render(request, 'signin.html', {'form': form})


# Signup view for registration functionality
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            auth_login(request, user)  # Log the user in automatically after signup
            return redirect('home')  # Redirect to the home page after successful signup
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
