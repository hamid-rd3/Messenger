"""This file manages the html files for the chat app."""

# Importing libraries
from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.

# Creating an object of the user model

user = get_user_model()


def index(request):
    """Render the index.html file and exclude the current user."""
    users = user.objects.exclude(username=request.user.username)
    return render(request, "index.html", context={"users": users})


def chatPage(request):
    """Render the main_chat.html file and exclude the current user."""
    users = user.objects.exclude(username=request.user.username)
    return render(request, "main_chat.html", context={"users": users,
                                                      "user": user_obj})
