from django.contrib import admin
from .models import Task
from .models import Departamento, Cargo, Empleado, Nomina, Novedad

# Register your models here.
admin.site.register(Task)
admin.site.register(Departamento)
admin.site.register(Cargo)
admin.site.register(Empleado)
admin.site.register(Nomina)
admin.site.register(Novedad)
