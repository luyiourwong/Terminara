# Terminara

A terminal-based ai simulation game.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/luyiourwong/Terminara
    cd Terminara
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
    On Windows, use `.venv\Scripts\activate`

3.  **Install the dependencies:**
    ```bash
    pip install -e .
    ```

## Usage

### Method 1: Using the installed command (Recommended)
After installation, run the game with:
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
On Windows, use `terminara\main.py`

### Method 3: Background execution for testing
This is a long-live program, so if you want to test it, you can use this command instead:

Unix/Linux/macOS
```bash
python -m terminara.main > app.log 2>&1 &
```
or Windows (background with start)
```bash
python terminara\main.py > app.log 2>&1
```

## Pack to Executable

1. **Prerequisites**
    ```bash
    pip install pyinstaller
    ```

2. **Run the Packaging Command**
    ```bash
    pyinstaller terminara.spec
    ```
After packaging is complete, the executable will be located in the `dist` directory

## Development

### Unit testing
```bash
python -m unittest discover -v
```