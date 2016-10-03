import unittest

# Todos las funciones de prueba se ejecutan de manera independiente.
# Todos las funciones de prueba deben comenzar con la palabra test.

# TAREA: Completar los requerimientos del programa.
# http://148.217.200.108:89


class TestFiguras(unitest.TestCase):

    def setUp(self):
        self.figura = Figuras()

    def test_area_cuadrado_lado_5(self):
        # figura = Figuras()
        resultado = self.figura.cuadrado(5)
        self.assertEqual(25, resultado)

    def test_area_cuadrado_lado_5(self):
        # figura = Figuras()
        resultado = self.figura.cuadrado(6)
        self.assertEqual(36, resultado)

    def test_area_cuadrado_lado_g(self):
        # figura = Figuras()
        resultado = self.figura.cuadrado('g')
        self.assertEqual('dato incorrecto', resultado)

    def tearDown():
        pass

if __name__ == '__main__':
    unittest.main()
