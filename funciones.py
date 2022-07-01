import math as m
import unittest

"""El archivo funciones incluye 3 funciones creadas que van a ser testeadas con 5 test en pytest y 5 test con unittest

        En el archivo test_funciones.py están los 5 test con pytest y en el propio archivo funciones.py están los 5 test con unittest
    """

def factorial (n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    
def area_circulo (radio):
    if radio < 0:
        raise ValueError("El radio debe ser positivo")
    return m.pi * radio**2

def primo (n):
    if n == 1:
        return False
    for i in range(2, int(m.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


"""unitest"""

class TestFactorial(unittest.TestCase):
    def test_Factorial(self):
        self.assertEqual(factorial(5), 120)
        
    def test_Area_circulo(self):
        self.assertEqual(area_circulo(5), m.pi * 25)
        
    def test_esPrimo(self):
        self.assertTrue(primo(5))       
    
    def test_error_TipoDato(self):
        with self.assertRaises(TypeError):
            factorial("cinco")
            
    def test_error_ValorNegativo(self):
        with self.assertRaises(ValueError):
            area_circulo(-5)        
            
if __name__ == '__main__':
    unittest.main()            