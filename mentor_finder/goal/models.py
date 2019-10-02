from django.db import models
from mentor_finder.mentee.models import Mentee
from mentor_finder.mentor.models import Mentor

class Goal(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    assigned_to = models.ForeignKey(Mentee, on_delete=models.CASCADE)
    assigned_from = models.ForeignKey(Mentor, on_delete=models.CASCADE)