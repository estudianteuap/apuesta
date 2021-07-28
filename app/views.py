from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from app.models import Equipo, Jugador, Evento
# Create your views here.
class IndexViews(generic.ListView):
    template_name='app/index.html'
    context_object_name='equipos'
    def get_queryset(self):
        return Equipo.objects.order_by('nombre')
    