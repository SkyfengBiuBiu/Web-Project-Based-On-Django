from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models import CustomUser
from datetime import datetime

# Create your models here.
class ChatMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    headline = models.DateTimeField(default=datetime.now, blank=True)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["headline"]


class Discussion(models.Model):
    """ Write your answer in 7.1 here. """
    topic = models.CharField(max_length=200,default='family', blank=False, null=False)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='creator')
    users = models.ManyToManyField(CustomUser,related_name='users')
    chatMessage = models.ManyToManyField(ChatMessage)
    date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ["date"]