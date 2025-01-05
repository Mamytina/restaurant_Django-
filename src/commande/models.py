from django.db import models


from nouriture.models import Nouritures
from clients.models import Clients
from listes.models import listesCommandes

# Create your models here.
class Commandes(models.Model):
    numero_commande=models.CharField(max_length=32, null=True)
    date_commande=models.DateTimeField(blank=True, null=True)
    id_nouritures = models.ForeignKey(Nouritures, on_delete=models.SET_NULL,null=True)
    id_clients = models.ForeignKey(Clients, on_delete=models.SET_NULL,null=True)  
    id_listescommande = models.ForeignKey(listesCommandes, on_delete=models.SET_NULL,null=True)