from django.db import models
from django.contrib.auth.models import User
from mentor_finder.mentor.models import Mentor


class Mentee(models.Model):
    name = models.CharField(max_length=35)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_link = models.CharField(max_length=4000)
    # personality = models.ForeignKey(Personality)
    # goals = models.ForeignKey(Goal)
    mentors = ManyToManyField(Mentor)
    # messages = ForeignKey(Message)

    def __str__(self):
        return self.name
