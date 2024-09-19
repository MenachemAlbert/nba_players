
def calculation_ppg_ratio(players, player):
    players_on_position = filter(lambda x: x['position'] == player['position'], players)
    points_per_game = lambda x: x['points'] / x['games']
    avg = average(list(map(points_per_game, players_on_position)))
    return points_per_game(player) / avg


def average(x):
    return sum(x) / len(x)
