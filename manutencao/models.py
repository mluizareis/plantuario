from django.db import models
from datetime import datetime

class Adubacao(models.Model):
    data_adubacao = models.DateTimeField(default=datetime, blank=True)
    produto = models.CharField(max_length=200)
    observacao = models.TextField()

class Controle_de_pragas(models.Model):
    data_controle = models.DateTimeField(default=datetime, blank=True)
    tipo_praga = models.CharField(max_length=200)
    produto = models.CharField(max_length=200)
    observacao = models.TextField()

class Troca_de_vaso(models.Model):
    data_troca = models.DateTimeField(default=datetime, blank=True)
    substrato = models.TextField()
    tipo_vaso = models.CharField(max_length=200)
    observacao = models.TextField()
