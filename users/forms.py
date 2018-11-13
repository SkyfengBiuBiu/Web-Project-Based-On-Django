from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.forms import inlineformset_factory
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .models import CustomUser, CustomUserProfile


# Normal User Forms
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'address')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    def send_mail(self, request, user):
        current_site = get_current_site(request)
        site_name = current_site.name
        domain = current_site.domain

        subject_template_name = 'users/signup_subject.txt'
        email_template_name = 'users/signup_email_template.html'
        from_email = 'no-reply@' + site_name
        to_email = self.cleaned_data['email']

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

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=True)
        # Create an empty profile for users
        CustomUserProfile.objects.create(user=user)
        # Send validation Email on sign-up
        self.send_mail(self.request, user)
        return user


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone', 'address')

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})


class CustomUserProfileChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUserProfile
        fields = ['gender', 'age', 'date_of_birth', 'photo']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserProfileChangeForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['age'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_of_birth'].widget.attrs.update({'class': 'form-control'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control'})


CustomUserProfileFormSet = inlineformset_factory(CustomUser, CustomUserProfile, form=CustomUserProfileChangeForm,
                                                 can_delete=False)


# Admin User Forms
class CustomUserAdminCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'address')

    def send_mail(self, request, user):
        current_site = get_current_site(request)
        site_name = current_site.name
        domain = current_site.domain

        subject_template_name = 'users/signup_subject.txt'
        email_template_name = 'users/signup_email_template.html'
        from_email = 'no-reply@' + site_name
        to_email = self.cleaned_data['email']

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

    def save(self, commit=True):
        user = super(CustomUserAdminCreationForm, self).save(commit=True)
        # Create an empty profile for users
        CustomUserProfile.objects.create(user=user)
        # Send validation Email on sign-up
        self.send_mail(self.request, user)
        return user


class CustomUserAdminChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone', 'address')


class CustomUserProfileAdminChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUserProfile
        fields = ('gender', 'age', 'date_of_birth', 'photo')
