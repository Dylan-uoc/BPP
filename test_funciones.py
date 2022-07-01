from funciones import *
import pytest

"""El archivo funciones incluye 3 funciones creadas que van a ser testeadas con 5 test en pytest y 5 test con unittest

        En el archivo test_funciones.py están los 5 test con pytest y en el propio archivo funciones.py están los 5 test con unittest
    """

def test_factorial():
    assert factorial(5) == 120
    
def test_area_circulo():
    assert area_circulo(5) == m.pi * 25
    
def test_primo():
    assert primo(5) == True
    
def test_control_non_int():
    with pytest.raises(TypeError):
        factorial("cinco")
        
def test_control_radio_negativo():
    with pytest.raises(ValueError):
        area_circulo(-5)
                          