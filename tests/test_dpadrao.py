import pytest
from stat_funcs import StatsN2

@pytest.mark.dpadrao
def test_dpadrao_variancia_zero(stats):
    assert stats.dpadrao(0) == 0

@pytest.mark.dpadrao
def test_dpadrao_variancia_positiva(stats):
    variancia = 4.0
    resultado_esperado = 2.0
    assert stats.dpadrao(variancia) == pytest.approx(resultado_esperado)

@pytest.mark.dpadrao
@pytest.mark.parametrize("variancia, resultado_esperado", [
    (0.25, 0.5),
    (1.0, 1.0),
    (2.25, 1.5),
    (9.0, 3.0)
])
def test_dpadrao_parametrizado(stats, variancia, resultado_esperado):
    assert stats.dpadrao(variancia) == pytest.approx(resultado_esperado)

@pytest.mark.dpadrao
@pytest.mark.xfail
def test_dpadrao_variancia_negativa(stats):
    assert stats.dpadrao(-1) == 0

