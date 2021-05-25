from django import forms
from django.contrib.auth.models import User
from .models import Communaute, Commentaire, Post


class SubscriptionForm(forms.Form):
    community = forms.CharField(max_length=30)
    action = forms.CharField(max_length=20)


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('post', 'auteur', 'contenu')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('date_creation',)