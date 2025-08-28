# Django Template

This is a complete Django template with a structured architecture including:

- Apps: Modular components (greeting, health)
- Views: Class-based views for handling requests
- Services: Business logic implementations
- Models: Data models
- URLs: URL routing configurations

## Project Structure

```
.
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
├── PROJECT_NAME/          # Main project directory
│   ├── __init__.py
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL configuration
│   ├── views.py           # Main views
│   ├── wsgi.py
│   └── asgi.py
├── greeting/              # Greeting app
│   ├── __init__.py
│   ├── apps.py            # App configuration
│   ├── models.py          # Data models
│   ├── views.py           # Views
│   ├── services.py        # Business logic
│   ├── urls.py            # URL configuration
│   ├── migrations/        # Database migrations
│   └── templates/         # HTML templates
└── health/                # Health check app
    ├── __init__.py
    ├── apps.py            # App configuration
    ├── models.py          # Data models
    ├── views.py           # Views
    ├── services.py        # Business logic
    ├── urls.py            # URL configuration
    └── migrations/        # Database migrations
```

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Endpoints

- `GET /` - Welcome message
- `GET /greeting` - Personalized greeting using system username
- `GET /greeting/{name}` - Personalized greeting for a specific name
- `GET /health` - Health check