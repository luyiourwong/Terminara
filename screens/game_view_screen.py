from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Button, Static
from textual.containers import Vertical, Horizontal

from screens.details_view_screen import DetailsViewScreen
from screens.options_menu_screen import OptionsMenuScreen


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

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        with Horizontal(id="nav_buttons"):
            yield Button("[D] Details", id="details_button")
            yield Button("[O] Options", id="options_button")
        
        yield Static(
            "You find yourself standing at the edge of a mysterious forest. "
            "The ancient trees tower above you, their branches swaying gently in the wind. "
            "Strange sounds echo from within the depths of the woodland. "
            "What do you choose to do?",
            id="scenario_text"
        )
        
        with Vertical(id="choice_buttons"):
            yield Button("1. Enter the forest cautiously", id="choice_1")
            yield Button("2. Call out to see if anyone responds", id="choice_2")
            yield Button("3. Search for another path around", id="choice_3")
            yield Button("4. Turn back and leave", id="choice_4")

    def on_mount(self) -> None:
        """Set initial focus to the first choice button when the screen is mounted."""
        self.query_one("#choice_1").focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "details_button":
            self.app.push_screen(DetailsViewScreen())
        elif event.button.id == "options_button":
            self.app.push_screen(OptionsMenuScreen())
        elif event.button.id in ["choice_1", "choice_2", "choice_3", "choice_4"]:
            pass

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
