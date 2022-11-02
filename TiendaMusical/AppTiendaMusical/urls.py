from django.urls import path

from .views import amplificador, inicio, instrumento, usuario

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('usuario/', usuario, name="Usuario"),
    path('instrumento/', instrumento, name="Instrumento"),
    path('amplificador/', amplificador, name="Amplificador"),
]
