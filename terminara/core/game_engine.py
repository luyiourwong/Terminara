from typing import List
from terminara.core.state_manager import StateManager
from terminara.objects.world_settings import WorldSettings
from terminara.objects.scenario import Scenario, Choice, VariableAction, ItemAction


class GameEngine:
    def __init__(self, world_settings: WorldSettings):
        self.world_settings = world_settings
        self.state_manager = StateManager(world_settings=self.world_settings)
        self._scenarios: List[Scenario] = [
            Scenario(
                text="You find yourself standing at the edge of a mysterious forest. The ancient trees tower above you, their branches swaying gently in the wind. Strange sounds echo from within the depths of the woodland. What do you choose to do?",
                choices=[
                    Choice(text="1. Enter the forest cautiously"),
                    Choice(text="2. Call out to see if anyone responds"),
                    Choice(
                        text="3. Search the trees for something",
                        actions=[
                            ItemAction(
                                item_name="wood",
                                quantity=1
                            )
                        ]
                    ),
                    Choice(text="4. Turn back and leave")
                ]
            ),
            Scenario(
                text="You step into the forest. A thick fog surrounds you, and the path ahead is barely visible. You hear a twig snap nearby.",
                choices=[
                    Choice(
                        text="1. Continue cautiously on the path",
                        actions=[
                            VariableAction(
                                variable_name="hp",
                                value="-5"
                            )
                        ]
                    ),
                    Choice(text="2. Retreat from the forest")
                ]
            )
        ]
        self._current_scenario_index = 0

    def get_initial_scenario(self) -> Scenario:
        return self._scenarios[0]

    def get_next_scenario(self, choice: int) -> Scenario:
        # Apply the choice to the current scenario.
        current_scenario: Scenario = self._scenarios[self._current_scenario_index]
        current_choice: Choice = current_scenario.choices[choice - 1]
        for action in current_choice.actions:
            if isinstance(action, VariableAction):
                self.state_manager.modify_variable(action.variable_name, action.value)
            elif isinstance(action, ItemAction):
                if action.quantity < 0:
                    self.state_manager.remove_item(action.item_name, action.quantity)
                else:
                    self.state_manager.add_item(action.item_name, action.quantity)

        # This is a placeholder implementation that ignores the choice and cycles
        # between the two scenarios.
        self._current_scenario_index = (self._current_scenario_index + 1) % len(
            self._scenarios
        )
        return self._scenarios[self._current_scenario_index]
