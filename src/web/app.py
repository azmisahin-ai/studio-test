# src/web/app.py
import os
from flask import Flask

from .socket import initialize
from .api import blueprint as api_blueprint, api
from gevent.pywsgi import WSGIServer  # Import the WSGIServer from gevent


# Get environment variables
APP_ENV = os.environ.get("APP_ENV")
APP_NAME = os.environ.get("APP_NAME")
HOST_IP = os.environ.get("HOST_IP")
TCP_PORT = os.environ.get("TCP_PORT")
port_number = int(os.environ.get("TCP_PORT"))


def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    # Register the API Blueprint with a URL prefix
    app.register_blueprint(api_blueprint, url_prefix="/api")

    # Ability to access endpoints via socket.
    io = initialize(app, api)

    # Get API paths from the request object
    paths = [
        rule.rule
        for rule in app.url_map.iter_rules()
        if rule.endpoint.startswith("api.")
    ]

    @app.route("/")
    def home():
        """API Gateway Home

        Returns:
            dict: JSON response containing welcome message, application name, and environment.
        """
        return {
            "message": "Welcome to the API Gateway!",
            "application": APP_NAME,
            "environment": APP_ENV,
            "paths": paths,
        }

    return app, io


# Build Flask app to migrate to Gunicorn
app, io = create_app()


# Build Flask app to migrate to Gunicorn
if __name__ == "__main__":
    # Run the Flask app using Gunicorn with SocketIO support
    http_server = WSGIServer(HOST_IP, port_number, app)
    http_server.start()
    io.init_app(app)
    io.run(app, host=HOST_IP, port=port_number)
