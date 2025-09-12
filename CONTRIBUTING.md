[![Quality Gate Status]()](
[![Coverage]()]()

# Contributing

Will accept contributions after 1.0.0 release.

## Development

### Installation

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

3.  **Install the dependencies (dev version):**
    ```bash
    pip install -e .[dev]
    ```

### Start Method 1: Using the installed command (Recommended)
After installation, run the game with:
```bash
terminara
```

### Start Method 2: Direct execution
Cross-platform way
```bash
python -m terminara.main
```
or
```bash
python terminara/main.py
```
On Windows, use `terminara\main.py`

### Start Method 3: Background execution for testing
This is a long-live program, so if you want to test it, you can use this command instead:

Unix/Linux/macOS
```bash
python -m terminara.main > app.log 2>&1 &
```
or Windows (background with start)
```bash
python terminara\main.py > app.log 2>&1
```

### Start Method 4: Textual debug mode (To see the logs)
First start the textual console:
```bash
textual console
```
then start project:
```bash
textual run --dev terminara\main.py
```


### Pack to Executable

1. **Prerequisites**
    ```bash
    pip install pyinstaller
    ```

2. **Run the Packaging Command**
    ```bash
    pyinstaller terminara.spec
    ```
After packaging is complete, the executable will be located in the `dist` directory

### Linting
Setting file is in `.flake8`
```bash
python -m flake8 terminara
```

### Unit testing
```bash
python -m unittest discover -v
```

## Versioning

This library follows [Semantic Versioning](http://semver.org/) and managed by [Release Please](https://github.com/googleapis/release-please).

## Links

- [GitHub Repository](https://github.com/luyiourwong/Terminara)
- [Issue Tracker](https://github.com/luyiourwong/Terminara/issues)
- [Sonarcloud]()