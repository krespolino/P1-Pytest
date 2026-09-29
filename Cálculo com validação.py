import pytest

def test_desconto_valido():
    assert aplicar_desconto(200, 10) == 180.0

def test_desconto_zero():
    assert aplicar_desconto(200, 0) == 200.0

def test_desconto_cem_por_cento():
    assert aplicar_desconto(200, 100) == 0.0

def test_desconto_invalido():
    with pytest.raises(ValueError):
        aplicar_desconto(200, 150)