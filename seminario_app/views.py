from .serializers import InscritoSerializer, InstitucionSerializer
from .models import Inscrito, Institucion
from .forms import InscritoForm, InstitucionForm
from django.http import Http404, JsonResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


# AGREGAR index
def index(request):
    return render(request, 'index.html')

# Formulario basado en clases
class AgregarInscritoView(FormView):
    template_name = 'inscrito_form.html'
    form_class = InscritoForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# Formulario basado en funciones
def agregar_institucion(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InstitucionForm()

    return render(request, 'institucion_form.html', {'form': form})


#Datos del autor
def autorJson(request):
    datos = {
        'id' : 1,
        'nombre': 'Christian',
        'apePat' : 'Loyola',
        'apeMat' : 'Soto',
        'asignatura': 'Programación Back End',
        'sección': 'IEI171',
        'ocupación': 'Pilotar el EVA para que Rei no deba hacerlo de nuevo',
    }
    return JsonResponse(datos)


# Vistas basadas en clases para el modelo Inscrito
class InscritoList(APIView):
    def get(self, request):
        inscrit = Inscrito.objects.all()
        serial = InscritoSerializer(inscrit, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial = InscritoSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class InscritoDetalle(APIView):
    def get_object(self, id):
        try:
            return Inscrito.objects.get(pk=id)
        except Inscrito.DoesNotExist:
            return Http404
    
    def get(self, request, id):
        inscrit = self.get_object(id)
        serial = InscritoSerializer(inscrit)
        return Response(serial.data)
    
    def put(self, request, id):
        inscrit = self.get_object(id)
        serial = InscritoSerializer(inscrit, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        inscrit = self.get_object(id)
        inscrit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      

# Vistas basadas en funciones para el modelo Institucion
@api_view(['GET', 'POST'])
def institucion_lista(request):
    if request.method == 'GET':
        institu = Institucion.objects.all()
        serial = InstitucionSerializer(institu, many=True)
        return Response(serial.data)
    
    elif request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detalle(request, id):
    try:
        institu = Institucion.objects.get(pk=id)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(institu)
        return Response(serial.data)
        
    if request.method == 'PUT':
        serial = InstitucionSerializer(institu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        institu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)