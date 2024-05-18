from django.urls import path, include
from rest_framework import routers
from .views import PeliculaViewSet, GeneroPeliculaViewSet, PeliculaGeneroViewSet, AutorViewSet, LibroViewSet, AutorLibroViewSet, PeliculasEnRangoViewSet

router = routers.DefaultRouter()
router.register(r'peliculas', PeliculaViewSet, 'peliculas')
router.register(r'generospelicula', GeneroPeliculaViewSet, 'generospelicula')
router.register(r'peliculageneros', PeliculaGeneroViewSet, 'peliculageneros')
router.register(r'autores', AutorViewSet, 'autores')
router.register(r'libros', LibroViewSet, 'libros')
router.register(r'libroautores', AutorLibroViewSet, 'libroautores')
router.register(r'lista-peliculas-rango', PeliculasEnRangoViewSet, basename='lista-peliculas-rango')

urlpatterns = [
    path('api/productos/', include(router.urls)),
]