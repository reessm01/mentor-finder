from django.db import models
from mentor_finder.site_user.models import SiteUser

class Goal(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    assigned_to = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    assigned_from = models.ForeignKey(SiteUser, on_delete=models.CASCADE)