from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label


class GameViewScreen(Screen):
    """The main game view screen."""

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        yield Label("Game View Screen")
