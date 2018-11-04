from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .models import CustomUser, CustomUserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'address')

    def send_mail(self, user):
        subject_template_name = 'users/signup_subject.txt'
        email_template_name = 'users/signup_email_template.html'
        from_email = 'no-reply@stormy-brook-84564.herokuapp.com'
        to_email = user.email

        context = {
            'email': to_email,
            'domain': 'stormy-brook-84564.herokuapp.com',
            'site_name': 'Group003 SNS',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'user': user,
            'token': default_token_generator.make_token(user),
            'protocol': 'https'
        }

        subject = loader.render_to_string(subject_template_name, context)
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)
        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        email_message.send()

    def save(self, commit=True):
        user = super().save(commit=True)
        # Create an empty profile for users
        CustomUserProfile.objects.create(user=user)
        # Send validation Email on sign-up
        self.send_mail(user)
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone', 'address')


class CustomUserProfileChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUserProfile
        fields = ('date_of_birth', 'photo')
