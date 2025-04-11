import unittest
import act7_1_numeros

class TestRacionales(unittest.TestCase):
    def test_print_hello(self):
        # Crear una instancia de la clase racionales
        racional = act7_1_numeros.racionales(0.5)
        
        # Llamar al método print_hello y verificar el resultado
        resultado = racional.print_hello()
        self.assertEqual(resultado, "Hola David")

if __name__ == '__main__':
    unittest.main()