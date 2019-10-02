from django.db import models
from mentor_finder.site_user.models import Site_User

class Review(models.Model):
   text = models.TextField()
   reviwer =  models.ForeignKey(Site_User, on_delete=models.CASCADE)
   reviewed = models.ForeignKey(Site_User, on_delete=models.CASCADE)