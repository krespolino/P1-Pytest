import pytest

def test_media_notas_diferentes():
    assert calcular_media([6, 8, 10]) == pytest.approx(8.0)

def test_media_notas_iguais():
    assert calcular_media([7, 7, 7]) == pytest.approx(7.0)

def test_media_uma_unica_nota():
    assert calcular_media([9]) == pytest.approx(9.0)

def test_media_lista_vazia():
    with pytest.raises(ValueError):
        calcular_media([])


##sem essa validação, a divisão por len(notas) == 0 geraria um ZeroDivisionError inesperado, e o teste garante que o erro seja tratado de forma clara e controlada com ValueError.