import pytest
from models.SeasonStats import SeasonStats
from repository.season_repository import (create_season, find_all_seasons,
                                          find_season_by_id, update_season, delete_season)


@pytest.fixture(scope="module")
def setup_database():
    seasons = find_all_seasons()
    return seasons


def test_find_all_seasons(setup_database):
    seasons = setup_database
    assert len(seasons) > 0, "No seasons found in the database"


def test_create_season():
    new_season = SeasonStats(team="Bulls", position="Guard", season=2023, points=30,
                             games=82, two_percent=0.5, three_percent=0.4, atr=2, ppg_ratio=1.2, player_id=1)
    season_id = create_season(new_season)
    assert season_id is not None, "Failed to create a new season"


def test_find_season_by_id():
    season_id = 61
    found_season = find_season_by_id(season_id)
    assert found_season is not None, f"Season with ID {season_id} not found in the database"


def test_update_season():
    updated_season = SeasonStats(id=61, team="Updated Team", position="SG", season=2023, points=35,
                                 games=82, two_percent=0.55, three_percent=0.45, atr=2, ppg_ratio=1.3, player_id=1)
    update_season(updated_season)
    season_after_update = find_season_by_id(61)
    assert season_after_update.team == "Updated Team", "Failed to update the season"


def test_delete_season():
    season_id_to_delete = 61
    delete_season(season_id_to_delete)
    deleted_season = find_season_by_id(season_id_to_delete)
    assert deleted_season is None, "Season was not deleted"
