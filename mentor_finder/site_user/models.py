from django.db import models
from django.contrib.auth.models import User
from mentor_finder.message.models import Message
from mentor_finder.personality.models import Personality

class SiteUser(models.Model):
    headline = models.TextField(max_length=280, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_link = models.CharField(max_length=255, blank=True)
    personality = models.ForeignKey(Personality, on_delete=models.CASCADE)
    messages = models.ManyToManyField(Message, blank=True, null=True)
    is_mentor = models.BooleanField(default=False)
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
