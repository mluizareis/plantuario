from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:planta_id>', views.planta, name='planta')
]