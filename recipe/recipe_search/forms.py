from django import forms

from .models import Recipe, Review

class PostForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', ]