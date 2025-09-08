import pathlib
from typing import Optional, cast

from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Button, Select, Static

from terminara.core.world_handler import load_world
from terminara.main import TerminalApp
from terminara.objects.world_settings import WorldSettings


class NewGameScreen(Screen):
    """The new game screen for the game."""

    world_settings: Optional[WorldSettings] = None

    BINDINGS = [
        Binding("1", "load_world", "Load World"),
        Binding("2", "start_game", "Start Game"),
        Binding("up", "focus_previous", "Select previous"),
        Binding("down", "focus_next", "Select next"),
        Binding("enter", "press_selected", "Activate selected button"),
    ]

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        yield Select([], prompt="Select a world (Press Enter to select)")
        yield Static("---")
        yield Static("World Name: ", id="world_name")
        yield Static("Description: ", id="world_description")
        yield Static("System Prompt: ", id="system_prompt")
        yield Static("User Prompt: ", id="user_prompt")
        yield Static("Lore Entries: ", id="lore_entries")
        yield Static("Game Variables: ", id="game_variables")
        yield Static("Items: ", id="items")
        yield Static("---")
        yield Button("1. Load World", id="load_world")
        yield Button("2. Start Game", id="start_game", disabled=True)

    def on_mount(self) -> None:
        """Populate the select widget with world files."""
        worlds_path = pathlib.Path(__file__).parent.parent / "data" / "worlds"
        world_files = [
            f.stem for f in worlds_path.iterdir() if f.suffix == ".json" and f.stem != "world_schema"
        ]
        self.query_one(Select).set_options([(world, world) for world in world_files])

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "load_world":
            self.action_load_world()
        elif event.button.id == "start_game":
            self.action_start_game()

    def action_load_world(self) -> None:
        """Handle the load world button press."""
        world_name = self.query_one(Select).value
        if world_name:
            self.world_settings = load_world(str(world_name))
            self.query_one("#world_name", Static).update(
                f"World Name: {self.world_settings.world.name}"
            )
            self.query_one("#world_description", Static).update(
                f"Description: {self.world_settings.world.description}"
            )
            self.query_one("#system_prompt", Static).update(
                f"System Prompt: {'Set' if self.world_settings.ai.system else 'Not Set'}"
            )
            self.query_one("#user_prompt", Static).update(
                f"User Prompt: {'Set' if self.world_settings.ai.prompt else 'Not Set'}"
            )
            self.query_one("#lore_entries", Static).update(
                f"Lore Entries ({len(self.world_settings.ai.lore)}): {', '.join(self.world_settings.ai.lore.keys())}"
            )
            self.query_one("#game_variables", Static).update(
                f"Game Variables ({len(self.world_settings.variables)}): {', '.join(self.world_settings.variables.keys())}"
            )
            self.query_one("#items", Static).update(
                f"Items ({len(self.world_settings.items)}): {', '.join(self.world_settings.items.keys())}"
            )
            self.query_one("#start_game", Button).disabled = False

    def action_start_game(self) -> None:
        """Handle button press events."""
        if self.world_settings:
            terminal_app = cast(TerminalApp, self.app)
            terminal_app.start_game(world_settings=self.world_settings)

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
