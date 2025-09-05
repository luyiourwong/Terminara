from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button

from terminara.screens.game_view_screen import GameViewScreen


class NewGameScreen(Screen):
    """The new game screen for the game."""

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        yield Button("Start Game", id="start_game")

    def on_mount(self) -> None:
        """Set initial focus to the first button when the screen is mounted."""
        self.query_one("#start_game").focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "start_game":
            self.app.push_screen(GameViewScreen())
