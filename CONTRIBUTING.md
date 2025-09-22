[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=luyiourwong_Terminara&metric=alert_status&token=9656e42def76d262c45d1417496ac053f54c30e9)](https://sonarcloud.io/summary/new_code?id=luyiourwong_Terminara)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=luyiourwong_Terminara&metric=coverage&token=9656e42def76d262c45d1417496ac053f54c30e9)](https://sonarcloud.io/summary/new_code?id=luyiourwong_Terminara)

# Contributing

Will accept contributions after 1.0.0 release.

## Development

<details>
<summary>Installation & Running</summary>

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
start /b python terminara\main.py > app.log 2>&1
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
</details>

### Linting
Setting file is in `.flake8`
```bash
python -m flake8 terminara
```

### Unit testing & Coverage
```bash
python -m pytest --cov=terminara tests
```

## Pull Request Guidelines

When you submit a pull request, a few things will happen automatically:

- **Automatic Summary & Review**: [gemini-code-assist](https://github.com/apps/gemini-code-assist) will automatically summarize the changes and perform a preliminary review. You don't need to follow all the suggestions from the bot.
- **CI/CD**: A continuous integration pipeline will run to ensure the code quality. This includes running [unit tests](#unit-testing--coverage) and [linting](#linting).

To ensure a smooth process, it is highly recommended that you run the tests and linter locally before pushing your changes.

## Pack to Executable

### Manually Packaging

1. **Prerequisites**
    ```bash
    pip install pyinstaller
    ```

2. **Run the Packaging Command**
    ```bash
    pyinstaller terminara.spec
    ```
After packaging is complete, the executable will be located in the `dist` directory

<details>
<summary>Release Packaging</summary>

### Github Action Packaging

Github action is used to build the release executable for Windows, Linux and MacOS. This will automatically trigger when a new release is merged to the main branch..

| Platform | Action Label     | OS                  | File Format                     |
|----------|------------------|---------------------|---------------------------------|
| Windows  | `windows-latest` | Windows Server 2025 | terminara_windows_[version].exe |
| Linux    | `ubuntu-22.04`   | Ubuntu 22.04 LTS    | terminara_linux_[version]       |
| MacOS    | `macos-latest`   | macOS 15 (Sequoia)  | terminara_macos_[version]       |

Action will also generate a full compressed file that contains [data folder](terminara/data) and executable files, format is `terminara-[platform]-full-[version].zip`.
</details>

## File Structure

### Configuration Storage
Configuration files are stored in OS-appropriate locations:

| OS      | Location                                   |
|---------|--------------------------------------------|
| Windows | `%LOCALAPPDATA%\Terminara\`                |
| Linux   | `~/.local/share/Terminara/`                |
| MacOS   | `~/Library/Application Support/Terminara/` |

## Versioning

This library follows [Semantic Versioning](http://semver.org/) and managed by [Release Please](https://github.com/googleapis/release-please).

## Links

- [GitHub Repository](https://github.com/luyiourwong/Terminara)
- [Issue Tracker](https://github.com/luyiourwong/Terminara/issues)
- [Sonarcloud]()
