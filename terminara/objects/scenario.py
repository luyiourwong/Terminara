from dataclasses import dataclass, field
from typing import List, Any
from abc import ABC


class Action(ABC):
    """Abstract base class for an action to be executed."""


@dataclass
class VariableAction(Action):
    """An action that modifies a game variable."""
    variable_name: str
    value: Any


@dataclass
class ItemAction(Action):
    """An action that adds or removes an item from the inventory."""
    item_name: str
    quantity: int


@dataclass
class Choice:
    """Represents a player's choice, with text and resulting actions."""
    text: str
    actions: List[Action] = field(default_factory=list)


@dataclass
class Scenario:
    """Represents a scenario in the game, with a description and choices."""
    text: str
    choices: List[Choice]
