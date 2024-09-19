from dataclasses import dataclass


@dataclass
class SeasonStats:
    team: str
    position: str
    season: int
    points: int
    games: int
    two_percent: float
    three_percent: float
    atr: float
    ppg_ratio: float
    player_id: int
    id: int = None
