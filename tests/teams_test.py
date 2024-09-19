import pytest
from models.Team import Team
from repository.teams_repository import create_team, find_all_teams, find_team_by_id, update_team, delete_team


@pytest.fixture(scope="module")
def setup_database():
    teams = find_all_teams()
    return teams


def test_find_all_teams(setup_database):
    teams = setup_database
    assert len(teams) > 0, "No teams found in the database"


def test_create_team():
    new_team = Team(team_name="Chicago Bulls", player_ids=[1, 2, 3])
    team_id = create_team(new_team)
    assert team_id is not None, "Failed to create a new team"


def test_find_team_by_id():
    team_id = 1
    found_team = find_team_by_id(team_id)
    assert found_team is not None, f"Team with ID {team_id} not found in the database"


def test_update_team():
    updated_team = Team(id=1, team_name="Updated Team", player_ids=[1, 4, 5])
    update_team(updated_team)
    team_after_update = find_team_by_id(1)
    assert team_after_update.team_name == "Updated Team", "Failed to update the team"


def test_delete_team():
    team_id_to_delete = 1
    delete_team(team_id_to_delete)
    deleted_team = find_team_by_id(team_id_to_delete)
    assert deleted_team is None, "Team was not deleted"
