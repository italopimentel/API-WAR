import pytest
from map import Map  

@pytest.fixture
def map_instance():
    return Map()

def test_initial_territories_empty(map_instance):
    assert map_instance.get_territories() == []

def test_replace_territories(map_instance):
    new_territories = ["Brasil", "Argentina"]
    map_instance.replace_territories(new_territories)
    assert map_instance.get_territories() == new_territories

def test_add_territory(map_instance):
    territory = "México"
    map_instance.add_territory(territory)
    assert territory in map_instance.get_territories()

def test_add_multiple_territories(map_instance):
    territories = ["Egito", "Islândia", "Inglaterra"]
    for t in territories:
        map_instance.add_territory(t)
    assert map_instance.get_territories() == territories
