from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from .views import (
    DepartamentoViewSet, CargoViewSet, EmpleadoViewSet, NominaViewSet,
    NovedadViewSet, InformacionPersonalViewSet, EmpleadosNominaViewSet,
    ContarEmpleadosViewSet, CargosYPensionViewSet, ConteoEPSViewSet,
    ConteoPensionViewSet, ContarEmpleadosPorCargo, ContarEmpleadosPorDependencia,
    ListaEmpleadosCargoASCViewSet, ListaEmpleadosEPSASCViewSet, ListaEmpleadosNombreASCViewSet, ListaEmpleadosNombreDESCViewSet,

)

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet, 'departamentos')
router.register(r'cargos', CargoViewSet, 'cargos')
router.register(r'empleados', EmpleadoViewSet, 'empleados')
router.register(r'nominas', NominaViewSet, 'nominas')
router.register(r'novedades', NovedadViewSet, 'novedades')

# Custom endpoints
router.register(r'informacion-personal', InformacionPersonalViewSet, basename='informacion-personal')
router.register(r'empleados-nomina', EmpleadosNominaViewSet, basename='empleados-nomina')
router.register(r'total-empleados', ContarEmpleadosViewSet, basename='total-empleados')
router.register(r'cargos-pension', CargosYPensionViewSet, basename='cargos-pension')
router.register(r'conteo-eps', ConteoEPSViewSet, basename='conteo-eps')
router.register(r'conteo-pension', ConteoPensionViewSet, basename='conteo-pension')
router.register(r'conteo-empleados-por-cargo', ContarEmpleadosPorCargo, basename='conteo-empleados-por-cargo')
router.register(r'conteo-empleados-por-dependencia', ContarEmpleadosPorDependencia, basename='conteo-empleados-por-dependencia')
router.register(r'lista-empleados-por-cargoASC', ListaEmpleadosCargoASCViewSet, basename='lista-empleados-por-cargoASC')
router.register(r'lista-empleados-por-EPSASC', ListaEmpleadosEPSASCViewSet, basename='lista-empleados-por-EPSASC')
router.register(r'lista-empleados-por-nombreASC', ListaEmpleadosNombreASCViewSet, basename='lista-empleados-por-nombreASC')
router.register(r'lista-empleados-por-nombreDESC', ListaEmpleadosNombreDESCViewSet, basename='lista-empleados-por-nombreDESC')


urlpatterns = [
    path('api/empleados/', include(router.urls)),
    path('docs/', include_docs_urls(title="Empleados API")),
]
