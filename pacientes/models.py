from django.db import models
from .storage_backends import ReportesPDFStorage, ImagenesMedicasStorage

class Paciente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Examen(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    
    # Almacenamiento en Azure Blob Storage - Contenedor 1
    reporte_pdf = models.FileField(storage=ReportesPDFStorage(), upload_to='reportes/', blank=True, null=True)
    
    # Almacenamiento en Azure Blob Storage - Contenedor 2
    imagen_medica = models.ImageField(storage=ImagenesMedicasStorage(), upload_to='imagenes/', blank=True, null=True)

    def __str__(self):
        return f"Examen de {self.paciente.nombre} - {self.fecha}"