from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']
        exclude = ['author']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти пользователя")


class CommentForm(forms.Form):
    text = forms.CharField(max_length=1000, required=False, label="Комментарий")

