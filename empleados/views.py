from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from .serializers import DepartamentoSerializer, CargoSerializer, EmpleadoSerializer, NominaSerializer, NovedadSerializer
from .models import Departamento, Cargo, Empleado, Nomina, Novedad
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from django.db import connection


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


    filter_backends = [DjangoFilterBackend]

    filterset_fields = {
        'Cedula' : ['gte', 'lte'],
    }

class NominaViewSet(viewsets.ModelViewSet):
    queryset = Nomina.objects.all()
    serializer_class = NominaSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'Fecha' : ['gte', 'lte'],
        'Empleado' :['exact'],
    }

class NovedadViewSet(viewsets.ModelViewSet):
    queryset = Novedad.objects.all()
    serializer_class = NovedadSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'Fecha' : ['gte', 'lte'],
        'Empleado' :['exact'],
    }

class InformacionPersonalViewSet(viewsets.ViewSet):
    def list(self, request):
        with connection.cursor() as cursor:
            cursor.execute("CALL informacion_personal()")
            resultados = cursor.fetchall()

        # Procesar los resultados según sea necesario
        # Por ejemplo, formatearlos utilizando un serializador
        data = self.procesar_resultados(resultados)

        return Response(data)

    def procesar_resultados(self, resultados):
        # Procesa los resultados según sea necesario
        # Por ejemplo, formatearlos utilizando un serializador
        processed_data = []
        for resultado in resultados:
            processed_data.append({
                'empleado_id': resultado[0],
                'departamento_id': resultado[1],
                'cargo_id': resultado[2],
                'fecha_ingreso': resultado[3],
                'eps': resultado[4],
                'fondo_pension': resultado[5],
                'sueldo':resultado[6]
            })
        return processed_data