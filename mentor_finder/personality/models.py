from django.db import models

class Personality(models.Model):
    title = models.CharField(max_length=4)
    detail = models.TextField()