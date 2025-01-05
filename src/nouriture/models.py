from django.db import models

# Create your models here.
class Nouritures(models.Model):
    photo_ntr=models.CharField(max_length=32, null=True)
    nom_ntr = models.CharField(max_length=32, null=True)
    ingredient_ntr=models.CharField(max_length=32, null=True)
    prix_ntr=models.DecimalField(max_digits=10, decimal_places=3)
    
    