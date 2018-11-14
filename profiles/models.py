from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import CustomUser


# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    last_modified = models.DateTimeField(_('last modified'), auto_now=True)
    content = models.CharField(_('post'), max_length=140)

    class Meta:
        ordering = ['-created_time', '-last_modified']

    def __str__(self):
        return self.content


class Comment(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    last_modified = models.DateTimeField(_('last modified'), auto_now=True)
    content = models.CharField(_('comment'), max_length=140)

    class Meta:
        ordering = ['-created_time', '-last_modified']

    def __str__(self):
        return self.content
