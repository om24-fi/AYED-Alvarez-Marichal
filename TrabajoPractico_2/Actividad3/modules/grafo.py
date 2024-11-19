import sys

class Vertice:
    """Define un vértice con conexiones a otros vértices y distancia inicial infinita."""
    def __init__(self, nombre):
        self._nombre = nombre
        self._conexiones = {}
        self._distancia = sys.maxsize
        self._predecesor = None

    def agregar_conexion(self, vertice, ponderacion):
        self._conexiones[vertice] = ponderacion

    def obtener_conexiones(self):
        return self._conexiones.keys()

    def obtener_ponderacion(self, vertice):
        return self._conexiones[vertice]

    @property
    def distancia(self):
        return self._distancia

    @distancia.setter
    def distancia(self, dist):
        self._distancia = dist

    @property
    def predecesor(self):
        return self._predecesor

    @predecesor.setter
    def predecesor(self, predecesor):
        self._predecesor = predecesor

    def obtener_nombre(self):
        return self._nombre

class Grafo:
    """Define un grafo como un conjunto de vértices y aristas no dirigidas."""
    def __init__(self):
        self._vertices = {}

    def agregar_vertice(self, nombre):
        vertice = Vertice(nombre)
        self._vertices[nombre] = vertice
        return vertice

    def obtener_vertice(self, nombre):
        return self._vertices.get(nombre, None)

    def agregar_arista(self, desde, hasta, peso):
        if desde not in self._vertices:
            self.agregar_vertice(desde)
        if hasta not in self._vertices:
            self.agregar_vertice(hasta)
        self._vertices[desde].agregar_conexion(self._vertices[hasta], peso)
        self._vertices[hasta].agregar_conexion(self._vertices[desde], peso)

def cargar_grafo(desde_archivo):
    """Carga un grafo desde un archivo donde cada línea representa una arista con peso."""
    grafo = Grafo()
    with open(desde_archivo, 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(', ')
            if len(datos) == 3:
                desde, hasta, distancia = datos
                grafo.agregar_arista(desde, hasta, int(distancia))
    return grafo

