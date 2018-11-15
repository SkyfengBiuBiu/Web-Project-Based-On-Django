from django import forms

from profiles.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'privacy_level']

    def save(self, commit=True):
        self.instance.owner = self.owner
        return super(forms.ModelForm, self).save(commit=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
