from django.db import models

from Account.models import Profile
from .models import *
from Comic.models import Chapter,Comic
# Create your models here.

class Viewed (models.Model):
    Comic = models.ForeignKey(Comic,on_delete=models.CASCADE,related_name="vieweds")
    Chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    Profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
