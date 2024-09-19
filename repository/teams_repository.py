from typing import List

from models.Player import Player
from models.Team import Team
from repository.database import get_db_connection


def create_team(team: Team) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO teams (team_name, player_ids)
            VALUES (%s, %s) RETURNING id
        """, (team.team_name, team.player_ids))
        new_id = cursor.fetchone()['id']
        connection.commit()
        return new_id


def find_all_teams() -> List[Team]:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM teams")
            res = cursor.fetchall()
            teams = [Team(**t) for t in res]
            return teams


def find_team_by_id(team_id: int) -> Team | None:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM teams WHERE id = %s", (team_id,))
            res = cursor.fetchone()
            if res:
                return Team(**res)
            else:
                return None


def update_team(team: Team) -> Team:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE teams
                SET team_name = %s, player_ids = %s
                WHERE id = %s
            """, (team.team_name, team.player_ids, team.id))
            connection.commit()
    return team


def delete_team(team_id: int):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM teams WHERE id = %s", (team_id,))
            connection.commit()
