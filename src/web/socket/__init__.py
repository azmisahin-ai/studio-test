# src/web/socket/__init__.py
from flask_socketio import SocketIO


def initialize(app, api):
    io = SocketIO(app, cors_allowed_origins="*")

    @io.on("message")
    def handle_ws_message(message):
        response = getApi(message)
        io.emit("message", response)

    def getApi(message):
        return f"Invalid API route: {message}"
