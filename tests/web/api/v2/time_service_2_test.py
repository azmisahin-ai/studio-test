# tests/web/api/v2/test_time_service_2.py
import unittest
from src.web.api.v2.time_service_v2 import TimeServiceV2
from datetime import datetime, timedelta


class TimeService2Test(unittest.TestCase):

    def test_get_current_time_utc(self):
        time_service_v2 = TimeServiceV2()
        response = time_service_v2.get()

        assert "current_time_utc" in response
        assert isinstance(response["current_time_utc"], str)

        # Optional: Test UTC format
        utc_time_str = response["current_time_utc"]
        utc_time = datetime.strptime(utc_time_str, "%Y-%m-%d %H:%M:%S")

        # Check if the UTC offset is within an acceptable range (e.g., 0 or None)
        assert utc_time.utcoffset() in (timedelta(0), None)


if __name__ == "__main__":
    unittest.main()
