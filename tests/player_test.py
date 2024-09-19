import pytest
from models.Player import Player
from repository.players_repository import (create_player, find_all_players, find_player_by_name, update_player, delete_player)


@pytest.fixture(scope="module")
def setup_database():
    players = find_all_players()
    return players


def test_find_all_players(setup_database):
    players = setup_database
    assert len(players) > 0, "No players found in the database"


def test_create_player():
    new_player = Player(player_name="Michael Jordan")
    player_id = create_player(new_player)
    assert player_id is not None, "Failed to create a new player"


def test_find_player_by_name():
    player_name = "Michael Jordan"
    found_player_id = find_player_by_name(player_name)
    assert found_player_id is not None, f"Player {player_name} not found in the database"


def test_update_player():
    updated_player = Player(id=28, player_name="Updated ")
    update_player(updated_player)
    player_after_update = find_player_by_name("Updated ")
    assert player_after_update is not None, "Failed to update the player"


def test_delete_player():
    player_id_to_delete = 28
    delete_player(player_id_to_delete)
    deleted_player = find_player_by_name("Updated ")
    assert deleted_player is None, "Player was not deleted"
