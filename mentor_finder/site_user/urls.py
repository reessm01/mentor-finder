from django.contrib import admin
from django.urls import path
from .models import SiteUser

from .views import login_view, register_view

admin.register(SiteUser)

url_patterns = [
    path('login/', login_view, name='login'),
    path('register', register_view, name='register'),
]
