from django.contrib import admin
from django.urls import path

from mentor_finder.goal.models import Goal, Task

admin.site.register(Goal)
admin.site.register(Task)

url_patterns = []
