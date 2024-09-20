import random
import time
import matplotlib.pyplot as plt

class RadixSort:
    """
    Esta clase encapsula un algoritmo de ordenamiento Radix Sort.
    Proporciona métodos para agregar elementos a una lista, ordenar la lista
    usando Radix Sort y obtener la lista ordenada.
    """

    def __init__(self):
        """Inicializa una instancia de RadixSort con una lista vacía."""
        self.lista = []

    def agregar_elemento(self, elemento):
        """
        Agrega un elemento entero a la lista.
        Si el tipo del elemento no es válido, lanza un TypeError.

        :param elemento: Elemento a agregar (int)
        """
        if not isinstance(elemento, int):
            raise TypeError("Solo se pueden agregar enteros a la lista.")
        self.lista.append(elemento)

    def _maximo(self):
        """Encuentra el valor máximo en la lista."""
        return max(self.lista) if self.lista else 0

    def _contar(self, exp):
        """
        Contar el número de ocurrencias de los dígitos en cada posición.

        :param exp: El exponente de 10 que indica la posición del dígito a contar.
        """
        n = len(self.lista)
        output = [0] * n
        count = [0] * 10

        # Contar ocurrencias
        for i in range(n):
            index = (self.lista[i] // exp) % 10
            count[index] += 1

        # Cambiar count[i] para que contenga la posición final de este dígito en output[]
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Construir la lista de salida
        i = n - 1
        while i >= 0:
            index = (self.lista[i] // exp) % 10
            output[count[index] - 1] = self.lista[i]
            count[index] -= 1
            i -= 1

        # Copiar el output[] a lista[]
        for i in range(n):
            self.lista[i] = output[i]

    def ordenar(self):
        """
        Ordena la lista en orden ascendente usando el algoritmo de Radix Sort.
        Si la lista está vacía, lanza un ValueError.
        """
        if not self.lista:
            raise ValueError("No se puede ordenar una lista vacía.")

        # Encuentra el máximo número para saber el número de dígitos
        max_num = self._maximo()

        # Ordenar por cada dígito
        exp = 1
        while max_num // exp > 0:
            self._contar(exp)
            exp *= 10

    def obtener_lista(self):
        """
        Retorna la lista ordenada. Si la lista está vacía, lanza un ValueError.
        
        :return: Lista de elementos
        """
        if not self.lista:
            raise ValueError("La lista está vacía.")
        
        return self.lista

def medir_tiempos():
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
    medir_tiempos()


#Aqui la parte: de corroborar con una lista de datos

listadesordenada=RadixSort()
for num in range(500):
    x=random.randint(10000,99999)
    listadesordenada.agregar_elemento(x)
z=listadesordenada.obtener_lista()
print(f"la lista desordenada es: {z}")
listadesordenada.ordenar()
z=listadesordenada.obtener_lista()
print(f"la lista ordenada ahora es {z}")
