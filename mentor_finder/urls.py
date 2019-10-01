from django.contrib import admin
from django.urls import path

from mentor_finder.mentor.urls import url_patterns as mentor_urls
from mentor_finder.mentee.urls import url_patterns as mentee_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += mentee_urls

urlpatterns += mentor_urls
