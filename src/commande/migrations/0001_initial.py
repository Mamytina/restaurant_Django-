# Generated by Django 5.0.1 on 2025-01-05 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('listes', '0001_initial'),
        ('nouriture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commandes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_commande', models.CharField(max_length=32, null=True)),
                ('date_commande', models.DateTimeField(blank=True, null=True)),
                ('id_clients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.clients')),
                ('id_listescommande', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listes.listescommandes')),
                ('id_nouritures', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nouriture.nouritures')),
            ],
        ),
    ]
