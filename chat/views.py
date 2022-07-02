"""This file manages the html files for the chat app."""

# Importing libraries
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

# Creating an object of the user model

user = get_user_model()


def index(request):
    """Render the index.html file and exclude the current user."""
    users = user.objects.exclude(username=request.user.username)
    return render(request, "index.html", context={"users": users})


def chatPage(request, username):
    """Render the main_chat.html file and exclude the current user."""
    user_obj = user.objects.get(username=username)
    users = user.objects.exclude(username=request.user.username)
    return render(request, "main_chat.html", context={"users": users,
                                                      "user": user_obj})


def register(request):
    form = UserCreationForm()
    if form.is_valid():
        username=form.cleaned_data.get('username')
        messages.success(request,f'Account created  for {username}!')
    else:
        form=UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})
