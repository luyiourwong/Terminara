from typing import cast

from textual import work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Button, Static, Input
from textual.containers import Vertical, Horizontal

from terminara.main import TerminalApp
from terminara.objects.scenario import Scenario, Choice
from terminara.screens.details_view_screen import DetailsViewScreen
from terminara.screens.options_menu_screen import OptionsMenuScreen


class GameViewScreen(Screen):
    """The main game view screen."""

    CSS = """
    #nav_header {
        height: 1;
        dock: top;
    }
    
    #nav_header Button {
        width: auto;
        margin-right: 1;
    }

    #loading_status {
        width: auto;
        margin-left: 1;
    }
    
    #scenario_text {
        margin: 1 0;
        padding: 1;
        border: solid white;
    }
    
    #choice_buttons {
        dock: bottom;
        height: 5;
    }
    
    #choice_buttons Button {
        margin-bottom: 0;
    }

    #custom_choice_input {
        height: 1;
        margin: 0;
        padding: 0;
        border: none;
    }
    """

    BINDINGS = [
        Binding("d", "press_button('details_button')", "Details"),
        Binding("o", "press_button('options_button')", "Options"),
        Binding("1", "press_button('choice_1')", "Choice 1"),
        Binding("2", "press_button('choice_2')", "Choice 2"),
        Binding("3", "press_button('choice_3')", "Choice 3"),
        Binding("4", "press_button('choice_4')", "Choice 4"),
        Binding("up", "focus_previous", "Select previous"),
        Binding("down", "focus_next", "Select next"),
        Binding("left", "press_button('details_button')", "Details"),
        Binding("right", "press_selected", "Activate selected button"),
        Binding("enter", "press_selected", "Activate selected button"),
    ]

    def __init__(self) -> None:
        super().__init__()

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        with Horizontal(id="nav_header"):
            yield Button("[D] Details", id="details_button")
            yield Button("[O] Options", id="options_button")
            yield Static(id="loading_status")

        yield Static("", id="scenario_text")

        with Vertical(id="choice_buttons"):
            yield Button("", id="choice_1")
            yield Button("", id="choice_2")
            yield Button("", id="choice_3")
            yield Button("", id="choice_4")
            yield Input(placeholder="Or type your own choice...", id="custom_choice_input")

    def on_mount(self) -> None:
        """Set initial focus and load the first scenario."""
        terminal_app = cast(TerminalApp, self.app)
        self._update_scenario_view(terminal_app.game_engine.get_current_scenario())
        self.query_one("#choice_1").focus()

    def _update_scenario_view(self, scenario: Scenario) -> None:
        """Update the scenario text and choice buttons."""
        self.query_one("#scenario_text", Static).update(scenario.text)
        buttons = self.query("Vertical#choice_buttons > Button")
        num_choices = min(len(scenario.choices), 4)
        for i, button in enumerate(buttons):
            if i < num_choices:
                button.label = scenario.choices[i].text
                button.display = True
            else:
                button.label = ""
                button.display = False

    def _toggle_ui_elements(self, disabled: bool) -> None:
        """Enable or disable the choice buttons and custom input."""
        self.query_one("#choice_buttons").disabled = disabled
        self.query_one("#custom_choice_input").disabled = disabled
        self.query_one("#details_button").disabled = disabled
        self.query_one("#options_button").disabled = disabled

    def _process_choice(self, choice: Choice) -> None:
        """Process the player's choice and fetch the next scenario."""
        loading_status = self.query_one("#loading_status", Static)
        loading_status.update("generating next scenario...")
        self._toggle_ui_elements(True)

        # 启动 worker 处理耗时操作
        self._get_scenario_worker(choice)

    @work(thread=True)
    def _get_scenario_worker(self, choice: Choice) -> None:
        """Worker to fetch the next scenario in background."""
        terminal_app = cast(TerminalApp, self.app)
        next_scenario = terminal_app.game_engine.get_next_scenario(choice)

        # 使用 call_from_thread 安全地更新 UI
        self.app.call_from_thread(self._update_scenario_complete, next_scenario)

    def _update_scenario_complete(self, next_scenario: Scenario) -> None:
        """Complete the scenario update on the main thread."""
        self._update_scenario_view(next_scenario)
        loading_status = self.query_one("#loading_status", Static)
        loading_status.update("")
        self._toggle_ui_elements(False)
        self.query_one("#choice_1").focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "details_button":
            self.app.push_screen(DetailsViewScreen())
        elif event.button.id == "options_button":
            self.app.push_screen(OptionsMenuScreen())
        elif event.button.id.startswith("choice_"):
            choice_number = int(event.button.id.split("_")[1])
            terminal_app = cast(TerminalApp, self.app)
            current_choice = terminal_app.game_engine.get_choice(choice_number)
            self._process_choice(current_choice)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle the submission of the custom choice input."""
        custom_choice = Choice(text=event.value)
        self._process_choice(custom_choice)
        event.input.clear()

    def action_press_button(self, button_id: str) -> None:
        """Press a button by its ID."""
        button = self.query_one(f"#{button_id}", Button)
        if not button.disabled:
            button.press()

    def action_focus_previous(self) -> None:
        """Focus on the previous button."""
        self.focus_previous()

    def action_focus_next(self) -> None:
        """Focus on the next button."""
        self.focus_next()

    def action_press_selected(self) -> None:
        """Trigger the currently focused button."""
        focused = self.app.focused
        if isinstance(focused, Button) and not focused.disabled:
            focused.press()
