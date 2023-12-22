from django.db import models

class Inscrito(models.Model):
    ESTADOS = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    institucion = models.ForeignKey('Institucion', on_delete=models.CASCADE)
    hora_inscripcion = models.TimeField(auto_now_add=True)
    estado = models.CharField(max_length=11, choices=ESTADOS, default='RESERVADO')
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
            return f"{self.nombre} - {self.institucion}"

class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre