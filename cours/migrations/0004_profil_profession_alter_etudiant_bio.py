# Generated by Django 4.1.2 on 2022-11-09 13:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0003_theme_document_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='profession',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='bio',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
