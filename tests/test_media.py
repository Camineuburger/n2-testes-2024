import pytest
from stat_funcs import StatsN2

@pytest.mark.media
def test_media_lista_vazia(stats, lista_vazia):
    assert stats.media(lista_vazia) == 0

@pytest.mark.media
def test_media_lista_um_elemento(stats):
    assert stats.media([10]) == 10

@pytest.mark.media
@pytest.mark.parametrize("lista, resultado_esperado", [
    ([1, 2, 3, 4, 5], 3),
    ([10, 20, 30], 20),
    ([1, 1, 1, 1], 1)
])
def test_media_parametrizado(stats, lista, resultado_esperado):
    assert stats.media(lista) == resultado_esperado

@pytest.mark.media
def test_media_lista_numeros_negativos(stats):
    assert stats.media([-1, -2, -3, -4, -5]) == -3

@pytest.mark.media
@pytest.mark.xfail
def test_media_lista_string_falha(stats):
    assert stats.media(["a", "b", "c"]) == 0
