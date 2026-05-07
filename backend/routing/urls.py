from django.urls import path

from .views import (
    ciudades,
    resolver_ruta
)

urlpatterns = [
    path('cities/', ciudades),
    path('solve/', resolver_ruta)
]