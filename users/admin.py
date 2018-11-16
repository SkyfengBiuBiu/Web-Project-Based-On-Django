from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.db import transaction
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _

from .forms import CustomUserProfileAdminChangeForm, CustomUserAdminCreationForm
from .models import CustomUser, CustomUserProfile, PrivacySettings


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', 'first_name', 'last_name', 'phone', 'address')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active')

    add_form = CustomUserAdminCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'phone', 'address', 'password1', 'password2'),
        }),
    )

    def save_model(self, request, obj, form, change):
        if ~obj.is_superuser:
            obj.is_active = False

        with transaction.atomic():
            super(UserAdmin, self).save_model(request, obj, form, change)
            # Create an empty profile for users
            CustomUserProfile.objects.create(user=obj)
            # Create an privacy settings for users
            PrivacySettings.objects.create(user=obj)
            # Send validation Email on sign-up
            self.send_mail(request, obj)

    def send_mail(self, request, user):
        current_site = get_current_site(request)
        site_name = current_site.name
        domain = current_site.domain

        subject_template_name = 'users/signup_subject.txt'
        email_template_name = 'users/signup_email_template.html'
        from_email = 'no-reply@' + site_name
        to_email = user.email

        context = {
            'email': to_email,
            'domain': domain,
            'site_name': 'Group003 SNS',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'user': user,
            'token': default_token_generator.make_token(user),
            'protocol': 'https' if request.is_secure() else 'http'
        }

        subject = loader.render_to_string(subject_template_name, context)
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)
        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        email_message.send()


class CustomUserProfileAdmin(admin.ModelAdmin):
    form = CustomUserProfileAdminChangeForm
    list_display = ('user', 'age', 'date_of_birth', 'photo', 'gender')


class PrivacySettingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'real_name_p', 'email_p', 'phone_p', 'address_p', 'profile_p', 'friend_list_p')


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUserProfile, CustomUserProfileAdmin)
admin.site.register(PrivacySettings, PrivacySettingsAdmin)
