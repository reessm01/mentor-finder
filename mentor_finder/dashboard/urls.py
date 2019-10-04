from django.contrib import admin
from django.urls import path

from .views import *

url_patterns = [
    path('dashboard', dashboard.as_view(), name='dashboard'),
]
