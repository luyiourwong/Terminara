from dataclasses import dataclass
from typing import List


@dataclass
class Scenario:
    """Represents a scenario in the game, with a description and choices."""
    text: str
    choices: List[str]