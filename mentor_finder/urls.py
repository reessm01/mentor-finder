from django.contrib import admin
from django.urls import path

from mentor_finder.dashboard.urls import url_patterns as dashboard_urls
from mentor_finder.industry.urls import url_patterns as industry_urls
from mentor_finder.goal.urls import url_patterns as goal_urls
from mentor_finder.review.urls import url_patterns as review_urls
from mentor_finder.personality.urls import url_patterns as personality_urls
from mentor_finder.message.urls import url_patterns as message_urls
from mentor_finder.site_user.urls import url_patterns as site_user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += site_user_urls
urlpatterns += message_urls
urlpatterns += personality_urls
urlpatterns += review_urls
urlpatterns += goal_urls
urlpatterns += industry_urls
urlpatterns += dashboard_urls
