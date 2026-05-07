from .nodo import Nodo


def dfs_limitado(
    conexiones,
    nodo,
    objetivo,
    visitados,
    limite
):

    if limite <= 0:
        return None

    visitados.append(nodo.get_datos())

    if nodo.get_datos() == objetivo:
        return nodo

    for ciudad in conexiones[nodo.get_datos()].keys():

        hijo = Nodo(ciudad)

        hijo.set_padre(nodo)

        if ciudad not in visitados:

            solucion = dfs_limitado(
                conexiones,
                hijo,
                objetivo,
                visitados,
                limite - 1
            )

            if solucion:
                return solucion

    return None


def dfs_iterativo(conexiones, inicio, objetivo):

    for limite in range(1, 50):

        visitados = []

        nodo_inicial = Nodo(inicio)

        solucion = dfs_limitado(
            conexiones,
            nodo_inicial,
            objetivo,
            visitados,
            limite
        )

        if solucion:

            ruta = []

            while solucion:
                ruta.append(solucion.get_datos())
                solucion = solucion.get_padre()

            ruta.reverse()

            return {
                "ruta": ruta,
                "visitados": visitados
            }

    return None