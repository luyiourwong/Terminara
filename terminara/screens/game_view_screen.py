from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Button, Static
from textual.containers import Vertical, Horizontal

from terminara.core.game_engine import GameEngine
from terminara.objects.scenario import Scenario
from terminara.objects.world_settings import WorldSettings
from terminara.screens.details_view_screen import DetailsViewScreen
from terminara.screens.options_menu_screen import OptionsMenuScreen


class GameViewScreen(Screen):
    """The main game view screen."""

    BINDINGS = [
        Binding("d", "show_details", "Details"),
        Binding("o", "show_options", "Options"),
        Binding("1", "press_choice_1", "Choice 1"),
        Binding("2", "press_choice_2", "Choice 2"),
        Binding("3", "press_choice_3", "Choice 3"),
        Binding("4", "press_choice_4", "Choice 4"),
        Binding("up", "focus_previous", "Select previous"),
        Binding("down", "focus_next", "Select next"),
        Binding("enter", "press_selected", "Activate selected button"),
    ]

    def __init__(self, world_settings: WorldSettings) -> None:
        super().__init__()
        self.world_settings = world_settings
        self.game_engine = GameEngine(world_settings=self.world_settings)

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        with Horizontal(id="nav_buttons"):
            yield Button("[D] Details", id="details_button")
            yield Button("[O] Options", id="options_button")

        yield Static("", id="scenario_text")

        with Vertical(id="choice_buttons"):
            yield Button("", id="choice_1")
            yield Button("", id="choice_2")
            yield Button("", id="choice_3")
            yield Button("", id="choice_4")

    def on_mount(self) -> None:
        """Set initial focus and load the first scenario."""
        initial_scenario = self.game_engine.get_initial_scenario()
        self._update_scenario_view(initial_scenario)
        self.query_one("#choice_1").focus()

    def _update_scenario_view(self, scenario: Scenario) -> None:
        """Update the scenario text and choice buttons."""
        self.query_one("#scenario_text", Static).update(scenario.text)
        buttons = self.query("Vertical#choice_buttons > Button")
        num_choices = min(len(scenario.choices), 4)
        for i, button in enumerate(buttons):
            if i < num_choices:
                button.label = scenario.choices[i]
                button.display = True
            else:
                button.label = ""
                button.display = False

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "details_button":
            self.app.push_screen(DetailsViewScreen())
        elif event.button.id == "options_button":
            self.app.push_screen(OptionsMenuScreen())
        elif event.button.id.startswith("choice_"):
            choice_number = int(event.button.id.split("_")[1])
            next_scenario = self.game_engine.get_next_scenario(choice_number)
            self._update_scenario_view(next_scenario)

    def action_show_details(self) -> None:
        """Show the details screen."""
        self.app.push_screen(DetailsViewScreen())

    def action_show_options(self) -> None:
        """Show the options screen."""
        self.app.push_screen(OptionsMenuScreen())

    def action_press_choice_1(self) -> None:
        """Directly trigger choice 1."""
        button = self.query_one("#choice_1", Button)
        if not button.disabled:
            button.press()

    def action_press_choice_2(self) -> None:
        """Directly trigger choice 2."""
        button = self.query_one("#choice_2", Button)
        if not button.disabled:
            button.press()

    def action_press_choice_3(self) -> None:
        """Directly trigger choice 3."""
        button = self.query_one("#choice_3", Button)
        if not button.disabled:
            button.press()

    def action_press_choice_4(self) -> None:
        """Directly trigger choice 4."""
        button = self.query_one("#choice_4", Button)
        if not button.disabled:
            button.press()

    def action_focus_previous(self) -> None:
        """Focus on the previous button."""
        self.focus_previous(Button)

    def action_focus_next(self) -> None:
        """Focus on the next button."""
        self.focus_next(Button)

    def action_press_selected(self) -> None:
        """Trigger the currently focused button."""
        focused = self.app.focused
        if isinstance(focused, Button) and not focused.disabled:
            focused.press()
