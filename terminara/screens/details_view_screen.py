from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Label


class DetailsViewScreen(Screen):
    """The details view screen showing player information."""

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        yield Label("Details View Screen - Player information will be displayed here")
