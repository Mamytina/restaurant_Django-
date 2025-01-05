from django.db import models

# Create your models here.
class Clients(models.Model):
    nom_clients=models.CharField(max_length=32, null=True)
    prenom_clients = models.CharField(max_length=32, null=True)
    numero_clients= models.CharField(max_length=32, null=True)
    adress_clients= models.CharField(max_length=32, null=True)
    email_clients= models.EmailField(unique=True)
    
    
    