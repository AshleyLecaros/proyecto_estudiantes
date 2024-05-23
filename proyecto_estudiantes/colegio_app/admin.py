from django.contrib import admin
from .models import Estudiante, Curso, Profesor, Direccion

# Register your models here.

class ProfesorAdmin(admin.ModelAdmin):
    fields = ['rut', 'nombre', 'apellido', 'activo', 'fecha_registro', 'fecha_modificacion', 'creado_por'] 
    readonly_fields = ['fecha_registro', 'fecha_modificacion']
    
class EstudianteAdmin(admin.ModelAdmin):
    fields = ['rut', 'nombre', 'apellido', 'fecha_nacimiento', 'activo', 'fecha_registro', 'fecha_modificacion', 'creado_por']
    readonly_fields = ['fecha_registro', 'fecha_modificacion']
    
class DireccionAdmin(admin.ModelAdmin): 
    fields = ['direccion_id', 'calle', 'numero', 'departamento', 'comuna', 'ciudad', 'region', 'estudiante']
    
class CursoAdmin(admin.ModelAdmin):
    fields = ['codigo', 'nombre', 'version', 'profesor']
    
admin.site.register(Curso, CursoAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Direccion, DireccionAdmin)
 
    
    
     
    
