from django.contrib import admin
from django.urls import path
from .models import Mentee

from .views import login_view, register_view

admin.register(Mentee)

url_patterns = [
    path('login/', login_view, name='login'),
    path('register', register_view, name='register'),
]
