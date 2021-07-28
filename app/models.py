from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre=models.CharField(max_length=100)
    ciudad=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    


class Jugador(models.Model):
    equipo=models.ForeignKey(Equipo, on_delete=models.CASCADE)
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    fecha_nacimient=models.DateTimeField("Fecha de Nacimiento")
    nacionalidad=models.CharField(max_length=60)
    stat_fuerza=models.IntegerField(default=1)
    stat_defensa=models.IntegerField(default=1)
    stat_velocidad=models.IntegerField(default=1)
    stat_resistencia=models.IntegerField(default=1)
    estado=models.BooleanField(default=True)
    def __str__(self):
        return self.nombres + " " + self.apellidos
    

class Evento(models.Model):
    nombre=models.CharField(max_length=100)
    fecha_inicio=models.DateTimeField("Fecha de Inicio")
    fecha_fin=models.DateTimeField("Fecha de Fin")
    def __str__(self):
        return self.nombre

class Juego(models.Model):
    evento=models.ForeignKey(Evento, on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=100)
    fecha_partido=models.DateTimeField("Fecha del Partido")
    def __str__(self):
        return self.descripcion
    

class Historial(models.Model):
    juego=models.ForeignKey(Juego, on_delete=models.CASCADE)
    equipo=models.ForeignKey(Equipo, on_delete=models.CASCADE)
    puntaje=models.IntegerField()
    promedio_stat_fuerza=models.IntegerField(default=1)
    promedio_stat_defensa=models.IntegerField(default=1)
    promedio_stat_velocidad=models.IntegerField(default=1)
    promedio_stat_resistencia=models.IntegerField(default=1)
    def __str__(self):
        return self.equipo
    
    