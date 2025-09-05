# Terminara

A terminal-based ai simulation game.

## Usage
### Method 1: Install as package (Recommended)
```bash
pip install -e .
```
then run the game with:
```bash
terminara
```

### Method 2: Direct execution
Cross-platform way
```bash
python -m terminara.main
```
or
```bash
python terminara/main.py
```

### Method 3: Background execution for testing
This is a long-live program, so if you want to test it, you can use this command instead:

Unix/Linux/macOS
```bash
python -m terminara.main > app.log 2>&1 &
```

## Objective

To create a terminal-based AI simulation game using Python and the `textual` library. The game features an AI-driven storyteller that generates scenarios and choices for the player within a customizable world setting.

## Structure

```
terminara/
|-- main.py             # Application entry point
|-- core/
|   |-- __init__.py
|   |-- game_engine.py    # Main game loop and logic
|   |-- ai_narrator.py    # Handles interaction with the AI model
|   |-- state_manager.py  # Manages game state, saving, and loading
|   `-- world_handler.py  # Handles importing/exporting of world settings
|-- objects/
|   |-- __init__.py
|   `-- scenario.py       # Defines the data structure for game scenarios
|-- screens/
|   |-- __init__.py
|   |-- main_menu_screen.py      # Main menu screen (default entry view)
|   |-- new_game_screen.py       # Screen for configuring new game settings
|   |-- game_view_screen.py      # Main gameplay screen
|   |-- details_view_screen.py   # Screen for displaying player details
|   `-- options_menu_screen.py   # Screen for game options
|-- data/
|   |-- saves/            # Directory for saved game files
|   `-- worlds/           # Directory for world setting files
|-- requirements.txt
`-- terminara.spec        # PyInstaller spec file
```

## Key Functional

- **AI as Game Master:** The core of the game is an AI that generates narrative scenarios and player choices based on a predefined world setting.
- **Text-Based GUI:** The user interface is built with `textual`, focusing on a clean, text-centric experience.
- **Context Caching System:** A temporary storage system to provide the AI with consistent memory and context, independent of the AI's own memory limitations.
- **Save & Load System:** Allows players to save their game progress and load it later.
- **World Setting Management:** World settings can be exported to a file for sharing and imported to start new games in different worlds.

### GUI Screens

1.  **Main Menu:** The initial screen with options to "Load Game" and "Start New Game".
2.  **New Game Screen:** Allows the player to import a world setting file and configure initial game parameters.
3.  **Game Screen:** The main gameplay interface, displaying the text-based scenario and a list of choices. It includes buttons to open the "Details" and "Options" screens.
4.  **Details Screen:** A screen that shows player-specific information, such as status, inventory, etc. The content of this screen is dynamic and depends on the loaded world setting.
5.  **Options Screen:** An in-game menu with options to "Save Game," "Load Game," and "Exit."

## Implementation Steps

1.  **Project Setup:** Initialize the project structure and dependencies.
2.  **Core System Development:**
    -   Implement the `world_handler.py` for loading, parsing, and exporting world setting files.
    -   Develop the `state_manager.py` to handle game state serialization (saving) and deserialization (loading).
    -   Create the `ai_narrator.py` to manage communication with the AI model, including the context caching system.
3.  **GUI Implementation (Screens):**
    -   Build the static screens: `main_menu_screen.py` and `new_game_screen.py`.
    -   Develop the dynamic game interface: `game_view_screen.py`, `details_view_screen.py`, and `options_menu_screen.py`.
4.  **Game Logic Integration:**
    -   Implement the main `game_engine.py` to tie the core systems and GUI screens together.
    -   Establish the flow of the game from starting a new game to playing and saving.
5.  **Testing & Refinement:**
    -   Test each component individually.
    -   Conduct end-to-end testing of the game loop.
    -   Refine the user experience based on testing.

## Dependencies

- Python 3.13+
- textual 6.0.0+

<details>
<summary><strong>Note: textual 6 (release at 2025/08/30) has breaking changes list below.</strong></summary>

- Added bar_renderable to ProgressBar widget
- Added OptionList.set_options
- Added TextArea.suggestion
- Added TextArea.placeholder
- Added Header.format_title and App.format_title for easier customization of title in the Header
- Added Widget.get_line_filters and App.get_line_filters
- Added Binding.Group
- Added DOMNode.displayed_children
- Added TextArea.hide_suggestion_on_blur boolean
- Added OptionList.highlighted_option property
- Added TextArea.update_suggestion method
- Added textual.getters.app

- Breaking change: The renderable property on the Static widget has been changed to content.
- Breaking change: HeaderTitle widget is now a static, with no text and sub_text reactives
- Breaking change: Renamed Label constructor argument renderable to content for consistency
- Breaking change: Optimization to line API to avoid applying background styles to widget content. In practice this means that you can no longer rely on blank Segments automatically getting the background color.
</details>
