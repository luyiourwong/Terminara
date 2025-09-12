import keyring
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Button, Input, Label

from terminara import SERVICE_NAME
from terminara.screens.load_game_screen import LoadGameScreen
from terminara.screens.new_game_screen import NewGameScreen


class MainMenuScreen(Screen):
    """The main menu screen for the game."""

    CSS = """
    #settings_box {
        margin: 0;
        padding: 0;
        border: solid white;
        height: 8;
    }
    Input {
        height: 1;
        margin: 0;
        padding: 0;
        border: none;
    }
    """

    # Define key bindings for the screen
    BINDINGS = [
        Binding("1", "press_button_1", "Press button 1"),
        Binding("2", "press_button_2", "Press button 2"),
        Binding("up", "focus_previous", "Select previous"),
        Binding("down", "focus_next", "Select next"),
        Binding("right", "press_selected", "Activate selected button"),
        Binding("enter", "press_selected", "Activate selected button"),
    ]

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        yield Button("1. Start New Game", id="start_new_game")
        yield Button("2. Load Game", id="load_game")

        with Container(id="settings_box"):
            yield Label("AI Settings: (OpenAI compatibility)")
            yield Input(placeholder="Host (Leave empty to use the default OpenAI endpoint)", id="ai_host")
            yield Input(placeholder="Key", id="ai_key", password=True)
            yield Input(placeholder="Model", id="ai_model")
            yield Button("Apply", id="apply_settings")
            yield Button("Clear", id="clear_settings")

    def on_mount(self) -> None:
        """Set initial focus and load settings when the screen is mounted."""
        self.query_one("#start_new_game").focus()

        # Load saved settings from keyring
        ai_host = keyring.get_password(SERVICE_NAME, "ai_host")
        ai_key = keyring.get_password(SERVICE_NAME, "ai_key")
        ai_model = keyring.get_password(SERVICE_NAME, "ai_model")

        if ai_host:
            self.query_one("#ai_host", Input).value = ai_host
        if ai_key:
            self.query_one("#ai_key", Input).value = ai_key
        if ai_model:
            self.query_one("#ai_model", Input).value = ai_model

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "start_new_game":
            self.app.switch_screen(NewGameScreen())
        elif event.button.id == "load_game":
            self.app.push_screen(LoadGameScreen())
        elif event.button.id == "apply_settings":
            # Save the settings to keyring
            ai_host = self.query_one("#ai_host", Input).value
            ai_key = self.query_one("#ai_key", Input).value
            ai_model = self.query_one("#ai_model", Input).value

            keyring.set_password(SERVICE_NAME, "ai_host", ai_host)
            keyring.set_password(SERVICE_NAME, "ai_key", ai_key)
            keyring.set_password(SERVICE_NAME, "ai_model", ai_model)
        elif event.button.id == "clear_settings":
            # Clear the input fields
            self.query_one("#ai_host", Input).value = ""
            self.query_one("#ai_key", Input).value = ""
            self.query_one("#ai_model", Input).value = ""

            # Delete the saved credentials
            keyring.delete_password(SERVICE_NAME, "ai_host")
            keyring.delete_password(SERVICE_NAME, "ai_key")
            keyring.delete_password(SERVICE_NAME, "ai_model")

    def action_press_button_1(self) -> None:
        """Directly trigger the first button (Start New Game)."""
        button = self.query_one("#start_new_game", Button)
        if not button.disabled:
            button.press()

    def action_press_button_2(self) -> None:
        """Directly trigger the second button (Load Game)."""
        button = self.query_one("#load_game", Button)
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
