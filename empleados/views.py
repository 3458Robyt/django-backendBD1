from rest_framework import viewsets
from rest_framework.response import Response
from django.db import connection
from rest_framework.views import APIView
from .serializers import (
    DepartamentoSerializer, CargoSerializer, EmpleadoSerializer,
    NominaSerializer, NovedadSerializer
)
from .models import Departamento, Cargo, Empleado, Nomina, Novedad
from django_filters.rest_framework import DjangoFilterBackend

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
        'Cedula': ['gte', 'lte'],
    }

class NominaViewSet(viewsets.ModelViewSet):
    queryset = Nomina.objects.all()
    serializer_class = NominaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'FechaIngreso': ['gte', 'lte'],
        'Empleado': ['exact'],
    }

class NovedadViewSet(viewsets.ModelViewSet):
    queryset = Novedad.objects.all()
    serializer_class = NovedadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'Fecha': ['gte', 'lte'],
        'Empleado': ['exact'],
    }

class InformacionPersonalViewSet(viewsets.ViewSet):
    def list(self, request):
        with connection.cursor() as cursor:
            cursor.callproc("informacion_personal")
            resultados = cursor.fetchall()
        data = self.procesar_resultados(resultados)
        return Response(data)

    def retrieve(self, request, pk=None):
        with connection.cursor() as cursor:
            cursor.callproc("informacion_personal_por_id", [pk])
            resultados = cursor.fetchall()
        data = self.procesar_resultados(resultados)
        return Response(data)

    def procesar_resultados(self, resultados):
        processed_data = []
        for resultado in resultados:
            processed_data.append({
                'empleado_id': resultado[0],
                'nombre': resultado[1],
                'apellido': resultado[2],
                'nombre_departamento': resultado[3],
                'nombre_cargo': resultado[4],
                'fecha_ingreso': resultado[5],
                'eps': resultado[6],
                'fondo_pension': resultado[7],
                'sueldo': resultado[8],
                'descripcion_novedad': resultado[9],
                'fecha_novedad': resultado[10]
            })
        return processed_data

class EmpleadosNominaViewSet(viewsets.ViewSet):
    def list(self, request):
        with connection.cursor() as cursor:
            cursor.execute("CALL listar_empleados")
            resultados = cursor.fetchall()
        data = self.procesar_resultados(resultados)
        return Response(data)

    def procesar_resultados(self, resultados):
        processed_data = []
        for resultado in resultados:
            processed_data.append({
                'empleado_id': resultado[0],
                'nombre': resultado[1],
                'apellido': resultado[2],
                'nombre_cargo': resultado[3],
                'nombre_departamento': resultado[4]
            })
        return processed_data

class ContarEmpleadosViewSet(viewsets.ViewSet):
    def list(self, request):
        with connection.cursor() as cursor:
            cursor.execute("CALL contar_empleados")
            resultados = cursor.fetchall()
        data = self.procesar_resultados(resultados)
        return Response(data)

    def procesar_resultados(self, resultados):
        processed_data = []
        for resultado in resultados:
            processed_data.append({
                'total_empleados': resultado[0]
            })
        return processed_data

class CargosYPensionViewSet(viewsets.ViewSet):
    def list(self, request):
        with connection.cursor() as cursor:
            cursor.execute("CALL PensionYCargo")
            resultados = cursor.fetchall()
        data = self.procesar_resultados(resultados)
        return Response(data)

    def procesar_resultados(self, resultados):
        processed_data = []
        for resultado in resultados:
            processed_data.append({
                'empleado_id': resultado[0],
                'nombre': resultado[1],
                'apellido': resultado[2],
                'nombre_cargo': resultado[3],
                'fondo_pension': resultado[4]
            })
        return processed_data

class ConteoEPSViewSet(viewsets.ViewSet):
    def list(self, request):
        with connection.cursor() as cursor:
            cursor.execute("CALL Conteo_EPS")
            resultados = cursor.fetchall()
        data = self.procesar_resultados(resultados)
        return Response(data)

    def procesar_resultados(self, resultados):
        processed_data = []
        for resultado in resultados:
            processed_data.append({
                'EPS': resultado[0],
                'total_afiliados': resultado[1],
            })
        return processed_data

class ConteoPensionViewSet(viewsets.ViewSet):
    def list(self, request):
        with connection.cursor() as cursor:
            cursor.execute("CALL Conteo_Pension")
            resultados = cursor.fetchall()
        data = self.procesar_resultados(resultados)
        return Response(data)

    def procesar_resultados(self, resultados):
        processed_data = []
        for resultado in resultados:
            processed_data.append({
                'entidad_pension': resultado[0],
                'total_afiliados': resultado[1],
            })
        return processed_data

class ContarEmpleadosPorDependencia(viewsets.ViewSet):
    def list(self, request):
        with connection.cursor() as cursor:
            cursor.callproc('contar_empleados_por_dependencia')
            results = cursor.fetchall()
        data = [{'departamento': row[0], 'cantidad': row[1]} for row in results]
        return Response(data)

class ContarEmpleadosPorCargo(viewsets.ViewSet):
    def list(self, request):
        with connection.cursor() as cursor:
            cursor.callproc('contar_empleados_por_cargo')
            results = cursor.fetchall()
        data = [{'cargo': row[0], 'cantidad': row[1]} for row in results]
        return Response(data)
