# Generated by Django 4.2.5 on 2023-10-11 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0006_pulsera_era_comentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pulsera',
            old_name='apellido',
            new_name='album',
        ),
        migrations.RenameField(
            model_name='pulsera',
            old_name='nombre',
            new_name='autor',
        ),
    ]