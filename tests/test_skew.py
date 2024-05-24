import pytest
import numpy as np
import scipy.stats
from stat_funcs import StatsN2

@pytest.mark.skew
def test_skew_lista_vazia(stats, lista_vazia):
    with pytest.raises(ValueError):
        stats.skew(lista_vazia)

@pytest.mark.skew
def test_skew_distribuicao_normal(stats):
    lista = [1, 2, 3, 4, 5]
    resultado_esperado = "Distribuição normal"
    skewness = stats.skew(lista)
    print(f"Skewness for normal distribution {lista}: {skewness}")
    assert skewness == resultado_esperado

@pytest.mark.skew
def test_skew_distribuicao_negativa(stats):
    lista = [10, 9, 8, 7, 1]
    resultado_esperado = "Distribuição negativa"
    skewness_value = scipy.stats.skew(np.array(lista), bias=False)
    print(f"Raw skewness value for negative distribution {lista}: {skewness_value}")
    skewness = stats.skew(lista)
    print(f"Skewness for negative distribution {lista}: {skewness}")
    assert skewness == resultado_esperado

@pytest.mark.skew
def test_skew_distribuicao_positiva(stats):
    lista = [1, 2, 3, 4, 10]
    resultado_esperado = "Distribuição positiva"
    skewness = stats.skew(lista)
    print(f"Skewness for positive distribution {lista}: {skewness}")
    assert skewness == resultado_esperado

@pytest.mark.skew
@pytest.mark.parametrize("lista, resultado_esperado", [
    ([1, 2, 3, 4, 5], "Distribuição normal"),
    ([10, 9, 8, 7, 1], "Distribuição negativa"),
    ([1, 2, 2, 2, 10], "Distribuição positiva")
])
def test_skew_parametrizado(stats, lista, resultado_esperado):
    skewness_value = scipy.stats.skew(np.array(lista), bias=False)
    print(f"Raw skewness value for {lista}: {skewness_value}")
    skewness = stats.skew(lista)
    print(f"Skewness for {lista}: {skewness}")
    assert skewness == resultado_esperado

@pytest.mark.skew
@pytest.mark.xfail
def test_skew_lista_strings(stats):
    lista = ["a", "b", "c"]
    stats.skew(lista)
