# FastAPI Template

This is a complete FastAPI template with a structured architecture including:

- Routes: API endpoint definitions
- Controllers: Business logic handlers
- Services: Core functionality implementations
- Models: Data models and validation

## Project Structure

```
.
├── main.py                 # Application entry point
├── requirements.txt        # Project dependencies
├── routes/                 # API route definitions
│   ├── __init__.py
│   ├── health.py          # Health check endpoint
│   └── greeting.py        # Greeting endpoints
├── controllers/            # Business logic
│   ├── __init__.py
│   └── greeting_controller.py
├── services/               # Core services
│   ├── __init__.py
│   ├── health_service.py
│   └── greeting_service.py
└── models/                 # Data models
    ├── __init__.py
    └── greeting.py
```

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Visit `http://localhost:8000/docs` for API documentation.

## Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /greeting` - Personalized greeting using system username
- `GET /greeting/{name}` - Personalized greeting for a specific name