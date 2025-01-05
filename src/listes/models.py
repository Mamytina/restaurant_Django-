from django.db import models

# Create your models here.
class listesCommandes(models.Model):
    listes_listesCommandes=models.CharField(max_length=32, null=True)
    statue_listesCommandes = models.IntegerField(default=1)