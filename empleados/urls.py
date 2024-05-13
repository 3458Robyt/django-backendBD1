from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import TaskViewSet
from .views import DepartamentoViewSet, CargoViewSet, EmpleadoViewSet, NominaViewSet, NovedadViewSet, InformacionPersonalViewSet


#Api versioning
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, 'tasks')
router.register(r'departamentos', DepartamentoViewSet, 'departamentos')
router.register(r'cargos', CargoViewSet, 'cargos')
router.register(r'empleados', EmpleadoViewSet, 'empleados')
router.register(r'nominas', NominaViewSet, 'nominas')
router.register(r'novedades', NovedadViewSet, 'novedades')
router.register(r'aa', InformacionPersonalViewSet, 'aa')



urlpatterns = [
    path('api/empleados/', include(router.urls)),
    path('docs/', include_docs_urls(title="Tasks API"))
]
