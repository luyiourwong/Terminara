import unittest
from pathlib import Path
import json

from terminara.core.world_handler import load_world
from terminara.objects.world_settings import (
    WorldSettings,
    WorldInfo,
    AiPrompt,
    Item,
    NumericVariable,
)


class TestWorldHandler(unittest.TestCase):
    def setUp(self):
        self.worlds_dir = Path("terminara") / "data" / "worlds"
        self.worlds_dir.mkdir(exist_ok=True)
        self.test_world_data = {
            "world": {"name": "test_world", "description": "A test world"},
            "ai": {
                "system": "Test system prompt",
                "prompt": "Test user prompt",
                "lore": {"key": "value"},
            },
            "variables": {
                "health": {
                    "type": "numeric",
                    "description": "Player health",
                    "value": 100,
                    "min_value": 0,
                    "max_value": 100,
                }
            },
            "items": {
                "potion": {
                    "name": "Health Potion",
                    "description": "Restores health.",
                    "attributes": {"heal_amount": 20},
                }
            },
        }
        self.test_world_file = self.worlds_dir / "test_world.json"
        with open(self.test_world_file, "w") as f:
            json.dump(self.test_world_data, f)

    def tearDown(self):
        self.test_world_file.unlink()

    def test_load_world(self):
        world_settings = load_world("test_world")

        self.assertIsInstance(world_settings, WorldSettings)
        self.assertIsInstance(world_settings.world, WorldInfo)
        self.assertEqual(world_settings.world.name, "test_world")

        self.assertIsInstance(world_settings.ai, AiPrompt)
        self.assertEqual(world_settings.ai.system, "Test system prompt")

        self.assertIn("health", world_settings.variables)
        self.assertIsInstance(world_settings.variables["health"], NumericVariable)
        self.assertEqual(world_settings.variables["health"].value, 100)

        self.assertIn("potion", world_settings.items)
        self.assertIsInstance(world_settings.items["potion"], Item)
        self.assertEqual(world_settings.items["potion"].name, "Health Potion")


if __name__ == "__main__":
    unittest.main()