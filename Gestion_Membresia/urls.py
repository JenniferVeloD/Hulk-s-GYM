from django.urls import path 
from . import views 

urlpatterns = [
        path('agregar-categoria/', views.agregar_membresia, name='agregar_membresia'),
        path('editar-membresia/', views.editar_membresia, name='editar_membresia'),
        path('eliminar-categoria/', views.eliminar_membresia, name='eliminar_membresia')
        ]
"""
Urls para añadir una nueva membresía, editar membresia y eliminar membresia
"""
