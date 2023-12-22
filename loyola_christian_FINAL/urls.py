"""
URL configuration for loyola_christian_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from seminario_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    # Formulario basado en clases
    path('inscrito/agregar/', views.AgregarInscritoView.as_view(), name='agregar-inscrito'),
    # Formulario basado en funciones
    path('institucion/agregar/', views.agregar_institucion, name='agregar-institucion'),
    # Class Based View del modelo Inscrito
    path('inscrito_lista/', views.InscritoList.as_view(), name='inscrito-lista'),
    path('inscrito_lista/<int:id>/', views.InscritoDetalle.as_view(), name='inscrito-detalle'),
    # Function Based View de modelo Institución
    path('institucion_lista/', views.institucion_lista, name='institucion-lista'),
    path('institucion_lista/<int:id>/', views.institucion_detalle, name='institucion-detalle'),
    # Datos del autor
    path('autor/', views.autorJson, name='autor-json'),
]