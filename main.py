import os

from textual.app import App

from screens.main_menu_screen import MainMenuScreen


class TerminalApp(App):
    CSS_PATH = os.path.join("screens", "styles.tcss")

    def on_mount(self) -> None:
        self.app.push_screen(MainMenuScreen())


if __name__ == "__main__":
    main_app = TerminalApp()
    main_app.run()
