import unittest
from modules.Ejercicio1b import OrdenamientoQuicksort 

class TestOrdenamientoQuicksort(unittest.TestCase):

    def setUp(self):
        # Arrange: Crear una instancia de OrdenamientoQuicksort antes de cada prueba
        self.ordenador = OrdenamientoQuicksort()

    def test_agregar_elemento(self):
        # Arrange: Lista está vacía y queremos agregar un número
        elemento = 5
        # Act: Agregar un elemento a la lista
        self.ordenador.agregar_elemento(elemento)
        # Assert: Verificar que el elemento se agregó correctamente
        self.assertEqual(self.ordenador.obtener_lista(), [elemento])

    def test_agregar_elemento_invalido(self):
        # Arrange: Intentamos agregar un tipo inválido
        elemento_invalido = [1, 2, 3]
        # Act & Assert: Verificar que se lanza la excepción correcta
        with self.assertRaises(TypeError):
            self.ordenador.agregar_elemento(elemento_invalido)

    def test_ordenar_lista_vacia(self):
        # Arrange: No se agregaron elementos (lista vacía)
        # Act & Assert: Intentar ordenar la lista vacía debería lanzar un ValueError
        with self.assertRaises(ValueError):
            self.ordenador.obtener_lista()

    def test_ordenar(self):
        # Arrange: Agregamos varios elementos a la lista
        self.ordenador.agregar_elemento(5)
        self.ordenador.agregar_elemento(3)
        self.ordenador.agregar_elemento(10)
        lista_esperada = [3, 5, 10]
        # Act: Ordenamos la lista
        resultado = self.ordenador.obtener_lista()
        # Assert: Verificamos que la lista esté ordenada correctamente
        self.assertEqual(resultado, lista_esperada)

if __name__ == '__main__':
    unittest.main()
