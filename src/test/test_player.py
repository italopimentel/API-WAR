import pytest 
from player import Player
from objective import Objective

@pytest.fixture
def player_instance():
    return Player("Player1")

def test_initial_values(player_instance):
    assert player_instance.get_name() == "Player1"
    assert player_instance.get_color() is None
    assert player_instance.get_army() == 0

def test_set_color(player_instance):
    player_instance.set_color("Branco")
    assert player_instance.get_color() == "Branco"

def test_add_army(player_instance):
    player_instance.add_army(1)
    assert player_instance.get_army() == 1
    player_instance.add_army(5)
    assert player_instance.get_army() == 6

def test_set_objective(player_instance):
    objective_text = "Destruir totalmente OS EXÉRCITOS PRETOS."
    objective = Objective(objective_text)
    player_instance.set_objective(objective)
    assert player_instance.get_objective() == objective
    assert player_instance.get_objective().get_objective() == objective_text
