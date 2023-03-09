from django import forms
from .models import Post
import re

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your-title"}))
    class Meta:
        model = Post
        fields = [
            'title',
            'subtitle',
            'text',
        ]

    # Validation
    def validation(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if re.search(r'^\w+$', title):
            raise forms.ValidationError("This is not a valid title")

class RawPostForm(forms.Form):
    title = forms.CharField(max_length=50)
    subtitle = forms.CharField(max_length=120)
    text = forms.CharField(widget=forms.Textarea)