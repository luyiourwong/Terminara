import os

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import ListView, Static, Button

from terminara.screens.widgets.file_list_item import FileListItem

SAVES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "saves")


class LoadGameScreen(ModalScreen):
    """A modal screen for loading a saved game."""

    BINDINGS = [
        Binding("r", "press_button('return')", "Return"),
        Binding("up", "focus_previous", "Select previous"),
        Binding("down", "focus_next", "Select next"),
        Binding("left", "press_button('return')", "Return"),
        Binding("right", "press_selected", "Activate selected button"),
        Binding("enter", "press_selected", "Activate selected button"),
    ]

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        yield Static("Load Game (Press tab to switch focus)")
        yield Static("---")
        with Vertical(id="load-game-container"):
            yield ListView(id="load-game-list")
        yield Static("---")
        yield Button("[R] Return", id="return")

    def on_mount(self) -> None:
        """Populate the list of save files."""
        list_view = self.query_one(ListView)
        if not os.path.exists(SAVES_DIR):
            os.makedirs(SAVES_DIR)

        for filename in os.listdir(SAVES_DIR):
            if filename.endswith(".json"):
                file_path = os.path.join(SAVES_DIR, filename)
                list_view.append(FileListItem(file_path))

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Handle a save file being selected."""
        if isinstance(event.item, FileListItem):
            self.dismiss(event.item.file_path)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle the 'Save as New' button being pressed."""
        if event.button.id == "return":
            self.app.pop_screen()

    def action_press_button(self, button_id: str) -> None:
        """Press a button by its ID."""
        button = self.query_one(f"#{button_id}", Button)
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
