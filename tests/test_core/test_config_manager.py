from pathlib import Path
import pytest
from terminara.core.config_manager import ConfigManager
import platform

@pytest.fixture
def config_manager(tmp_path: Path, monkeypatch) -> ConfigManager:
    """
    Fixture to create a ConfigManager that uses a temporary directory for its config file.
    """
    # We monkeypatch the __init__ to use a temporary directory
    # This is to isolate tests from the user's actual configuration
    # and from each other.

    def mock_init(self):
        self.config_dir = tmp_path / "Terminara"
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.config_file = self.config_dir / "config.json"

    monkeypatch.setattr(ConfigManager, "__init__", mock_init)

    return ConfigManager()


class TestConfigManager:
    """Test suite for the ConfigManager class."""

    # We test the real __init__ separately without the fixture
    def test_init_creates_directory(self, monkeypatch, tmp_path: Path):
        """Test that ConfigManager's constructor creates the config directory."""

        # We patch platform.system to control which config path is used
        monkeypatch.setattr(platform, "system", lambda: "Linux")
        # We patch Path.home to point to our temp directory for predictability
        monkeypatch.setattr(Path, "home", lambda: tmp_path)

        expected_config_dir = tmp_path / '.local' / 'share' / "Terminara"
        assert not expected_config_dir.exists()

        # This should create the directory
        ConfigManager()

        assert expected_config_dir.exists()

    def test_get_config_no_file(self, config_manager: ConfigManager):
        """Test get_config() when the config file doesn't exist."""
        assert config_manager.get_config() == {}

    def test_get_config_empty_file(self, config_manager: ConfigManager):
        """Test get_config() when the config file is empty and raises JSONDecodeError."""
        config_manager.config_file.touch()
        assert config_manager.get_config() == {}

    def test_get_config_invalid_json(self, config_manager: ConfigManager):
        """Test get_config() with an invalid JSON file."""
        config_manager.config_file.write_text("this is not json")
        assert config_manager.get_config() == {}

    def test_save_and_get_config(self, config_manager: ConfigManager):
        """Test saving a configuration and then retrieving it."""
        config_data = {"hello": "world", "number": 123}
        config_manager.save_config(config_data)

        retrieved_config = config_manager.get_config()
        assert retrieved_config == config_data

    def test_get_value(self, config_manager: ConfigManager):
        """Test retrieving a single value from the configuration."""
        config_data = {"key1": "value1", "key2": "value2"}
        config_manager.save_config(config_data)

        assert config_manager.get_value("key1") == "value1"

    def test_get_nonexistent_value(self, config_manager: ConfigManager):
        """Test that get_value() returns None for a key that does not exist."""
        assert config_manager.get_value("nonexistent_key") is None

    def test_set_value(self, config_manager: ConfigManager):
        """Test setting a single value in the configuration."""
        config_manager.set_value("new_key", "new_value")

        # Verify by reading the whole config
        config = config_manager.get_config()
        assert config.get("new_key") == "new_value"

        # Verify using get_value
        assert config_manager.get_value("new_key") == "new_value"

    def test_set_value_overwrites_existing(self, config_manager: ConfigManager):
        """Test that set_value() overwrites an existing value."""
        config_manager.set_value("key_to_overwrite", "initial_value")
        config_manager.set_value("key_to_overwrite", "updated_value")

        assert config_manager.get_value("key_to_overwrite") == "updated_value"

    def test_delete_value(self, config_manager: ConfigManager):
        """Test removing a single value from the configuration."""
        config_data = {"key_to_keep": "A", "key_to_delete": "B"}
        config_manager.save_config(config_data)

        config_manager.delete_value("key_to_delete")

        config = config_manager.get_config()
        assert "key_to_keep" in config
        assert "key_to_delete" not in config

    def test_delete_nonexistent_value(self, config_manager: ConfigManager):
        """Test that deleting a nonexistent key does not raise an error."""
        config_data = {"existing_key": "value"}
        config_manager.save_config(config_data)

        config_manager.delete_value("nonexistent_key")

        # Check that the original data is untouched
        assert config_manager.get_config() == config_data