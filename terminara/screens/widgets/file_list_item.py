import os
from datetime import datetime

from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import ListItem, Label, Static


class FileListItem(ListItem):
    """A ListItem that displays a filename and its modification time."""

    def __init__(self, file_path: str) -> None:
        super().__init__()
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        try:
            mod_time = os.path.getmtime(file_path)
            self.mod_time_str = datetime.fromtimestamp(mod_time).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        except FileNotFoundError:
            self.mod_time_str = "New File"

    def compose(self) -> ComposeResult:
        """Create the content of the list item."""
        with Horizontal():
            yield Label(self.file_name, classes="file-name")
            yield Static("---")
            yield Label(self.mod_time_str, classes="file-mod-time")