from django.db import models
from django.contrib.auth.models import User
from mentor_finder.mentor.models import Mentor
from mentor_finder.message.models import Message
from mentor_finder.personality.models import Personality

class Goal(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()

class Mentee(models.Model):
    name = models.CharField(max_length=35)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_link = models.CharField(max_length=255)
    personality = models.ForeignKey(Personality)
    goals = models.ForeignKey(Goal, verbose_name='Goals')
    mentors = models.ManyToManyField(Mentor)
    messages = models.ForeignKey(Message)

    def __str__(self):
        return self.name
