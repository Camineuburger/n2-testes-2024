import pytest
from stat_funcs import StatsN2

@pytest.mark.multimodal
def test_multimodal_lista_vazia(stats, lista_vazia):
    assert stats.multimodal(lista_vazia) == "Lista vazia"

@pytest.mark.multimodal
def test_multimodal_lista_um_elemento(stats):
    assert stats.multimodal([10]) == "Não é multimodal"

@pytest.mark.multimodal
def test_multimodal_lista_multimodal(stats):
    lista = [1, 2, 2, 3, 3, 4]
    resultado_esperado = [2, 3]
    assert stats.multimodal(lista) == resultado_esperado

@pytest.mark.multimodal
def test_multimodal_lista_unimodal(stats):
    lista = [1, 2, 2, 3, 4]
    resultado_esperado = "Não é multimodal"
    assert stats.multimodal(lista) == resultado_esperado

@pytest.mark.multimodal
@pytest.mark.parametrize("lista, resultado_esperado", [
    ([1, 1, 2, 2, 3], [1, 2]),
    ([5, 5, 6, 6, 7], [5, 6]),
    ([10, 20, 20, 30, 30, 40], [20, 30])
])
def test_multimodal_parametrizado(stats, lista, resultado_esperado):
    assert stats.multimodal(lista) == resultado_esperado

@pytest.mark.multimodal
@pytest.mark.xfail
def test_multimodal_lista_strings(stats):
    lista = ["a", "b", "b", "c", "c"]
    resultado_esperado = ["b", "c"]
    assert stats.multimodal(lista) == resultado_esperado
