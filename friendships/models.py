from django.db import models
from users.models import CustomUser
# Create your models here.
class Friendship(models.Model):
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_1')
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_2')
    date = models.DateTimeField("request published")

    class Meta:
        ordering = []

class FriendshipRequest(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recipient')
    date = models.DateTimeField("chat published")
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.sender

    class Meta:
        ordering = ["date"]
