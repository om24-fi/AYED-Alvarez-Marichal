import unittest
from modules.Ejercicio1c import RadixSort  # Asegúrate de que este nombre coincida con el archivo donde está la implementación de RadixSort

class TestRadixSort(unittest.TestCase):
    def setUp(self):
        """Configura el entorno para las pruebas."""
        self.ordenador = RadixSort()

    def test_agregar_elemento(self):
        """Prueba agregar elementos a la lista."""
        self.ordenador.agregar_elemento(5)
        self.ordenador.agregar_elemento(10)
        self.ordenador.agregar_elemento(3)
        self.assertEqual(self.ordenador.obtener_lista(), [5, 10, 3])

    def test_ordenar(self):
        """Prueba el ordenamiento de la lista."""
        self.ordenador.agregar_elemento(170)
        self.ordenador.agregar_elemento(45)
        self.ordenador.agregar_elemento(75)
        self.ordenador.agregar_elemento(90)
        self.ordenador.agregar_elemento(802)
        self.ordenador.agregar_elemento(24)
        self.ordenador.agregar_elemento(2)
        self.ordenador.agregar_elemento(66)
        self.ordenador.ordenar()
        self.assertEqual(self.ordenador.obtener_lista(), [2, 24, 45, 66, 75, 90, 170, 802])

    def test_ordenar_lista_vacia(self):
        """Prueba la ordenación de una lista vacía."""
        with self.assertRaises(ValueError):
            self.ordenador.ordenar()

    def test_obtener_lista_vacia(self):
        """Prueba obtener la lista cuando está vacía."""
        with self.assertRaises(ValueError):
            self.ordenador.obtener_lista()

    def test_agregar_elemento_no_entero(self):
        """Prueba agregar un elemento no entero."""
        with self.assertRaises(TypeError):
            self.ordenador.agregar_elemento("cadena")

    def test_lista_con_datos_aleatorios(self):
        """Prueba con una lista de números aleatorios."""
        import random
        for _ in range(500):
            self.ordenador.agregar_elemento(random.randint(10000, 99999))
        self.ordenador.ordenar()
        lista_ordenada = sorted(self.ordenador.obtener_lista())
        self.assertEqual(self.ordenador.obtener_lista(), lista_ordenada)

if __name__ == "__main__":
    unittest.main()
