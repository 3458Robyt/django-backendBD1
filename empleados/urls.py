from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import TaskViewSet
from .views import DepartamentoViewSet, CargoViewSet, EmpleadoViewSet, NominaViewSet, NovedadViewSet, InformacionPersonalViewSet, EmpleadosNominaViewSet, ContarEmpleadosViewSet, CargosYPensionViewSet, ConteoEPSViewSet, ConteoPensionViewSet


#Api versioning
#CRUD de todas las tablas
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, 'tasks')
router.register(r'departamentos', DepartamentoViewSet, 'departamentos')
router.register(r'cargos', CargoViewSet, 'cargos')
router.register(r'empleados', EmpleadoViewSet, 'empleados')
router.register(r'nominas', NominaViewSet, 'nominas')
router.register(r'novedades', NovedadViewSet, 'novedades')



#Obtener información de los empleados
router.register(r'informacion-personal', InformacionPersonalViewSet, 'informacion-personal')
#Datos importantes Nomina join Empleado
router.register(r'empleados-nomina', EmpleadosNominaViewSet, 'empleados_nomina')
#Conteo cantidad de empleados
router.register(r'total-empleados', ContarEmpleadosViewSet, 'total-empleados')
#Lista empleados cargo y pensión
router.register(r'cargos-pension', CargosYPensionViewSet, 'cargos-pension')
#Conteo eps
router.register(r'conteo-eps', ConteoEPSViewSet, 'conteo-eps')
#Conteo Pension
router.register(r'conteo-pension', ConteoPensionViewSet, 'conteo-pension')





urlpatterns = [
    path('api/empleados/', include(router.urls)),
    path('docs/', include_docs_urls(title="Tasks API"))
]
