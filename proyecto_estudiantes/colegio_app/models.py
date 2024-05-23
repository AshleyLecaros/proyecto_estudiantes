from django.db import models
from django.utils import timezone

# Create your models here.

class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)
    creado_por = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ['nombre', 'apellido', 'rut']
    
class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    activo = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)
    creado_por = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ['nombre', 'apellido', 'rut']
    
class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    departamento = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    region = models.CharField(max_length=50, null=False, blank=False)
    estudiante = models.OneToOneField('estudiante', on_delete=models.CASCADE, related_name='direccion', null=False, blank=False, unique=True)
    
    def __str__(self):
        return f"{self.calle} {self.numero}, {self.comuna}, {self.ciudad}, {self.region}"
    
    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"
        ordering = ['direccion_id']
    
class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True, null=False, blank=False, unique=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    version = models.IntegerField()
    profesor = models.ManyToManyField('profesor', related_name='curso')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['nombre']
    
    
    
    
    
    
    
    
    
    
