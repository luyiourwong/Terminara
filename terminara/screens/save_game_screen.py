import json
import os
from datetime import datetime
from typing import cast

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import ListView, Button, Static

from terminara.main import TerminalApp
from terminara.screens.widgets.file_list_item import FileListItem

SAVES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "saves")


class SaveGameScreen(ModalScreen):
    """A modal screen for saving the current game."""

    BINDINGS = [
        Binding("r", "press_button('return')", "Return"),
        Binding("s", "press_button('save-new-button')", "Quick Save"),
        Binding("up", "focus_previous", "Select previous"),
        Binding("down", "focus_next", "Select next"),
        Binding("left", "press_button('return')", "Return"),
        Binding("right", "press_selected", "Activate selected button"),
        Binding("enter", "press_selected", "Activate selected button"),
    ]

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        yield Static("Save Game (Press tab to switch focus)")
        yield Static("---")
        with Vertical(id="save-game-container"):
            yield ListView(id="save-game-list")
        yield Static("---")
        yield Button("[S] Save new file", id="save-new-button")
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
        self.query_one("#save-new-button").focus()

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Handle a save file being selected for overwriting."""
        if isinstance(event.item, FileListItem):
            self.dismiss(event.item.file_path)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle the 'Save as New' button being pressed."""
        if event.button.id == "return":
            self.app.pop_screen()
        elif event.button.id == "save-new-button":
            terminal_app = cast(TerminalApp, self.app)
            game_state = terminal_app.game_engine.state_manager.save_game()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{terminal_app.world_settings_file}_{timestamp}.json"
            save_data = {
                "world": f"{terminal_app.world_settings_file}.json",
                "game_state": game_state
            }
            file_path = os.path.join(SAVES_DIR, file_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as f:
                json.dump(save_data, f, indent=4)
            self.dismiss(file_path)

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