import os
from django.core.management.base import BaseCommand
from productos.utils import cargar_libros_desde_json

class Command(BaseCommand):
    help = 'Carga datos de libros desde un archivo JSON'

    def add_arguments(self, parser):
        parser.add_argument('ruta_archivo', type=str, help='La ruta al archivo JSON con los datos de los libros')

    def handle(self, *args, **kwargs):
        ruta_archivo = kwargs['ruta_archivo']
        
        if not os.path.exists(ruta_archivo):
            self.stdout.write(self.style.ERROR(f'El archivo {ruta_archivo} no existe.'))
            return

        cargar_libros_desde_json(ruta_archivo)
        self.stdout.write(self.style.SUCCESS(f'Se han cargado los libros desde el archivo JSON.'))
