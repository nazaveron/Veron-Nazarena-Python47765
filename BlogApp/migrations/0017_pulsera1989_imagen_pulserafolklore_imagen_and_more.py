# Generated by Django 4.2.5 on 2023-10-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0016_delete_pulseraspeaknow'),
    ]

    operations = [
        migrations.AddField(
            model_name='pulsera1989',
            name='imagen',
            field=models.ImageField(default='n', upload_to='pulseras_fotos'),
        ),
        migrations.AddField(
            model_name='pulserafolklore',
            name='imagen',
            field=models.ImageField(default='n', upload_to='pulseras_fotos'),
        ),
        migrations.AddField(
            model_name='pulseralover',
            name='imagen',
            field=models.ImageField(default='n', upload_to='pulseras_fotos'),
        ),
        migrations.AddField(
            model_name='pulserareputation',
            name='imagen',
            field=models.ImageField(default='n', upload_to='pulseras_fotos'),
        ),
    ]
