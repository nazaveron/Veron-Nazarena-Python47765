# Generated by Django 4.2.5 on 2023-10-02 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Eras',
        ),
        migrations.AddField(
            model_name='swifties',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]