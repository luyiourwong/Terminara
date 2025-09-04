from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label


class OptionsMenuScreen(Screen):
    """The options menu screen for game settings."""

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        yield Label("Options Menu Screen - Game settings will be displayed here")
