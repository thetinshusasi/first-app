# First App

A Python project with virtual environment and TOML configuration.

## Features

- Virtual environment setup
- TOML-based project configuration
- CLI interface with Click
- Rich terminal output
- HTTP requests functionality

## Installation

1. **Clone or create the project directory**

   ```bash
   cd first-app
   ```

2. **Create virtual environment**

   ```bash
   python3 -m venv venv
   ```

3. **Activate virtual environment**

   ```bash
   # On macOS/Linux:
   source venv/bin/activate

   # On Windows:
   venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -e .
   ```

## Usage

### Basic Commands

```bash
# Show help
python src/main.py --help

# Display project information
python src/main.py info

# Show welcome message
python src/main.py hello

# Fetch data from a URL
python src/main.py fetch

# Fetch data from a specific URL
python src/main.py fetch --url https://api.github.com/users/octocat
```

### Development Setup

For development dependencies:

```bash
pip install -e ".[dev]"
```

## Project Structure

```
first-app/
├── venv/                 # Virtual environment
├── src/                  # Source code
│   ├── __init__.py
│   └── main.py          # Main application
├── pyproject.toml       # Project configuration
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Configuration

The project uses `pyproject.toml` for configuration, which includes:

- Project metadata
- Dependencies
- Development tools configuration (Black, MyPy)
- Build system settings

## License

MIT License
