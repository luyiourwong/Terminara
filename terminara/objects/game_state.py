from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class GameState:
    """Represents the current state of the game."""
    variables: Dict[str, Any] = field(default_factory=dict)
    inventory: Dict[str, int] = field(default_factory=dict)