from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Button


class OptionsMenuScreen(Screen):
    """The options menu screen for the game."""

    BINDINGS = [
        Binding("r", "press_button('return')", "Return"),
        Binding("s", "press_button('save_game')", "Save Game"),
        Binding("l", "press_button('load_game')", "Load Game"),
        Binding("t", "press_button('title')", "Title"),
        Binding("e", "press_button('exit')", "Exit"),
        Binding("up", "focus_previous", "Select previous"),
        Binding("down", "focus_next", "Select next"),
        Binding("enter", "press_selected", "Activate selected button"),
    ]

    def compose(self) -> ComposeResult:
        """Create the content of the screen."""
        yield Button("[R] Return", id="return")
        yield Button("[S] Save Game", id="save_game")
        yield Button("[L] Load Game", id="load_game")
        yield Button("[T] Title", id="title")
        yield Button("[E] Exit", id="exit")

    def on_mount(self) -> None:
        """Set initial focus to the first button when the screen is mounted."""
        self.query_one("#return").focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "return":
            self.app.pop_screen()
        elif event.button.id == "save_game":
            from terminara.screens.save_game_screen import SaveGameScreen
            self.app.push_screen(SaveGameScreen())
        elif event.button.id == "load_game":
            from terminara.screens.load_game_screen import LoadGameScreen
            self.app.push_screen(LoadGameScreen())
        elif event.button.id == "title":
            from terminara.screens.main_menu_screen import MainMenuScreen
            self.app.pop_screen()
            self.app.switch_screen(MainMenuScreen())
        elif event.button.id == "exit":
            self.app.exit()

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
