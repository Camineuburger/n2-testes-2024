import pytest
from collections import Counter
from stat_funcs import StatsN2

@pytest.mark.amodal
def test_amodal_lista_vazia(stats, lista_vazia):
    assert stats.amodal(lista_vazia) == "Não existe moda"

@pytest.mark.amodal
def test_amodal_lista_amodal(stats):
    lista = [1, 2, 3, 4]
    resultado_esperado = "Não existe moda"
    assert stats.amodal(lista) == resultado_esperado

@pytest.mark.amodal
def test_amodal_lista_com_moda(stats):
    lista = [1, 2, 2, 3, 4]
    resultado_esperado = "Existe moda"
    assert stats.amodal(lista) == resultado_esperado

@pytest.mark.amodal
@pytest.mark.parametrize("lista, resultado_esperado", [
    ([1, 2, 3, 4, 5], "Não existe moda"),
    ([5, 5, 6, 6, 7, 8], "Existe moda"),
    ([9, 10, 11, 12, 13, 14], "Não existe moda")
])
def test_amodal_parametrizado(stats, lista, resultado_esperado):
    assert stats.amodal(lista) == resultado_esperado

@pytest.mark.amodal
@pytest.mark.xfail
def test_amodal_lista_strings(stats):
    lista = ["a", "b", "b", "c"]
    assert stats.amodal(lista) == "Não existe moda"
