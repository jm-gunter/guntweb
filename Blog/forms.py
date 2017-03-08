from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['class'] = 'text-area'

    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['class'] = 'text-area'

    class Meta:
        model = Comment
        fields = ('author', 'text',)
