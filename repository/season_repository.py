from typing import List
from models.SeasonStats import SeasonStats
from repository.database import get_db_connection


def create_season(season_tats: SeasonStats) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO season_stats (team, position, season, points, games,
             two_percent, three_percent, atr, ppg_ratio, player_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
        """, (season_tats.team, season_tats.position, season_tats.season, season_tats.points, season_tats.games,
              season_tats.two_percent, season_tats.three_percent, season_tats.atr, season_tats.ppg_ratio,
              season_tats.player_id))
        new_id = cursor.fetchone()['id']
        connection.commit()
        return new_id


def find_all_seasons() -> List[SeasonStats]:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM season_stats")
            res = cursor.fetchall()
            seasons = [SeasonStats(**s) for s in res]
            return seasons


def find_season_by_id(season_id: int) -> SeasonStats | None:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM season_stats WHERE id = %s", (season_id,))
            res = cursor.fetchone()
            if res:
                return SeasonStats(**res)
            else:
                return None


def delete_season(season_id: int):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM season_stats WHERE id = %s", (season_id,))
            connection.commit()


def update_season(season_stats: SeasonStats) -> SeasonStats:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE season_stats
                SET team = %s, position = %s, season = %s, points = %s, games = %s, 
                    two_percent = %s, three_percent = %s, atr = %s, ppg_ratio = %s, player_id = %s
                WHERE id = %s
            """, (season_stats.team, season_stats.position,
                  season_stats.season, season_stats.points, season_stats.games,
                  season_stats.two_percent, season_stats.three_percent, season_stats.atr, season_stats.ppg_ratio,
                  season_stats.player_id, season_stats.id))
            connection.commit()
    return season_stats
