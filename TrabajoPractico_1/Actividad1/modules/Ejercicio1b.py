import random
import matplotlib.pyplot as plt
import time

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

def medir_tiempos_quicksort():
    tamaños = list(range(1, 1001))  
    tiempos_quicksort = []
    tiempos_sorted = []

    for tamaño in tamaños:
        
        lista = [random.randint(10000, 99999) for _ in range(tamaño)]

        # Medir tiempo para OrdenamientoQuicksort
        quicksort = OrdenamientoQuicksort()
        for numero in lista:
            quicksort.agregar_elemento(numero)
        
        start_time = time.time()
        quicksort.obtener_lista()
        end_time = time.time()
        tiempos_quicksort.append(end_time - start_time)

        # Medir tiempo para sorted()
        start_time = time.time()
        sorted(lista)
        end_time = time.time()
        tiempos_sorted.append(end_time - start_time)

    # Graficar resultados
    plt.figure(figsize=(12, 6))
    plt.plot(tamaños, tiempos_quicksort, label='Quicksort', color='blue')
    plt.plot(tamaños, tiempos_sorted, label='sorted()', color='red')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Tiempo de Ejecución vs Tamaño de la Lista')
    plt.legend()
    plt.grid(True)
    plt.show()

    
    
if __name__ == "__main__":
    medir_tiempos_quicksort()
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
