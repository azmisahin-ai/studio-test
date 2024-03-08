# src/web/api/v2/time_service_v2.py
from flask_restx import Resource
from datetime import datetime


class TimeServiceV2(Resource):
    def get(self):
        """Get the current time in UTC."""
        utc_time = datetime.utcnow()
        return {"current_time_utc": utc_time.strftime("%Y-%m-%d %H:%M:%S")}
