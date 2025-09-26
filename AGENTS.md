# Terminara

A terminal-based ai simulation game.

## Usage
Read [CONTRIBUTING](CONTRIBUTING.md) for instructions on how to run the project in development mode.

## Objective

To create a terminal-based AI simulation game using Python and the `textual` library. The game features an AI-driven storyteller that generates scenarios and choices for the player within a customizable world setting.

## Structure

```
.
|-- terminara/
|   |-- __init__.py         # Auto versioning via Release Please
|   |-- main.py             # Application entry point
|   |-- core/
|   |   |-- __init__.py
|   |   |-- game_engine.py    # Main game loop and logic
|   |   |-- ai_narrator.py    # Handles interaction with the AI model
|   |   |-- state_manager.py  # Manages game state, saving, and loading
|   |   `-- world_handler.py  # Handles importing/exporting of world settings
|   |-- objects/
|   |   |-- __init__.py
|   |   |-- game_state.py     # Defines the data structure for game state
|   |   |-- world_settings.py # Defines the data structure for world settings
|   |   `-- scenario.py       # Defines the data structure for game scenarios
|   |-- screens/
|   |   |-- __init__.py
|   |   |-- main_menu_screen.py      # Main menu screen (default entry view)
|   |   |-- new_game_screen.py       # Screen for configuring new game settings
|   |   |-- game_view_screen.py      # Main gameplay screen
|   |   |-- details_view_screen.py   # Screen for displaying player details
|   |   |-- options_menu_screen.py   # Screen for game options
|   |   |-- load_game_screen.py      # Screen for loading saved game files
|   |   |-- save_game_screen.py      # Screen for saving saved game files
|   |   |-- styles.tcss              # Styles for the screens
|   |   `-- widgets/
|   |       |-- __init__.py
|   |       `-- file_list_item.py    # Widget for displaying save files in a list
|   `-- data/
|       |-- schema/           # Json schema files for world settings and saves
|       |-- saves/            # Directory for saved game files
|       `-- worlds/           # Directory for world setting files
|-- tests/
|   |-- __init__.py
|   `-- test_core/
|       |-- __init__.py
|       `-- test_world_handler.py       # Unit test files
|-- AGENTS.md             # Guide for AI coding agents
|-- CONTRIBUTING.md       # Guide for contribute & development
|-- README.md             # Guide for using this project
|-- pyproject.toml        # Python project configuration
`-- terminara.spec        # PyInstaller spec file
```

## Key Functional

- **AI as Game Master:** The core of the game is an AI that generates narrative scenarios and player choices based on a predefined world setting.
- **Text-Based GUI:** The user interface is built with `textual`, focusing on a clean, text-centric experience.
- **Context Caching System:** A temporary storage system to provide the AI with consistent memory and context, independent of the AI's own memory limitations.
- **Save & Load System:** Allows players to save their game progress and load it later.
- **World Setting Management:** World settings can be exported to a file for sharing and imported to start new games in different worlds.
