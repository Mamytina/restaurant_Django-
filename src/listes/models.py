from django.db import models

# Create your models here.
class listesCommandes(models.Model):
    listes_listesCommandes=models.CharField(max_length=32, null=True)
    total_listesCommandes=models.DecimalField(max_digits=10, decimal_places=3)
    statue_listesCommandes = models.IntegerField(default=1)