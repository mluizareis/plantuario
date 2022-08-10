# Generated by Django 4.1 on 2022-08-10 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adubacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_adubacao', models.DateTimeField(blank=True, default=datetime.datetime)),
                ('produto', models.CharField(max_length=200)),
                ('observacao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Controle_de_pragas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_controle', models.DateTimeField(blank=True, default=datetime.datetime)),
                ('tipo_praga', models.CharField(max_length=200)),
                ('produto', models.CharField(max_length=200)),
                ('observacao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Troca_de_vaso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_troca', models.DateTimeField(blank=True, default=datetime.datetime)),
                ('substrato', models.TextField()),
                ('tipo_vaso', models.CharField(max_length=200)),
                ('observacao', models.TextField()),
            ],
        ),
    ]
