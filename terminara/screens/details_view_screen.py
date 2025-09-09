from typing import cast

from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Static

from terminara.main import TerminalApp


class DetailsViewScreen(Screen):
    """The details view screen showing player information."""

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        yield Vertical(
            Static(id="details_content"),
            Button("Return", id="return_button", variant="primary"),
        )

    def on_mount(self) -> None:
        """Fetch and display the details when the screen is mounted."""
        terminal_app = cast(TerminalApp, self.app)
        state_manager = terminal_app.game_engine.state_manager
        variables = state_manager.get_all_variables()
        inventory = state_manager.get_inventory()

        # Format variables
        vars_str = "[b]Game Variables:[/b]\n"
        if variables:
            for name, value in variables.items():
                vars_str += f"  - {name}: {value}\n"
        else:
            vars_str += "  - (None)\n"

        # Format inventory
        inv_str = "\n[b]Inventory:[/b]\n"
        if inventory:
            for item, quantity in inventory.items():
                inv_str += f"  - {item}: {quantity}\n"
        else:
            inv_str += "  - (Empty)\n"

        details_content = self.query_one("#details_content", Static)
        details_content.update(vars_str + inv_str)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle the return button press."""
        if event.button.id == "return_button":
            self.app.pop_screen()
