from flask import Blueprint, jsonify, request

from repository.players_repository import find_all_players
from repository.season_repository import find_seasons_by_player_id

players_blueprint = Blueprint("players", __name__)


@players_blueprint.route("/", methods=['GET'])
def get_players():
    position = request.args.get('position')

    players = find_all_players()
    response_data = []

    for player in players:
        seasons = find_seasons_by_player_id(player.id)

        if position and not any(s.position == position for s in seasons):
            continue

        if not seasons:
            continue

        total_points = sum(s.points for s in seasons)
        total_games = sum(s.games for s in seasons)
        total_two_percent = sum(s.two_percent for s in seasons) / len(seasons) if seasons else 0
        total_three_percent = sum(s.three_percent for s in seasons) / len(seasons) if seasons else 0
        total_atr = sum(s.atr for s in seasons) / len(seasons) if seasons else 0
        total_ppg_ratio = sum(s.ppg_ratio for s in seasons) / len(seasons) if seasons else 0

        first_season = seasons[0] if seasons else None
        season_years = [s.season for s in seasons]
        season_position = first_season.position if first_season else None
        season_team = first_season.team if first_season else None

        player_data = {
            "team": season_team,
            "position": season_position,
            "seasons": season_years,
            "playerName": player.player_name,
            "points": total_points,
            "games": total_games,
            "twoPercent": total_two_percent,
            "threePercent": total_three_percent,
            "ATR": total_atr,
            "ppg_ratio": total_ppg_ratio
        }

        response_data.append(player_data)

    return jsonify(response_data), 200
