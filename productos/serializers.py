from rest_framework import serializers
from .models import Pelicula, GeneroPelicula, PeliculaGenero, Autor, Libro, AutorLibro

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'

class GeneroPeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroPelicula
        fields = '__all__'

class PeliculaGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeliculaGenero
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class AutorLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorLibro
        fields = '__all__'






