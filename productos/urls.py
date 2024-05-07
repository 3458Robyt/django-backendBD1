from django.urls import path, include
from rest_framework import routers
from .views import PeliculaViewSet, GeneroLibroViewSet, GeneroPeliculaViewSet, LibroViewSet, LibroAutorViewSet, LibroGeneroViewSet, AutorViewSet, PeliculaGeneroViewSet

router = routers.DefaultRouter()
router.register(r'peliculas', PeliculaViewSet, 'peliculas')
router.register(r'generoslibro', GeneroLibroViewSet, 'generoslibro')
router.register(r'generospelicula', GeneroPeliculaViewSet, 'generospelicula')
router.register(r'libros', LibroViewSet, 'libros')
router.register(r'libroautores', LibroAutorViewSet, 'libroautores')
router.register(r'librogeneros', LibroGeneroViewSet, 'librogeneros')
router.register(r'autores', AutorViewSet, 'autores')
router.register(r'peliculageneros', PeliculaGeneroViewSet, 'peliculageneros')

urlpatterns = [
    path('api/productos/', include(router.urls)),
]