from typing import List

from models.Player import Player
from repository.database import get_db_connection


def create_player(player: Player) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO players (player_Name)
            VALUES (%s) RETURNING id
        """, (player.player_name,))
        new_id = cursor.fetchone()['id']
        connection.commit()
        return new_id


def find_all_players() -> List[Player]:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM players")
            res = cursor.fetchall()
            players = [Player(**p) for p in res]
            return players


def find_player_by_name(player_name) -> Player | None:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM players WHERE player_Name = %s", (player_name,))
            res = cursor.fetchone()
            if res:
                return res['id']
            else:
                return None


def find_player_by_id(player_id: int) -> Player | None:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM players WHERE id = %s", (player_id,))
            res = cursor.fetchone()
            if res:
                return res
            else:
                return None


def delete_player(id_player: int):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM players WHERE id = %s", (id_player,))
            connection.commit()


def update_player(player: Player) -> Player:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE players
                SET player_name = %s
                WHERE id = %s
            """, (player.player_name, player.id))
            connection.commit()
    return player
