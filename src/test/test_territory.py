import pytest
from territory import Territory
from player import Player

@pytest.fixture
def territory():
    return Territory("Brasil", "América do Sul")

@pytest.fixture
def player():
    return Player("Player1")

def test_initial_values(territory):
    assert territory.get_name() == "Brasil"
    assert territory.get_region() == "América do Sul"
    assert territory.get_army() == 0
    assert territory.get_dominant_player_name() == "None"

def test_set_dominant_player(territory, player):
    territory.set_dominant_player(player)
    assert territory.get_dominant_player_name() == "Player1"

def test_add_army(territory):
    territory.add_army(5)
    assert territory.get_army() == 5
    territory.add_army(10)
    assert territory.get_army() == 15

def test_get_dominant_player_name_none(territory):
    assert territory.get_dominant_player_name() == "None"
