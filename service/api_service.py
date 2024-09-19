from api.api import get_all_players_from_api
from models.Player import Player
from models.SeasonStats import SeasonStats
from repository.players_repository import create_player, find_player_by_name
from repository.season_repository import create_season
from utils.calculates import calculation_ppg_ratio


def get_players_and_seasons():
    players_data = get_all_players_from_api()

    for player_data in players_data:
        player_id = find_player_by_name(player_data['playerName'])
        if not player_id:
            player = Player(player_name=player_data['playerName'])
            player_id = create_player(player)
        ppg_ratio = calculation_ppg_ratio(players_data, player_data)

        season_stats = SeasonStats(
            team=player_data['team'],
            position=player_data['position'],
            season=player_data['season'],
            points=player_data['points'],
            games=player_data['games'],
            two_percent=player_data.get('twoPercent') if player_data.get('twoPercent') is not None else 0.0,
            three_percent=player_data.get('threePercent') if player_data.get('threePercent') is not None else 0.0,
            atr=int(player_data['assists'] / player_data['turnovers']) if player_data['turnovers'] != 0 else 0,
            ppg_ratio=ppg_ratio,
            player_id=player_id
        )
        create_season(season_stats)


