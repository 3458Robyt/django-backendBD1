import os
import json
from .models import Pelicula, GeneroPelicula, PeliculaGenero
from datetime import datetime
from django.db import transaction
from .models import Libro, Autor, AutorLibro

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



def parse_date(date_str):
    if not date_str:
        return None
    for fmt in ("%m/%d/%Y", "%m/%Y", "%Y"):
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    return None

def cargar_libros_desde_json(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        datos_libros = json.load(archivo)

    autores_libros_a_crear = []

    with transaction.atomic():
        for datos in datos_libros:
            try:
                numero_paginas = datos.get("num_pages")
                if isinstance(numero_paginas, str) and numero_paginas.isdigit():
                    numero_paginas = int(numero_paginas)
                elif not isinstance(numero_paginas, int):
                    numero_paginas = None

                ratings_count = datos.get("ratings_count")
                if isinstance(ratings_count, str) and ratings_count.isdigit():
                    ratings_count = int(ratings_count)
                elif not isinstance(ratings_count, int):
                    ratings_count = None

                text_reviews_count = datos.get("text_reviews_count")
                if isinstance(text_reviews_count, str) and text_reviews_count.isdigit():
                    text_reviews_count = int(text_reviews_count)
                elif not isinstance(text_reviews_count, int):
                    text_reviews_count = None

                fecha_publicacion = parse_date(datos.get("publication_date"))
                anio_publicacion = fecha_publicacion.year if fecha_publicacion else 1900  # Valor por defecto

                libro = Libro(
                    titulo=datos["title"],
                    isbn=datos.get("isbn"),
                    isbn13=datos.get("isbn13"),
                    codigo_idioma=datos.get("language_code"),
                    numero_paginas=numero_paginas,
                    fecha_publicacion=fecha_publicacion,
                    editorial=datos.get("publisher"),
                    anio_publicacion=anio_publicacion,
                    calificacion=float(datos["average_rating"]) if datos.get("average_rating") else None,
                    promedio_calificacion=None,
                    cantidad_calificaciones=ratings_count,
                    cantidad_resenas=text_reviews_count
                )
                libro.save()  # Guardar el libro primero para usarlo en las relaciones

                autores_nombres = datos["authors"].split(", ")
                for nombre_autor in autores_nombres:
                    if len(nombre_autor) > 100:
                        nombre_autor = nombre_autor[:100]
                    autor, creado = Autor.objects.get_or_create(nombre_autor=nombre_autor)
                    autores_libros_a_crear.append(AutorLibro(libro=libro, autor=autor))

            except ValueError as e:
                print(f"Error al procesar el libro {datos['title']}: {e}")
                continue
            except Exception as e:
                print(f"Error inesperado al procesar el libro {datos['title']}: {e}")
                continue

        AutorLibro.objects.bulk_create(autores_libros_a_crear)

    print(f"Se han cargado libros desde el archivo JSON.")