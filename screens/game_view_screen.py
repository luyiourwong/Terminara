from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Label

class GameViewScreen(Screen):
    """The main game view screen."""

    BINDINGS = [
        Binding("escape", "open_options_menu", "Options"),
    ]

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        yield Label("Game View Screen")

    def action_open_options_menu(self) -> None:
        """Open the options menu."""
        self.app.push_screen("options_menu")
