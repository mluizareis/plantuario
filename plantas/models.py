from django.db import models
from django.conf import settings
from datetime import datetime
from plantas.choices import ILUMINACAO, REGA
from usuario.models import Usuario

class Planta(models.Model):
    nome_popular = models.CharField(max_length=200)
    nome_cientifico = models.CharField(max_length=200)
    origem = models.CharField(max_length=200)
    data_chegada = models.DateTimeField(default=datetime, blank=True)
    observacoes = models.TextField()
    iluminacao = models.CharField(max_length=1, choices=ILUMINACAO, blank=False, null=False)
    rega = models.CharField(max_length=1, choices=REGA, blank=False, null=False)
    proprietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_cientifico