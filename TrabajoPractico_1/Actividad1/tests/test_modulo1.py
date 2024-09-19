# Archivo de test para realizar pruebas unitarias del modulo1
import unittest 
# Código que vamos a probar
# Dentro de tests/test_ordenamiento.py
from modules.Ejercicio1a import OrdenamientoBurbuja
# importa tu clase del archivo correspondiente

class TestOrdenamientoBurbuja(unittest.TestCase):

    def setUp(self):
        # Arrange: Crear una instancia de OrdenamientoBurbuja antes de cada prueba
        self.ordenador = OrdenamientoBurbuja()

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
            self.ordenador.ordenar()

    def test_ordenar(self):
        # Arrange: Agregamos varios elementos a la lista
        self.ordenador.agregar_elemento(5)
        self.ordenador.agregar_elemento(3)
        self.ordenador.agregar_elemento(10)
        lista_esperada = [3, 5, 10]
        
        # Act: Ordenamos la lista
        self.ordenador.ordenar()
        
        # Assert: Verificamos que la lista esté ordenada correctamente
        self.assertEqual(self.ordenador.obtener_lista(), lista_esperada)

    def test_ordenar_con_strings(self):
        # Arrange: Agregamos elementos con cadenas de texto
        self.ordenador.agregar_elemento("xyz")
        self.ordenador.agregar_elemento("abc")
        lista_esperada = ["abc", "xyz"]
        
        # Act: Ordenamos la lista
        self.ordenador.ordenar()
        
        # Assert: Verificamos que la lista esté ordenada alfabéticamente
        self.assertEqual(self.ordenador.obtener_lista(), lista_esperada)

    def test_ordenar_lista_con_flotantes(self):
        # Arrange: Agregamos números flotantes
        self.ordenador.agregar_elemento(2.5)
        self.ordenador.agregar_elemento(3.7)
        self.ordenador.agregar_elemento(1.2)
        lista_esperada = [1.2, 2.5, 3.7]
        
        # Act: Ordenamos la lista
        self.ordenador.ordenar()
        
        # Assert: Verificamos que los flotantes estén ordenados correctamente
        self.assertEqual(self.ordenador.obtener_lista(), lista_esperada)

    def test_obtener_lista_vacia(self):
        # Arrange: No se agregaron elementos a la lista
        
        # Act & Assert: Intentar obtener una lista vacía debería lanzar un ValueError
        with self.assertRaises(ValueError):
            self.ordenador.obtener_lista()


if __name__ == '__main__':
    unittest.main()
