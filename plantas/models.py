from django.db import models
from django.conf import settings
from datetime import datetime
from plantas.choices import ILUMINACAO, REGA
from usuario.models import Usuario

class Planta(models.Model):
    nome_popular = models.CharField(max_length=200, blank=True)
    nome_cientifico = models.CharField(max_length=200)
    origem = models.CharField(max_length=200, blank=True)
    data_chegada = models.DateTimeField(default=datetime.now, blank=True)
    observacoes = models.TextField(blank=True)
    iluminacao = models.CharField(max_length=1, choices=ILUMINACAO, blank=False, null=False)
    rega = models.CharField(max_length=1, choices=REGA, blank=False, null=False)
    proprietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    foto_planta = models.ImageField(upload_to ='fotos/%d/%m/%Y/', blank=True)
    def __str__(self):
        return self.nome_cientifico