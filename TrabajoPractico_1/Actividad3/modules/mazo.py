from modules.listadoblementeenlazada import ListaDobleEnlazada
from .carta import Carta

class DequeEmptyError(Exception):
    pass

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()  # Usamos ListaDobleEnlazada para gestionar las cartas

    def poner_carta_arriba(self, carta):
        """Añade una carta al principio del mazo (arriba)."""
        self.cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        """Añade una carta al final del mazo (abajo)."""
        self.cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """Retira la carta que está en la parte superior del mazo.
        Lanza DequeEmptyError si el mazo está vacío."""
        if self.cartas.esta_vacia():
            raise DequeEmptyError("No se puede sacar una carta de un mazo vacío.")
        
        carta = self.cartas.extraer(0)  # Sacamos la primera carta (arriba)
        if mostrar:
            print(f"Se saca la carta: {carta}")
        return carta

    def __len__(self):
        """Devuelve el número de cartas en el mazo."""
        return len(self.cartas)

    def __str__(self):
        """Devuelve la representación del mazo en forma de cadena."""
        return " ".join(str(carta) for carta in self.cartas)  # Mostrar las cartas del mazo
