from django.contrib import admin
from .models import Adubacao, Controle_de_pragas, Troca_de_vaso

admin.site.register(Adubacao)
admin.site.register(Controle_de_pragas)
admin.site.register(Troca_de_vaso)