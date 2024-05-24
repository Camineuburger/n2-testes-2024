import pytest
from stat_funcs import StatsN2

@pytest.fixture
def stats():
    return StatsN2()

@pytest.fixture
def lista_vazia():
    return []

@pytest.fixture
def lista_unimodal():
    return [1, 2, 2, 3, 4]

@pytest.fixture
def lista_multimodal():
    return [1, 2, 2, 3, 3, 4]

@pytest.fixture
def lista_amodal():
    return [1, 1, 2, 2, 3, 3, 4, 4]

@pytest.fixture
def pesos():
    return [0.1, 0.2, 0.3, 0.4]
