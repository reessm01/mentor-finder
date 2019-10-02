from django.db import models
from django.contrib.auth.models import User
from mentor_finder.mentee.models import Mentee

class Industry(models.Model):
    title = models.CharField(max_length=100)

class Mentee(Mentee):
    mentees = models.ManyToManyField(Mentee)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)