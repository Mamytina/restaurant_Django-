from django.db import models

# Create your models here.
from django.db import models


from nouriture.models import Nouritures
# Create your models here.
class superAdmin(models.Model):
    nom_superAdmin=models.CharField(max_length=32, null=True)
    prenom_superAdmin = models.CharField(max_length=32, null=True)
    mot_de_passe_superAdmin= models.CharField(max_length=32, null=True)
    id_nouritures = models.ForeignKey(Nouritures, on_delete=models.SET_NULL,null=True)