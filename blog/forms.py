from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta(object):
        model = Post
        fields = ('title', 'text',)
