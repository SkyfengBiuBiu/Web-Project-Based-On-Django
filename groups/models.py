from django.db import models

# Create your models here.

from users.models import CustomUser

class Group(models.Model):

    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    groupName = models.CharField(max_length = 255)
    description = models.TextField(null = True)
    member = models.ManyToManyField(CustomUser)
