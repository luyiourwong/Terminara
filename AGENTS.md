# Guides for AI Agents and Vibecoding

Terminara is a terminal-based ai simulation game.
To create a terminal-based AI simulation game using Python and the `textual` library. The game features an AI-driven storyteller that generates scenarios and choices for the player within a customizable world setting.

## Usage
Read [README.md](README.md) for instructions on how to run the project in production mode.
Read [CONTRIBUTING](CONTRIBUTING.md) for instructions on how to run the project in development mode.

## Key Functional

- **AI as Game Master:** The core of the game is an AI that generates narrative scenarios and player choices based on a predefined world setting.
- **Text-Based GUI:** The user interface is built with `textual`, focusing on a clean, text-centric experience.
- **Context Caching System:** A temporary storage system to provide the AI with consistent memory and context, independent of the AI's own memory limitations.
- **Save & Load System:** Allows players to save their game progress and load it later.
- **World Setting Management:** World settings can be exported to a file for sharing and imported to start new games in different worlds.

## Execution & Environment Management

- Virtual Environment: Always prefer using executables from the `.venv` virtual environment under the project directory (i.e., `.venv\\Scripts\\python.exe`).
- Package Management: When managing packages, prefer using the `uv` command over global `pip` or `python`. Always add dependencies to `pyproject.toml` first, then run `uv sync` instead of using `uv add`.

## Project Structure & Modularity

- Distributed Structure: Prefer structuring code into distributed folders or modules, avoiding concentrating large amounts of code in a single file.
  - Example: Use a distributed structure such as `config/manager.py` (logic handling) paired with `config/models.py` (Pydantic BaseModel data definitions), rather than consolidating everything into a single `config.py`.

## Types & Data Structures

- Explicit Types: Always define type hints in detail. Every method's inputs and outputs must have type definitions.
- Data Structures: Prefer using Pydantic's `BaseModel` to define data structures; avoid passing complex data using raw `dict` wherever possible.

## Code Style & Formatting

- Frequent Logging: Add `logger` statements at I/O entry/exit points, API call sites, and major operations. Debug-level logging for non-critical items is also encouraged.
- Linter & Formatter: When writing or modifying Python code, use `ruff` for both linting and formatting (`ruff check . --fix & ruff format .`).
