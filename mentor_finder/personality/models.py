from django.db import models

class Personality(models.Model):
    title = models.CharField(max_length=4, unique=True)
    detail = models.TextField()
    related = models.ManyToManyField("self")

    def __str__(self):
        return self.title
