from django.contrib import admin
from .models import Equipo, Jugador, Evento, Juego, Historial

class JugadorInLine(admin.StackedInline):
    model=Jugador
    extra=1

class EquipoAdmin(admin.ModelAdmin):
    inlines=[JugadorInLine]


class HistorialInLine(admin.StackedInline):
    model=Historial
    extra=1

class JuegoAdmin(admin.ModelAdmin):
    inlines=[HistorialInLine]
    
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador)
admin.site.register(Evento)
admin.site.register(Juego, JuegoAdmin)
admin.site.register(Historial)
# Register your models here.
