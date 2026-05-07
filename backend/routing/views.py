from rest_framework.decorators import api_view
from rest_framework.response import Response

from routing.data.roads import ROADS
from routing.services.routing_service import RoutingService


@api_view(['GET'])
def ciudades(request):

    return Response(list(ROADS.keys()))


@api_view(['POST'])
def resolver_ruta(request):

    origen = request.data.get("origen")
    destino = request.data.get("destino")

    resultado = RoutingService.resolver(
        origen,
        destino
    )

    return Response(resultado)