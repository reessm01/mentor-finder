from django.contrib import admin
from django.urls import path

from mentor_finder.goal.urls import url_patterns as goal_urls
from mentor_finder.review.urls import url_patterns as review_urls
from mentor_finder.personality.urls import url_patterns as personality_urls
from mentor_finder.message.urls import url_patterns as message_urls
from mentor_finder.mentor.urls import url_patterns as mentor_urls
from mentor_finder.mentee.urls import url_patterns as mentee_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += mentee_urls
urlpatterns += mentor_urls
urlpatterns += message_urls
urlpatterns += personality_urls
urlpatterns += review_urls

urlpatterns += goal_urls
