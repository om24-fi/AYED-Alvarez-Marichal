import time
import matplotlib.pyplot as plt
from modules.listadoblementeenlazada import ListaDobleEnlazada

# Aplicación secundaria
def medir_tiempos(N):
    lista = ListaDobleEnlazada()

    # Rellenar la lista con N elementos
    for i in range(N):
        lista.agregar_al_final(i)

    # Medir el tiempo de __len__
    start_time = time.time()
    len(lista)
    len_time = time.time() - start_time

    # Medir el tiempo de copiar
    start_time = time.time()
    lista.copiar()
    copy_time = time.time() - start_time

    # Medir el tiempo de invertir
    start_time = time.time()
    lista.invertir()
    invert_time = time.time() - start_time

    return len_time, copy_time, invert_time

# Valores de N a evaluar
valores_N = [100, 500, 1000, 5000, 10000, 50000]

# Almacenar los resultados
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

# Ejecutar las mediciones para cada valor de N
for N in valores_N:
    len_time, copy_time, invert_time = medir_tiempos(N)
    tiempos_len.append(len_time)
    tiempos_copiar.append(copy_time)
    tiempos_invertir.append(invert_time)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(valores_N, tiempos_len, label='len()')
plt.plot(valores_N, tiempos_copiar, label='copiar()')
plt.plot(valores_N, tiempos_invertir, label='invertir()')
plt.xlabel('N (Cantidad de elementos)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('N vs Tiempo de ejecución')
plt.legend()
plt.grid(True)
plt.show()