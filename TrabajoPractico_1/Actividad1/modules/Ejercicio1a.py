import random
import time
import matplotlib.pyplot as plt

class OrdenamientoBurbuja:
    """
    Esta clase encapsula una lista y provee métodos para agregar elementos,
    ordenar la lista usando el algoritmo de burbuja y obtener la lista.
    """

    def __init__(self):
        """Inicializa una instancia de OrdenamientoBurbuja con una lista vacía."""
        self.lista = []

    def agregar_elemento(self, elemento):
        """
        Agrega un elemento (entero, flotante o cadena) a la lista.
        Si el tipo del elemento no es válido, lanza un TypeError.

        :param elemento: Elemento a agregar (int, float, str)
        """
        if not isinstance(elemento, (int, float, str)):
            raise TypeError("Solo se pueden agregar enteros, flotantes o cadenas de texto a la lista.")
        
        self.lista.append(elemento)

    def ordenar(self):
        """
        Ordena la lista en orden ascendente (de menor a mayor) usando el algoritmo de burbuja.
        Si la lista está vacía, lanza un ValueError.
        """
        if not self.lista:
            raise ValueError("No se puede ordenar una lista vacía.")

        for numPasada in range(len(self.lista) - 1):
            for i in range(len(self.lista) - 1 - numPasada):
                if isinstance(self.lista[i], (int, float)) and isinstance(self.lista[i + 1], (int, float)):
                    if self.lista[i] > self.lista[i + 1]:
                        self.lista[i], self.lista[i + 1] = self.lista[i + 1], self.lista[i]
                elif isinstance(self.lista[i], str) and isinstance(self.lista[i + 1], str):
                    if self.lista[i].lower() > self.lista[i + 1].lower():
                        self.lista[i], self.lista[i + 1] = self.lista[i + 1], self.lista[i]
                else:
                    raise TypeError("La lista contiene elementos de tipos incompatibles para la comparación.")

    def obtener_lista(self):
        """
        Retorna la lista ordenada. Si la lista está vacía, lanza un ValueError.
        
        :return: Lista de elementos
        """
        if not self.lista:
            raise ValueError("La lista está vacía.")
        
        return self.lista

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


#Aqui la parte: de corroborar con una lista de datos

listadesordenada=OrdenamientoBurbuja()
for num in range(500):
    x=random.randint(10000,99999)
    listadesordenada.agregar_elemento(x)
z=listadesordenada.obtener_lista()
print(f"la lista desordenada es: {z}")
listadesordenada.ordenar()
z=listadesordenada.obtener_lista()
print(f"la lista ordenada ahora es {z}")
