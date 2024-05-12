import os
from django.db import transaction
from .models import Pelicula, GeneroPelicula, PeliculaGenero

def cargar_peliculas_desde_dat(ruta_archivo):
    peliculas_a_crear = []
    pelicula_generos_a_crear = []

    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    with transaction.atomic():
        for linea in lineas:
            datos = linea.strip().split('::')
            pelicula_id = int(datos[0])
            titulo_anio = datos[1].rsplit(' (', 1)
            titulo = titulo_anio[0].strip()
            anio_lanzamiento = int(titulo_anio[1][:-1])

            # Crear instancia de Pelicula y añadir a la lista
            pelicula = Pelicula(titulo=titulo, anio_lanzamiento=anio_lanzamiento)
            peliculas_a_crear.append(pelicula)

        # Usar bulk_create para crear todas las instancias de Pelicula
        Pelicula.objects.bulk_create(peliculas_a_crear)

        # Recuperar todas las instancias de Pelicula recién creadas
        peliculas_creadas = Pelicula.objects.filter(titulo__in=[pelicula.titulo for pelicula in peliculas_a_crear])

        # Crear instancias de PeliculaGenero asociadas a las Peliculas
        for pelicula, linea in zip(peliculas_creadas, lineas):
            datos = linea.strip().split('::')
            generos = datos[2].split('|')
            for genero in generos:
                genero_obj, _ = GeneroPelicula.objects.get_or_create(nombre_genero=genero)
                pelicula_genero = PeliculaGenero(pelicula=pelicula, genero=genero_obj)
                pelicula_generos_a_crear.append(pelicula_genero)

        # Usar bulk_create para crear todas las instancias de PeliculaGenero
        PeliculaGenero.objects.bulk_create(pelicula_generos_a_crear)

    print(f"Se han cargado {len(lineas)} películas desde el archivo .dat.")
