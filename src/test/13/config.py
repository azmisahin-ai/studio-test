# config.py
import os

APP_ENV = os.environ.get("APP_ENV", "development")
APP_NAME = os.environ.get("APP_NAME", "Awesome App")

def get_greeting_message():
    # Implement logic to customize greeting based on environment or other criteria
    if APP_ENV == "production":
        return f"Welcome to {APP_NAME}!"
    else:
        return f"Hello from {APP_NAME}!"