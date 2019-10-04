from django.db import models
from mentor_finder.site_user.models import SiteUser

class Task(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=180)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(SiteUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Goal(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    tasks = models.ManyToManyField(Task, blank=True)
    assigned_to = models.ForeignKey(
        SiteUser,
        on_delete=models.CASCADE,
        related_name='mentee'
        )
    assigned_from = models.ForeignKey(
        SiteUser,
        on_delete=models.CASCADE,
        related_name='mentor'
        )

    def __str__(self):
        return self.title
