import pytest
import operaciones

def test_suma():
    x = 4
    y = 7
    resultado = 11
    assert resultado == operaciones.sumar(x,y)

def test_resta():
    x = 12
    y = 5
    resultado =7
    assert resultado == operaciones.restar(x,y)

def test_multiplicacion():
    x = 4
    y = 3
    resultado = 12
    assert resultado == operaciones.multiplicar(x,y)

def test_division():
    x = 20
    y = 4
    resultado = 5
    assert resultado == operaciones.dividir(x,y)
