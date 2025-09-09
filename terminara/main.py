import os
import sys
from typing import Optional

from textual.app import App

from terminara.core.game_engine import GameEngine
from terminara.objects.world_settings import WorldSettings


def get_resource_path(relative_path):
    """Get the absolute path of the resource file, suitable for development and packaging environments"""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller packaged environment
        return os.path.join(getattr(sys, '_MEIPASS'), relative_path)
    # Development Environment
    return os.path.join(os.path.dirname(__file__), relative_path)


class TerminalApp(App):
    CSS_PATH = get_resource_path(os.path.join("screens", "styles.tcss"))

    game_engine: Optional[GameEngine] = None

    def on_mount(self) -> None:
        from terminara.screens.main_menu_screen import MainMenuScreen
        self.push_screen(MainMenuScreen())

    def start_game(self, world_settings: WorldSettings):
        """Start a new game."""
        self.game_engine = GameEngine(world_settings=world_settings)
        from terminara.screens.game_view_screen import GameViewScreen
        self.push_screen(GameViewScreen())


def main():
    """Main entry point for the application."""
    main_app = TerminalApp()
    main_app.run()


if __name__ == "__main__":
    main()
