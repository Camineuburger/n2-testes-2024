import pytest
from stat_funcs import StatsN2

@pytest.mark.mediana
def test_mediana_lista_vazia(stats, lista_vazia):
    assert stats.mediana(lista_vazia) == 0

@pytest.mark.mediana
def test_mediana_lista_um_elemento(stats):
    assert stats.mediana([10]) == 10

@pytest.mark.mediana
def test_mediana_lista_impar(stats):
    lista = [3, 1, 4, 2, 5]
    resultado_esperado = 3
    assert stats.mediana(lista) == resultado_esperado

@pytest.mark.mediana
def test_mediana_lista_par(stats):
    lista = [3, 1, 4, 2]
    resultado_esperado = 2.5
    assert stats.mediana(lista) == resultado_esperado

@pytest.mark.mediana
@pytest.mark.parametrize("lista, resultado_esperado", [
    ([1, 2, 3], 2),
    ([1, 2, 3, 4], 2.5),
    ([7, 8, 3, 1, 2], 3),
    ([10, 20, 30, 40], 25)
])
def test_mediana_parametrizado(stats, lista, resultado_esperado):
    assert stats.mediana(lista) == resultado_esperado

@pytest.mark.mediana
@pytest.mark.xfail
def test_mediana_lista_strings(stats):
    lista = ["a", "b", "c"]
    stats.mediana(lista)
