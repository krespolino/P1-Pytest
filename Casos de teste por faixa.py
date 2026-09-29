import pytest

def test_classificar_imc_abaixo_do_peso():
    assert classificar_imc(17.0) == "Abaixo do peso"

def test_classificar_imc_peso_normal():
    assert classificar_imc(22.0) == "Peso normal"

def test_classificar_imc_acima_do_peso():
    assert classificar_imc(30.0) == "Acima do peso"

def test_classificar_imc_fronteira_18_5():
    # 18.5 não é < 18.5, então entra em "Peso normal"
    assert classificar_imc(18.5) == "Peso normal"