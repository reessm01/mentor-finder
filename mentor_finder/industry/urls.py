from django.contrib import admin
from django.urls import path

from .models import Industry

admin.site.register(Industry)

url_patterns = []
