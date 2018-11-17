from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.forms import inlineformset_factory
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .models import Discussion,CustomUser


# Normal User Forms
class DiscussionCreationForm(forms.ModelForm):
    #users=forms.MultipleChoiceField()

    class Meta():
        model = Discussion
        fields = ('topic', 'users')

    def __init__(self, *args, **kwargs):
        super(DiscussionCreationForm, self).__init__(*args, **kwargs)
        self.fields['topic'].widget.attrs.update({'class': 'form-control'})
        self.fields['users'] = forms.ModelMultipleChoiceField(CustomUser.objects.all(),widget=forms.CheckboxSelectMultiple())

    def save(self, commit=True):
        self.instance.creator=self.creator
        return super(forms.ModelForm, self).save(commit=True)



