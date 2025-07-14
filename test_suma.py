import unittest
from suma import sumar, restar, multiplicar, dividir

class TestOperacionesMatematicas(unittest.TestCase):
    
    def test_sumar(self):
        # Casos básicos
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)
        # Casos con cero
        self.assertEqual(sumar(0, 0), 0)
        self.assertEqual(sumar(5, 0), 5)
        self.assertEqual(sumar(0, -3), -3)
        # Números decimales
        self.assertAlmostEqual(sumar(2.5, 3.7), 6.2)
    
    def test_restar(self):
        # Casos básicos
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(3, 5), -2)
        self.assertEqual(restar(-1, -1), 0)
        # Casos con cero
        self.assertEqual(restar(0, 0), 0)
        self.assertEqual(restar(5, 0), 5)
        self.assertEqual(restar(0, 3), -3)
        # Números negativos
        self.assertEqual(restar(-5, -3), -2)
        self.assertEqual(restar(-5, 3), -8)
        # Números decimales
        self.assertAlmostEqual(restar(5.5, 2.3), 3.2)
    
    def test_multiplicar(self):
        # Casos básicos
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(-2, 3), -6)
        self.assertEqual(multiplicar(-2, -3), 6)
        # Casos con cero
        self.assertEqual(multiplicar(0, 5), 0)
        self.assertEqual(multiplicar(7, 0), 0)
        self.assertEqual(multiplicar(0, 0), 0)
        # Casos con uno
        self.assertEqual(multiplicar(1, 8), 8)
        self.assertEqual(multiplicar(8, 1), 8)
        # Números decimales
        self.assertAlmostEqual(multiplicar(2.5, 4.0), 10.0)
    
    def test_dividir(self):
        # Casos básicos
        self.assertEqual(dividir(10, 2), 5.0)
        self.assertEqual(dividir(15, 3), 5.0)
        self.assertEqual(dividir(-10, 2), -5.0)
        self.assertEqual(dividir(-10, -2), 5.0)
        # Casos con uno
        self.assertEqual(dividir(8, 1), 8.0)
        # Números decimales
        self.assertAlmostEqual(dividir(7.5, 2.5), 3.0)
        # División que resulta en decimal
        self.assertAlmostEqual(dividir(1, 3), 0.3333333333333333)
    
    def test_dividir_por_cero(self):
        # Prueba que se lance la excepción correcta al dividir por cero
        with self.assertRaises(ValueError) as context:
            dividir(5, 0)
        self.assertEqual(str(context.exception), "No se puede dividir por cero")
        
        with self.assertRaises(ValueError):
            dividir(-5, 0)
        
        with self.assertRaises(ValueError):
            dividir(0, 0)

if __name__ == '__main__':
    unittest.main()