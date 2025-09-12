# Terminara

A terminal-based ai simulation game.

## How to use

You can download the executable application from [latest release](https://github.com/luyiourwong/Terminara/releases/latest).

The full compressed file includes the executable file and the default world settings file. You can only download the executable file if you are updating the game to the latest version.

<details>
<summary><strong>Manual run</strong></summary>

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

3.  **Install the dependencies:**
    ```bash
    pip install -e .
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
</details>

## AI Setup

After starting the application, you need to configure the AI settings from the main menu.

![AI Settings](doc/ai_settings.png)

You need to fill in the following fields: (OpenAI compatibility API)
- **Host**: The API endpoint. Leave it empty to use the default OpenAI endpoint.
- **API Key**: Your API key for the AI service.
- **Model**: The model you want to use.

Click "Apply" to save the settings.

### Examples

#### 1. [OpenAI](https://platform.openai.com/) (Default)
- **Host**: (leave empty)
- **API Key**: `YOUR_OPENAI_API_KEY`
- **Model**: `gpt-4o-mini-2024-07-18`

#### 2. [Google AI Studio](http://aistudio.google.com/)
- **Host**: `https://generativelanguage.googleapis.com/v1beta/openai/`
- **API Key**: `YOUR_GEMINI_API_KEY`
- **Model**: `gemini-2.0-flash`

## Links

- [GitHub Repository](https://github.com/luyiourwong/Terminara)
- [Contribute & Develop Guide](CONTRIBUTING.md)

## License

This project is licensed under the [MIT License](LICENSE).
