from django import forms
from .models import Comment
from .models import TextContent

class TextContentForm(forms.ModelForm):
    class Meta:
        model = TextContent
        fields = ['title', 'content', 'content_type', 'image', 'video_url']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']


