from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Button


class MainMenuScreen(Screen):
    """The main menu screen for the game."""

    # Define key bindings for the screen
    BINDINGS = [
        Binding("1", "press_button_1", "Press button 1"),
        Binding("2", "press_button_2", "Press button 2"),
        Binding("up", "focus_previous", "Select previous"),
        Binding("down", "focus_next", "Select next"),
        Binding("enter", "press_selected", "Activate selected button"),
    ]

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        yield Button("1. Start New Game", id="start_new_game")
        yield Button("2. Load Game", id="load_game")

    def on_mount(self) -> None:
        """Set initial focus to the first button when the screen is mounted."""
        self.query_one("#start_new_game").focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "start_new_game":
            # TODO: Implement start new game functionality
            pass
        elif event.button.id == "load_game":
            # TODO: Implement load game functionality
            pass

    def action_press_button_1(self) -> None:
        """Directly trigger the first button (Start New Game)."""
        button = self.query_one("#start_new_game", Button)
        if not button.disabled:
            button.press()

    def action_press_button_2(self) -> None:
        """Directly trigger the second button (Load Game)."""
        button = self.query_one("#load_game", Button)
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
