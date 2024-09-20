from modules.Ejercicio1a import listadesordenada
from modules.Ejercicio1b import OrdenamientoQuicksort
from modules.Ejercicio1c import RadixSort
import matplotlib.pyplot as plt
import time
import random

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

def medir_tiemposra():
    tamaños = list(range(1, 1001))  # Tamaños de la lista de 1 a 1000
    tiempos_radix = []
    tiempos_sorted = []

    for tamaño in tamaños:
        # Generar lista de números aleatorios
        lista = [random.randint(10000, 99999) for _ in range(tamaño)]

        # Medir tiempo para Radix Sort
        radix_sort = RadixSort()
        for numero in lista:
            radix_sort.agregar_elemento(numero)
        
        start_time = time.time()
        radix_sort.ordenar()
        end_time = time.time()
        tiempos_radix.append(end_time - start_time)

        # Medir tiempo para sorted()
        start_time = time.time()
        sorted(lista)
        end_time = time.time()
        tiempos_sorted.append(end_time - start_time)

    # Graficar resultados
    plt.figure(figsize=(12, 6))
    plt.plot(tamaños, tiempos_radix, label='Radix Sort', color='blue')
    plt.plot(tamaños, tiempos_sorted, label='sorted()', color='red')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Tiempo de Ejecución vs Tamaño de la Lista')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    medir_tiemposra()

    
def medir_tiempos_burbuja():
    tamaños = list(range(1, 1001))  # Tamaños de la lista de 1 a 1000
    tiempos_burbuja = []
    tiempos_sorted = []

    for tamaño in tamaños:
        # Generar lista de números aleatorios
        lista = [random.randint(10000, 99999) for _ in range(tamaño)]

        # Medir tiempo para OrdenamientoBurbuja
        burbuja = OrdenamientoBurbuja()
        for numero in lista:
            burbuja.agregar_elemento(numero)
        
        start_time = time.time()
        burbuja.ordenar()
        end_time = time.time()
        tiempos_burbuja.append(end_time - start_time)

        # Medir tiempo para sorted()
        start_time = time.time()
        sorted(lista)
        end_time = time.time()
        tiempos_sorted.append(end_time - start_time)

    # Graficar resultados
    plt.figure(figsize=(12, 6))
    plt.plot(tamaños, tiempos_burbuja, label='Ordenamiento Burbuja', color='blue')
    plt.plot(tamaños, tiempos_sorted, label='sorted()', color='red')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Tiempo de Ejecución vs Tamaño de la Lista')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    medir_tiempos_burbuja()