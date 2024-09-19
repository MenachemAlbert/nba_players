from flask import Blueprint, jsonify, request

from repository.players_repository import find_all_players
from repository.season_repository import find_seasons_by_player_id
from service.players_service import get_res_player

players_blueprint = Blueprint("players", __name__)


@players_blueprint.route("/", methods=['GET'])
def get_players():
    position = request.args.get('position')

    players = find_all_players()

    for player in players:
        seasons = find_seasons_by_player_id(player.id)

        if position and not any(s.position == position for s in seasons):
            continue

        if not seasons:
            continue
        res = get_res_player(seasons, player)

        return jsonify(res), 200
