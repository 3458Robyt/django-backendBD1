from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PeliculaSerializer, GeneroPeliculaSerializer, PeliculaGeneroSerializer, AutorSerializer, LibroSerializer, AutorLibroSerializer
from .models import Pelicula, GeneroPelicula, PeliculaGenero, Autor, Libro, AutorLibro
from rest_framework.response import Response
from django.db import connection

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class GeneroPeliculaViewSet(viewsets.ModelViewSet):
    queryset = GeneroPelicula.objects.all()
    serializer_class = GeneroPeliculaSerializer

class PeliculaGeneroViewSet(viewsets.ModelViewSet):
    queryset = PeliculaGenero.objects.all()
    serializer_class = PeliculaGeneroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class AutorLibroViewSet(viewsets.ModelViewSet):
    queryset = AutorLibro.objects.all()
    serializer_class = AutorLibroSerializer

class PeliculasEnRangoViewSet(viewsets.ViewSet):
    def list(self, request):
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')

        if not fecha_inicio or not fecha_fin:
            return Response({'error': 'Por favor, proporciona una fecha de inicio y una fecha de fin.'}, status=400)

        with connection.cursor() as cursor:
            cursor.callproc("Lista_peliculas_anio", [fecha_inicio, fecha_fin])
            resultados = cursor.fetchall()

        data = self.procesar_resultados(resultados)
        return Response(data)

    def procesar_resultados(self, resultados):
        processed_data = []
        for resultado in resultados:
            processed_data.append({
                'PeliculaID': resultado[0],
                'Titulo': resultado[1],
                'Anio-lanzamiento': resultado[2],
                'NombreGenero': resultado[3]
            })
        return processed_data