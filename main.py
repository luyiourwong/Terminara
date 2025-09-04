import os

from textual.app import App

from screens.main_menu_screen import MainMenuScreen
from screens.options_menu_screen import OptionsMenuScreen
from screens.game_view_screen import GameViewScreen


class TerminalApp(App):
    CSS_PATH = os.path.join("screens", "styles.tcss")

    SCREENS = {
        "main_menu": MainMenuScreen,
        "options_menu": OptionsMenuScreen,
        "game_view": GameViewScreen,
    }

    def on_mount(self) -> None:
        self.push_screen(MainMenuScreen())


if __name__ == "__main__":
    main_app = TerminalApp()
    main_app.run()
