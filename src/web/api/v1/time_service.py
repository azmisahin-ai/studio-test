# src/web/api/v1/time_service.py
from flask_restx import Resource
from datetime import datetime


class TimeService(Resource):
    def get(self):
        """Get the current time."""
        current_time = datetime.now()
        return {"current_time": current_time.strftime("%Y-%m-%d %H:%M:%S")}
