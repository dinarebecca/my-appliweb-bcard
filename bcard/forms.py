from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Utilisateur

class UtilisateurCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Utilisateur
        fields = ('nom','prenom','fonction','telephone')

class UtilisateurChangeForm(UserChangeForm):

    class Meta:
        model = Utilisateur
        fields = ('nom','prenom','fonction','telephone')