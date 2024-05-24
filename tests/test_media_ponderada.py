import pytest
from stat_funcs import StatsN2

@pytest.mark.media_ponderada
def test_media_ponderada_lista_vazia(stats, lista_vazia, pesos):
    assert stats.media_ponderada(lista_vazia, pesos) == 0

@pytest.mark.media_ponderada
def test_media_ponderada_igual_com_pesos(stats):
    lista = [1, 2, 3, 4]
    pesos = [1, 1, 1, 1]
    resultado_esperado = 2.5
    assert stats.media_ponderada(lista, pesos) == pytest.approx(resultado_esperado)

@pytest.mark.media_ponderada
@pytest.mark.parametrize("lista, pesos, resultado_esperado", [
    ([1, 2, 3, 4], [1, 1, 1, 1], 2.5),
    ([10, 20, 30], [0.2, 0.3, 0.5], 23),
    ([1, 2, 3], [0.1, 0.3, 0.6], 2.5)
])
def test_media_ponderada_parametrizado(stats, lista, pesos, resultado_esperado):
    assert stats.media_ponderada(lista, pesos) == pytest.approx(resultado_esperado)

@pytest.mark.media_ponderada
def test_media_ponderada_lista_com_pesos_diferentes(stats):
    lista = [1, 2, 3]
    pesos = [0.1, 0.3, 0.6]
    resultado_esperado = 2.5
    assert stats.media_ponderada(lista, pesos) == pytest.approx(resultado_esperado)

@pytest.mark.media_ponderada
@pytest.mark.xfail
def test_media_ponderada_lista_pesos_tamanho_diferente(stats):
    lista = [1, 2, 3]
    pesos = [0.1, 0.3]
    stats.media_ponderada(lista, pesos)
