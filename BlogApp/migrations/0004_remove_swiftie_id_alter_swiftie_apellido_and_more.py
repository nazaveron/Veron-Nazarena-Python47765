# Generated by Django 4.2.5 on 2023-10-02 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0003_rename_swifties_swiftie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='swiftie',
            name='id',
        ),
        migrations.AlterField(
            model_name='swiftie',
            name='Apellido',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='swiftie',
            name='Email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='swiftie',
            name='Nacionalidad',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='swiftie',
            name='Nombre',
            field=models.CharField(max_length=100),
        ),
    ]