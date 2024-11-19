from modules.grafo import cargar_grafo
from modules.algoritmo_prim import prim, calcular_sumas_distancias

# Simula la propagación de noticias desde una aldea de inicio a sus vecinas en el MST
def bea_propagacion(grafo, mst, inicio):
    visitados = set()
    cola = [(inicio, None)]
    visitados.add(inicio)
    
    print("Distribución de noticias:")
    while cola:
        actual, predecesor = cola.pop(0)
        if predecesor is None:
            print(f"{actual} es la aldea de inicio.")
        else:
            print(f"{actual} recibe la noticia de: {predecesor}")

        vecinos = [
            vecino.obtener_nombre()
            for vecino in grafo.obtener_vertice(actual).obtener_conexiones()
            if vecino.obtener_nombre() in mst and vecino.obtener_nombre() not in visitados
        ]

        if vecinos:
            print(f"{actual} envía la noticia a: {', '.join(vecinos)}")
        for vecino in vecinos:
            cola.append((vecino, actual))
            visitados.add(vecino)

# Muestra las aldeas en el grafo en orden alfabético
def mostrar_aldeas_alfabeticamente(grafo):
    aldeas_ordenadas = sorted(grafo._vertices.keys())
    print("Aldeas en orden alfabético:")
    for aldea in aldeas_ordenadas:
        print(aldea)

# Ejecución principal: carga el grafo, encuentra el MST, y propaga noticias
def main():
    grafo = cargar_grafo("data/aldeas.txt")
    mostrar_aldeas_alfabeticamente(grafo)
    aldea_inicio = "Peligros"
    mst = prim(grafo, aldea_inicio)

    suma_distancias, total_suma = calcular_sumas_distancias(grafo, mst)
    print("Sumas de distancias para cada aldea:")
    for aldea, distancia in suma_distancias.items():
        print(f"{aldea}: {distancia}")
    print(f"Suma total de distancias: {total_suma}")

    bea_propagacion(grafo, mst, aldea_inicio)

if __name__ == "__main__":
    main()

