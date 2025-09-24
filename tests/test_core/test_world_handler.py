import json
import unittest
from pathlib import Path

from terminara.core.world_handler import load_world
from terminara.objects.scenario import Scenario, VariableAction
from terminara.objects.world_settings import (
    WorldSettings,
    WorldInfo,
    AiPrompt,
    Item,
    NumericVariable,
    ScenarioSettings, TextVariable,
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
                },
                "rank": {
                    "type": "text",
                    "description": "Player rank",
                    "value": "Novice",
                }
            },
            "items": {
                "potion": {
                    "name": "Health Potion",
                    "description": "Restores health.",
                    "attributes": {"heal_amount": 20},
                }
            },
            "scenario": {
                "init": {
                    "text": "You stand at the entrance to a mysterious cave in the test world.",
                    "choices": [
                        {
                            "text": "1. Enter the cave boldly"
                        },
                        {
                            "text": "2. Peek inside cautiously",
                            "actions": [
                                {
                                    "variable_name": "health",
                                    "value": "-10"
                                }
                            ]
                        },
                        {
                            "text": "3. Flee into the misty woods",
                            "actions": [
                                {
                                    "item_name": "potion",
                                    "quantity": 1
                                }
                            ]
                        }
                    ]
                }
            }
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
        self.assertIsInstance(world_settings.variables["rank"], TextVariable)
        self.assertEqual(world_settings.variables["rank"].value, "Novice")

        self.assertIn("potion", world_settings.items)
        self.assertIsInstance(world_settings.items["potion"], Item)
        self.assertEqual(world_settings.items["potion"].name, "Health Potion")

        # Test scenario loading
        self.assertIsInstance(world_settings.scenario, ScenarioSettings)
        self.assertIsNotNone(world_settings.scenario.init)
        self.assertIsInstance(world_settings.scenario.init, Scenario)
        self.assertEqual(world_settings.scenario.init.text, "You stand at the entrance to a mysterious cave in the test world.")
        self.assertEqual(len(world_settings.scenario.init.choices), 3)
        self.assertEqual(world_settings.scenario.init.choices[0].text, "1. Enter the cave boldly")
        self.assertEqual(len(world_settings.scenario.init.choices[0].actions), 0)
        self.assertEqual(world_settings.scenario.init.choices[1].text, "2. Peek inside cautiously")
        self.assertEqual(len(world_settings.scenario.init.choices[1].actions), 1)
        self.assertIsInstance(world_settings.scenario.init.choices[1].actions[0], VariableAction)
        self.assertEqual(world_settings.scenario.init.choices[1].actions[0].variable_name, "health")
        self.assertEqual(world_settings.scenario.init.choices[1].actions[0].value, "-10")


if __name__ == "__main__":
    unittest.main()