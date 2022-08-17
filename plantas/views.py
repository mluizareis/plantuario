from django.shortcuts import render, get_object_or_404
from .models import Planta

def index(request):

    plantas = Planta.objects.order_by('nome_cientifico')
    dados = {
        'plantas' : plantas, 
    }
    return render(request, 'index.html', dados)

def planta(request, planta_id):

    planta_id = get_object_or_404(Planta, pk=planta_id) 
    planta_a_exibir = {
        'planta': planta_id
    }
    return render(request, 'planta.html', planta_a_exibir)