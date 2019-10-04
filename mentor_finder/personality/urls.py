from django.contrib import admin
from django.urls import path

from mentor_finder.personality.models import Personality

admin.site.register(Personality)

url_patterns = []
