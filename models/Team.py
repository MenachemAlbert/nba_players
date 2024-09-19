from dataclasses import dataclass
from typing import List


@dataclass
class Team:
    team_name: str
    player_ids: List[int]
    id: int = None
