from django.db import models

# Create your models here.
from users.models import CustomUser

class Event(models.Model):

    url = models.URLField(max_length=200)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    eventName = models.CharField(max_length=255)
    description = models.TextField(null= True)
    category = models.IntegerField(default=0)
    duration = models.DurationField()
    place = models.TextField(null=True)
    users = models.ManyToManyField(CustomUser)