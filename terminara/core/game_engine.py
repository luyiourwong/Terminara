from typing import List
from terminara.core.state_manager import StateManager
from terminara.objects.world_settings import WorldSettings
from terminara.objects.scenario import Scenario


class GameEngine:
    def __init__(self, world_settings: WorldSettings):
        self.world_settings = world_settings
        self.state_manager = StateManager(world_settings=self.world_settings)
        scenarios_data = [
            {
                "text": "You find yourself standing at the edge of a mysterious forest. The ancient trees tower above you, their branches swaying gently in the wind. Strange sounds echo from within the depths of the woodland. What do you choose to do?",
                "choices": [
                    "1. Enter the forest cautiously",
                    "2. Call out to see if anyone responds",
                    "3. Search for another path around",
                    "4. Turn back and leave",
                ],
            },
            {
                "text": "You step into the forest. A thick fog surrounds you, and the path ahead is barely visible. You hear a twig snap nearby.",
                "choices": [
                    "1. Continue cautiously on the path",
                    "2. Retreat from the forest",
                ],
            },
        ]
        self._scenarios: List[Scenario] = [
            Scenario(**data) for data in scenarios_data
        ]
        self._current_scenario_index = 0

    def get_initial_scenario(self) -> Scenario:
        return self._scenarios[0]

    def get_next_scenario(self, choice: int) -> Scenario:
        # This is a placeholder implementation that ignores the choice and cycles
        # between the two scenarios.
        self._current_scenario_index = (self._current_scenario_index + 1) % len(
            self._scenarios
        )
        return self._scenarios[self._current_scenario_index]
