import os

from terminara.core.ai_narrator import AiNarrator
from terminara.core.state_manager import StateManager
from terminara.objects.game_state import GameState
from terminara.objects.scenario import Scenario, Choice, VariableAction, ItemAction
from terminara.objects.world_settings import WorldSettings


def get_initial_scenario() -> Scenario:
    return Scenario(
        text="You find yourself standing at the edge of a mysterious forest. The ancient trees tower above you, their branches swaying gently in the wind. Strange sounds echo from within the depths of the woodland. What do you choose to do?",
        choices=[
            Choice(
                text="1. Enter the forest cautiously",
                actions=[
                    VariableAction(
                        variable_name="hp",
                        value="-5"
                    )
                ]
            ),
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
    )


class GameEngine:
    def __init__(self, world_settings: WorldSettings, game_state: GameState | None = None,
                 load_scenario: Scenario | None = None):
        self.world_settings = world_settings
        self.state_manager = StateManager(world_settings=self.world_settings)
        self.ai_narrator = AiNarrator(
            host=os.getenv("OPENAI_API_HOST"),  # TODO load env for testing, change to config later?
            key=os.getenv("OPENAI_API_KEY"),
            model=os.getenv("OPENAI_API_MODEL")
        )
        if game_state is not None:
            self.state_manager.load_game(game_state)
        if load_scenario is not None:
            self.current_scenario = load_scenario
        else:
            self.current_scenario = get_initial_scenario()

    def get_current_scenario(self) -> Scenario:
        return self.current_scenario

    def get_next_scenario(self, choice: int | None = None) -> Scenario:
        # Apply the choice to the current scenario.
        if choice:
            current_choice: Choice = self.current_scenario.choices[choice - 1]
            current_choice_str = current_choice.text
            for action in current_choice.actions:
                if isinstance(action, VariableAction):
                    self.state_manager.modify_variable(action.variable_name, action.value)
                elif isinstance(action, ItemAction):
                    if action.quantity < 0:
                        self.state_manager.remove_item(action.item_name, action.quantity)
                    else:
                        self.state_manager.add_item(action.item_name, action.quantity)
        else:
            current_choice_str = "nothing"

        if not self.current_scenario:
            self.current_scenario = get_initial_scenario()
            return self.current_scenario

        # Generate the next scenario.
        game_state = self.state_manager.save_game()
        scenario = self.ai_narrator.generate_scenario(self.current_scenario.text, current_choice_str,
                                                      self.world_settings, game_state)
        choices = self.ai_narrator.generate_choice(scenario, self.world_settings, game_state)
        new_scenario = Scenario(
            text=scenario,
            choices=choices.choices
        )
        self.current_scenario = new_scenario
        return new_scenario
