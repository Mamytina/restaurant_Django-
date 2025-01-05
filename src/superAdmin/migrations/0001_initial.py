# Generated by Django 5.0.1 on 2025-01-05 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nouriture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='superAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_superAdmin', models.CharField(max_length=32, null=True)),
                ('prenom_superAdmin', models.CharField(max_length=32, null=True)),
                ('mot_de_passe_superAdmin', models.CharField(max_length=32, null=True)),
                ('id_nouritures', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nouriture.nouritures')),
            ],
        ),
    ]
