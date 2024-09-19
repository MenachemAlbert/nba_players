import requests


def get_from_api(url):
    return requests.get(url).json()


years = [2022, 2023, 2024]


def get_all_players_of_season(season):
    url = f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={season}&&pageSize=20"
    return get_from_api(url)


def get_all_players_from_api():
    players = []
    for s in years:
        season_players = get_all_players_of_season(s)
        players.extend(season_players)
    return players
