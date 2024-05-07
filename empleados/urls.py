from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet
from .views import DepartamentoViewSet, CargoViewSet, EmpleadoViewSet, NominaViewSet, NovedadViewSet

#Api versioning
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, 'tasks')
router.register(r'departamentos', DepartamentoViewSet, 'departamentos')
router.register(r'cargos', CargoViewSet, 'cargos')
router.register(r'empleados', EmpleadoViewSet, 'empleados')
router.register(r'nominas', NominaViewSet, 'nominas')
router.register(r'novedades', NovedadViewSet, 'novedades')

urlpatterns = [
    path('api/empleados/', include(router.urls)),
]