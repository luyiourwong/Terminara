import json
import os
import pathlib
from typing import Union

from terminara.objects.scenario import Scenario, Choice, ItemAction, VariableAction
from terminara.objects.world_settings import (
    WorldSettings,
    WorldInfo,
    AiPrompt,
    Item,
    NumericVariable,
    TextVariable,
    ScenarioSettings,
)


def _parse_scenario(scenario_data: dict) -> Scenario:
    choices = []
    for choice_data in scenario_data.get("choices", []):
        actions = []
        for action_data in choice_data.get("actions", []):
            if "variable_name" in action_data:
                actions.append(VariableAction(**action_data))
            elif "item_name" in action_data:
                actions.append(ItemAction(**action_data))
        choices.append(Choice(text=choice_data["text"], actions=actions))
    return Scenario(text=scenario_data["text"], choices=choices)


def load_world(world_name: str) -> WorldSettings:
    """
    Loads a world from a JSON file.

    Args:
        world_name: The name of the world to load.

    Returns:
        The loaded world settings.
    """
    world_file = pathlib.Path(os.getcwd()) / "terminara" / "data" / "worlds" / f"{world_name}.json"

    with open(world_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    world_info = WorldInfo(**data["world"])
    ai_prompt = AiPrompt(**data["ai"])

    items = {
        item_name: Item(**item_data)
        for item_name, item_data in data.get("items", {}).items()
    }

    variables: dict[str, Union[NumericVariable, TextVariable]] = {}
    for var_name, var_data in data.get("variables", {}).items():
        var_type = var_data.pop("type")
        if var_type == "numeric":
            variables[var_name] = NumericVariable(**var_data)
        elif var_type == "text":
            variables[var_name] = TextVariable(**var_data)

    scenario_settings = ScenarioSettings()
    if "scenario" in data and "init" in data["scenario"]:
        scenario_data = data["scenario"]["init"]
        scenario_settings.init = _parse_scenario(scenario_data)

    return WorldSettings(
        world=world_info,
        ai=ai_prompt,
        items=items,
        variables=variables,
        scenario=scenario_settings,
    )
