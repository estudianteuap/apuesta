from django.contrib import admin
from .models import Equipo, Jugador, Evento, Juego, Historial

class JugadorInLine(admin.StackedInline):
    model=Jugador
    extra=1

class EquipoAdmin(admin.ModelAdmin):
    inlines=[JugadorInLine]

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador)
admin.site.register(Evento)
admin.site.register(Juego)
admin.site.register(Historial)
# Register your models here.
