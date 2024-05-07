from rest_framework import serializers
from .models import Pelicula, GeneroLibro, GeneroPelicula, Libro, LibroAutor, LibroGenero, Autor, PeliculaGenero

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

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class GeneroLibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroLibro
        fields = '__all__'

class LibroGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroGenero
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroAutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroAutor
        fields = '__all__'
