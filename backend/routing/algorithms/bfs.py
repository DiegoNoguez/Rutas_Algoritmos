from .nodo import Nodo


def bfs(conexiones, inicio, objetivo):

    visitados = []
    frontera = []

    nodo_inicial = Nodo(inicio)

    frontera.append(nodo_inicial)

    while frontera:

        nodo = frontera.pop(0)

        visitados.append(nodo.get_datos())

        if nodo.get_datos() == objetivo:

            ruta = []

            while nodo:
                ruta.append(nodo.get_datos())
                nodo = nodo.get_padre()

            ruta.reverse()

            return {
                "ruta": ruta,
                "visitados": visitados
            }

        for ciudad in conexiones[nodo.get_datos()].keys():

            hijo = Nodo(ciudad)

            hijo.set_padre(nodo)

            if (
                ciudad not in visitados and
                not hijo.en_lista(frontera)
            ):
                frontera.append(hijo)

    return None