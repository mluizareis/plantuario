# Generated by Django 4.1 on 2022-08-15 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planta',
            name='foto_planta',
        ),
    ]
