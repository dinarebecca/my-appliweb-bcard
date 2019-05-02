from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UtilisateurCreationForm, UtilisateurChangeForm
from .models import Utilisateur

class UtilisateurAdmin(UserAdmin):
    add_form = UtilisateurCreationForm
    form = UtilisateurChangeForm
    model = Utilisateur
    list_display = ['nom','prenom','fonction','telephone',]

admin.site.register(Utilisateur, UtilisateurAdmin)