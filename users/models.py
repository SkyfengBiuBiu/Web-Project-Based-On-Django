from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from discussions.models import Discussion

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    email = models.EmailField(_('email address'), blank=False)
    phone = models.CharField(_('phone number'), max_length=20, blank=False)
    address = models.CharField(_('address'), max_length=254, blank=False)
    discussions = models.ManyToManyField(Discussion)
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )


class CustomUserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    # Additional information
    age = models.PositiveIntegerField(_('age'), default=0, blank=True, null=True)
    date_of_birth = models.DateField(_('birthday'), blank=True, null=True)
    photo = models.ImageField(_(''), upload_to='users/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
