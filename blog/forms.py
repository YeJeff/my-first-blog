from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta(object):
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    class Meta(object):
        model = Comment
        fields = ('author', 'text',)
