"""
Test pour les opérations du module operators.py

Ce fichier teste les quatres opérations : addition, soustraction, multiplication, division
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from operators import add, subtract, multiply, divide
import pytest


def test_add_integer_numbers():
    """Teste l'addition avec des nombres entiers"""
    result = add(10, 4)
    assert result == 14


def test_add_decimal_numbers():
    """Teste l'addition avec des nombres decimaux"""
    assert add(3.8, 3.2) == 7.0


def test_add_negative_numbers():
    """Teste l'addition avec des nombres negatifs"""
    assert add(-9, 5) == -4
    assert add(12, -7) == 5
    assert add(-6, -5) == -11


def test_subtract_integer_numbers():
    """Teste la soustraction avec des nombres entiers"""
    result = subtract(16, 6)
    assert result == 10

def test_multiply_integer_numbers():
    """Teste la multiplication avec des nombres entiers"""
    result = multiply(2, 10)
    assert result ==20


def test_divide_integer_numbers():
    """Teste la division avec des nombres entiers"""
    result = divide(20, 4)
    assert result == 5.0

def test_divide_with_decimals():
    """Teste que la division retourne bien un float avec decimales"""
    result = divide(11, 4)
    assert result == 2.75

def test_divide_negative_numbers():
    """Teste la division avec des nombres negatifs"""
    assert divide(-18, 3) == -6.0
    assert divide(24, -6) == -4.0
    assert divide(-30, -5) == 6.0


def test_divide_by_zero_error():
    """Verifie qu'une ZeroDivisionError est levee quand b vaut 0"""
    with pytest.raises(ZeroDivisionError):
        divide(25, 0)
