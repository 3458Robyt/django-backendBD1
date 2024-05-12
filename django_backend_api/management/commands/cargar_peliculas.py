import sys
import os

# Agregar la ruta al directorio que contiene 'productos' al sys.path
productos_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'productos'))
if productos_path not in sys.path:
    sys.path.append(productos_path)

# Ahora puedes importar cargar_peliculas_desde_dat desde productos.utils
from productos.utils import cargar_peliculas_desde_dat
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Carga películas desde un archivo .dat'

    def add_arguments(self, parser):
        parser.add_argument('ruta_archivo', type=str, help='Ruta al archivo .dat')

    def handle(self, *args, **kwargs):
        ruta_archivo = kwargs['ruta_archivo']
        cargar_peliculas_desde_dat(ruta_archivo)
        self.stdout.write(self.style.SUCCESS('¡Se han cargado las películas correctamente!'))
