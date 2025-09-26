from dataclasses import dataclass, field
from typing import Dict, Any, Optional
from abc import ABC

from terminara.objects.scenario import Scenario


@dataclass
class GameVariable(ABC):
    """Represents a variable in the game."""
    description: str
    value: Any


@dataclass
class NumericVariable(GameVariable):
    """Represents a numeric variable in the game."""
    value: int | float
    min_value: int | float | None = None
    max_value: int | float | None = None


@dataclass
class TextVariable(GameVariable):
    """Represents a text variable in the game."""
    value: str


@dataclass
class Item:
    """Represents an item in the game."""
    name: str
    description: str
    attributes: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AiPrompt:
    """Represents the AI prompt in the game."""
    system: str
    prompt: str
    lore: Dict[str, str] = field(default_factory=dict)


@dataclass
class WorldInfo:
    """Represents the world information of the game."""
    name: str
    description: str


@dataclass
class ScenarioSettings:
    """Represents the scenario settings of the game."""
    init: Optional[Scenario] = None


@dataclass
class WorldSettings:
    """Represents the world settings of the game."""
    world: WorldInfo = field(default_factory=WorldInfo)
    ai: AiPrompt = field(default_factory=AiPrompt)
    variables: Dict[str, GameVariable] = field(default_factory=dict)
    items: Dict[str, Item] = field(default_factory=dict)
    scenario: ScenarioSettings = field(default_factory=ScenarioSettings)
