# Generated by Django 4.1.2 on 2022-11-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0004_profil_profession_alter_etudiant_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='historique',
            name='identifiant',
            field=models.CharField(default='', max_length=1000),
        ),
    ]