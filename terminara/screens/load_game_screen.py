import json
import os
from typing import cast

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.screen import ModalScreen
from textual.widgets import ListView, Static, Button

from terminara.main import TerminalApp
from terminara.objects.game_state import GameState
from terminara.screens.widgets.file_list_item import FileListItem

SAVES_DIR = os.path.join(os.getcwd(), "terminara", "data", "saves")


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
        yield Static("Load Game")
        yield Static("---")
        with Vertical(id="save-game-container"):
            yield ListView(id="save-game-list")
        yield Static("---")
        yield Button("[R] Return", id="return")

    def _refresh_save_list(self) -> None:
        """Clears and repopulates the list of save files."""
        list_view = self.query_one(ListView)
        list_view.clear()  # Clear existing items

        if not os.path.exists(SAVES_DIR):
            os.makedirs(SAVES_DIR)

        # Get all json files with their modification times
        save_files_with_times = []
        for filename in os.listdir(SAVES_DIR):
            if filename.endswith(".json"):
                file_path = os.path.join(SAVES_DIR, filename)
                try:
                    mod_time = os.path.getmtime(file_path)
                    save_files_with_times.append((mod_time, file_path))
                except FileNotFoundError:
                    # Handle cases where file might be deleted between listdir and getmtime
                    pass

        # Sort files by modification time in descending order (newest first)
        save_files_with_times.sort(key=lambda x: x[0], reverse=True)

        for mod_time, file_path in save_files_with_times:
            list_view.append(FileListItem(file_path))

    def on_mount(self) -> None:
        """Populate the list of save files."""
        self._refresh_save_list()

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Handle a save file being selected."""
        if isinstance(event.item, FileListItem):
            self.load_file(event.item.file_path)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle the 'Save as New' button being pressed."""
        if event.button.id == "return":
            self.app.pop_screen()

    def load_file(self, file_name: str) -> None:
        """Load a save file."""
        terminal_app = cast(TerminalApp, self.app)
        file_path = os.path.join(SAVES_DIR, file_name)
        if not os.path.exists(file_path):
            print(f"Error: Save file '{file_path}' not found.")
            return
        with open(file_path, "r") as f:
            save_data = json.load(f)

        world_name = save_data.get("world")
        game_state_dict = save_data.get("game_state")
        if not world_name or game_state_dict is None:
            print(f"Error: Invalid save file format in '{file_name}'. Missing 'world' or 'game_state'.")
            return
        # Loading World Settings
        from terminara.core.world_handler import load_world
        world_settings = load_world(world_name)
        try:
            game_state = GameState(
                variables=game_state_dict.get('variables', {}),
                inventory=game_state_dict.get('inventory', {})
            )
        except Exception as e:
            print(f"Error: Failed to reconstruct GameState from loaded data: {e}")
            return
        # Set the current world setting file in the application, consistent with `action_load_world`
        terminal_app.world_settings_file = world_name
        terminal_app.load_game(world_settings, game_state)

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
        if isinstance(focused, ListView) and not focused.disabled:
            highlight_item = focused.highlighted_child
            if isinstance(highlight_item, FileListItem):
                self.load_file(highlight_item.file_path)
