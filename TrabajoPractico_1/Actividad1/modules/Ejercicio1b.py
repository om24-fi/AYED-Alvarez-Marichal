import random

class OrdenamientoQuicksort:
    def __init__(self):
        self.lista = []

    def agregar_elemento(self, elemento):
        if not isinstance(elemento, int):
            raise TypeError("Solo se pueden agregar enteros a la lista.")
        self.lista.append(elemento)

    def quicksort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[len(lista) // 2]
        menor = [x for x in lista if x < pivote]
        medio = [x for x in lista if x == pivote]
        mayor = [x for x in lista if x > pivote]
        return self.quicksort(menor) + medio + self.quicksort(mayor)

    def obtener_lista(self):
        if not self.lista:
            raise ValueError("No se puede ordenar una lista vacía.")
        sorted_list = self.quicksort(self.lista)
        return sorted_list

#Aqui la parte: de corroborar con una lista de datos

listadesordenada=OrdenamientoQuicksort()
for num in range(500):
    x=random.randint(10000,99999)
    listadesordenada.agregar_elemento(x)
z=listadesordenada.obtener_lista()
print(f"la lista desordenada es: {z}")
listadesordenada.quicksort(z)
y=listadesordenada.obtener_lista()
print(f"la lista ordenada ahora es {y}")
