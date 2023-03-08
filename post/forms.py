from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'subtitle',
            'text',
        ]

class RawPostForm(forms.Form):
    title = forms.CharField(max_length=50)
    subtitle = forms.CharField(max_length=120)
    text = forms.CharField()