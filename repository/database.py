import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQL_URI


def get_db_connection():
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)


def create_tables():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS "players" (
                    id SERIAL PRIMARY KEY,
                    player_Name VARCHAR(255) NOT NULL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS "teams" (
                    id SERIAL PRIMARY KEY,
                    team_name VARCHAR(255) NOT NULL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS "season_stats" (
                    id SERIAL PRIMARY KEY,
                    team VARCHAR(255) NOT NULL,
                    position VARCHAR(50) NOT NULL,                 
                    season INT NOT NULL,
                    points INT NOT NULL,
                    games INT NOT NULL,
                    two_percent FLOAT NOT NULL,
                    three_percent FLOAT NOT NULL,
                    ATR FLOAT NOT NULL,
                    PPG_Ratio FLOAT NOT NULL,
                    player_id INT REFERENCES players(id) ON DELETE CASCADE
                )
            """)
            connection.commit()
