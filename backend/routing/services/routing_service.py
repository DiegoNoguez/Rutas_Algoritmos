from routing.algorithms.bfs import bfs
from routing.algorithms.dfs import dfs_iterativo
from routing.algorithms.ucs import ucs

from routing.data.roads import ROADS


class RoutingService:

    @staticmethod
    def resolver(origen, destino):

        return {

            "bfs": bfs(
                ROADS,
                origen,
                destino
            ),

            "dfs": dfs_iterativo(
                ROADS,
                origen,
                destino
            ),

            "ucs": ucs(
                ROADS,
                origen,
                destino
            )
        }