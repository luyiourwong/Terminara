import os
import sys
from typing import Optional

from textual.app import App

from terminara.core.config_manager import ConfigManager
from terminara.core.game_engine import GameEngine
from terminara.objects.game_state import GameState
from terminara.objects.scenario import Scenario
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

    config_manager: Optional[ConfigManager] = None
    world_settings_file: Optional[str] = None
    game_engine: Optional[GameEngine] = None

    def __init__(self) -> None:
        super().__init__()
        self.config_manager = ConfigManager()

    def on_mount(self) -> None:
        from terminara.screens.main_menu_screen import MainMenuScreen
        self.push_screen(MainMenuScreen())

    def start_game(self, world_settings: WorldSettings):
        """Start a new game."""
        self.game_engine = GameEngine(self, world_settings=world_settings)
        from terminara.screens.game_view_screen import GameViewScreen
        self.switch_screen(GameViewScreen())

    def load_game(self, world_settings: WorldSettings, game_state: GameState, load_scenario: Scenario):
        """Load a saved game."""
        self.game_engine = GameEngine(self, world_settings=world_settings, game_state=game_state, load_scenario=load_scenario)  # noqa: E501

        # Check if GameViewScreen exists, if not create it
        try:
            game_screen = self.app.get_screen("GameViewScreen")
            game_screen.pop_until_active()
        except KeyError:
            # Screen doesn't exist, create and push it
            from terminara.screens.game_view_screen import GameViewScreen
            self.switch_screen(GameViewScreen())


def main():
    """Main entry point for the application."""
    main_app = TerminalApp()
    main_app.run()


if __name__ == "__main__":
    main()
