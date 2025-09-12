from abc import ABC
from dataclasses import dataclass
from typing import List, Union

from pydantic import BaseModel


class Action(BaseModel, ABC):
    """Abstract base class for an action to be executed."""
    pass


class VariableAction(Action):
    """An action that modifies a game variable."""
    variable_name: str
    value: str


class ItemAction(Action):
    """An action that adds or removes an item from the inventory."""
    item_name: str
    quantity: int


class Choice(BaseModel):
    """Represents a player's choice, with text and resulting actions."""
    text: str
    actions: List[Union[VariableAction, ItemAction]] = []


class Choices(BaseModel):
    choices: List[Choice]


@dataclass
class Scenario:
    """Represents a scenario in the game, with a description and choices."""
    text: str
    choices: List[Choice]
