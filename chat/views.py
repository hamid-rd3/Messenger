"""This file manages the html files for the chat app."""

# Importing libraries
from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.

# Creating an object of the user model

user = get_user_model()
