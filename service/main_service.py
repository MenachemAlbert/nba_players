from repository.database import create_tables
from repository.players_repository import find_all_players
from repository.season_repository import find_all_seasons
from service.api_service import get_players_and_seasons


def seed():
    all_players = find_all_players()
    all_seasons = find_all_seasons()
    if all_players and len(all_players) > 0 and all_seasons and len(all_seasons) > 0:
        return
    get_players_and_seasons()


def initial_db():
    create_tables()
    seed()
