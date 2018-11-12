from django import forms

from profiles.models import Post, Comment


class ProfileForm():
    pass


class ProfileSettingsForm(forms.ModelForm):
    pass


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
