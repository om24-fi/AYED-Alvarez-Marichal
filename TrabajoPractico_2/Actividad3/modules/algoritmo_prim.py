import sys
from .monticulo import MonticuloBinario

def prim(grafo, inicio_nombre):
    """Implementa el algoritmo de Prim para encontrar el árbol de expansión mínima desde un vértice inicial."""
    inicio = grafo.obtener_vertice(inicio_nombre)
    if not inicio:
        raise ValueError("La aldea de inicio no existe en el grafo")

    cp = MonticuloBinario()
    for vertice in grafo._vertices.values():
        vertice.distancia = sys.maxsize
        vertice.predecesor = None
    inicio.distancia = 0

    cp.construir_monticulo(list(grafo._vertices.values()))

    while not cp.esta_vacio():
        vertice_actual = cp.eliminar_min()
        for vecino in vertice_actual.obtener_conexiones():
            nuevo_costo = vertice_actual.obtener_ponderacion(vecino)
            if vecino.distancia > nuevo_costo:
                vecino.predecesor = vertice_actual
                cp.actualizar_distancia(vecino, nuevo_costo)

    return {vertice.obtener_nombre(): vertice.predecesor for vertice in grafo._vertices.values()}

def calcular_sumas_distancias(grafo, mst):
    """Calcula y retorna las distancias de cada aldea a su predecesor en el MST y la suma total."""
    suma_distancias = {}
    for aldea, predecesor in mst.items():
        if predecesor:
            distancia = grafo.obtener_vertice(predecesor.obtener_nombre()).obtener_ponderacion(grafo.obtener_vertice(aldea))
            suma_distancias[aldea] = distancia
    total_suma = sum(suma_distancias.values())
    return suma_distancias, total_suma
