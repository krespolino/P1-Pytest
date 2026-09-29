import pytest 

def test_senha_valida():
    assert senha_valida("abcdef12") is True

def test_senha_curta_demais():
    assert senha_valida("abc1") is False

def test_senha_sem_numero():
    assert senha_valida("abcdefghij") is False

def test_senha_com_exatamente_8_caracteres():
    assert senha_valida("abcdefg1") is True  