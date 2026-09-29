import pytest 

def test_frete_faixa_leve():
    assert calcular_frete(3) == 10.0

def test_frete_faixa_media():
    assert calcular_frete(7) == 20.0

def test_frete_faixa_pesada():
    assert calcular_frete(15) == 35.0

def test_frete_fronteira_5():
    assert calcular_frete(5) == 10.0   # <= 5 ainda é a primeira faixa

def test_frete_fronteira_10():
    assert calcular_frete(10) == 20.0  # <= 10 ainda é a segunda faixa