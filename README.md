# Flask Student Portal v1

A modular Flask application for managing student registrations.

## Features
- Homepage and navigation
- Student registration (POST)
- Student listing (GET)
- Student Details page
- Modular structure with Flask Blueprints
- Jinja2 templates
- Unit tests with `pytest`

## Quick Start

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python run.py
   ```
   Access the app at `http://127.0.0.1:5000`

4. Run tests:
   ```bash
   pytest
   ```
