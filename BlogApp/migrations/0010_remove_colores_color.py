# Generated by Django 4.2.5 on 2023-10-12 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0009_colores_delete_mil989_alter_era_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colores',
            name='color',
        ),
    ]
