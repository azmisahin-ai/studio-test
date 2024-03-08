# src/app.py

from flask import Flask
# Import ".routes" could not be resolvedPylancereportMissingImports
# from .routes import routes_bp
from src.routes import routes_bp
app = Flask(__name__, template_folder="templates")

app.register_blueprint(routes_bp)

if __name__ == "__main__":
    app.run()
