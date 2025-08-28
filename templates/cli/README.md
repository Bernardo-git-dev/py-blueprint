# CLI Template

This is a complete CLI template with a structured architecture including:

- Commands: CLI command implementations
- Services: Core functionality implementations

## Project Structure

```
.
├── main.py                 # Application entry point
├── requirements.txt        # Project dependencies
├── commands/               # CLI commands
│   ├── __init__.py
│   ├── greet.py           # Greeting command
│   └── health.py          # Health check command
└── services/               # Core services
    ├── __init__.py
    ├── greeting_service.py
    └── health_service.py
```

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the CLI:
   ```bash
   python main.py
   ```

## Commands

- `python main.py` - Basic greeting with system username
- `python main.py greet [name]` - Greet a specific user
- `python main.py health` - Check system health
- `python main.py --help` - Show help message
- `python main.py greet --help` - Show help for greet command