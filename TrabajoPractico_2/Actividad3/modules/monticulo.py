import math

class MonticuloBinario:
    """Define un montículo binario mínimo para organizar vértices según su distancia."""
    def __init__(self):
        self._lista_monticulo = [-math.inf]
        self._tamano_actual = 0

    def _infilt_arriba(self, i):
        while i // 2 > 0:
            if self._lista_monticulo[i].distancia < self._lista_monticulo[i // 2].distancia:
                self._lista_monticulo[i], self._lista_monticulo[i // 2] = self._lista_monticulo[i // 2], self._lista_monticulo[i]
            i = i // 2

    def insertar(self, vertice):
        self._lista_monticulo.append(vertice)
        self._tamano_actual += 1
        self._infilt_arriba(self._tamano_actual)

    def _infilt_abajo(self, i):
        while (i * 2) <= self._tamano_actual:
            hm = self._hijo_min(i)
            if self._lista_monticulo[i].distancia > self._lista_monticulo[hm].distancia:
                self._lista_monticulo[i], self._lista_monticulo[hm] = self._lista_monticulo[hm], self._lista_monticulo[i]
            i = hm

    def _hijo_min(self, i):
        if i * 2 + 1 > self._tamano_actual:
            return i * 2
        else:
            return i * 2 if self._lista_monticulo[i * 2].distancia < self._lista_monticulo[i * 2 + 1].distancia else i * 2 + 1

    def eliminar_min(self):
        if self.esta_vacio():
            raise ValueError("El montículo está vacío.")
        valor_sacado = self._lista_monticulo[1]
        self._lista_monticulo[1] = self._lista_monticulo[self._tamano_actual]
        self._tamano_actual -= 1
        self._lista_monticulo.pop()
        self._infilt_abajo(1)
        return valor_sacado

    def construir_monticulo(self, lista):
        """Construye el montículo inicial a partir de una lista de vértices."""
        self._tamano_actual = len(lista)
        self._lista_monticulo = [0] + lista[:]
        for i in range(self._tamano_actual // 2, 0, -1):
            self._infilt_abajo(i)

    def esta_vacio(self):
        return self._tamano_actual == 0

    def buscar_min(self):
        if self.esta_vacio():
            return None
        return self._lista_monticulo[1]

    def tamano(self):
        return self._tamano_actual

    def actualizar_distancia(self, vertice, nueva_distancia):
        """Actualiza la distancia de un vértice y ajusta su posición en el montículo."""
        for i in range(1, self._tamano_actual + 1):
            if self._lista_monticulo[i] == vertice:
                vertice.distancia = nueva_distancia
                self._infilt_arriba(i)
                break
