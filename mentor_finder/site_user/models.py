from django.db import models
from django.contrib.auth.models import User
from mentor_finder.message.models import Message
from mentor_finder.personality.models import Personality

class Goal(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()

class SiteUser(models.Model):
    name = models.CharField(max_length=35)
    headline = models.TextField(max_length=280)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_link = models.CharField(max_length=255)
    personality = models.ForeignKey(Personality, on_delete=models.CASCADE)
    goals = models.ManyToManyField(Goal, verbose_name='Goals')
    messages = models.ManyToManyField(Message)
    is_mentor = models.BooleanField(default=False)
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.name
