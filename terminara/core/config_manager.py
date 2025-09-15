import os
import json
import platform
from pathlib import Path


class ConfigManager:
    """Manages AI configurations."""

    def __init__(self):
        """Initializes the AiConfigManager and ensures the config directory exists."""
        system = platform.system()
        if system == "Windows":
            base_dir = Path(os.environ.get('LOCALAPPDATA', Path.home() / 'AppData' / 'Local'))
        elif system == "Darwin":  # macOS
            base_dir = Path.home() / 'Library' / 'Application Support'
        else:  # Linux
            base_dir = Path.home() / '.local' / 'share'

        self.config_dir = base_dir / "Terminara"
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.config_file = self.config_dir / "config.json"

    def get_config(self) -> dict:
        """
        Loads the configuration from ai_config.json.

        Returns:
            dict: The configuration data. Returns an empty dictionary if the file doesn't exist.
        """
        if not self.config_file.exists():
            return {}
        with open(self.config_file, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def save_config(self, config_data: dict):
        """
        Saves a dictionary to ai_config.json.

        Args:
            config_data (dict): The configuration data to save.
        """
        with open(self.config_file, 'w') as f:
            json.dump(config_data, f, indent=4)

    def get_value(self, key: str):
        """
        Retrieves a single value from the configuration.

        Args:
            key (str): The key of the value to retrieve.

        Returns:
            The value associated with the key, or None if the key doesn't exist.
        """
        config = self.get_config()
        return config.get(key)

    def set_value(self, key: str, value):
        """
        Sets a single value in the configuration.

        Args:
            key (str): The key of the value to set.
            value: The value to set.
        """
        config = self.get_config()
        config[key] = value
        self.save_config(config)

    def delete_value(self, key: str):
        """
        Removes a single value from the configuration.

        Args:
            key (str): The key of the value to remove.
        """
        config = self.get_config()
        if key in config:
            del config[key]
            self.save_config(config)
