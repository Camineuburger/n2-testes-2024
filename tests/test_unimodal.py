import pytest
from stat_funcs import StatsN2

@pytest.mark.unimodal
def test_unimodal_lista_vazia(stats, lista_vazia):
    with pytest.raises(ValueError):
        stats.unimodal(lista_vazia)

@pytest.mark.unimodal
def test_unimodal_lista_um_elemento(stats):
    assert stats.unimodal([10]) == 10

@pytest.mark.unimodal
def test_unimodal_lista_unimodal(stats):
    lista = [1, 2, 2, 3, 4]
    resultado_esperado = 2
    assert stats.unimodal(lista) == resultado_esperado

@pytest.mark.unimodal
def test_unimodal_lista_multimodal(stats):
    lista = [1, 2, 2, 3, 3, 4]
    resultado_esperado = "Não é unimodal"
    assert stats.unimodal(lista) == resultado_esperado

@pytest.mark.unimodal
@pytest.mark.parametrize("lista, resultado_esperado", [
    ([1, 1, 2, 2, 3], "Não é unimodal"),
    ([5, 5, 6, 6, 7], "Não é unimodal"),
    ([9, 10, 10, 11], 10)
])
def test_unimodal_parametrizado(stats, lista, resultado_esperado):
    assert stats.unimodal(lista) == resultado_esperado

@pytest.mark.unimodal
@pytest.mark.xfail
def test_unimodal_lista_strings(stats):
    lista = ["a", "b", "b", "c"]
    assert stats.unimodal(lista) == "b"
