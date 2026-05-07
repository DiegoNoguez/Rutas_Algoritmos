from .nodo import Nodo


def ucs(conexiones, inicio, objetivo):

    visitados = []
    frontera = []

    nodo_inicial = Nodo(inicio)
    nodo_inicial.set_costo(0)

    frontera.append(nodo_inicial)

    while frontera:

        frontera = sorted(
            frontera,
            key=lambda x: x.get_costo()
        )

        nodo = frontera.pop(0)

        visitados.append(nodo.get_datos())

        if nodo.get_datos() == objetivo:

            ruta = []

            costo = nodo.get_costo()

            while nodo:
                ruta.append(nodo.get_datos())
                nodo = nodo.get_padre()

            ruta.reverse()

            return {
                "ruta": ruta,
                "visitados": visitados,
                "costo": costo
            }

        if nodo.get_datos() not in conexiones:
            continue

        for ciudad, distancia in conexiones[nodo.get_datos()].items():

            hijo = Nodo(ciudad)

            hijo.set_padre(nodo)

            nuevo_costo = nodo.get_costo() + distancia

            hijo.set_costo(nuevo_costo)

            if ciudad not in visitados:
                frontera.append(hijo)

    return {
        "ruta": [],
        "visitados": visitados,
        "costo": 0
    }