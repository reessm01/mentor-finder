from django.contrib import admin
from django.urls import path

from mentor_finder.message.models import Message

admin.site.register(Message)

url_patterns = []
