class GameEngine:
    def __init__(self):
        self._scenarios = [
            {
                "text": "You find yourself standing at the edge of a mysterious forest. The ancient trees tower above you, their branches swaying gently in the wind. Strange sounds echo from within the depths of the woodland. What do you choose to do?",
                "choices": [
                    "1. Enter the forest cautiously",
                    "2. Call out to see if anyone responds",
                    "3. Search for another path around",
                    "4. Turn back and leave",
                ],
            },
            {
                "text": "You step into the forest. A thick fog surrounds you, and the path ahead is barely visible. You hear a twig snap nearby.",
                "choices": [
                    "1. Investigate the sound",
                    "2. Stay still and listen",
                    "3. Continue cautiously on the path",
                    "4. Retreat from the forest",
                ],
            },
        ]
        self._current_scenario_index = 0

    def get_initial_scenario(self):
        return self._scenarios[0]

    def get_next_scenario(self, choice: int):
        # This is a placeholder implementation that ignores the choice and cycles
        # between the two scenarios.
        self._current_scenario_index = (self._current_scenario_index + 1) % len(
            self._scenarios
        )
        return self._scenarios[self._current_scenario_index]