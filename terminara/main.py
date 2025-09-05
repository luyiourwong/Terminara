import os
import sys

from textual.app import App

from terminara.screens.main_menu_screen import MainMenuScreen


def get_resource_path(relative_path):
    """Get the absolute path of the resource file, suitable for development and packaging environments"""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller packaged environment
        return os.path.join(getattr(sys, '_MEIPASS'), relative_path)
    # Development Environment
    return os.path.join(os.path.dirname(__file__), relative_path)


class TerminalApp(App):
    CSS_PATH = get_resource_path(os.path.join("screens", "styles.tcss"))

    def on_mount(self) -> None:
        self.push_screen(MainMenuScreen())

def main():
    """Main entry point for the application."""
    main_app = TerminalApp()
    main_app.run()

if __name__ == "__main__":
    main()
