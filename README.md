# Web Application with Message Board

This is a Flask web application that allows users to post messages and view them in a message board format.

## Features

- Home page (index.html)
- Message submission form (message.html)
- Message viewing page (read.html)
- Error handling for 404 pages
- Static file serving (CSS and images)
- JSON-based message storage

## Setup

1. Install Poetry (if not already installed):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:

```bash
poetry install
```

3. Run the application:

```bash
poetry run python app.py
```

The application will be available at http://localhost:3000

## Project Structure

- `app.py` - Main application file
- `templates/` - HTML templates
- `static/` - Static files (CSS, images)
- `storage/` - Directory for storing messages in JSON format
- `pyproject.toml` - Poetry configuration and dependencies
