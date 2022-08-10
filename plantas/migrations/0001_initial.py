# Generated by Django 4.1 on 2022-08-10 18:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_popular', models.CharField(max_length=200)),
                ('nome_cientifico', models.CharField(max_length=200)),
                ('origem', models.CharField(max_length=200)),
                ('data_chegada', models.DateTimeField(blank=True, default=datetime.datetime)),
                ('observacoes', models.TextField()),
                ('iluminacao', models.CharField(choices=[('1', 'Sol pleno'), ('2', 'Meia Sombra'), ('3', 'Sombra')], max_length=1)),
                ('rega', models.CharField(choices=[('1', 'Pouco frequente'), ('2', 'Moderada'), ('3', 'Frequente')], max_length=1)),
                ('foto_planta', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario')),
            ],
        ),
    ]
