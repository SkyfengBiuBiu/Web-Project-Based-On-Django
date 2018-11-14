from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models import CustomUser


# Create your models here.
class ChatMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    headline = models.DateTimeField("chat published")
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["headline"]


class Discussion(models.Model):
    """ Write your answer in 7.1 here. """
    url = models.URLField(max_length=255, unique=True, default='')
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    users = models.ManyToManyField(CustomUser)
    chatMessage = models.ManyToManyField(ChatMessage)

    class Meta:
        ordering = ["url"]
