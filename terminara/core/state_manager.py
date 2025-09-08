from typing import Dict, Any

from terminara.objects.world_settings import WorldSettings


class StateManager:
    """Manages the game state, including variables and inventory."""

    def __init__(self, world_settings: WorldSettings):
        """
        Initializes the StateManager with the given world settings.

        Args:
            world_settings: The world settings object.
        """
        self._variables: Dict[str, Any] = {
            name: var.value for name, var in world_settings.variables.items()
        }
        self._inventory: Dict[str, int] = {}
        # Known items are stored in world_settings.items, but inventory starts empty.

    def get_variable(self, name: str) -> Any:
        """
        Gets the value of a game variable.

        Args:
            name: The name of the variable.

        Returns:
            The value of the variable, or None if it doesn't exist.
        """
        return self._variables.get(name)

    def set_variable(self, name: str, value: Any):
        """
        Sets the value of a game variable.

        Args:
            name: The name of the variable.
            value: The new value for the variable.
        """
        self._variables[name] = value

    def get_all_variables(self) -> Dict[str, Any]:
        """
        Gets the entire variables dictionary.

        Returns:
            A dictionary containing all game variables.
        """
        return self._variables

    def get_inventory(self) -> Dict[str, int]:
        """
        Gets the player's current inventory.

        Returns:
            A dictionary representing the inventory (item_name: quantity).
        """
        return self._inventory

    def add_item(self, item_name: str, quantity: int = 1):
        """
        Adds an item to the inventory.

        Args:
            item_name: The name of the item to add.
            quantity: The quantity to add.
        """
        if quantity <= 0:
            return
        self._inventory[item_name] = self._inventory.get(item_name, 0) + quantity

    def remove_item(self, item_name: str, quantity: int = 1):
        """
        Removes an item from the inventory.

        Args:
            item_name: The name of the item to remove.
            quantity: The quantity to remove.
        """
        if quantity <= 0:
            return
        current_quantity = self._inventory.get(item_name, 0)
        if current_quantity > quantity:
            self._inventory[item_name] = current_quantity - quantity
        else:
            self._inventory.pop(item_name, None)

    def save_game(self, file_path: str):
        """
        Saves the current game state to a file. (Not yet implemented)

        Args:
            file_path: The path to the save file.
        """
        pass

    def load_game(self, file_path: str):
        """
        Loads the game state from a file. (Not yet implemented)

        Args:
            file_path: The path to the save file.
        """
        pass