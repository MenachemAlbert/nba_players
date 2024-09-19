from flask import Blueprint, request, jsonify

from models.Team import Team
from repository.players_repository import find_player_by_id
from repository.teams_repository import create_team

fantastic_team_blueprint = Blueprint("fantastic_team", __name__)


@fantastic_team_blueprint.route("/", methods=["POST"])
def create_fantasy_team():
    data = request.get_json()
    team_name = data.get("team_name")
    player_ids = data.get("player_ids")

    if len(player_ids) < 5:
        return jsonify({"error": "At least 5 players are required"}), 400

    positions = set()
    for player_id in player_ids:
        player = find_player_by_id(player_id)
        if player:
            positions.add(player["position"])
        else:
            return jsonify({"error": f"Player with ID {player_id} not found"}), 404

    if len(positions) < 5:
        return jsonify({"error": "A player is required for each position"}), 400

    team_id = create_team(Team(team_name=team_name, player_ids=player_ids))
    return jsonify({"team_id": team_id, "team_name": team_name}), 201
