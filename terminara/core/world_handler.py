import json
from pathlib import Path
from typing import Union

from terminara.objects.world_settings import (
    WorldSettings,
    WorldInfo,
    AiPrompt,
    Item,
    NumericVariable,
    TextVariable,
    GameVariable,
)


def load_world(world_name: str) -> WorldSettings:
    """
    Loads a world from a JSON file.

    Args:
        world_name: The name of the world to load.

    Returns:
        The loaded world settings.
    """
    world_file = Path(__file__).parent.parent / "data" / "worlds" / f"{world_name}.json"

    with open(world_file, "r") as f:
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

    return WorldSettings(
        world=world_info,
        ai=ai_prompt,
        items=items,
        variables=variables,
    )