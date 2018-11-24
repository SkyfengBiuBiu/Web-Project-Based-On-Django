from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    email = models.EmailField(_('email address'), blank=False)
    phone = models.CharField(_('phone number'), max_length=20, blank=False)
    address = models.CharField(_('address'), max_length=254, blank=False)

    class Meta(AbstractUser.Meta):
        ordering = ['-date_joined']

    def has_privacy_perm(self, user, permission):
        if PrivacySettings.PUBLIC == permission:
            return True
        elif PrivacySettings.FRIENDS == permission:
            from friendships.models import Friendship
            friendship = Friendship.objects.filter(Q(user1=self, user2=user) | Q(user1=user, user2=self))
            if friendship.exists():
                return True
            return False
        elif PrivacySettings.JUST_ME == permission:
            return False
        return False

    def is_friend(self, user):
        from friendships.models import Friendship
        friendship = Friendship.objects.filter(Q(user1=self, user2=user) | Q(user1=user, user2=self))
        if friendship.exists():
            return friendship[0]
        return None


class CustomUserProfile(models.Model):
    last_modified = models.DateTimeField(_('last modified'), auto_now=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    # Additional information
    age = models.PositiveSmallIntegerField(_('age'), default=0, blank=True, null=True)
    date_of_birth = models.DateField(_('birthday'), blank=True, null=True)
    photo = models.ImageField(_('photo'), upload_to='users/%Y/%m/%d', blank=True, null=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class PrivacySettings(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    PUBLIC = 'pb'
    FRIENDS = 'fr'
    JUST_ME = 'jm'
    SETTING_CHOICES = (
        (PUBLIC, 'Public'),
        (FRIENDS, 'Friends'),
        (JUST_ME, 'Just me')
    )
    real_name_p = models.CharField(_('real name privacy'), max_length=2, choices=SETTING_CHOICES, default=PUBLIC)
    email_p = models.CharField(_('email privacy'), max_length=2, choices=SETTING_CHOICES, default=PUBLIC)
    phone_p = models.CharField(_('phone privacy'), max_length=2, choices=SETTING_CHOICES, default=PUBLIC)
    address_p = models.CharField(_('address privacy'), max_length=2, choices=SETTING_CHOICES, default=PUBLIC)
    profile_p = models.CharField(_('profile privacy'), max_length=2, choices=SETTING_CHOICES, default=PUBLIC)

    friend_list_p = models.CharField(_('friends privacy'), max_length=2, choices=SETTING_CHOICES, default=PUBLIC)

    def __str__(self):
        return 'Privacy Settings for {}'.format(self.user.username)
