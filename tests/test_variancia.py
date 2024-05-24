import pytest
from stat_funcs import StatsN2

@pytest.mark.variancia
def test_variancia_lista_vazia(stats, lista_vazia):
    with pytest.raises(ZeroDivisionError):
        stats.variancia(lista_vazia)

@pytest.mark.variancia
def test_variancia_lista_um_elemento(stats):
    with pytest.raises(ZeroDivisionError):
        stats.variancia([10])

@pytest.mark.variancia
def test_variancia_lista_variancia(stats):
    lista = [2, 4, 4, 4, 5, 5, 7, 9]
    resultado_esperado = 4.571428571428571
    assert stats.variancia(lista) == pytest.approx(resultado_esperado)

@pytest.mark.variancia
@pytest.mark.parametrize("lista, resultado_esperado", [
    ([1, 2, 3, 4, 5], 2.5),
    ([10, 10, 10, 10, 10], 0.0),
    ([1, 2, 3, 4, 5, 6], 3.5)
])
def test_variancia_parametrizado(stats, lista, resultado_esperado):
    assert stats.variancia(lista) == pytest.approx(resultado_esperado)

@pytest.mark.variancia
@pytest.mark.xfail
def test_variancia_lista_strings(stats):
    lista = ["a", "b", "c"]
    stats.variancia(lista)
