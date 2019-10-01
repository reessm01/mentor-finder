from django.db import models
from django.contrib.auth.models import User
from mentor_finder.mentee.models import Mentee


class Mentee(models.Model):
    name = models.CharField(max_length=35)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_link = models.CharField(max_length=4000)
    # personality = models.ForeignKey(Personality)
    # goals = models.ManyToManyField(Goal)
    mentees = ManyToManyField(Mentee)
    # industry = ForeignKey(Industry)
    # reviews = ManyToManyField(Review)
    # messages = ForeignKey(Message)

    def __str__(self):
        return self.name
