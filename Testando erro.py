import pytest 

def test_sacar_valido():
    assert sacar(100, 40) == 60

def test_sacar_saldo_insuficiente():
    with pytest.raises(ValueError):
        sacar(100, 150)