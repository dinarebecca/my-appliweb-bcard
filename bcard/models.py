from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models




class Utilisateur(AbstractUser):
    nom = models.CharField(max_length =20)
    prenom = models.CharField(max_length =20)
    fonction= models.CharField(max_length =45)
    telephone = models.CharField(max_length =20)

def __str__(self):
        return self.email

class test(models.Model):
        idtest = models.AutoField(primary_key=True)
        nom = models.CharField(max_length=20)