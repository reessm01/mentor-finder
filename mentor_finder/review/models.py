from django.db import models
from mentor_finder.mentor.models import Mentor
from mentor_finder.mentor.models import Mentee

class Review(models.Model):
   text = models.TextField()
   reviwer =  models.ForeignKey(Mentee, on_delete=models.CASCADE)
   reviewed = models.ForeignKey(Mentor, on_delete=models.CASCADE)